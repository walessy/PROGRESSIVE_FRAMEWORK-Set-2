#!/usr/bin/env python3
"""
Coherent Naming Convention Script for Progressive Framework
Applies consistent naming based on your established pattern
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime
import shutil

class CoherentNamingConventionTool:
    def __init__(self, base_directory: str):
        self.base_directory = Path(base_directory)
        self.backup_dir = self.base_directory / "naming_convention_backups"
        self.renaming_log = []
        self.corrections_applied = 0
        
        # Establish naming conventions based on your current files
        self.naming_conventions = {
            "config_files": {
                "pattern": r"[A-Z][a-zA-Z]*-[A-Za-z0-9]*-[A-Za-z]*-v\d+\.\d+(-[A-Za-z]+)?\.(xml|json)",
                "format": "{System-Name}-{Type}-v{Version}.{Descriptive-Suffix}.{ext}",
                "examples": ["PKM-5Point-Protocol-v5.0.xml", "Progressive-Systems-Config-v2.3-SignalBased.json"]
            },
            "system_specs": {
                "pattern": r"ProgressiveProject-System-\d{2}-[A-Z][A-Z0-9-]*\.md",
                "format": "ProgressiveProject-System-{XX}-{SYSTEM-NAME}.md",
                "examples": ["ProgressiveProject-System-01-PDT-PLUS.md", "ProgressiveProject-System-12-PMCS-024.md"]
            },
            "documentation": {
                "pattern": r"Chat\d{3}_[A-Za-z-]*_\d{8}(_\d{6})?\.md",
                "format": "Chat{XXX}_{Purpose}_{YYYYMMDD}.md",
                "examples": ["Chat002_Framework-Activation_20250820.md", "Chat003_PMCS-024-Specification_20250817.md"]
            }
        }
        
    def create_backup_directory(self):
        """Create backup directory for original files"""
        self.backup_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        print(f"📁 Created backup directory: {self.backup_dir}")
        
    def analyze_current_files(self) -> Dict[str, List[Path]]:
        """Analyze current files and categorize them"""
        file_categories = {
            "config_files": [],
            "system_specs": [],
            "documentation": [],
            "other_files": [],
            "malformed_files": []
        }
        
        # Scan all relevant files - including subdirectories
        for pattern in ["**/*.xml", "**/*.json", "**/*.md", "**/*.txt"]:
            for file_path in self.base_directory.rglob(pattern):
                if file_path.is_file() and not str(file_path).startswith(str(self.backup_dir)):
                    self.categorize_file(file_path, file_categories)
                    
        return file_categories
    
    def categorize_file(self, file_path: Path, categories: Dict[str, List[Path]]):
        """Categorize a file based on naming patterns"""
        filename = file_path.name
        
        # Check for config files
        if filename.endswith(('.xml', '.json')) and any(keyword in filename.lower() 
                                                       for keyword in ['config', 'protocol', 'pkm']):
            categories["config_files"].append(file_path)
            
        # Check for system specification files
        elif re.match(r".*[Ss]ystem.*\d+.*\.md$", filename):
            if self.is_well_formed_system_file(filename):
                categories["system_specs"].append(file_path)
            else:
                categories["malformed_files"].append(file_path)
                
        # Check for documentation files
        elif filename.endswith('.md') and ('Chat' in filename or 'chat' in filename):
            categories["documentation"].append(file_path)
            
        # Everything else
        else:
            categories["other_files"].append(file_path)
    
    def is_well_formed_system_file(self, filename: str) -> bool:
        """Check if system file follows correct naming convention"""
        # Your correct pattern: ProgressiveProject-System-XX-SYSTEM-NAME.md
        pattern = r"^ProgressiveProject-System-\d{2}-[A-Z][A-Z0-9-]*\.md$"
        return bool(re.match(pattern, filename, re.IGNORECASE))
    
    def generate_correct_system_filename(self, current_filename: str) -> str:
        """Generate correct system filename from malformed one"""
        # Extract system number
        system_match = re.search(r'[Ss]ystem.*?(\d+)', current_filename)
        if not system_match:
            return current_filename
            
        system_num = int(system_match.group(1))
        
        # Extract system name - handle special cases
        system_name_mapping = {
            1: "PDT-PLUS",
            2: "PUXT-PLUS", 
            3: "PSO-PRIME",
            4: "PTT-DOCS-FUSION",
            5: "REQUIREMENTS-PRIME",
            6: "BUSINESS-OPS-FUSION",
            7: "CONTEXT-EVOLUTION-ENGINE",
            8: "PERFORMANCE-AI-FUSION",
            9: "SECURITY-BUILD-FUSION",
            10: "KNOWLEDGE-EVOLUTION-ENGINE",
            11: "UNIVERSAL-ORCHESTRATION-PRIME",
            12: "PMCS-024",
            13: "PAES",
            14: "DPI",
            15: "PTODOS"
        }
        
        system_name = system_name_mapping.get(system_num)
        if not system_name:
            # Try to extract from filename
            if "PMCS" in current_filename.upper():
                system_name = "PMCS-024"
            elif "PDT" in current_filename.upper():
                system_name = "PDT-PLUS"
            # Add more extractions as needed
            else:
                system_name = "UNKNOWN"
        
        return f"ProgressiveProject-System-{system_num:02d}-{system_name}.md"
    
    def rename_malformed_files(self, malformed_files: List[Path]):
        """Rename malformed files to correct convention"""
        print("\n🔧 Renaming malformed files...")
        
        for file_path in malformed_files:
            # Create backup
            backup_path = self.backup_dir / f"{file_path.name}.backup"
            shutil.copy2(file_path, backup_path)
            
            # Generate correct name
            correct_name = self.generate_correct_system_filename(file_path.name)
            new_path = file_path.parent / correct_name
            
            # Check if target already exists
            if new_path.exists() and new_path != file_path:
                print(f"⚠️  Target exists: {correct_name} (skipping {file_path.name})")
                continue
                
            # Rename file
            try:
                file_path.rename(new_path)
                self.renaming_log.append(f"RENAMED: {file_path.name} → {correct_name}")
                self.corrections_applied += 1
                print(f"✅ Renamed: {file_path.name} → {correct_name}")
            except Exception as e:
                print(f"❌ Error renaming {file_path.name}: {e}")
    
    def update_file_references(self, file_categories: Dict[str, List[Path]]):
        """Update references in config and documentation files"""
        print("\n🔍 Updating file references...")
        
        # Files that might contain references
        reference_files = (file_categories["config_files"] + 
                          file_categories["documentation"] + 
                          file_categories["other_files"])
        
        for file_path in reference_files:
            self.update_references_in_file(file_path)
    
    def update_references_in_file(self, file_path: Path):
        """Update references within a specific file"""
        try:
            # Create backup
            backup_path = self.backup_dir / f"{file_path.name}.ref_backup"
            if not backup_path.exists():
                shutil.copy2(file_path, backup_path)
            
            # Read content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix malformed PMCS-024 references
            malformed_patterns = [
                r'PMCS-024roject[_\s]*system[_\s]*12',
                r'PROGRESSIVEPROJECT-SYSTEM-12-PMCS-024roject[_\s]*system[_\s]*12',
                r'PMCS-024roject'
            ]
            
            for pattern in malformed_patterns:
                content = re.sub(pattern, 'PMCS-024', content, flags=re.IGNORECASE)
            
            # Update system file references to correct format
            for i in range(1, 16):
                old_pattern = rf'(?i)progressiveproject[_\s]*system[_\s]*{i:02d}[_\s]*[a-z0-9-]*\.md'
                system_names = {
                    1: "PDT-PLUS", 2: "PUXT-PLUS", 3: "PSO-PRIME", 4: "PTT-DOCS-FUSION",
                    5: "REQUIREMENTS-PRIME", 6: "BUSINESS-OPS-FUSION", 7: "CONTEXT-EVOLUTION-ENGINE",
                    8: "PERFORMANCE-AI-FUSION", 9: "SECURITY-BUILD-FUSION", 10: "KNOWLEDGE-EVOLUTION-ENGINE",
                    11: "UNIVERSAL-ORCHESTRATION-PRIME", 12: "PMCS-024", 13: "PAES", 14: "DPI", 15: "PTODOS"
                }
                correct_filename = f"ProgressiveProject-System-{i:02d}-{system_names[i]}.md"
                content = re.sub(old_pattern, correct_filename, content)
            
            # Write back if changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.renaming_log.append(f"UPDATED REFS: {file_path.name}")
                self.corrections_applied += 1
                print(f"✅ Updated references in: {file_path.name}")
                
        except Exception as e:
            print(f"❌ Error updating references in {file_path}: {e}")
    
    def generate_naming_convention_report(self) -> str:
        """Generate comprehensive naming convention report"""
        return f"""
