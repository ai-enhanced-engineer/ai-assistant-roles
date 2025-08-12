# Integration Patterns

**Work in Progress** - This guide contains integration patterns and code examples for using AI Assistant Roles programmatically.

## Overview

The prompts in this repository can be integrated into your applications programmatically. Below are examples for common AI frameworks and APIs.

## OpenAI API

```python
from openai import OpenAI
# Assuming you have a function to load prompts
# from ai_assistant_roles import load_prompt

client = OpenAI()
system_prompt = load_prompt("software-architect")

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
# from ai_assistant_roles import load_prompt

client = anthropic.Anthropic()
system_prompt = load_prompt("backend-engineer")

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
# from ai_assistant_roles import load_prompt

llm = ChatOpenAI(model="gpt-4")
system_prompt = load_prompt("data-scientist")

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
# from ai_assistant_roles import load_prompt

system_prompt = load_prompt("research-engineer")

llm = OpenAI(model="gpt-4", system_prompt=system_prompt)
service_context = ServiceContext.from_defaults(llm=llm)
```

## Python API (Coming Soon)

A Python package for programmatic access to these prompts is under development. It will provide:

- `load_prompt(role)` - Load a prompt by role name
- `list_prompts()` - List all available roles
- `prompt_exists(role)` - Check if a role exists
- `PromptManager` - Advanced prompt management with context injection

## Manual Integration

For now, you can manually integrate these prompts by:

1. Reading the markdown files directly from the `roles/` directory
2. Using the prompt content as system messages in your AI applications
3. Customizing prompts based on your specific needs

## Contributing

If you have integration examples for other frameworks or improvements to these patterns, please submit a pull request!