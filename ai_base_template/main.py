"""Main module for AI Base Template service"""


def hello_world() -> str:
    """Simple function to test the package."""
    return "Hello from AI Base Template!"


def get_version() -> str:
    """Get the package version."""
    from . import __version__
    return __version__