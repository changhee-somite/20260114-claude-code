#!/usr/bin/env python3
"""
Search Claude Code conversation history.

Usage:
    python search.py <keyword> [--project <path>] [--limit <n>] [--sessions-only]
    python search.py --list [--project <path>]
    python search.py --session <session-id> [--project <path>]

Examples:
    python search.py "image insertion"
    python search.py "pptx" --project "/Users/me/myproject"
    python search.py --list
    python search.py --session abc123-def456
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional


def get_projects_dir() -> Path:
    """Get the Claude Code projects directory."""
    return Path.home() / '.claude' / 'projects'


def encode_project_path(path: str) -> str:
    """Encode a project path to match Claude's folder naming."""
    return path.replace('/', '-').replace(' ', '-')


def list_sessions(project_filter: Optional[str] = None) -> List[Dict]:
    """List all sessions, optionally filtered by project."""
    base = get_projects_dir()
    sessions = []

    for proj_dir in sorted(base.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True):
        if not proj_dir.is_dir():
            continue

        # Filter by project if specified
        if project_filter:
            encoded = encode_project_path(project_filter)
            if encoded not in proj_dir.name:
                continue

        index_file = proj_dir / 'sessions-index.json'
        if not index_file.exists():
            continue

        try:
            with open(index_file, 'r') as f:
                data = json.load(f)

            for entry in data.get('entries', []):
                sessions.append({
                    'sessionId': entry.get('sessionId'),
                    'project': proj_dir.name,
                    'projectPath': entry.get('projectPath', ''),
                    'title': entry.get('customTitle') or entry.get('firstPrompt', '')[:60],
                    'created': entry.get('created', ''),
                    'modified': entry.get('modified', ''),
                    'messageCount': entry.get('messageCount', 0),
                    'gitBranch': entry.get('gitBranch', '')
                })
        except (json.JSONDecodeError, IOError):
            continue

    # Sort by modified date
    sessions.sort(key=lambda x: x.get('modified', ''), reverse=True)
    return sessions


def search_keyword(keyword: str, project_filter: Optional[str] = None,
                   limit: int = 20, sessions_only: bool = False) -> List[Dict]:
    """Search for a keyword across all sessions."""
    base = get_projects_dir()
    results = []
    seen_sessions = set()

    pattern = re.compile(keyword, re.IGNORECASE)

    for proj_dir in base.iterdir():
        if not proj_dir.is_dir():
            continue

        if project_filter:
            encoded = encode_project_path(project_filter)
            if encoded not in proj_dir.name:
                continue

        for jsonl_file in proj_dir.glob('*.jsonl'):
            session_id = jsonl_file.stem
            session_matches = []

            try:
                with open(jsonl_file, 'r') as f:
                    for line_num, line in enumerate(f, 1):
                        try:
                            data = json.loads(line)

                            # Extract text content
                            msg = data.get('message', {})
                            content_parts = msg.get('content', [])

                            text_content = []
                            for part in content_parts:
                                if isinstance(part, dict):
                                    if part.get('type') == 'text':
                                        text_content.append(part.get('text', ''))
                                    elif part.get('type') == 'tool_result':
                                        text_content.append(str(part.get('content', '')))

                            full_text = ' '.join(text_content)

                            if pattern.search(full_text):
                                # Find the matching snippet
                                match = pattern.search(full_text)
                                start = max(0, match.start() - 50)
                                end = min(len(full_text), match.end() + 100)
                                snippet = full_text[start:end]

                                session_matches.append({
                                    'line': line_num,
                                    'role': msg.get('role', 'unknown'),
                                    'snippet': snippet,
                                    'timestamp': data.get('timestamp', '')
                                })

                        except json.JSONDecodeError:
                            continue

                if session_matches:
                    if sessions_only:
                        if session_id not in seen_sessions:
                            seen_sessions.add(session_id)
                            results.append({
                                'sessionId': session_id,
                                'project': proj_dir.name,
                                'matchCount': len(session_matches),
                                'firstMatch': session_matches[0]
                            })
                    else:
                        for match in session_matches:
                            results.append({
                                'sessionId': session_id,
                                'project': proj_dir.name,
                                **match
                            })

                    if len(results) >= limit:
                        return results

            except IOError:
                continue

    return results[:limit]


