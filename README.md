# AI Assistant Roles

A simple system for storing and managing AI assistant personality prompts. Each prompt defines a specific role with expertise, communication style, and guidelines.

## What is this?

This project provides:
- A collection of AI assistant prompts for different roles
- Simple Python API for loading prompts
- Git-based version control for prompt evolution
- Easy-to-edit Markdown format

## Quick Start

### 1. Browse Available Prompts

Check the `prompts/` directory to see available roles:
- `backend-engineer.md` - Backend development expertise
- `data-scientist.md` - Data science and ML focus
- `code-reviewer.md` - Code review specialist

### 2. Use in Python

```python
from ai_assistant_roles.prompts import load_prompt, list_prompts

# List available roles
roles = list_prompts()
print(roles)  # ['backend-engineer', 'code-reviewer', 'data-scientist']

# Load a specific prompt
prompt = load_prompt('backend-engineer')
print(prompt)
```

### 3. Use Directly

Simply read the markdown files in `prompts/` directory and copy the content to your AI assistant.

## Project Structure

```
ai-assistant-roles/
├── prompts/                 # Prompt storage
│   ├── backend-engineer.md
│   ├── data-scientist.md
│   └── code-reviewer.md
├── ai_assistant_roles/      # Python package
│   ├── __init__.py
│   └── prompts.py          # Prompt loading utilities
└── tests/                  # Test suite
```

## Adding New Prompts

1. Create a new `.md` file in the `prompts/` directory
2. Name it using kebab-case (e.g., `frontend-engineer.md`)
3. Follow the existing format:
   ```markdown
   # Role Name
   
   Brief description of the role and expertise.
   
   ## Core Expertise
   - List key areas of knowledge
   
   ## Communication Style
   - How to communicate
   
   ## When Providing Solutions
   - Guidelines for responses
   ```

## Versioning

This project uses Git tags for versioning:
- View current version: `git describe --tags`
- Checkout specific version: `git checkout v1.0.0`
- Create new version: `git tag -a v1.0.1 -m "Add new prompts"`

## Python API

### Functions

- `load_prompt(role: str) -> str`: Load a prompt by role name
- `list_prompts() -> list[str]`: List all available roles
- `prompt_exists(role: str) -> bool`: Check if a role exists

### Example Usage

```python
from ai_assistant_roles.prompts import load_prompt

# Load and use with OpenAI
import openai

prompt = load_prompt('data-scientist')
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "Help me analyze this dataset..."}
    ]
)
```

## Development

### Setup Environment

```bash
# Create virtual environment
make environment-create

# Run tests
make unit-test

# Format and lint
make format lint
```

### Running Tests

```bash
make test
```

## Contributing

1. Add new prompts to `prompts/` directory
2. Test loading with the Python API
3. Update this README if needed
4. Create a pull request

## License

[Your License Here]