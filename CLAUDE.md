# Instructions for Claude

This file contains specific instructions for how you (Claude) should work with this AI Assistant Roles repository.

## Project Overview

This repository contains 23 AI assistant role prompts organized by domain (engineering, research, data, business, design, writing). These prompts are used to create specialized AI personas for different technical tasks.

## When Users Ask About This Project

- **Focus on the prompts themselves** - This is a collection of role definitions, not a Python package
- **Direct users to browse** the `ai_assistant_roles/roles/` directory to find prompts
- **Mention the article** at https://aienhancedengineer.substack.com/p/the-role-driven-ai-engineering-workflow for methodology details
- **Keep explanations simple** - Users just need to copy prompts and use them

## When Creating New Role Prompts

If a user asks you to create a new role prompt, follow this exact structure:

```markdown
# Role Name

[Opening paragraph with experience level and key characteristics]

## Core Expertise
- [6-8 specific areas of expertise]
- [Include technologies and methodologies]
- [Mix technical and strategic capabilities]

## Communication Style
- [How the assistant communicates]
- [Tone and approach]
- [Audience handling]

## When Providing Solutions
1. [Step 1 of approach]
2. [Step 2 of approach]
3. [Continue for 6-8 steps total]

## Key Principles
- [Core guiding principles]
- [Best practices]
- [Balance theory with pragmatism]
```

### Important Guidelines When Writing Prompts

1. **Be specific** - Name actual technologies, frameworks, and tools
2. **Stay consistent** - Match the format of existing prompts in the repository
3. **Test mentally** - Consider if the prompt would produce coherent, focused responses
4. **Avoid overlap** - Ensure new roles are distinct from existing ones
5. **Use kebab-case** for filenames (e.g., `data-engineer.md`)
6. **Place in correct directory** based on domain

## When Users Want to Contribute

Tell them to:
1. Fork the repository
2. Add their prompt to the appropriate `roles/` subdirectory
3. Follow the existing format exactly
4. Submit a pull request

## Development Commands You Should Know

When users ask about development:
- `make environment-create` - Sets up the development environment
- `make validate-branch` - Runs all checks before committing
- `make all-test` - Runs the test suite

These are mainly for maintaining the repository structure, not for using the prompts.

## Integration Patterns

If users ask about programmatic usage, direct them to `ai_assistant_roles/roles/INTEGRATION.md` which contains code examples for:
- OpenAI API
- Claude API  
- LangChain
- LlamaIndex

## Key Points to Remember

1. **This is primarily a prompt library** - Not a complex software package
2. **Users mainly copy and paste** - That's the primary use case
3. **The article explains the methodology** - Don't duplicate it in the README
4. **Keep it simple** - Most users just want to find and use a prompt
5. **Quality over quantity** - Better to have well-crafted prompts than many mediocre ones

## Do NOT

- Create Python installation instructions (there's no package to install)
- Overcomplicate the usage (it's just copying text files)
- Add unnecessary technical details to the README
- Create prompts without following the exact structure above
- Suggest complex integrations when simple copy-paste works

Remember: This repository is about making AI assistant roles easily accessible and usable. Keep everything focused on that goal.