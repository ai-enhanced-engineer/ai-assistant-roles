# AI Assistant Roles - Development Guide

A system for storing and managing AI assistant personality prompts. Each prompt defines a specific role with expertise, communication style, and guidelines for consistent AI behavior.

## Project Structure

```
ai-assistant-roles/
├── prompts/              # AI role prompt definitions
│   ├── engineering/      # Engineering-focused roles
│   │   ├── software-engineer.md
│   │   ├── backend-engineer.md
│   │   ├── software-architect.md
│   │   └── systems-architect.md
│   └── other-domains/    # Other domain roles
├── ai_assistant_roles/   # Python package
│   ├── __init__.py
│   └── main.py          # Prompt loading utilities
├── tests/               # Test suite
├── Makefile            # Development automation
└── pyproject.toml      # Project config & dependencies
```

## Quick Start

### Setup
```bash
make environment-create   # Creates Python 3.12 env with uv
make environment-sync     # Updates dependencies
```

### Development Commands
```bash
make format              # Auto-format with Ruff
make lint                # Lint and auto-fix issues
make type-check          # Type check with MyPy
make validate-branch     # Run all checks before PR
```

### Testing
```bash
make unit-test           # Run unit tests
make functional-test     # Run functional tests
make all-test           # Run all tests with coverage
```

## Development Workflow

1. **Write code** following Python conventions:
   - Classes: `PascalCase`
   - Functions/variables: `snake_case` 
   - Constants: `UPPER_SNAKE_CASE`
   - Max line length: 120 characters

2. **Validate before committing**:
   ```bash
   make validate-branch     # Runs linting and tests
   ```

3. **Test thoroughly**:
   - Unit tests: `@pytest.mark.unit`
   - Functional tests: `@pytest.mark.functional`
   - Integration tests: `@pytest.mark.integration`

## Key Technologies

- **FastAPI**: Modern Python web framework
- **Pydantic**: Data validation using Python type annotations
- **MyPy**: Static type checking
- **Ruff**: Fast Python linter and formatter
- **pytest**: Testing framework
- **uv**: Fast Python package manager

## ML/Data Science Stack

- **scikit-learn**: Machine learning library
- **XGBoost/LightGBM**: Gradient boosting frameworks
- **PyTorch**: Deep learning framework
- **pandas/numpy**: Data manipulation
- **SHAP**: Model interpretability

## Best Practices

- Type hints on all functions
- Pydantic models for data validation
- Structured logging with loguru
- Environment-based configuration
- No hardcoded secrets
- Test coverage > 80%

## Creating New Role Prompts

### Guidelines for Writing Role Prompts

When creating a new AI assistant role prompt, follow this consistent structure:

#### 1. File Naming
- Use kebab-case for file names (e.g., `software-architect.md`)
- Place in appropriate subdirectory under `prompts/`
- Group related roles together (e.g., engineering, data-science, business)

#### 2. Prompt Structure

Each prompt should include these sections in order:

```markdown
# Role Name

[Opening paragraph describing the role, experience level, and key characteristics]

## Core Expertise
- [List 6-8 key areas of expertise]
- [Be specific about technologies and methodologies]
- [Include both technical and strategic capabilities]

## Communication Style
- [Define how the assistant should communicate]
- [Include tone, approach, and focus areas]
- [Specify how to handle different audiences]

## When Providing Solutions
1. [Step-by-step approach the assistant should follow]
2. [Usually 6-8 numbered steps]
3. [Include analysis, implementation, and validation]

## Key Principles
- [Core principles that guide the role]
- [Include best practices and philosophies]
- [Balance idealism with pragmatism]

## [Optional: Additional Section]
- [Some roles may need an extra section]
- [e.g., "Architectural Thinking" or "Testing Philosophy"]
```

#### 3. Writing Guidelines

- **Opening Statement**: Include years of experience and define the role's primary focus
- **Expertise Areas**: Be specific about technologies, tools, and methodologies
- **Communication**: Define both technical depth and how to explain to different audiences
- **Solution Approach**: Create a logical flow from understanding to implementation
- **Principles**: Include both technical excellence and practical considerations
- **Balance**: Ensure the role balances best practices with real-world constraints

#### 4. Consistency Checks

- Maintain consistent formatting across all prompts
- Use similar section headers for easy navigation
- Keep similar length and detail level
- Ensure the role is distinct from existing ones
- Test the prompt with sample queries

## Getting Started

1. Clone the repository
2. Run `make environment-create`
3. Add new prompts to `prompts/` directory
4. Test loading with Python API
5. Use `make validate-branch` before commits

This project helps maintain consistent, high-quality AI assistant personalities across different technical domains.