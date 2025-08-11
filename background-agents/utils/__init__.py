"""
Utilities Package for Background AI Agents

This package contains utility modules for the background AI agents system:
- Configuration loading and validation
- Logging setup and management
- Common utilities and helpers
"""

from .config_loader import ConfigLoader
from .logger_setup import setup_logging, setup_agent_logger, get_elite_logger_context

__all__ = [
    "ConfigLoader",
    "setup_logging",
    "setup_agent_logger", 
    "get_elite_logger_context"
]

__version__ = "1.0.0"
__author__ = "XFG STARK Background Agents Team"
