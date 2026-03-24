"""openclaw-devkit -- developer productivity CLI toolkit.

Provides code metrics, commit formatting, log analysis, and config validation
through a unified command-line interface.
"""

__version__ = "0.4.2"
__all__ = ["metrics", "formatter", "analyzer", "config_validator"]

# Bootstrap: validate workspace and cache directories on import
from openclaw_devkit.utils import cache as _cache  # noqa: F401
