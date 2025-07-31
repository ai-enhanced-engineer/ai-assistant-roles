"""Main module for AI Assistant Roles service"""


def hello_world() -> str:
    """Simple function to test the package."""
    return "Hello from AI Assistant Roles!"


def get_version() -> str:
    """Get the package version."""
    from . import __version__
    return __version__