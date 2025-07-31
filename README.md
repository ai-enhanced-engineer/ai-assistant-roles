# AI Base Template

A minimal Python template for AI/ML projects with modern tooling, designed to help you start projects faster with best practices built-in.

## What is this?

This is a simple, clean Python project template that comes pre-configured with:
- Modern Python development tools
- ML/Data science libraries
- Testing infrastructure
- Code quality automation
- Clean project structure

Perfect for starting new AI/ML experiments, research projects, or proof-of-concepts without setting up all the tooling from scratch.

## Features

- 🐍 **Python 3.12** with modern packaging via uv
- 🧪 **Testing setup** with pytest (unit, functional, integration markers)
- 🔧 **Code quality** with Ruff (formatting + linting) and MyPy (type checking)
- 📊 **ML-ready** with pre-configured data science libraries
- 📝 **Type hints** and Pydantic for data validation
- 🔍 **Logging** with loguru for better debugging
- ⚡ **Make commands** for common development tasks
- 📓 **Jupyter** support for experimentation

## Quick Start

### Prerequisites
- Python 3.12+
- Make

### Setup

1. Clone or use this template:
```bash
git clone <repository-url> my-ai-project
cd my-ai-project
```

2. Create environment and install dependencies:
```bash
make environment-create
```

3. Start coding! Your code goes in `ai_base_template/`

4. Run tests to make sure everything works:
```bash
make unit-test
```

## Project Structure

```
ai-base-template/
├── ai_base_template/      # Your Python package
│   ├── __init__.py       # Package initialization
│   └── main.py           # Example module
├── tests/                # Test files
│   └── test_main.py      # Example tests
├── research/             # Notebooks and experiments
│   └── EDA.ipynb        # Exploratory data analysis
├── testing/              # Test utilities and scripts
├── Makefile             # Development commands
├── pyproject.toml       # Project configuration
├── CLAUDE.md            # Development guide
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Development Workflow

### Essential Commands

```bash
# Environment
make environment-create   # First-time setup
make environment-sync     # Update after changing dependencies

# Code Quality
make format              # Auto-format code
make lint               # Fix linting issues
make type-check         # Check types
make validate-branch    # Run all checks (before committing)

# Testing
make unit-test          # Run unit tests
make functional-test    # Run functional tests
make all-test          # Run all tests with coverage
```

### Adding Code

1. Add your modules to `ai_base_template/`
2. Write corresponding tests in `tests/`
3. Use type hints for better code quality
4. Run `make validate-branch` before committing

## Pre-installed Libraries

### ML/Data Science
- **numpy** - Numerical computing
- **pandas** - Data manipulation
- **scikit-learn** - Classical ML algorithms
- **XGBoost** - Gradient boosting
- **LightGBM** - Fast gradient boosting
- **PyTorch** - Deep learning
- **SHAP** - Model explainability

### Development Tools
- **pytest** - Testing framework
- **ruff** - Fast Python linter/formatter
- **mypy** - Static type checker
- **pre-commit** - Git hooks
- **loguru** - Better logging
- **python-dotenv** - Environment variables
- **jupyter** - Interactive notebooks

## Configuration

Use environment variables for configuration. Create a `.env` file in the project root:

```env
# Example .env
LOG_LEVEL=DEBUG
DATA_PATH=./data
MODEL_PATH=./models
RANDOM_SEED=42
```

Load them in your code:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Testing Strategy

The template includes three test levels:

```python
@pytest.mark.unit        # Fast, isolated tests
@pytest.mark.functional  # Feature/workflow tests
@pytest.mark.integration # Tests with external dependencies
```

Run specific test types:
```bash
make unit-test
make functional-test
make integration-test
```

## Starting Your Project

1. **Rename the package**: Change `ai_base_template` to your project name
2. **Update pyproject.toml**: Set your project name, version, and description
3. **Clean up examples**: Remove the example code in `main.py`
4. **Start building**: Add your own modules and logic
5. **Document as you go**: Update this README with your project specifics

## Best Practices Included

- ✅ Modern Python packaging with uv
- ✅ Comprehensive .gitignore
- ✅ Pre-configured linting and formatting
- ✅ Type checking setup
- ✅ Test structure with markers
- ✅ Makefile automation
- ✅ Clean project layout
- ✅ Development guide (CLAUDE.md)

## Tips

- Use `make validate-branch` before every commit
- Keep dependencies in `pyproject.toml`
- Write tests as you code
- Use type hints everywhere
- Check CLAUDE.md for detailed guidelines

## License

[Your License Here]

---

Built to help you start AI/ML projects faster 🚀