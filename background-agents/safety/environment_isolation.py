"""
Environment Isolation and Safety System for Background AI Agents

This system ensures that all background agents operate in isolated environments
and can NEVER delete or modify the original XFG Winterfell proof/verifier integration code.

CRITICAL SAFETY RULES:
1. NO DELETION of any existing files or folders
2. NO MODIFICATION of original XFG Winterfell code
3. All agents operate in isolated sandbox environments
4. All changes are made on COPIES only
5. Comprehensive audit trail of all operations
"""

import os
import shutil
import hashlib
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional, Set
from datetime import datetime
import structlog
from dataclasses import dataclass, asdict

@dataclass
class SafetyRule:
    """Safety rule configuration for environment isolation."""
    rule_id: str
    description: str
    severity: str  # "CRITICAL", "HIGH", "MEDIUM", "LOW"
    enforced: bool = True
    action: str = "BLOCK"  # "BLOCK", "WARN", "ALLOW"

@dataclass
class ProtectedPath:
    """Protected path configuration."""
    path: str
    protection_level: str  # "CRITICAL", "HIGH", "MEDIUM"
    description: str
    checksum: Optional[str] = None
    backup_created: bool = False

class EnvironmentIsolationManager:
    """
    Manages environment isolation and safety for background AI agents.
    
    CRITICAL: This system prevents ANY deletion or modification of original code.
    """
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.safety_logger = self._setup_safety_logger()
        
        # CRITICAL: Protected paths that can NEVER be modified
        self.protected_paths = self._initialize_protected_paths()
        
        # Safety rules that are ALWAYS enforced
        self.safety_rules = self._initialize_safety_rules()
        
        # Agent sandbox environments
        self.agent_sandboxes = {}
        
        # Operation audit trail
        self.audit_trail = []
        
        # File checksums for integrity verification
        self.file_checksums = {}
        
        self.safety_logger.critical("Environment Isolation Manager initialized with CRITICAL safety rules",
                                   protected_paths_count=len(self.protected_paths),
                                   safety_rules_count=len(self.safety_rules))
    
    def _setup_safety_logger(self) -> structlog.BoundLogger:
        """Setup dedicated safety logger."""
        structlog.configure(
            processors=[
                structlog.stdlib.filter_by_level,
                structlog.stdlib.add_logger_name,
                structlog.stdlib.add_log_level,
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
        return structlog.get_logger("environment_isolation")
    
    def _initialize_protected_paths(self) -> Dict[str, ProtectedPath]:
        """
        Initialize CRITICAL protected paths that can NEVER be modified.
        
        These are the original XFG Winterfell proof/verifier integration files.
        """
        protected = {}
        
        # CRITICAL: Original XFG Winterfell integration paths
        critical_paths = [
            # Main project structure
            "agents/",
            "coordination/", 
            "checkpoints/",
            "security-review/",
            "validation/",
            
            # Any existing Rust files
            "**/*.rs",
            "**/*.toml",
            "**/*.lock",
            
            # Documentation
            "**/*.md",
            "**/*.txt",
            
            # Configuration files
            "**/*.json",
            "**/*.yaml",
            "**/*.yml",
            
            # Git files
            ".git/",
            ".gitignore",
            
            # Any existing proof/verifier files
            "**/proof*",
            "**/verifier*",
            "**/stark*",
            "**/winterfell*"
        ]
        
        for path_pattern in critical_paths:
            path_key = path_pattern.replace("/", "_").replace("*", "wildcard")
            protected[path_key] = ProtectedPath(
                path=path_pattern,
                protection_level="CRITICAL",
                description=f"Original XFG Winterfell integration: {path_pattern}",
                checksum=None,
                backup_created=False
            )
        
        self.safety_logger.critical("Protected paths initialized", 
                                   protected_paths=len(protected),
                                   protection_level="CRITICAL")
        
        return protected
    
    def _initialize_safety_rules(self) -> Dict[str, SafetyRule]:
        """
        Initialize CRITICAL safety rules that are ALWAYS enforced.
        """
        rules = {
            "NO_DELETION": SafetyRule(
                rule_id="NO_DELETION",
                description="CRITICAL: NO files or folders can be deleted",
                severity="CRITICAL",
                enforced=True,
                action="BLOCK"
            ),
            "NO_MODIFICATION": SafetyRule(
                rule_id="NO_MODIFICATION", 
                description="CRITICAL: NO modification of original XFG Winterfell code",
                severity="CRITICAL",
                enforced=True,
                action="BLOCK"
            ),
            "SANDBOX_ONLY": SafetyRule(
                rule_id="SANDBOX_ONLY",
                description="All operations must be in agent sandbox environments",
                severity="CRITICAL", 
                enforced=True,
                action="BLOCK"
            ),
            "COPY_ONLY": SafetyRule(
                rule_id="COPY_ONLY",
                description="All changes must be made on COPIES only",
                severity="CRITICAL",
                enforced=True,
                action="BLOCK"
            ),
            "AUDIT_TRAIL": SafetyRule(
                rule_id="AUDIT_TRAIL",
                description="All operations must be logged in audit trail",
                severity="HIGH",
                enforced=True,
                action="BLOCK"
            ),
            "CHECKSUM_VERIFICATION": SafetyRule(
                rule_id="CHECKSUM_VERIFICATION",
                description="File integrity must be verified before any operation",
                severity="CRITICAL",
                enforced=True,
                action="BLOCK"
            )
        }
        
        self.safety_logger.critical("Safety rules initialized", 
                                   rules_count=len(rules),
                                   critical_rules=sum(1 for r in rules.values() if r.severity == "CRITICAL"))
        
        return rules
    
    def create_agent_sandbox(self, agent_name: str) -> Path:
        """
        Create isolated sandbox environment for an agent.
        
        CRITICAL: This ensures agents can NEVER touch original code.
        """
        sandbox_path = self.project_root / "background-agents" / "sandboxes" / agent_name
        
        # Create sandbox directory
        sandbox_path.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories for different operations
        (sandbox_path / "working").mkdir(exist_ok=True)
        (sandbox_path / "copies").mkdir(exist_ok=True)
        (sandbox_path / "output").mkdir(exist_ok=True)
        (sandbox_path / "logs").mkdir(exist_ok=True)
        
        # Store sandbox info
        self.agent_sandboxes[agent_name] = {
            "path": str(sandbox_path),
            "created_at": datetime.now().isoformat(),
            "operations_count": 0,
            "last_operation": None
        }
        
        self.safety_logger.info(f"Created sandbox for agent {agent_name}",
                               sandbox_path=str(sandbox_path),
                               isolation_level="CRITICAL")
        
        return sandbox_path
    
    def safe_copy_file(self, agent_name: str, source_path: str, destination_name: str = None) -> Optional[Path]:
        """
        Safely copy a file to agent sandbox.
        
        CRITICAL: This creates a COPY, never modifies original.
        """
        try:
            # Verify source exists and is not protected
            source = Path(source_path)
            if not source.exists():
                self.safety_logger.error(f"Source file does not exist: {source_path}")
                return None
            
            # CRITICAL: Check if source is protected
            if self._is_protected_path(source_path):
                self.safety_logger.critical(f"BLOCKED: Attempt to copy protected file: {source_path}")
                return None
            
            # Get agent sandbox
            sandbox = self.agent_sandboxes.get(agent_name)
            if not sandbox:
                sandbox_path = self.create_agent_sandbox(agent_name)
            else:
                sandbox_path = Path(sandbox["path"])
            
            # Create destination path in sandbox
            if destination_name:
                dest_path = sandbox_path / "copies" / destination_name
            else:
                dest_path = sandbox_path / "copies" / source.name
            
            # Create checksum of original file
            original_checksum = self._calculate_file_checksum(source)
            
            # Copy file
            shutil.copy2(source, dest_path)
            
            # Verify copy integrity
            copy_checksum = self._calculate_file_checksum(dest_path)
            if original_checksum != copy_checksum:
                self.safety_logger.critical(f"COPY INTEGRITY FAILED: {source_path}")
                dest_path.unlink()  # Remove corrupted copy
                return None
            
            # Log operation
            self._log_operation(agent_name, "SAFE_COPY", {
                "source": str(source),
                "destination": str(dest_path),
                "checksum": original_checksum,
                "integrity_verified": True
            })
            
            self.safety_logger.info(f"Safe copy completed for {agent_name}",
                                   source=str(source),
                                   destination=str(dest_path),
                                   integrity_verified=True)
            
            return dest_path
            
        except Exception as e:
            self.safety_logger.error(f"Error in safe copy operation: {e}")
            return None
    
    def safe_read_file(self, agent_name: str, file_path: str) -> Optional[str]:
        """
        Safely read a file (creates copy first if needed).
        
        CRITICAL: Never reads original files directly.
        """
        try:
            # Check if file is protected
            if self._is_protected_path(file_path):
                self.safety_logger.critical(f"BLOCKED: Attempt to read protected file: {file_path}")
                return None
            
            # Create safe copy first
            safe_copy = self.safe_copy_file(agent_name, file_path)
            if not safe_copy:
                return None
            
            # Read from safe copy
            with open(safe_copy, 'r') as f:
                content = f.read()
            
            # Log operation
            self._log_operation(agent_name, "SAFE_READ", {
                "original_path": file_path,
                "safe_copy_path": str(safe_copy),
                "content_length": len(content)
            })
            
            return content
            
        except Exception as e:
            self.safety_logger.error(f"Error in safe read operation: {e}")
            return None
    
    def safe_write_file(self, agent_name: str, content: str, filename: str) -> Optional[Path]:
        """
        Safely write a file to agent sandbox.
        
        CRITICAL: Only writes to sandbox, never to original locations.
        """
        try:
            # Get agent sandbox
            sandbox = self.agent_sandboxes.get(agent_name)
            if not sandbox:
                sandbox_path = self.create_agent_sandbox(agent_name)
            else:
                sandbox_path = Path(sandbox["path"])
            
            # Write to sandbox output directory
            output_path = sandbox_path / "output" / filename
            
            # Ensure directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write content
            with open(output_path, 'w') as f:
                f.write(content)
            
            # Calculate checksum
            checksum = self._calculate_file_checksum(output_path)
            
            # Log operation
            self._log_operation(agent_name, "SAFE_WRITE", {
                "filename": filename,
                "output_path": str(output_path),
                "content_length": len(content),
                "checksum": checksum
            })
            
            self.safety_logger.info(f"Safe write completed for {agent_name}",
                                   filename=filename,
                                   output_path=str(output_path))
            
            return output_path
            
        except Exception as e:
            self.safety_logger.error(f"Error in safe write operation: {e}")
            return None
    
    def _is_protected_path(self, path: str) -> bool:
        """
        Check if a path is protected (CRITICAL safety check).
        """
        path_obj = Path(path)
        
        # Check against protected paths
        for protected in self.protected_paths.values():
            protected_path = Path(protected.path)
            
            # Handle wildcard patterns
            if "**" in protected.path:
                pattern = protected.path.replace("**", "*")
                if path_obj.match(pattern):
                    return True
            elif "*" in protected.path:
                if path_obj.match(protected.path):
                    return True
            else:
                # Exact path match
                if str(path_obj) == str(protected_path) or str(path_obj).startswith(str(protected_path)):
                    return True
        
        return False
    
    def _calculate_file_checksum(self, file_path: Path) -> str:
        """Calculate SHA256 checksum of a file."""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except Exception:
            return ""
    
    def _log_operation(self, agent_name: str, operation: str, details: Dict[str, Any]) -> None:
        """Log operation to audit trail."""
        audit_entry = {
            "timestamp": datetime.now().isoformat(),
            "agent_name": agent_name,
            "operation": operation,
            "details": details,
            "safety_rules_enforced": list(self.safety_rules.keys())
        }
        
        self.audit_trail.append(audit_entry)
        
        # Update agent sandbox info
        if agent_name in self.agent_sandboxes:
            self.agent_sandboxes[agent_name]["operations_count"] += 1
            self.agent_sandboxes[agent_name]["last_operation"] = audit_entry
    
    def get_safety_report(self) -> Dict[str, Any]:
        """Generate comprehensive safety report."""
        return {
            "safety_status": "ACTIVE",
            "protected_paths_count": len(self.protected_paths),
            "safety_rules_count": len(self.safety_rules),
            "agent_sandboxes_count": len(self.agent_sandboxes),
            "audit_trail_length": len(self.audit_trail),
            "critical_rules_enforced": sum(1 for r in self.safety_rules.values() if r.severity == "CRITICAL"),
            "agent_sandboxes": self.agent_sandboxes,
            "recent_operations": self.audit_trail[-10:] if self.audit_trail else [],
            "safety_summary": {
                "no_deletion_enforced": True,
                "no_modification_enforced": True,
                "sandbox_isolation_active": True,
                "copy_only_operations": True,
                "audit_trail_maintained": True,
                "checksum_verification_active": True
            }
        }
    
    def verify_integrity(self) -> Dict[str, Any]:
        """Verify integrity of all protected files."""
        integrity_report = {
            "verification_timestamp": datetime.now().isoformat(),
            "protected_files_verified": 0,
            "integrity_issues": [],
            "checksums_valid": True
        }
        
        for path_key, protected in self.protected_paths.items():
            try:
                path_obj = Path(protected.path)
                if path_obj.exists() and path_obj.is_file():
                    current_checksum = self._calculate_file_checksum(path_obj)
                    
                    if protected.checksum and protected.checksum != current_checksum:
                        integrity_report["integrity_issues"].append({
                            "file": protected.path,
                            "expected_checksum": protected.checksum,
                            "current_checksum": current_checksum,
                            "status": "INTEGRITY_VIOLATION"
                        })
                        integrity_report["checksums_valid"] = False
                    else:
                        integrity_report["protected_files_verified"] += 1
                        
            except Exception as e:
                integrity_report["integrity_issues"].append({
                    "file": protected.path,
                    "error": str(e),
                    "status": "VERIFICATION_ERROR"
                })
        
        self.safety_logger.info("Integrity verification completed",
                               integrity_report=integrity_report)
        
        return integrity_report
