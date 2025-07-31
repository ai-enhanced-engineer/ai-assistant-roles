# AI Base Template - Development Guide

A Python template for ML/AI projects with FastAPI, designed for rapid prototyping and clean architecture.

## Project Structure

```
ai-base-template/
├── ai_base_template/      # Main application code
│   ├── __init__.py
│   └── main.py           # FastAPI entry point
├── tests/                # Test suite
│   └── test_main.py
├── research/             # Notebooks and experiments
│   └── EDA.ipynb        # Exploratory data analysis
├── testing/              # API testing utilities
├── Makefile             # Development automation
└── pyproject.toml       # Project config & dependencies
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

## Getting Started

1. Clone the template
2. Run `make environment-create`
3. Start coding in `ai_base_template/`
4. Add tests in `tests/`
5. Use `make validate-branch` before commits

This template provides a solid foundation for ML/AI projects with all the modern Python tooling pre-configured.