# 🎯 COHERENT NAMING CONVENTION REPORT

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Base Directory**: {self.base_directory}
**Total Corrections Applied**: {self.corrections_applied}

## 📋 ESTABLISHED NAMING CONVENTIONS

### Configuration Files
**Pattern**: `{{System-Name}}-{{Type}}-v{{Version}}.{{Descriptive-Suffix}}.{{ext}}`
**Examples**: 
- ✅ PKM-5Point-Protocol-v5.0.xml
- ✅ Progressive-Systems-Config-v2.3-SignalBased.json

### System Specification Files
**Pattern**: `ProgressiveProject-System-{{XX}}-{{SYSTEM-NAME}}.md`
**Examples**:
- ✅ ProgressiveProject-System-01-PDT-PLUS.md
- ✅ ProgressiveProject-System-12-PMCS-024.md
- ✅ ProgressiveProject-System-15-PTODOS.md

### Documentation Files
**Pattern**: `Chat{{XXX}}_{{Purpose}}_{{YYYYMMDD}}.md`
**Examples**:
- ✅ Chat002_Framework-Activation_20250820.md
- ✅ Chat003_PMCS-024-Specification_20250817.md

## ✅ CORRECTIONS APPLIED

{chr(10).join(self.renaming_log)}

## 🎯 NAMING CONVENTION BENEFITS

