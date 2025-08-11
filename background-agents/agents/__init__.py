"""
Background AI Agents Package for XFG STARK Project

This package contains all background AI agents configured to act as elite senior developers
with expert-level knowledge in cryptography and Rust programming.

All agents maintain the highest standards for:
- Cryptographic security
- Rust code quality  
- STARK proof implementation
- Zero-knowledge protocol correctness
- Performance optimization
"""

from .base_agent import BaseBackgroundAgent
from .coordination_monitor import CoordinationMonitorAgent
from .code_quality_guardian import CodeQualityGuardianAgent
from .security_sentinel import SecuritySentinelAgent
from .performance_monitor import PerformanceMonitorAgent
from .documentation_assistant import DocumentationAssistantAgent
from .integration_bridge import IntegrationBridgeAgent

__all__ = [
    "BaseBackgroundAgent",
    "CoordinationMonitorAgent", 
    "CodeQualityGuardianAgent",
    "SecuritySentinelAgent",
    "PerformanceMonitorAgent",
    "DocumentationAssistantAgent",
    "IntegrationBridgeAgent"
]

__version__ = "1.0.0"
__author__ = "XFG STARK Background Agents Team"
__description__ = "Elite Senior Developer Background Agents for XFG STARK Project"
