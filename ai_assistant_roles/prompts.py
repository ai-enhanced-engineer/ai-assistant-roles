"""Simple prompt loading system for AI assistant roles."""
from pathlib import Path
from typing import Optional


def load_prompt(role: str, prompts_dir: Optional[Path] = None) -> str:
    """Load a prompt by role name.
    
    Args:
        role: Name of the role (e.g., 'backend-engineer' or 'engineering/backend-engineer')
        prompts_dir: Optional custom prompts directory path
        
    Returns:
        The prompt content as a string
        
    Raises:
        FileNotFoundError: If the prompt file doesn't exist
    """
    if prompts_dir is None:
        # Default to roles directory relative to project root
        prompts_dir = Path(__file__).parent.parent / "roles"
    
    # Handle both flat names and paths with subdirectories
    prompt_file = prompts_dir / f"{role}.md"
    
    if not prompt_file.exists():
        raise FileNotFoundError(f"Prompt not found: {role}")
    
    return prompt_file.read_text(encoding="utf-8")


def list_prompts(prompts_dir: Optional[Path] = None) -> list[str]:
    """List all available prompt roles.
    
    Args:
        prompts_dir: Optional custom prompts directory path
        
    Returns:
        List of available role names (without .md extension)
    """
    if prompts_dir is None:
        prompts_dir = Path(__file__).parent.parent / "roles"
    
    if not prompts_dir.exists():
        return []
    
    # Find all .md files recursively and return relative paths
    prompts = []
    for p in prompts_dir.rglob("*.md"):
        relative_path = p.relative_to(prompts_dir)
        # Remove .md extension and convert to string
        role_name = str(relative_path)[:-3]
        prompts.append(role_name)
    
    return sorted(prompts)


def prompt_exists(role: str, prompts_dir: Optional[Path] = None) -> bool:
    """Check if a prompt exists for the given role.
    
    Args:
        role: Name of the role (with optional subdirectory path)
        prompts_dir: Optional custom prompts directory path
        
    Returns:
        True if the prompt exists, False otherwise
    """
    if prompts_dir is None:
        prompts_dir = Path(__file__).parent.parent / "roles"
    
    prompt_file = prompts_dir / f"{role}.md"
    return prompt_file.exists()