# AI Assistant Roles

A comprehensive collection of AI assistant personality prompts organized by domain. Each prompt defines a specific role with expertise, communication style, and guidelines for consistent AI behavior.

## What is this?

This project provides:
- **23 carefully crafted AI assistant prompts** across multiple domains
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

1. **Browse the roles** in the `ai_assistant_roles/roles/` directory
2. **Copy the content** of any role you need  
3. **Paste it** as a system prompt in your AI assistant (ChatGPT, Claude, etc.)

That's it! The roles are organized by domain (engineering, research, data, etc.) for easy navigation.

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

A simple Python API is available for programmatic access:
- `load_prompt(role)` - Load a prompt by role name
- `list_prompts()` - List all available roles
- `prompt_exists(role)` - Check if a role exists

## Adding New Roles

See [CLAUDE.md](CLAUDE.md) for detailed guidelines on creating new role prompts.

## Contributing

1. Fork the repository
2. Add new roles following the guidelines in [CLAUDE.md](CLAUDE.md)
3. Submit a pull request

## License

Apache License 2.0 - see [LICENSE](LICENSE) file for details.