def get_session_content(session_id: str, project_filter: Optional[str] = None) -> Optional[List[Dict]]:
    """Get the content of a specific session."""
    base = get_projects_dir()

    for proj_dir in base.iterdir():
        if not proj_dir.is_dir():
            continue

        if project_filter:
            encoded = encode_project_path(project_filter)
            if encoded not in proj_dir.name:
                continue

        session_file = proj_dir / f'{session_id}.jsonl'
        if not session_file.exists():
            continue

        messages = []
        try:
            with open(session_file, 'r') as f:
                for line in f:
                    try:
                        data = json.loads(line)
                        msg = data.get('message', {})
                        role = msg.get('role', 'unknown')

                        text_parts = []
                        for part in msg.get('content', []):
                            if isinstance(part, dict) and part.get('type') == 'text':
                                text_parts.append(part.get('text', ''))

                        if text_parts:
                            messages.append({
                                'role': role,
                                'text': '\n'.join(text_parts)[:1000],
                                'timestamp': data.get('timestamp', '')
                            })
                    except json.JSONDecodeError:
                        continue
        except IOError:
            continue

        return messages

    return None


def main():
    parser = argparse.ArgumentParser(
        description='Search Claude Code conversation history',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "image insertion"           Search for keyword
  %(prog)s --list                      List all sessions
  %(prog)s --list --project ~/myproj   List sessions for project
  %(prog)s --session abc123            Show session content
  %(prog)s "pptx" --sessions-only      Show matching sessions only
        """
    )
    parser.add_argument('keyword', nargs='?', help='Keyword to search for')
    parser.add_argument('--list', '-l', action='store_true', help='List all sessions')
    parser.add_argument('--session', '-s', help='Show content of specific session')
    parser.add_argument('--project', '-p', help='Filter by project path')
    parser.add_argument('--limit', '-n', type=int, default=20, help='Max results (default: 20)')
    parser.add_argument('--sessions-only', action='store_true', help='Show matching sessions only, not individual matches')

    args = parser.parse_args()

    if args.list:
        sessions = list_sessions(args.project)
        print(f"Found {len(sessions)} sessions\n")
        print(f"{'Modified':<12} {'Messages':>8} {'Title':<50} Session ID")
        print("-" * 100)
        for s in sessions[:args.limit]:
            modified = s['modified'][:10] if s['modified'] else 'Unknown'
            title = s['title'][:48] + '..' if len(s['title']) > 50 else s['title']
            print(f"{modified:<12} {s['messageCount']:>8} {title:<50} {s['sessionId'][:36]}")

        print(f"\nTo resume: claude --resume <session-id>")

    elif args.session:
        messages = get_session_content(args.session, args.project)
        if messages:
            print(f"Session: {args.session}\n")
            for m in messages:
                role = m['role'].upper()
                timestamp = m['timestamp'][:19] if m['timestamp'] else ''
                text = m['text'][:500] + '...' if len(m['text']) > 500 else m['text']
                print(f"[{timestamp}] {role}:")
                print(f"  {text}\n")
        else:
            print(f"Session not found: {args.session}")
            sys.exit(1)

    elif args.keyword:
        results = search_keyword(args.keyword, args.project, args.limit, args.sessions_only)
        print(f"Found {len(results)} matches for '{args.keyword}'\n")

        if args.sessions_only:
            print(f"{'Session ID':<38} {'Matches':>8} First Match")
            print("-" * 100)
            for r in results:
                snippet = r['firstMatch']['snippet'][:50].replace('\n', ' ')
                print(f"{r['sessionId']:<38} {r['matchCount']:>8} ...{snippet}...")
        else:
            for r in results:
                snippet = r['snippet'].replace('\n', ' ')[:80]
                print(f"[{r['sessionId'][:8]}...] Line {r['line']}: ...{snippet}...")

        print(f"\nTo resume: claude --resume <session-id>")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
