# AI Assistant Roles

A comprehensive collection of AI assistant personality prompts organized by domain. Each prompt defines a specific role with expertise, communication style, and guidelines for consistent AI behavior.

## What is this?

This project provides:
- **23+ carefully crafted AI assistant prompts** across multiple domains
- Simple Python API for programmatic access
- Git-based version control for prompt evolution
- Easy-to-edit Markdown format
- Semantic versioning support

## 📚 Available Roles

### Engineering (10 roles)
- `software-engineer` - Full-stack software development expertise
- `backend-engineer` - Backend systems and API development
- `frontend-engineer` - UI/UX and frontend technologies
- `ai-engineer` - AI/ML engineering and implementation
- `ai-product-engineer` - AI-powered product development
- `software-architect` - System design and architecture
- `systems-architect` - Infrastructure and distributed systems
- `devops-engineer` - CI/CD, automation, and operations
- `qa-tester` - Quality assurance and testing
- `code-reviewer` - Code review and best practices

### Research (6 roles)
- `research-engineer` - Applied research and implementation
- `deep-learning-researcher` - Neural networks and deep learning
- `language-model-expert` - LLMs and NLP expertise
- `multimodal-researcher` - Vision, audio, and multimodal AI
- `novel-techniques-researcher` - Cutting-edge AI research
- `statistical-ml-researcher` - Statistical machine learning

### Data (2 roles)
- `data-scientist` - Data analysis and machine learning
- `data-analyst` - Data exploration and insights

### Business (1 role)
- `product-manager` - Product strategy and management

### Design (1 role)
- `ux-designer` - User experience and interface design

### Writing (3 roles)
- `writing-assistant` - General writing support
- `linkedin-writer` - Professional LinkedIn content
- `introspection-writer` - Reflective and analytical writing

## Quick Start

### 1. Browse Available Roles

Explore the organized role structure:
```
ai_assistant_roles/roles/
├── business/
│   └── product-manager.md
├── data/
│   ├── data-analyst.md
│   └── data-scientist.md
├── design/
│   └── ux-designer.md
├── engineering/
│   ├── ai-engineer.md
│   ├── ai-product-engineer.md
│   ├── backend-engineer.md
│   ├── code-reviewer.md
│   ├── devops-engineer.md
│   ├── frontend-engineer.md
│   ├── qa-tester.md
│   ├── software-architect.md
│   ├── software-engineer.md
│   └── systems-architect.md
├── research/
│   ├── deep-learning-researcher.md
│   ├── language-model-expert.md
│   ├── multimodal-researcher.md
│   ├── novel-techniques-researcher.md
│   ├── research-engineer.md
│   └── statistical-ml-researcher.md
└── writing/
    ├── introspection-writer.md
    ├── linkedin-writer.md
    └── writing-assistant.md
```

### 2. Use in Python

```python
from ai_assistant_roles.prompts import load_prompt, list_prompts

# List all available roles
roles = list_prompts()
print(f"Available roles: {len(roles)}")
# Output: Available roles: 23

# Load a specific prompt
prompt = load_prompt('engineering/software-architect')
print(prompt[:100] + "...")

# Load from subdirectories
data_scientist = load_prompt('data/data-scientist')
ux_designer = load_prompt('design/ux-designer')
```

### 3. Use Directly

Simply copy the content from any `.md` file in the `ai_assistant_roles/roles/` directory and paste it as a system prompt in your AI assistant (ChatGPT, Claude, etc.).

## Project Structure

```
ai-assistant-roles/
├── ai_assistant_roles/      # Python package
│   ├── __init__.py
│   ├── prompts.py          # Role loading utilities
│   └── roles/              # All role definitions
│       ├── business/       # Business-focused roles
│       ├── data/          # Data science roles
│       ├── design/        # Design roles
│       ├── engineering/   # Software engineering roles
│       ├── research/      # Research roles
│       └── writing/       # Writing roles
├── tests/                  # Test suite
├── pyproject.toml         # Project configuration
├── Makefile              # Development automation
└── CLAUDE.md             # Development guidelines
```

## Python API

### Functions

- `load_prompt(role: str) -> str`: Load a prompt by role name (supports subdirectories)
- `list_prompts() -> list[str]`: List all available roles with their paths
- `prompt_exists(role: str) -> bool`: Check if a role exists

### Example: Integration with AI APIs

```python
from ai_assistant_roles.prompts import load_prompt
import openai

# Load a specialized role
prompt = load_prompt('engineering/ai-engineer')

# Use with OpenAI
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "Help me design a recommendation system"}
    ]
)

# Or with Anthropic Claude
import anthropic
claude = anthropic.Client()
response = claude.messages.create(
    model="claude-3-opus-20240229",
    system=prompt,
    messages=[{"role": "user", "content": "Help me design a recommendation system"}]
)
```

## Adding New Roles

1. Choose the appropriate subdirectory under `ai_assistant_roles/roles/`
2. Create a new `.md` file using kebab-case (e.g., `ml-engineer.md`)
3. Follow the consistent structure:

```markdown
# Role Name

Brief description of the role's expertise and experience level.

## Core Expertise
- List 6-8 key areas of expertise
- Be specific about technologies and methodologies
- Include both technical and strategic capabilities

## Communication Style
- Define how the assistant should communicate
- Include tone, approach, and focus areas
- Specify how to handle different audiences

## When Providing Solutions
1. Step-by-step approach the assistant should follow
2. Usually 6-8 numbered steps
3. Include analysis, implementation, and validation

## Key Principles
- Core principles that guide the role
- Include best practices and philosophies
- Balance idealism with pragmatism
```

See [CLAUDE.md](CLAUDE.md) for detailed guidelines on creating new role prompts.

## Development

### Setup Environment

```bash
# Create Python 3.12 environment
make environment-create

# Sync dependencies
make environment-sync
```

### Testing

```bash
# Run all tests with coverage
make all-test

# Run specific test types
make unit-test
make functional-test

# Validate before committing
make validate-branch
```

### Code Quality

```bash
# Format code
make format

# Lint and type check
make lint
make type-check
```

## Versioning

This project uses semantic versioning. Version is managed in `pyproject.toml`.

```bash
# View current version
grep version pyproject.toml

# Version is updated automatically via CI/CD
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add new roles following the guidelines
4. Ensure tests pass: `make validate-branch`
5. Submit a pull request

## License

[Your License Here]