"""
Logger Setup for Background AI Agents

Configures structured logging for all background agents with elite senior developer standards.
"""

import logging
import sys
from pathlib import Path
from typing import Optional
import structlog

def setup_logging(logger_name: str, log_level: str = "INFO", log_file: Optional[str] = None) -> structlog.BoundLogger:
    """
    Setup structured logging for background agents.
    
    Args:
        logger_name: Name of the logger
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file path
        
    Returns:
        Configured structured logger
    """
    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    # Configure structlog for elite standards
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    # Setup standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper())
    )
    
    # Add file handler if specified
    if log_file:
        log_file_path = logs_dir / log_file
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(logging.Formatter("%(message)s"))
        logging.getLogger().addHandler(file_handler)
    
    # Get the structured logger
    logger = structlog.get_logger(logger_name)
    
    # Add elite context to all log messages
    logger = logger.bind(
        elite_developer=True,
        expertise_level="expert",
        cryptography_expert=True,
        rust_expert=True,
        stark_proofs_expert=True
    )
    
    return logger

def setup_agent_logger(agent_name: str, log_level: str = "INFO") -> structlog.BoundLogger:
    """
    Setup logger for a specific agent with elite standards.
    
    Args:
        agent_name: Name of the agent
        log_level: Logging level
        
    Returns:
        Agent-specific structured logger
    """
    log_file = f"{agent_name}.log"
    return setup_logging(agent_name, log_level, log_file)

def get_elite_logger_context() -> dict:
    """
    Get standard elite developer context for logging.
    
    Returns:
        Dictionary with elite developer context
    """
    return {
        "role": "elite_senior_developer",
        "expertise_level": "expert",
        "specializations": [
            "cryptography",
            "rust_programming",
            "stark_proofs", 
            "zero_knowledge_proofs",
            "winterfell_framework"
        ],
        "code_standards": "production_grade",
        "security_mindset": "cryptographic_grade",
        "project": "XFG_STARK_Agent_Coordination"
    }
