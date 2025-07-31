"""Test module for AI Assistant Roles main functionality"""

import pytest

from ai_assistant_roles.main import get_version, hello_world


def test_hello_world():
    """Test the hello_world function."""
    result = hello_world()
    assert result == "Hello from AI Assistant Roles!"
    assert isinstance(result, str)


def test_get_version():
    """Test the get_version function."""
    version = get_version()
    assert version == "1.0.6"
    assert isinstance(version, str)


@pytest.mark.unit
def test_hello_world_unit():
    """Unit test for hello_world function."""
    assert hello_world() == "Hello from AI Assistant Roles!"


@pytest.mark.functional
def test_package_functionality():
    """Functional test for basic package functionality."""
    # Test that we can import and use the package
    from ai_assistant_roles import __version__
    assert __version__ == "1.0.6"
    
    # Test main functions work
    assert hello_world() == "Hello from AI Assistant Roles!"
    assert get_version() == "1.0.6"