#!/usr/bin/env python3
"""
Quick Phase 4 Implementation for Universal File Header System
Target remaining files for 35%+ compliance
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

class QuickPhase4:
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        
        # Quick Phase 4 header templates (ASCII safe)
        self.header_template = '''<!--
FILE: {filename}
WORKING_DIRECTORY: {working_dir}
PURPOSE: {purpose}
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: {date}_Phase4-Final-Push
STATUS: COMPLIANT - Universal Header System
BREATHING_FRAMEWORK: 15 Systems | 615+ Tests | Phase 4 Integration
PROGRESSIVE_ACADEMY: Foundation | Professional | Universal | Complete Ecosystem
-->'''
        
        self.py_header_template = '''#!/usr/bin/env python3
"""
FILE: {filename}
WORKING_DIRECTORY: {working_dir}
PURPOSE: {purpose}
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: {date}_Phase4-Final-Push
STATUS: COMPLIANT - Universal Header System
BREATHING_FRAMEWORK: 15 Systems | 615+ Tests | Phase 4 Integration
PROGRESSIVE_ACADEMY: Foundation | Professional | Universal | Complete Ecosystem
"""'''
        
        self.json_header_template = '''{
  "_header": {
    "FILE": "{filename}",
    "WORKING_DIRECTORY": "{working_dir}",
    "PURPOSE": "{purpose}",
    "CREATOR": "Amos Wales - Progressive Framework Pioneer",
    "UPDATED": "{date}_Phase4-Final-Push",
    "STATUS": "COMPLIANT - Universal Header System",
    "BREATHING_FRAMEWORK": "15 Systems | 615+ Tests | Phase 4 Integration",
    "PROGRESSIVE_ACADEMY": "Foundation | Professional | Universal | Complete Ecosystem"
  },'''
    
    def detect_purpose(self, file_path):
        """Detect purpose for Phase 4 files"""
        name = file_path.name.lower()
        
        if 'test' in name:
            return "Testing infrastructure and validation system"
        elif 'report' in name:
            return "System report and analytics documentation"
        elif 'signal' in name:
            return "Signal processing and trigger system component"
        elif 'log' in name:
            return "System logging and monitoring documentation"
        elif 'backup' in name:
            return "Backup and version control documentation"
        elif 'doc' in name or 'documentation' in name:
            return "System documentation and reference material"
        elif 'config' in name or 'setting' in name:
            return "System configuration and settings"
        elif 'version' in name or 'changelog' in name:
            return "Version control and change documentation"
        else:
            return "Progressive Framework system component"
    
    def has_header(self, file_path):
        """Check if file has header"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(600)
            indicators = ['FILE:', 'WORKING_DIRECTORY:', 'PURPOSE:', 'CREATOR:']
            return sum(1 for indicator in indicators if indicator in content) >= 3
        except:
            return False
    
    def apply_header(self, file_path):
        """Apply header to file"""
        try:
            if self.has_header(file_path):
                print(f"SKIP: {file_path.name} (already has header)")
                return True
            
            # Create backup
            backup_path = file_path.with_suffix(file_path.suffix + '.backup')
            shutil.copy2(file_path, backup_path)
            
            # Read existing content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                existing_content = f.read()
            
            # Choose template based on file type
            if file_path.suffix == '.py':
                template = self.py_header_template
            elif file_path.suffix == '.json':
                template = self.json_header_template
            else:
                template = self.header_template
            
            # Generate header
            header = template.format(
                filename=file_path.name,
                working_dir=str(file_path.parent).replace('\\', '/'),
                purpose=self.detect_purpose(file_path),
                date=datetime.now().strftime('%Y%m%d')
            )
            
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(header + '\n\n' + existing_content)
            
            print(f"SUCCESS: Applied Phase 4 header to {file_path.name}")
            return True
            
        except Exception as e:
            print(f"ERROR: {file_path.name} - {e}")
            return False
    
    def run_phase4(self):
        """Run Phase 4 processing"""
        print("=" * 60)
        print("PHASE 4: Final Push for 35%+ Compliance")
        print("TARGET: Documentation, reports, and test files")
        print("=" * 60)
        
        # Define Phase 4 patterns
        patterns = [
            "**/*test*.md", "**/*Test*.md",
            "**/*report*.json", "**/*report*.md", "**/*report*.txt",
            "**/*log*.txt", "**/*log*.md",
            "**/*signal*.py", "**/*signal*.md",
            "**/*doc*.md", "**/*notes*.md",
            "**/*backup*.md", "**/*version*.md",
            "**/*changelog*.md"
        ]
        
        # Find target files
        target_files = []
        for pattern in patterns:
            if pattern.startswith('**/'):
                search_pattern = pattern[3:]
                for file_path in self.base_dir.rglob(search_pattern):
                    if (file_path.is_file() and 
                        not file_path.name.startswith('.') and 
                        not self.has_header(file_path)):
                        try:
                            # Skip very large files
                            if file_path.stat().st_size < 5_000_000:  # < 5MB
                                target_files.append(file_path)
                        except:
                            continue
        
        # Remove duplicates
        target_files = list(set(target_files))
        print(f"FOUND: {len(target_files)} Phase 4 target files")
        
        success_count = 0
        for i, file_path in enumerate(target_files[:60]):  # Process up to 60 files
            if self.apply_header(file_path):
                success_count += 1
            
            # Progress indicator
            if (i + 1) % 10 == 0:
                print(f"PROGRESS: {i + 1}/{min(len(target_files), 60)} files processed")
        
        total_processed = min(len(target_files), 60)
        print("\n" + "=" * 60)
        print(f"PHASE 4 COMPLETE: {success_count}/{total_processed} files updated")
        print(f"SUCCESS RATE: {(success_count/total_processed*100):.1f}%")
        print("=" * 60)
        
        return success_count, total_processed

def main():
    import sys
    base_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    print("UNIVERSAL FILE HEADER SYSTEM - PHASE 4 FINAL PUSH")
    print("TARGET: 35%+ Compliance Achievement")
    
    phase4 = QuickPhase4(base_dir)
    phase4.run_phase4()

if __name__ == "__main__":
    main()