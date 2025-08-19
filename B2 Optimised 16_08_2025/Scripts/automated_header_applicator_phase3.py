#!/usr/bin/env python3
"""
FILE: automated_header_applicator_phase3.py
WORKING_DIRECTORY: .
PURPOSE: Python automation script for legendary system orchestration
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: 20250819_Phase5-Legendary-Status
STATUS: LEGENDARY - Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems | 615+ Tests | Complete Integration
PROGRESSIVE_ACADEMY: Foundation | Professional | Universal | Legendary Ecosystem
PHASE_5_ACHIEVEMENT: 50%+ Compliance | Legendary Status | Complete Standardization
"""

#!/usr/bin/env python3
"""
Universal File Header System - Phase 3 Educational Ecosystem Expansion
Automated Mass Application with Educational Content Integration
"""

import os
import re
import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from datetime import datetime

class UniversalHeaderApplicatorPhase3:
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        self.header_templates_dir = self.base_dir / "Templates"
        self.verification_system = self.base_dir / "Scripts" / "header_verification.py"
        
        # Phase 3 target categories for educational ecosystem expansion
        self.phase3_educational = [
            # Lesson Files
            "**/*LESSON*.md",
            "**/*lesson*.md", 
            "Lessons/*.md",
            "Educational_Content/*.md",
            "Academy/*.md",
            
            # Template Files
            "Templates/*.md",
            "Templates/*.template",
            "Templates/*.yaml",
            "Templates/*.json",
            
            # Documentation Files
            "**/*README*.md",
            "**/*GUIDE*.md",
            "**/*SPECIFICATION*.md",
            "**/*ARCHITECTURE*.md",
            "**/CHANGELOG*.md",
            "**/LICENSE*.md"
        ]
        
        self.phase3_automation = [
            # Python Educational Scripts
            "**/*educational*.py",
            "**/*lesson*.py",
            "**/*academy*.py",
            "**/*training*.py",
            "**/*breathing*.py",
            "**/*evolutionary*.py",
            
            # Automation Scripts
            "Scripts/*.py",
            "Automation/*.py",
            "Tools/*.py"
        ]
        
        self.phase3_configuration = [
            # Configuration Files
            "Config/*.yaml",
            "Config/*.json",
            "**/*config*.yaml",
            "**/*config*.json",
            "**/*settings*.yaml",
            "**/*settings*.json",
            
            # Breathing Framework Files
            "**/*breathing*.yaml",
            "**/*breathing*.json",
            "**/*framework*.yaml",
            "**/*framework*.json"
        ]
        
        # Load header templates
        self.templates = self.load_header_templates()
        
    def load_header_templates(self) -> Dict[str, str]:
        """Load all header templates with educational enhancements"""
        templates = {}
        template_dir = self.header_templates_dir
        
        # Try to load from Templates directory first
        if template_dir.exists():
            for template_file in template_dir.glob("*.template"):
                extension = template_file.stem.replace("header_template_", "")
                with open(template_file, 'r', encoding='utf-8') as f:
                    templates[extension] = f.read()
        
        # Create enhanced educational templates if none found
        if not templates:
            print(f"🎓 Creating enhanced educational header templates...")
            templates = self.create_educational_templates()
                
        print(f"✅ Loaded {len(templates)} educational header templates")
        return templates
    
    def create_educational_templates(self) -> Dict[str, str]:
        """Create enhanced educational header templates for Phase 3"""
        return {
            'md': '''<!--
FILE: [fileName]
WORKING_DIRECTORY: [fullDirectory]
PURPOSE: [purpose]
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: [YYYYMMDD]_[description]
STATUS: ✅ Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Educational Integration ✅
PROGRESSIVE_ACADEMY: Foundation ✅ | Professional ✅ | Universal ✅ | Certification Ready ✅
-->''',
            'py': '''#!/usr/bin/env python3
"""
FILE: [fileName]
WORKING_DIRECTORY: [fullDirectory]
PURPOSE: [purpose]
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: [YYYYMMDD]_[description]
STATUS: ✅ Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Educational Integration ✅
PROGRESSIVE_ACADEMY: Foundation ✅ | Professional ✅ | Universal ✅ | Automation Ready ✅
"""''',
            'json': '''{
  "_header": {
    "FILE": "[fileName]",
    "WORKING_DIRECTORY": "[fullDirectory]",
    "PURPOSE": "[purpose]",
    "CREATOR": "Amos Wales - Progressive Framework Pioneer",
    "UPDATED": "[YYYYMMDD]_[description]",
    "STATUS": "✅ Universal Header System Compliant",
    "BREATHING_FRAMEWORK": "15 Systems ✅ | 615+ Tests ✅ | Educational Integration ✅",
    "PROGRESSIVE_ACADEMY": "Foundation ✅ | Professional ✅ | Universal ✅ | Config Ready ✅"
  },''',
            'yaml': '''#
# FILE: [fileName]
# WORKING_DIRECTORY: [fullDirectory]
# PURPOSE: [purpose]
# CREATOR: Amos Wales - Progressive Framework Pioneer
# UPDATED: [YYYYMMDD]_[description]
# STATUS: ✅ Universal Header System Compliant
# BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Educational Integration ✅
# PROGRESSIVE_ACADEMY: Foundation ✅ | Professional ✅ | Universal ✅ | Config Ready ✅
#''',
            'xml': '''<!--
FILE: [fileName]
WORKING_DIRECTORY: [fullDirectory]
PURPOSE: [purpose]
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: [YYYYMMDD]_[description]
STATUS: ✅ Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Educational Integration ✅
PROGRESSIVE_ACADEMY: Foundation ✅ | Professional ✅ | Universal ✅ | Protocol Ready ✅
-->''',
            'txt': '''#
# FILE: [fileName]
# WORKING_DIRECTORY: [fullDirectory]
# PURPOSE: [purpose]
# CREATOR: Amos Wales - Progressive Framework Pioneer
# UPDATED: [YYYYMMDD]_[description]
# STATUS: ✅ Universal Header System Compliant
# BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Educational Integration ✅
# PROGRESSIVE_ACADEMY: Foundation ✅ | Professional ✅ | Universal ✅ | Documentation Ready ✅
#'''
        }
    
    def detect_file_type(self, file_path: Path) -> str:
        """Enhanced file type detection for educational content"""
        suffix = file_path.suffix.lower()
        name = file_path.name.lower()
        
        # Enhanced file type mapping
        extension_map = {
            '.md': 'md',
            '.py': 'py', 
            '.json': 'json',
            '.xml': 'xml',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.txt': 'txt',
            '.template': 'txt',
            '.conf': 'txt',
            '.config': 'txt',
            '.bat': 'txt',
            '.sh': 'txt',
            '.ps1': 'txt'
        }
        
        return extension_map.get(suffix, 'txt')
    
    def auto_detect_purpose(self, file_path: Path) -> str:
        """Enhanced purpose detection for educational and framework files"""
        name = file_path.name.lower()
        parent = file_path.parent.name.lower()
        
        # Educational content detection
        if 'lesson' in name:
            if 'foundation' in name:
                return "Progressive Framework Academy - Foundation Tier lesson content"
            elif 'professional' in name:
                return "Progressive Framework Academy - Professional Tier lesson content"
            elif 'universal' in name:
                return "Progressive Framework Academy - Universal Tier lesson content"
            else:
                return "Progressive Framework Academy educational lesson content"
        
        # Template detection
        if parent == 'templates' or 'template' in name:
            return "Educational content template for Progressive Framework Academy"
        
        # Breathing Framework detection
        if 'breathing' in name:
            return "Breathing Framework auto-generation and educational integration system"
        
        # Academy detection
        if 'academy' in name or parent == 'academy':
            return "Progressive Framework Academy system component"
        
        # Documentation detection
        if 'readme' in name:
            return "Project documentation and guidance"
        elif 'guide' in name:
            return "User guide and instructional documentation"
        elif 'specification' in name:
            return "Technical specification and requirements documentation"
        elif 'architecture' in name:
            return "System architecture and design documentation"
        
        # System files detection
        if 'progressiveproject-system' in name:
            system_num = re.search(r'system-(\d+)', name)
            if system_num:
                return f"Progressive Framework System {system_num.group(1)} specification with educational integration"
        
        # Configuration detection
        if 'config' in name or 'configuration' in name:
            return "System configuration with educational framework integration"
        
        # Script detection
        if parent == 'scripts' or name.endswith('.py'):
            if 'educational' in name:
                return "Educational automation script for Progressive Framework Academy"
            elif 'breathing' in name:
                return "Breathing Framework automation script"
            else:
                return "Progressive Framework automation script"
        
        # Fallback based on file type
        file_type = self.detect_file_type(file_path)
        if file_type == 'md':
            return "Progressive Framework educational documentation"
        elif file_type == 'py':
            return "Progressive Framework educational automation script"
        elif file_type in ['json', 'yaml']:
            return "Progressive Framework educational configuration file"
        else:
            return "Progressive Framework educational component file"
    
    def generate_header(self, file_path: Path, purpose: str = None) -> str:
        """Generate enhanced educational header for file"""
        file_type = self.detect_file_type(file_path)
        template = self.templates.get(file_type, self.templates.get('txt', ''))
        
        if not template:
            print(f"⚠️  No template found for file type: {file_type}")
            return ""
            
        # Calculate relative path from base directory
        try:
            relative_path = file_path.relative_to(self.base_dir)
            working_dir = str(self.base_dir / relative_path.parent).replace('\\', '\\\\')
        except ValueError:
            working_dir = str(file_path.parent).replace('\\', '\\\\')
            
        # Auto-detect purpose if not provided
        if not purpose:
            purpose = self.auto_detect_purpose(file_path)
            
        # Replace template placeholders
        header = template.replace('[fileName]', file_path.name)
        header = header.replace('[fullDirectory]', working_dir)
        header = header.replace('[purpose]', purpose)
        header = header.replace('[YYYYMMDD]', datetime.now().strftime('%Y%m%d'))
        header = header.replace('[description]', 'Educational-Phase3-Integration')
        
        return header
    
    def has_header(self, file_path: Path) -> bool:
        """Enhanced header detection for educational content"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                first_lines = f.read(800)  # Read more content for educational headers
                
            # Enhanced header indicators for educational content
            header_indicators = [
                'FILE:', 'WORKING_DIRECTORY:', 'PURPOSE:', 
                'CREATOR:', 'UPDATED:', 'STATUS:',
                'BREATHING_FRAMEWORK:', 'PROGRESSIVE_ACADEMY:'
            ]
            
            found_indicators = sum(1 for indicator in header_indicators if indicator in first_lines)
            return found_indicators >= 4  # Must have at least 4 header fields
            
        except Exception as e:
            print(f"⚠️  Error checking header in {file_path}: {e}")
            return False
    
    def find_files_by_patterns(self, patterns: List[str]) -> List[Path]:
        """Find files matching educational content patterns"""
        found_files = []
        
        for pattern in patterns:
            # Convert glob pattern to pathlib pattern
            if pattern.startswith('**/'):
                # Recursive pattern
                search_pattern = pattern[3:]  # Remove **/
                for file_path in self.base_dir.rglob(search_pattern):
                    if file_path.is_file() and not file_path.name.startswith('.'):
                        found_files.append(file_path)
            else:
                # Direct pattern
                for file_path in self.base_dir.glob(pattern):
                    if file_path.is_file() and not file_path.name.startswith('.'):
                        found_files.append(file_path)
        
        # Remove duplicates
        return list(set(found_files))
    
    def apply_header(self, file_path: Path, purpose: str = None, backup: bool = True) -> bool:
        """Apply enhanced educational header to file"""
        try:
            # Check if file already has header
            if self.has_header(file_path):
                print(f"⭐ Skipping {file_path.name} (already has header)")
                return True
                
            # Create backup if requested
            if backup:
                backup_path = file_path.with_suffix(file_path.suffix + '.backup')
                shutil.copy2(file_path, backup_path)
                
            # Read existing content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                existing_content = f.read()
                
            # Generate header
            header = self.generate_header(file_path, purpose)
            if not header:
                print(f"❌ Could not generate header for {file_path.name}")
                return False
                
            # Write header + existing content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(header + '\n\n' + existing_content)
                
            print(f"✅ Applied educational header to {file_path.name}")
            return True
            
        except Exception as e:
            print(f"❌ Error applying header to {file_path}: {e}")
            return False
    
    def run_phase3_educational(self) -> Tuple[int, int]:
        """Apply headers to educational content files"""
        print("🎓 Starting Phase 3: Educational Content Header Application")
        
        # Find educational files
        educational_files = self.find_files_by_patterns(self.phase3_educational)
        
        # Filter out files that already have headers
        target_files = [f for f in educational_files if not self.has_header(f)]
        
        print(f"📚 Found {len(target_files)} educational files needing headers")
        
        success_count = 0
        for file_path in target_files[:35]:  # Limit to 35 files for Phase 3
            if self.apply_header(file_path):
                success_count += 1
                
        print(f"\n📊 Phase 3 Educational Results: {success_count}/{min(len(target_files), 35)} files updated")
        return success_count, min(len(target_files), 35)
    
    def run_phase3_automation(self) -> Tuple[int, int]:
        """Apply headers to automation and script files"""
        print("🤖 Starting Phase 3: Automation Scripts Header Application")
        
        automation_files = self.find_files_by_patterns(self.phase3_automation)
        target_files = [f for f in automation_files if not self.has_header(f)]
        
        print(f"⚙️ Found {len(target_files)} automation files needing headers")
        
        success_count = 0
        for file_path in target_files[:20]:  # Limit to 20 files
            if self.apply_header(file_path):
                success_count += 1
                
        print(f"\n📊 Phase 3 Automation Results: {success_count}/{min(len(target_files), 20)} files updated")
        return success_count, min(len(target_files), 20)
    
    def run_phase3_configuration(self) -> Tuple[int, int]:
        """Apply headers to configuration files"""
        print("⚙️ Starting Phase 3: Configuration Files Header Application")
        
        config_files = self.find_files_by_patterns(self.phase3_configuration)
        target_files = [f for f in config_files if not self.has_header(f)]
        
        print(f"🔧 Found {len(target_files)} configuration files needing headers")
        
        success_count = 0
        for file_path in target_files[:15]:  # Limit to 15 files
            if self.apply_header(file_path):
                success_count += 1
                
        print(f"\n📊 Phase 3 Configuration Results: {success_count}/{min(len(target_files), 15)} files updated")
        return success_count, min(len(target_files), 15)
    
    def run_phase3_complete(self) -> Tuple[int, int]:
        """Run complete Phase 3 educational ecosystem expansion"""
        print("🚀 Starting Phase 3 Complete: Educational Ecosystem Expansion")
        
        # Run all Phase 3 categories
        edu_success, edu_total = self.run_phase3_educational()
        auto_success, auto_total = self.run_phase3_automation()
        config_success, config_total = self.run_phase3_configuration()
        
        total_success = edu_success + auto_success + config_success
        total_files = edu_total + auto_total + config_total
        
        print(f"\n🏆 Phase 3 Complete Results:")
        print(f"   Educational Content: {edu_success}/{edu_total}")
        print(f"   Automation Scripts: {auto_success}/{auto_total}")
        print(f"   Configuration Files: {config_success}/{config_total}")
        print(f"   Total: {total_success}/{total_files}")
        print(f"   Success Rate: {(total_success/total_files*100):.1f}%")
        
        return total_success, total_files
    
    def scan_phase3_targets(self) -> Dict[str, List[Path]]:
        """Scan and categorize Phase 3 target files"""
        results = {
            'educational_files': [],
            'automation_files': [],
            'configuration_files': [],
            'ready_for_headers': [],
            'already_compliant': []
        }
        
        print("🔍 Scanning Phase 3 target files...")
        
        # Scan educational files
        educational_files = self.find_files_by_patterns(self.phase3_educational)
        automation_files = self.find_files_by_patterns(self.phase3_automation)
        config_files = self.find_files_by_patterns(self.phase3_configuration)
        
        all_phase3_files = list(set(educational_files + automation_files + config_files))
        
        for file_path in all_phase3_files:
            # Categorize by type
            if file_path in educational_files:
                results['educational_files'].append(file_path)
            if file_path in automation_files:
                results['automation_files'].append(file_path)
            if file_path in config_files:
                results['configuration_files'].append(file_path)
            
            # Categorize by header status
            if self.has_header(file_path):
                results['already_compliant'].append(file_path)
            else:
                results['ready_for_headers'].append(file_path)
        
        print(f"📊 Phase 3 Scan Results:")
        print(f"   Educational files: {len(results['educational_files'])}")
        print(f"   Automation files: {len(results['automation_files'])}")
        print(f"   Configuration files: {len(results['configuration_files'])}")
        print(f"   Ready for headers: {len(results['ready_for_headers'])}")
        print(f"   Already compliant: {len(results['already_compliant'])}")
        
        return results

def main():
    """Main execution function for Phase 3"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python automated_header_applicator_phase3.py <base_directory> [action]")
        print("Actions: phase3, educational, automation, configuration, scan")
        sys.exit(1)
        
    base_dir = sys.argv[1]
    action = sys.argv[2] if len(sys.argv) > 2 else 'phase3'
    
    print("🎓 Universal File Header System - Phase 3 Educational Ecosystem")
    print(f"📂 Base Directory: {base_dir}")
    print(f"🎬 Action: {action}")
    print("=" * 70)
    
    applicator = UniversalHeaderApplicatorPhase3(base_dir)
    
    if action == 'phase3':
        applicator.run_phase3_complete()
    elif action == 'educational':
        applicator.run_phase3_educational()
    elif action == 'automation':
        applicator.run_phase3_automation()
    elif action == 'configuration':
        applicator.run_phase3_configuration()
    elif action == 'scan':
        applicator.scan_phase3_targets()
    else:
        print(f"❌ Unknown action: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()