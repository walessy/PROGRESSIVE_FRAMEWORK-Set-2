#!/usr/bin/env python3
"""
Universal File Header System - Automated Mass Application
Main script for automated header application across all phases
"""

import os
import re
import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from datetime import datetime

class UniversalHeaderApplicator:
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        self.header_templates_dir = self.base_dir / "Templates"
        self.verification_system = self.base_dir / "Scripts" / "header_verification.py"
        
        # Phase 1 and 2 file lists
        self.phase1_critical = [
            "PKM-5Point-Protocol-v8.0-EvolutionaryMapping.xml",
            "progressive-systems-config.json", 
            "11 615+ Test-to-Lesson Evolutionary Mapping Engine.md",
            "Breathing-Framework-Complete-Architecture.md",
            "Progressive-Framework-Academy-Complete-Specification.md"
        ]
        
        self.phase1_high = [
            "PROGRESSIVEPROJECT-SYSTEM-01-PDT-PLUS.md",
            "PROGRESSIVEPROJECT-SYSTEM-02-PUXT-PLUS.md",
            "PROGRESSIVEPROJECT-SYSTEM-03-PSO-PRIME.md", 
            "PROGRESSIVEPROJECT-SYSTEM-04-PTT-DOCS-FUSION.md",
            "PROGRESSIVEPROJECT-SYSTEM-05-REQUIREMENTS-PRIME.md",
            "PROGRESSIVEPROJECT-SYSTEM-06-BUSINESS-OPS-FUSION.md",
            "PROGRESSIVEPROJECT-SYSTEM-07-CONTEXT-EVOLUTION-ENGINE.md",
            "PROGRESSIVEPROJECT-SYSTEM-08-PERFORMANCE-AI-FUSION.md",
            "PROGRESSIVEPROJECT-SYSTEM-09-SECURITY-BUILD-FUSION.md",
            "PROGRESSIVEPROJECT-SYSTEM-10-KNOWLEDGE-EVOLUTION-ENGINE.md",
            "PROGRESSIVEPROJECT-SYSTEM-11-INTEGRATION-ORCHESTRATOR.md",
            "PROGRESSIVEPROJECT-SYSTEM-12-VALIDATION-CERTIFICATION-ENGINE.md",
            "PROGRESSIVEPROJECT-SYSTEM-13-META-COORDINATION-SUITE.md",
            "PROGRESSIVEPROJECT-SYSTEM-14-DPI.md",
            "PROGRESSIVEPROJECT-SYSTEM-15-PTODOS.md"
        ]
        
        # Load header templates
        self.templates = self.load_header_templates()
        
    def load_header_templates(self) -> Dict[str, str]:
        """Load all header templates from Templates directory or create built-in ones"""
        templates = {}
        template_dir = self.header_templates_dir
        
        # Try to load from Templates directory first
        if template_dir.exists():
            for template_file in template_dir.glob("*.template"):
                extension = template_file.stem.replace("header_template_", "")
                with open(template_file, 'r', encoding='utf-8') as f:
                    templates[extension] = f.read()
        
        # Create built-in templates if none found or directory missing
        if not templates:
            print(f"📝 Creating built-in header templates...")
            templates = self.create_builtin_templates()
                
        print(f"✅ Loaded {len(templates)} header templates")
        return templates
    
    def create_builtin_templates(self) -> Dict[str, str]:
        """Create built-in header templates for all file types"""
        return {
            'md': '''<!--
FILE: [fileName]
WORKING_DIRECTORY: [fullDirectory]
PURPOSE: [purpose]
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: [YYYYMMDD]_[description]
STATUS: ✅ Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Compliance ✅
-->''',
            'py': '''#!/usr/bin/env python3
"""
FILE: [fileName]
WORKING_DIRECTORY: [fullDirectory]
PURPOSE: [purpose]
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: [YYYYMMDD]_[description]
STATUS: ✅ Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Compliance ✅
"""''',
            'json': '''{
  "_header": {
    "FILE": "[fileName]",
    "WORKING_DIRECTORY": "[fullDirectory]",
    "PURPOSE": "[purpose]",
    "CREATOR": "Amos Wales - Progressive Framework Pioneer",
    "UPDATED": "[YYYYMMDD]_[description]",
    "STATUS": "✅ Universal Header System Compliant",
    "BREATHING_FRAMEWORK": "15 Systems ✅ | 615+ Tests ✅ | Compliance ✅"
  },''',
            'xml': '''<!--
FILE: [fileName]
WORKING_DIRECTORY: [fullDirectory]
PURPOSE: [purpose]
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: [YYYYMMDD]_[description]
STATUS: ✅ Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Compliance ✅
-->''',
            'yaml': '''#
# FILE: [fileName]
# WORKING_DIRECTORY: [fullDirectory]
# PURPOSE: [purpose]
# CREATOR: Amos Wales - Progressive Framework Pioneer
# UPDATED: [YYYYMMDD]_[description]
# STATUS: ✅ Universal Header System Compliant
# BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Compliance ✅
#''',
            'txt': '''#
# FILE: [fileName]
# WORKING_DIRECTORY: [fullDirectory]
# PURPOSE: [purpose]
# CREATOR: Amos Wales - Progressive Framework Pioneer
# UPDATED: [YYYYMMDD]_[description]
# STATUS: ✅ Universal Header System Compliant
# BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Compliance ✅
#'''
        }
    
    def detect_file_type(self, file_path: Path) -> str:
        """Detect file type for appropriate header template"""
        suffix = file_path.suffix.lower()
        
        # Map file extensions to template types
        extension_map = {
            '.md': 'md',
            '.py': 'py', 
            '.json': 'json',
            '.xml': 'xml',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.txt': 'txt',
            '.conf': 'conf',
            '.bat': 'bat',
            '.sh': 'sh',
            '.ps1': 'ps1'
        }
        
        return extension_map.get(suffix, 'txt')
    
    def generate_header(self, file_path: Path, purpose: str = None) -> str:
        """Generate appropriate header for file"""
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
        header = header.replace('[description]', 'Header-System-Integration')
        
        return header
    
    def auto_detect_purpose(self, file_path: Path) -> str:
        """Auto-detect file purpose based on name and location"""
        name = file_path.name.lower()
        parent = file_path.parent.name.lower()
        
        # Purpose detection patterns
        if 'progressiveproject-system' in name:
            system_num = re.search(r'system-(\d+)', name)
            if system_num:
                return f"Progressive Framework System {system_num.group(1)} specification"
        elif 'breathing-framework' in name:
            return "Breathing Framework core engine specification"
        elif 'pkm-5point' in name:
            return "Core protocol control configuration"
        elif 'config' in name or 'configuration' in name:
            return "System configuration and settings"
        elif parent == 'system_specs':
            return "System specification documentation"
        elif parent == 'scripts':
            return "Automation script for framework operations"
        elif parent == 'templates':
            return "Template file for system standardization"
        elif name.endswith('.md'):
            return "Documentation and specifications"
        elif name.endswith('.py'):
            return "Python automation script"
        elif name.endswith('.json'):
            return "Configuration data file"
        elif name.endswith('.xml'):
            return "XML configuration specification"
        else:
            return "Progressive Framework component file"
    
    def has_header(self, file_path: Path) -> bool:
        """Check if file already has a header"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                first_lines = f.read(500)  # Read first 500 chars
                
            # Check for header indicators
            header_indicators = [
                'FILE:', 'WORKING_DIRECTORY:', 'PURPOSE:', 
                'CREATOR:', 'UPDATED:', 'STATUS:',
                'BREATHING_FRAMEWORK:'
            ]
            
            found_indicators = sum(1 for indicator in header_indicators if indicator in first_lines)
            return found_indicators >= 4  # Must have at least 4 header fields
            
        except Exception as e:
            print(f"⚠️  Error checking header in {file_path}: {e}")
            return False
    
    def apply_header(self, file_path: Path, purpose: str = None, backup: bool = True) -> bool:
        """Apply header to a single file"""
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
                
            print(f"✅ Applied header to {file_path.name}")
            return True
            
        except Exception as e:
            print(f"❌ Error applying header to {file_path}: {e}")
            return False
    
    def apply_headers_batch(self, file_list: List[str], phase_name: str = "Batch") -> Tuple[int, int]:
        """Apply headers to a batch of files"""
        print(f"\n🚀 Starting {phase_name} header application...")
        success_count = 0
        total_count = 0
        
        for filename in file_list:
            # Find file in directory tree
            file_path = self.find_file(filename)
            if not file_path:
                print(f"⚠️  File not found: {filename}")
                continue
                
            total_count += 1
            if self.apply_header(file_path):
                success_count += 1
                
        print(f"\n📊 {phase_name} Results: {success_count}/{total_count} files updated")
        return success_count, total_count
    
    def find_file(self, filename: str) -> Optional[Path]:
        """Find file in directory tree"""
        for file_path in self.base_dir.rglob(filename):
            if file_path.is_file():
                return file_path
        return None
    
    def run_phase1_critical(self) -> Tuple[int, int]:
        """Run Phase 1 Critical file header application"""
        return self.apply_headers_batch(self.phase1_critical, "Phase 1 Critical")
    
    def run_phase1_high(self) -> Tuple[int, int]:
        """Run Phase 1 High Priority file header application"""
        return self.apply_headers_batch(self.phase1_high, "Phase 1 High Priority")
    
    def run_phase1_complete(self) -> Tuple[int, int]:
        """Run complete Phase 1 header application"""
        print("🎯 Starting Phase 1 Complete Header Application")
        
        critical_success, critical_total = self.run_phase1_critical()
        high_success, high_total = self.run_phase1_high()
        
        total_success = critical_success + high_success
        total_files = critical_total + high_total
        
        print(f"\n🏆 Phase 1 Complete Results:")
        print(f"   Critical Files: {critical_success}/{critical_total}")
        print(f"   High Priority: {high_success}/{high_total}")
        print(f"   Total: {total_success}/{total_files}")
        print(f"   Success Rate: {(total_success/total_files*100):.1f}%")
        
        return total_success, total_files
    
    def run_phase2_supporting(self) -> Tuple[int, int]:
        """Run Phase 2 supporting files header application"""
        print("🎯 Starting Phase 2 Supporting Files Header Application")
        
        # Find Python scripts, config files, and documentation
        phase2_files = []
        
        # Scan for Phase 2 target files
        for file_path in self.base_dir.rglob('*'):
            if file_path.is_file() and not file_path.name.startswith('.'):
                # Skip if already has header
                if self.has_header(file_path):
                    continue
                    
                # Include specific file types for Phase 2
                if (file_path.suffix.lower() in ['.py', '.json', '.yaml', '.yml', '.txt'] or
                    'README' in file_path.name.upper() or
                    'GUIDE' in file_path.name.upper() or
                    'CONFIG' in file_path.name.upper()):
                    phase2_files.append(file_path)
        
        print(f"📋 Found {len(phase2_files)} Phase 2 target files")
        
        success_count = 0
        for file_path in phase2_files[:30]:  # Limit to 30 files for Phase 2
            if self.apply_header(file_path):
                success_count += 1
                
        print(f"\n📊 Phase 2 Results: {success_count}/{min(len(phase2_files), 30)} files updated")
        return success_count, min(len(phase2_files), 30)
    
    def scan_all_files(self) -> Dict[str, List[Path]]:
        """Scan all files and categorize by type and header status"""
        results = {
            'with_headers': [],
            'without_headers': [],
            'by_type': {}
        }
        
        print("🔍 Scanning all files in project...")
        
        file_count = 0
        for file_path in self.base_dir.rglob('*'):
            if file_path.is_file() and not file_path.name.startswith('.'):
                file_count += 1
                file_type = self.detect_file_type(file_path)
                
                # Categorize by type
                if file_type not in results['by_type']:
                    results['by_type'][file_type] = []
                results['by_type'][file_type].append(file_path)
                
                # Categorize by header status
                if self.has_header(file_path):
                    results['with_headers'].append(file_path)
                else:
                    results['without_headers'].append(file_path)
                    
        print(f"📊 Scan complete: {file_count} files found")
        print(f"   With headers: {len(results['with_headers'])}")
        print(f"   Without headers: {len(results['without_headers'])}")
        print(f"   Compliance: {len(results['with_headers'])/file_count*100:.1f}%")
        
        return results
    
    def generate_compliance_report(self) -> Dict:
        """Generate detailed compliance report"""
        scan_results = self.scan_all_files()
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_files': len(scan_results['with_headers']) + len(scan_results['without_headers']),
            'compliant_files': len(scan_results['with_headers']),
            'non_compliant_files': len(scan_results['without_headers']),
            'compliance_rate': len(scan_results['with_headers']) / (len(scan_results['with_headers']) + len(scan_results['without_headers'])) * 100,
            'by_file_type': {}
        }
        
        # Analyze by file type
        for file_type, files in scan_results['by_type'].items():
            compliant = sum(1 for f in files if self.has_header(f))
            total = len(files)
            report['by_file_type'][file_type] = {
                'total': total,
                'compliant': compliant,
                'compliance_rate': compliant/total*100 if total > 0 else 0
            }
            
        return report

def main():
    """Main execution function"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python automated_header_applicator.py <base_directory> [action]")
        print("Actions: scan, phase1, critical, high, phase2, report")
        sys.exit(1)
        
    base_dir = sys.argv[1]
    action = sys.argv[2] if len(sys.argv) > 2 else 'phase1'
    
    print("🎯 Universal File Header System - Automated Mass Application")
    print(f"📁 Base Directory: {base_dir}")
    print(f"🎬 Action: {action}")
    print("=" * 60)
    
    applicator = UniversalHeaderApplicator(base_dir)
    
    if action == 'scan':
        applicator.scan_all_files()
    elif action == 'critical':
        applicator.run_phase1_critical()
    elif action == 'high':
        applicator.run_phase1_high()
    elif action == 'phase1':
        applicator.run_phase1_complete()
    elif action == 'phase2':
        applicator.run_phase2_supporting()
    elif action == 'report':
        report = applicator.generate_compliance_report()
        print(json.dumps(report, indent=2))
    else:
        print(f"❌ Unknown action: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()