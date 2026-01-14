# Skills System

## Summary
Skills are folders of instructions, scripts, and resources that Claude dynamically loads to improve performance on specialized tasks. They're elegantly simple: markdown files with YAML metadata.

## What Are Skills?

> Skills teach Claude how to complete specific tasks repeatably—whether creating branded documents, analyzing data with organizational workflows, or automating personal tasks.

### The Elegant Simplicity
- Just markdown files with instructions
- No heavyweight protocols
- Token-efficient (brief summaries scanned before full load)
- Shareable across different models and tools

## Skill Structure

### Basic Format
```yaml
---
name: my-skill-name
description: A clear description of what this skill does
---

# My Skill Name

[Instructions for Claude]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

### Required Fields
- `name`: Unique identifier (lowercase, hyphens)
- `description`: Complete description of purpose and usage

## Official Skills Repository

**Repository**: [github.com/anthropics/skills](https://github.com/anthropics/skills) (40.3k stars)

### Categories
| Category | Examples |
|----------|----------|
| Creative & Design | Art, music, design |
| Development & Technical | Web app testing, MCP servers |
| Enterprise & Communication | Branding, internal comms |
| Document Skills | DOCX, PDF, PPTX, XLSX |

### Installation (Claude Code)
```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

## Scientific Skills for Research

**Repository**: [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)

### Coverage
- **140 ready-to-use skills**
- 28+ Scientific databases (OpenAlex, PubMed, ChEMBL, UniProt)
- 55+ Python packages (RDKit, Scanpy, PyTorch)
- 15+ Scientific integrations (Benchling, DNAnexus, LatchBio)

### Categories
- Bioinformatics & Genomics (16+ skills)
- Cheminformatics & Drug Discovery (11+ skills)
- Clinical Research & Precision Medicine (12+ skills)
- Machine Learning & AI (15+ skills)

### Use Cases
1. **Drug Discovery**: ChEMBL queries, SAR analysis, virtual screening
2. **Single-Cell Analysis**: Scanpy workflows, cell type identification
3. **Multi-Omics Integration**: Combine RNA-seq, proteomics, metabolomics
4. **Clinical Variant Interpretation**: ClinVar, COSMIC annotations

## Creating Custom Skills

### Best Practices
1. **Self-Contained**: Each skill in own directory with SKILL.md
2. **Clear Instructions**: Detailed enough for Claude to understand
3. **Include Examples**: Concrete usage demonstrations
4. **Add Guidelines**: Constraints and best practices
5. **Supporting Files**: Scripts/resources in skill folder as needed

### Skill Learning
Skills can be created by Claude itself based on observed patterns - see the "Skill Learning" concept from DeepLearning.ai course.

## Key References

- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Scientific Skills for Claude](https://github.com/K-Dense-AI/claude-scientific-skills)
- [Simon Willison: Claude Skills](https://simonwillison.net/2025/Oct/16/claude-skills/)
- [Skills API Guide](https://docs.claude.com/en/api/skills-guide)
