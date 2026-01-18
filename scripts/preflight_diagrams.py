#!/usr/bin/env python3
"""
Preflight Diagrams: Convert natural language diagram descriptions to structured specs.

This script processes PRESENTATION.md files, finding **Diagram Description**: blocks
and converting them to structured **Diagram**: specifications that can be rendered
as vector graphics in PowerPoint.

Usage:
    python preflight_diagrams.py --input docs/PRESENTATION.md --output docs/PRESENTATION-processed.md

For LLM-powered conversion (requires ANTHROPIC_API_KEY):
    python preflight_diagrams.py --input docs/PRESENTATION.md --output docs/PRESENTATION-processed.md --use-llm

Author: Claude Code
Date: 2026-01-17
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional

# Try to import anthropic for LLM mode
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False


# Default style for diagrams
DEFAULT_STYLE = {
    "shape": "rounded_rectangle",
    "fill": "#E8F4F8",
    "line": "#2D5F73",
    "text_color": "#1A3A47"
}


def find_diagram_descriptions(content: str) -> List[Tuple[int, int, str]]:
    """
    Find all **Diagram Description**: blocks in the content.

    Returns list of (start_pos, end_pos, description_text) tuples.
    """
    results = []

    # Pattern to match **Diagram Description**: followed by text until next ** section or ---
    pattern = r'\*\*Diagram Description\*\*:\s*\n((?:(?!\*\*[A-Z]).)+?)(?=\n\*\*|\n---|\Z)'

    for match in re.finditer(pattern, content, re.DOTALL | re.IGNORECASE):
        start = match.start()
        end = match.end()
        description = match.group(1).strip()
        results.append((start, end, description))

    return results


def parse_description_heuristic(description: str) -> dict:
    """
    Parse a natural language diagram description using heuristics.

    This is a fallback when LLM is not available. It uses pattern matching
    to identify diagram type and extract nodes/edges.
    """
    desc_lower = description.lower()

    # Detect diagram type
    diagram_type = "flow"  # default
    if any(word in desc_lower for word in ["cycle", "circular", "loop back", "loops back"]):
        diagram_type = "cycle"
    elif any(word in desc_lower for word in ["comparison", "versus", "vs", "side by side", "two columns"]):
        diagram_type = "comparison"
    elif any(word in desc_lower for word in ["hierarchy", "tree", "parent", "children"]):
        diagram_type = "hierarchy"
    elif "vertical" in desc_lower:
        diagram_type = "flow_vertical"

    # Extract numbered items or parenthetical items
    # Pattern: (1) item, (2) item or 1. item, 2. item
    numbered_pattern = r'(?:\((\d+)\)|(\d+)\.)\s*([^,()\d][^,()]*?)(?=,|\(?\d+[.)]|$|then|and then)'
    numbered_matches = re.findall(numbered_pattern, description, re.IGNORECASE)

    nodes = []
    if numbered_matches:
        for match in numbered_matches:
            num = match[0] or match[1]
            text = match[2].strip().rstrip(',').strip()
            if text and len(text) > 2:
                node_id = f"node{num}"
                nodes.append({"id": node_id, "text": text})

    # If no numbered items, try to extract from phrases like "X leads to Y"
    if not nodes:
        # Try "stages:" or "steps:" followed by items
        stages_match = re.search(r'(?:stages?|steps?|phases?):\s*(.+?)(?:\.|$)', description, re.IGNORECASE)
        if stages_match:
            items = re.split(r',\s*(?:and\s+)?', stages_match.group(1))
            for i, item in enumerate(items):
                text = item.strip().rstrip('.')
                if text and len(text) > 2:
                    nodes.append({"id": f"node{i+1}", "text": text})

    # Generate edges based on diagram type
    edges = []
    if nodes:
        for i in range(len(nodes) - 1):
            edges.append({"from": nodes[i]["id"], "to": nodes[i+1]["id"]})

        # For cycle, add edge from last back to first
        if diagram_type == "cycle" and len(nodes) > 1:
            edges.append({"from": nodes[-1]["id"], "to": nodes[0]["id"]})

    # Extract style hints
    style = DEFAULT_STYLE.copy()
    if "blue" in desc_lower:
        style["fill"] = "#E8F4F8"
        style["line"] = "#2D5F73"
    elif "green" in desc_lower:
        style["fill"] = "#E8F8E8"
        style["line"] = "#2D732D"
    elif "orange" in desc_lower or "amber" in desc_lower:
        style["fill"] = "#FFF4E8"
        style["line"] = "#735F2D"

    if "rounded" in desc_lower:
        style["shape"] = "rounded_rectangle"
    elif "diamond" in desc_lower:
        style["shape"] = "diamond"

    return {
        "type": diagram_type,
        "position": "right",
        "width": 5.0,
        "nodes": nodes,
        "edges": edges,
        "style": style
    }


def convert_with_llm(description: str, client: 'anthropic.Anthropic') -> dict:
    """
    Use Claude to convert natural language description to structured diagram spec.
    """
    prompt = f"""Convert this natural language diagram description into a structured YAML-like specification.

