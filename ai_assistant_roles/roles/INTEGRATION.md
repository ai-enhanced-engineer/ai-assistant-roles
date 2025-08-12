# Integration Patterns

**Work in Progress** - This guide contains integration patterns and code examples for using AI Assistant Roles programmatically.

## Overview

The prompts in this repository can be integrated into your applications by reading the markdown files directly. Below are examples for common AI frameworks and APIs.

## Manual Integration

Currently, integrate these prompts by reading the markdown files directly:

```python
# Read a prompt file manually
def load_prompt(role_name):
    """Load a prompt from the roles directory."""
    import os
    
    # Define the base path to roles
    base_path = "ai_assistant_roles/roles"
    
    # Search for the role in different categories
    categories = ["engineering", "research", "data", "business", "design", "writing"]
    
    for category in categories:
        file_path = os.path.join(base_path, category, f"{role_name}.md")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read()
    
    raise FileNotFoundError(f"Role '{role_name}' not found")
```

## OpenAI API

```python
from openai import OpenAI

# Read the prompt file
with open('ai_assistant_roles/roles/engineering/software-architect.md', 'r') as f:
    system_prompt = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Design a scalable API gateway"}
    ]
)
```

## Claude API

```python
import anthropic

# Read the prompt file
with open('ai_assistant_roles/roles/engineering/backend-engineer.md', 'r') as f:
    system_prompt = f.read()

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "Implement a rate limiter in Python"}
    ]
)
```

## LangChain

```python
from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI

# Read the prompt file
with open('ai_assistant_roles/roles/data/data-scientist.md', 'r') as f:
    system_prompt = f.read()

llm = ChatOpenAI(model="gpt-4")
messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content="Analyze this dataset for patterns")
]

response = llm(messages)
```

## LlamaIndex

```python
from llama_index import ServiceContext
from llama_index.llms import OpenAI

# Read the prompt file
with open('ai_assistant_roles/roles/research/research-engineer.md', 'r') as f:
    system_prompt = f.read()

llm = OpenAI(model="gpt-4", system_prompt=system_prompt)
service_context = ServiceContext.from_defaults(llm=llm)
```

## Helper Function Example

Here's a complete example of a helper function to load prompts:

```python
import os
from pathlib import Path

class PromptLoader:
    def __init__(self, base_path="ai_assistant_roles/roles"):
        self.base_path = Path(base_path)
        self.categories = ["engineering", "research", "data", "business", "design", "writing"]
    
    def load_prompt(self, role_name):
        """Load a prompt by role name."""
        for category in self.categories:
            file_path = self.base_path / category / f"{role_name}.md"
            if file_path.exists():
                return file_path.read_text()
        raise FileNotFoundError(f"Role '{role_name}' not found")
    
    def list_prompts(self):
        """List all available prompts."""
        prompts = []
        for category in self.categories:
            category_path = self.base_path / category
            if category_path.exists():
                for file in category_path.glob("*.md"):
                    prompts.append(file.stem)
        return prompts

# Usage
loader = PromptLoader()
prompt = loader.load_prompt("software-architect")
all_roles = loader.list_prompts()
```

## Python Package (Future)

A Python package for easier programmatic access is planned for future development. It will provide:

- `load_prompt(role)` - Load a prompt by role name
- `list_prompts()` - List all available roles
- `prompt_exists(role)` - Check if a role exists
- `PromptManager` - Advanced prompt management with context injection

## Contributing

If you have integration examples for other frameworks or improvements to these patterns, please submit a pull request!