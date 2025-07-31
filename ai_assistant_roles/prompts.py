"""Simple prompt loading system for AI assistant roles."""
from pathlib import Path
from typing import Optional


def load_prompt(role: str, prompts_dir: Optional[Path] = None) -> str:
    """Load a prompt by role name.
    
    Args:
        role: Name of the role (e.g., 'backend-engineer', 'data-scientist')
        prompts_dir: Optional custom prompts directory path
        
    Returns:
        The prompt content as a string
        
    Raises:
        FileNotFoundError: If the prompt file doesn't exist
    """
    if prompts_dir is None:
        # Default to prompts directory relative to project root
        prompts_dir = Path(__file__).parent.parent / "prompts"
    
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
        prompts_dir = Path(__file__).parent.parent / "prompts"
    
    if not prompts_dir.exists():
        return []
    
    return sorted([p.stem for p in prompts_dir.glob("*.md")])


def prompt_exists(role: str, prompts_dir: Optional[Path] = None) -> bool:
    """Check if a prompt exists for the given role.
    
    Args:
        role: Name of the role
        prompts_dir: Optional custom prompts directory path
        
    Returns:
        True if the prompt exists, False otherwise
    """
    if prompts_dir is None:
        prompts_dir = Path(__file__).parent.parent / "prompts"
    
    prompt_file = prompts_dir / f"{role}.md"
    return prompt_file.exists()