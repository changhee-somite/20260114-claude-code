# Objectives & Background

I want to prepare a 30 minute to 1 hour presentation to an internal computational team.
They are well versed to coding agents, IDEs like Cursor. I want to introduce them Claude Code and how to utilize them effectively.

Specifically, they want to know what difference there is between using Cursor IDE 
choosing our models ourselves, to using Claude Code. I believe there is a big difference,
but I want them to provide an objective assessment and the state of the field.

As a secondary objective, my intention is that the whole process involves Claude Code
as a WORKFLOW, and for this, I create a git repository to document the steps for its preparation,
including Claude Code SKILLS for pptx presentation file generation.


# Github repository

The github repository is mainly for committing the progress and changes of all the documentations
that slowly will be reorganized and created based on the interaction I make with Claude Code interface.
For each interaction that meaningfully changes/creates documentations, we will commit them with clear
concise description what operation has been done.

As the commit history will demonstrate how Claude Code workflow is being used, the eventual output should
act as a reference for the readers to find specific documentations or pointers.


# Organization and what to cover

At the moment, I have no organization of the presentation yet but I have several things
that I want to cover but flexible with your suggestions.

These topics, thoughts, references are found in scratch/SCRATCH.md, which we will

organize into topics with certain order that makes sense, and may have hierarchical structure
if that organization deemed helpful for legilibility. These developments will happen under docs/ directory.

Eventually, we will build in the docs/PRESENTATION.md that organizes the topics to cover and references 
to build an effective presentation. Please refer below for an effective presentation.

After the markdown documentation is complete, we could generate a .pptx file using SKILLs.

There is already a .pptx presentation template that has the powerpoint template and a brief
keywords regarding this matter.


# Effective powerpoint presentation file and its specification in PRESENTATION.md

* You should have one idea per slide
* The slide title should have a clear, concise one full sentence that summarizes that idea

* Sometimes it is needed to insert figures. 
    - If you can generate a figure, put that under figures/slideNo with clear instructions how to make them
    - If you grab that figure from web sources or jupyter notebook etc., you record also a markdown file how you grabbed them in which sources
    - If we are reorganizing the slides (inserting new slides etc.) we should also move the figures for proper tracking. To enforce this, the PRESENTATION.md should link relative path to the figure in question.




# Documentation Principles

* **README.md** should be a general overview with links to detailed documentation
* **Details belong in dedicated docs/** — Relegate technical details, workflows, and specifications to separate markdown files
* **Avoid verbose README** — Keep it scannable; readers can drill into linked documents for depth
* **docs/ organization**:
  - `docs/topics/` — Deep-dive topic documentation
  - `docs/PRESENTATION.md` — Slide outline
  - `docs/*.md` — Workflow specs, skill documentation, research notes


# Workflow

* Phase 1 : You first read the scratch/SCRATCH.md and do further research to compile and organize
* Phase 2 : We create relevant topic documentations as docs/TOPICS.md or even docs/topics/ etc.

* Every revision we commit to track how we improved our structure
* When I direct you make a .pptx file for review. But we will not edit the .pptx file but base everything on the committed documentation and figures.


