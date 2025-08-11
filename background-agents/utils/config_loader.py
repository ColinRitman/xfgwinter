"""
Configuration Loader for Background AI Agents

Handles loading and validation of agent configurations with elite senior developer standards.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
import structlog

class ConfigLoader:
    """
    Configuration loader for background agents with elite standards validation.
    
    Ensures all configurations meet the requirements for elite senior developers
    with expert cryptography and Rust knowledge.
    """
    
    def __init__(self):
        self.logger = structlog.get_logger("config_loader")
    
    def load_config(self, config_path: str) -> Dict[str, Any]:
        """
        Load configuration from file with elite standards validation.
        
        Args:
            config_path: Path to configuration file
            
        Returns:
            Validated configuration dictionary
            
        Raises:
            ValueError: If configuration doesn't meet elite standards
        """
        config_file = Path(config_path)
        
        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            # Validate elite standards
            self._validate_elite_standards(config)
            
            # Load environment variables
            config = self._load_environment_vars(config)
            
            self.logger.info("Configuration loaded successfully", 
                           config_path=config_path,
                           elite_standards="validated")
            
            return config
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in configuration file: {e}")
        except Exception as e:
            raise ValueError(f"Error loading configuration: {e}")
    
    def _validate_elite_standards(self, config: Dict[str, Any]) -> None:
        """
        Validate that configuration meets elite senior developer standards.
        
        Args:
            config: Configuration dictionary to validate
            
        Raises:
            ValueError: If standards are not met
        """
        # Check for required agent identity
        if "agent_identity" not in config:
            raise ValueError("Configuration missing agent_identity section")
        
        identity = config["agent_identity"]
        
        # Validate role
        if identity.get("role") != "elite_senior_developer":
            raise ValueError("Agent role must be 'elite_senior_developer'")
        
        # Validate expertise level
        if identity.get("seniority_level") != "expert":
            raise ValueError("Seniority level must be 'expert'")
        
        # Validate required expertise areas
        required_expertise = [
            "cryptography", "rust", "stark_proofs", 
            "zero_knowledge_proofs", "winterfell"
        ]
        
        expertise = identity.get("expertise", [])
        missing_expertise = [exp for exp in required_expertise if exp not in expertise]
        
        if missing_expertise:
            raise ValueError(f"Missing required expertise: {missing_expertise}")
        
        # Validate specialization
        if identity.get("specialization") != "cryptographic_implementation":
            raise ValueError("Specialization must be 'cryptographic_implementation'")
        
        self.logger.info("Elite standards validation passed",
                        expertise=expertise,
                        specialization=identity.get("specialization"))
    
    def _load_environment_vars(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Load environment variables into configuration.
        
        Args:
            config: Configuration dictionary
            
        Returns:
            Configuration with environment variables loaded
        """
        # Load from .env file if it exists
        env_file = Path(".env")
        if env_file.exists():
            from dotenv import load_dotenv
            load_dotenv()
        
        # Replace environment variable placeholders
        config_str = json.dumps(config)
        
        # Replace ${VAR_NAME} patterns with environment variables
        import re
        env_pattern = r'\$\{([^}]+)\}'
        
        def replace_env_var(match):
            var_name = match.group(1)
            value = os.getenv(var_name)
            if value is None:
                self.logger.warning(f"Environment variable not found: {var_name}")
                return match.group(0)  # Keep original if not found
            return value
        
        config_str = re.sub(env_pattern, replace_env_var, config_str)
        
        # Parse back to dictionary
        try:
            return json.loads(config_str)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing configuration with environment variables: {e}")
    
    def validate_agent_config(self, agent_name: str, agent_config: Dict[str, Any]) -> bool:
        """
        Validate specific agent configuration.
        
        Args:
            agent_name: Name of the agent
            agent_config: Agent-specific configuration
            
        Returns:
            True if configuration is valid
        """
        try:
            # Check if agent is enabled
            if not agent_config.get("enabled", False):
                self.logger.info(f"Agent {agent_name} is disabled")
                return True
            
            # Validate expertise requirements
            expertise_req = agent_config.get("expertise_requirements", {})
            required_levels = ["expert"]
            
            for req, level in expertise_req.items():
                if level not in required_levels:
                    self.logger.warning(f"Agent {agent_name} expertise level '{level}' for '{req}' is not at expert level")
            
            self.logger.info(f"Agent {agent_name} configuration validated")
            return True
            
        except Exception as e:
            self.logger.error(f"Agent {agent_name} configuration validation failed", error=str(e))
            return False
    
    def get_agent_config(self, config: Dict[str, Any], agent_name: str) -> Optional[Dict[str, Any]]:
        """
        Get configuration for a specific agent.
        
        Args:
            config: Full configuration dictionary
            agent_name: Name of the agent
            
        Returns:
            Agent-specific configuration or None if not found
        """
        return config.get(agent_name)
    
    def save_config(self, config: Dict[str, Any], config_path: str) -> None:
        """
        Save configuration to file.
        
        Args:
            config: Configuration dictionary
            config_path: Path to save configuration
        """
        config_file = Path(config_path)
        config_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        self.logger.info("Configuration saved", config_path=config_path)
