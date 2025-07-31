"""Tests for prompt loading functionality."""
import pytest
from pathlib import Path
from ai_assistant_roles.prompts import load_prompt, list_prompts, prompt_exists


@pytest.mark.unit
def test_load_prompt_success():
    """Test loading an existing prompt."""
    prompt = load_prompt("backend-engineer")
    assert isinstance(prompt, str)
    assert "Backend Engineer" in prompt
    assert len(prompt) > 100  # Should have substantial content


@pytest.mark.unit
def test_load_prompt_not_found():
    """Test loading a non-existent prompt."""
    with pytest.raises(FileNotFoundError, match="Prompt not found: non-existent-role"):
        load_prompt("non-existent-role")


@pytest.mark.unit
def test_list_prompts():
    """Test listing available prompts."""
    prompts = list_prompts()
    assert isinstance(prompts, list)
    assert len(prompts) >= 3  # We created at least 3 prompts
    assert "backend-engineer" in prompts
    assert "data-scientist" in prompts
    assert "code-reviewer" in prompts
    # Should be sorted
    assert prompts == sorted(prompts)


@pytest.mark.unit
def test_prompt_exists():
    """Test checking if prompts exist."""
    assert prompt_exists("backend-engineer") is True
    assert prompt_exists("data-scientist") is True
    assert prompt_exists("non-existent-role") is False


@pytest.mark.unit
def test_custom_prompts_directory(tmp_path):
    """Test using a custom prompts directory."""
    # Create a custom prompts directory
    custom_dir = tmp_path / "custom_prompts"
    custom_dir.mkdir()
    
    # Create a test prompt
    test_prompt = custom_dir / "test-role.md"
    test_prompt.write_text("# Test Role\n\nThis is a test prompt.")
    
    # Test loading from custom directory
    prompt = load_prompt("test-role", prompts_dir=custom_dir)
    assert "Test Role" in prompt
    
    # Test listing from custom directory
    prompts = list_prompts(prompts_dir=custom_dir)
    assert prompts == ["test-role"]
    
    # Test exists with custom directory
    assert prompt_exists("test-role", prompts_dir=custom_dir) is True
    assert prompt_exists("other-role", prompts_dir=custom_dir) is False


@pytest.mark.unit
def test_empty_prompts_directory(tmp_path):
    """Test behavior with empty prompts directory."""
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    
    prompts = list_prompts(prompts_dir=empty_dir)
    assert prompts == []


@pytest.mark.unit
def test_nonexistent_prompts_directory(tmp_path):
    """Test behavior with non-existent prompts directory."""
    nonexistent_dir = tmp_path / "does_not_exist"
    
    prompts = list_prompts(prompts_dir=nonexistent_dir)
    assert prompts == []