Description:
{description}

Output a JSON object with this structure:
{{
    "type": "cycle|flow|flow_vertical|comparison|hierarchy",
    "position": "right",
    "width": 5.0,
    "nodes": [
        {{"id": "unique_id", "text": "Display text"}}
    ],
    "edges": [
        {{"from": "source_id", "to": "target_id"}}
    ],
    "style": {{
        "shape": "rounded_rectangle",
        "fill": "#E8F4F8",
        "line": "#2D5F73",
        "text_color": "#1A3A47"
    }}
}}

Rules:
- Extract distinct stages/steps/elements as nodes
- Create edges showing the flow/connections described
- For cycles, include an edge from last node back to first
- Use short, clear text for nodes (max ~20 chars)
- Output ONLY the JSON object, no explanation"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = message.content[0].text.strip()

    # Extract JSON from response (handle markdown code blocks)
    if "```" in response_text:
        json_match = re.search(r'```(?:json)?\s*(\{.+?\})\s*```', response_text, re.DOTALL)
        if json_match:
            response_text = json_match.group(1)

    import json
    return json.loads(response_text)


def format_diagram_spec(spec: dict) -> str:
    """
    Format a diagram specification as a markdown code block.
    """
    lines = ["```diagram"]

    lines.append(f"type: {spec.get('type', 'flow')}")
    lines.append(f"position: {spec.get('position', 'right')}")
    lines.append(f"width: {spec.get('width', 5.0)}")
    lines.append("")

    lines.append("nodes:")
    for node in spec.get("nodes", []):
        lines.append(f"  - id: {node['id']}")
        lines.append(f"    text: {node['text']}")
    lines.append("")

    lines.append("edges:")
    for edge in spec.get("edges", []):
        lines.append(f"  - from: {edge['from']}")
        lines.append(f"    to: {edge['to']}")
    lines.append("")

    style = spec.get("style", DEFAULT_STYLE)
    lines.append("style:")
    lines.append(f"  shape: {style.get('shape', 'rounded_rectangle')}")
    lines.append(f"  fill: \"{style.get('fill', '#E8F4F8')}\"")
    lines.append(f"  line: \"{style.get('line', '#2D5F73')}\"")
    lines.append(f"  text_color: \"{style.get('text_color', '#1A3A47')}\"")

    lines.append("```")

    return "\n".join(lines)


def process_file(input_path: Path, output_path: Path, use_llm: bool = False) -> int:
    """
    Process a PRESENTATION.md file, converting diagram descriptions.

    Returns the number of diagrams converted.
    """
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all diagram descriptions
    descriptions = find_diagram_descriptions(content)

    if not descriptions:
        print("No **Diagram Description**: blocks found.")
        # Still write output (unchanged)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return 0

    print(f"Found {len(descriptions)} diagram description(s)")

    # Initialize LLM client if needed
    client = None
    if use_llm:
        if not HAS_ANTHROPIC:
            print("Warning: anthropic package not installed. Using heuristic parsing.")
            use_llm = False
        else:
            import os
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not api_key:
                print("Warning: ANTHROPIC_API_KEY not set. Using heuristic parsing.")
                use_llm = False
            else:
                client = anthropic.Anthropic(api_key=api_key)

    # Process in reverse order to preserve positions
    new_content = content
    for start, end, description in reversed(descriptions):
        print(f"\nProcessing: {description[:60]}...")

        # Convert description to spec
        if use_llm and client:
            try:
                spec = convert_with_llm(description, client)
                print("  (converted using LLM)")
            except Exception as e:
                print(f"  LLM conversion failed: {e}")
                print("  (falling back to heuristic)")
                spec = parse_description_heuristic(description)
        else:
            spec = parse_description_heuristic(description)
            print("  (converted using heuristic)")

        # Format the spec
        formatted = format_diagram_spec(spec)

        # Create replacement text
        replacement = f"**Diagram**:\n{formatted}"

        # Replace in content
        new_content = new_content[:start] + replacement + new_content[end:]

        print(f"  → {spec['type']} diagram with {len(spec['nodes'])} nodes")

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"\nWrote processed file to: {output_path}")
    return len(descriptions)


def main():
    parser = argparse.ArgumentParser(
        description="Convert natural language diagram descriptions to structured specs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Basic usage (heuristic parsing)
    python preflight_diagrams.py -i docs/PRESENTATION.md -o docs/PRESENTATION-processed.md

    # With LLM-powered conversion
    export ANTHROPIC_API_KEY=your_key
    python preflight_diagrams.py -i docs/PRESENTATION.md -o docs/PRESENTATION-processed.md --use-llm
"""
    )

    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Input PRESENTATION.md file"
    )
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Output processed file"
    )
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="Use Claude API for conversion (requires ANTHROPIC_API_KEY)"
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    count = process_file(input_path, output_path, args.use_llm)

    print(f"\nConverted {count} diagram(s)")


if __name__ == "__main__":
    main()