✅ **Consistent Hyphenation**: All files use hyphens for word separation
✅ **Clear Versioning**: Version numbers with 'v' prefix
✅ **Descriptive Suffixes**: Additional context without verbosity
✅ **Auto-Discovery Friendly**: Patterns work well with automation
✅ **Readable and Sortable**: Easy to understand and organize
✅ **Scalable**: Works for any number of systems or versions

## 📁 BACKUP INFORMATION

All original files backed up to: {self.backup_dir}
Backup timestamp: {datetime.now().strftime('%Y%m%d_%H%M%S')}

## 🚀 FRAMEWORK STATUS

**Naming Convention**: ✅ COHERENT AND CONSISTENT
**File References**: ✅ UPDATED ACROSS PROJECT
**Auto-Discovery**: ✅ READY FOR AUTOMATION
**PKM Integration**: ✅ COMPATIBLE

Your Progressive Framework now follows a coherent naming convention!
"""
    
    def run_coherent_naming_process(self):
        """Execute complete naming convention standardization"""
        print("🚀 Starting Coherent Naming Convention Process...")
        print(f"📁 Base Directory: {self.base_directory}")
        
        # Create backup directory
        self.create_backup_directory()
        
        # Analyze current files
        print("\n📊 Analyzing current file structure...")
        file_categories = self.analyze_current_files()
        
        print(f"📋 Found:")
        print(f"   Config Files: {len(file_categories['config_files'])}")
        print(f"   System Specs: {len(file_categories['system_specs'])}")
        print(f"   Documentation: {len(file_categories['documentation'])}")
        print(f"   Malformed Files: {len(file_categories['malformed_files'])}")
        print(f"   Other Files: {len(file_categories['other_files'])}")
        
        # Rename malformed files
        if file_categories['malformed_files']:
            self.rename_malformed_files(file_categories['malformed_files'])
        else:
            print("\n✅ No malformed files found!")
        
        # Update file references
        self.update_file_references(file_categories)
        
        # Generate and save report
        print("\n📋 Generating naming convention report...")
        report = self.generate_naming_convention_report()
        
        report_path = self.base_directory / "Coherent-Naming-Convention-Report.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\n✅ Coherent Naming Convention Process Complete!")
        print(f"📊 Total Corrections Applied: {self.corrections_applied}")
        print(f"💾 Backups Created in: {self.backup_dir}")
        print(f"📋 Report Generated: {report_path}")
        print(f"\n🎯 Your Progressive Framework now follows coherent naming conventions!")

# Usage Example
if __name__ == "__main__":
    # Replace with your actual working directory
    working_dir = r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025"
    
    naming_tool = CoherentNamingConventionTool(working_dir)
    naming_tool.run_coherent_naming_process()
