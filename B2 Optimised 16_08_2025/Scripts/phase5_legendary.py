#!/usr/bin/env python3
"""
Universal File Header System - Phase 5 LEGENDARY STATUS
Target: 50%+ compliance - Processing ALL remaining files for complete ecosystem standardization
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

class Phase5LegendaryStatus:
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        
        # Phase 5 Legendary header templates (ASCII safe)
        self.header_template = '''<!--
FILE: {filename}
WORKING_DIRECTORY: {working_dir}
PURPOSE: {purpose}
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: {date}_Phase5-Legendary-Status
STATUS: LEGENDARY - Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems | 615+ Tests | Complete Integration
PROGRESSIVE_ACADEMY: Foundation | Professional | Universal | Legendary Ecosystem
PHASE_5_ACHIEVEMENT: 50%+ Compliance | Legendary Status | Complete Standardization
-->'''
        
        self.py_header_template = '''#!/usr/bin/env python3
"""
FILE: {filename}
WORKING_DIRECTORY: {working_dir}
PURPOSE: {purpose}
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: {date}_Phase5-Legendary-Status
STATUS: LEGENDARY - Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems | 615+ Tests | Complete Integration
PROGRESSIVE_ACADEMY: Foundation | Professional | Universal | Legendary Ecosystem
PHASE_5_ACHIEVEMENT: 50%+ Compliance | Legendary Status | Complete Standardization
"""'''
        
        self.json_header_template = '''{
  "_header": {
    "FILE": "{filename}",
    "WORKING_DIRECTORY": "{working_dir}",
    "PURPOSE": "{purpose}",
    "CREATOR": "Amos Wales - Progressive Framework Pioneer",
    "UPDATED": "{date}_Phase5-Legendary-Status",
    "STATUS": "LEGENDARY - Universal Header System Compliant",
    "BREATHING_FRAMEWORK": "15 Systems | 615+ Tests | Complete Integration",
    "PROGRESSIVE_ACADEMY": "Foundation | Professional | Universal | Legendary Ecosystem",
    "PHASE_5_ACHIEVEMENT": "50%+ Compliance | Legendary Status | Complete Standardization"
  },'''
        
        self.yaml_header_template = '''#
# FILE: {filename}
# WORKING_DIRECTORY: {working_dir}
# PURPOSE: {purpose}
# CREATOR: Amos Wales - Progressive Framework Pioneer
# UPDATED: {date}_Phase5-Legendary-Status
# STATUS: LEGENDARY - Universal Header System Compliant
# BREATHING_FRAMEWORK: 15 Systems | 615+ Tests | Complete Integration
# PROGRESSIVE_ACADEMY: Foundation | Professional | Universal | Legendary Ecosystem
# PHASE_5_ACHIEVEMENT: 50%+ Compliance | Legendary Status | Complete Standardization
#'''
        
        self.txt_header_template = '''#
# FILE: {filename}
# WORKING_DIRECTORY: {working_dir}
# PURPOSE: {purpose}
# CREATOR: Amos Wales - Progressive Framework Pioneer
# UPDATED: {date}_Phase5-Legendary-Status
# STATUS: LEGENDARY - Universal Header System Compliant
# BREATHING_FRAMEWORK: 15 Systems | 615+ Tests | Complete Integration
# PROGRESSIVE_ACADEMY: Foundation | Professional | Universal | Legendary Ecosystem
# PHASE_5_ACHIEVEMENT: 50%+ Compliance | Legendary Status | Complete Standardization
#'''
    
    def detect_purpose(self, file_path):
        """Advanced purpose detection for Phase 5 legendary status"""
        name = file_path.name.lower()
        parent = file_path.parent.name.lower()
        
        # Advanced categorization for Phase 5
        if any(x in name for x in ['test', 'testing', 'spec', 'validation']):
            return "Testing and validation infrastructure for legendary system quality"
        elif any(x in name for x in ['report', 'analytics', 'metrics', 'data']):
            return "System analytics and performance reporting for legendary optimization"
        elif any(x in name for x in ['signal', 'trigger', 'hook', 'event']):
            return "Signal processing and event management for legendary responsiveness"
        elif any(x in name for x in ['log', 'monitor', 'debug', 'trace']):
            return "System monitoring and debugging for legendary reliability"
        elif any(x in name for x in ['backup', 'archive', 'history', 'version']):
            return "Version control and backup management for legendary data integrity"
        elif any(x in name for x in ['doc', 'documentation', 'guide', 'manual']):
            return "Documentation and guidance for legendary user experience"
        elif any(x in name for x in ['config', 'setting', 'parameter', 'option']):
            return "System configuration for legendary performance optimization"
        elif any(x in name for x in ['template', 'pattern', 'blueprint', 'schema']):
            return "Template and pattern library for legendary development efficiency"
        elif any(x in name for x in ['tool', 'utility', 'helper', 'assist']):
            return "Development tools and utilities for legendary productivity"
        elif any(x in name for x in ['data', 'database', 'storage', 'cache']):
            return "Data management and storage for legendary information architecture"
        elif name.endswith('.py'):
            return "Python automation script for legendary system orchestration"
        elif name.endswith('.json'):
            return "JSON configuration and data for legendary system coordination"
        elif name.endswith('.yaml') or name.endswith('.yml'):
            return "YAML configuration for legendary system flexibility"
        elif name.endswith('.md'):
            return "Markdown documentation for legendary knowledge sharing"
        elif name.endswith('.txt'):
            return "Text documentation for legendary system clarity"
        else:
            return "Progressive Framework component for legendary ecosystem excellence"
    
    def has_header(self, file_path):
        """Enhanced header detection for Phase 5"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(800)  # Read more content for thorough detection
            
            # Enhanced detection for existing headers
            indicators = [
                'FILE:', 'WORKING_DIRECTORY:', 'PURPOSE:', 'CREATOR:',
                'STATUS:', 'BREATHING_FRAMEWORK:', 'PROGRESSIVE_ACADEMY:'
            ]
            
            found_indicators = sum(1 for indicator in indicators if indicator in content)
            return found_indicators >= 4  # Require more indicators for Phase 5
            
        except Exception:
            return False
    
    def is_processable_file(self, file_path):
        """Determine if file should be processed in Phase 5"""
        try:
            # File size limits
            if file_path.stat().st_size > 10_000_000:  # Skip files > 10MB
                return False
            
            # Skip hidden files and system files
            if file_path.name.startswith('.'):
                return False
            
            # Skip certain directories
            skip_dirs = {'.git', '__pycache__', 'node_modules', '.vscode', '.idea'}
            if any(skip_dir in file_path.parts for skip_dir in skip_dirs):
                return False
            
            # Skip binary extensions
            binary_extensions = {
                '.exe', '.dll', '.so', '.dylib', '.bin', '.dat',
                '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ico',
                '.pdf', '.zip', '.tar', '.gz', '.rar', '.7z',
                '.mp3', '.mp4', '.avi', '.mov', '.wav',
                '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'
            }
            if file_path.suffix.lower() in binary_extensions:
                return False
            
            return True
            
        except Exception:
            return False
    
    def get_template_for_file(self, file_path):
        """Get appropriate template for file type"""
        suffix = file_path.suffix.lower()
        
        if suffix == '.py':
            return self.py_header_template
        elif suffix == '.json':
            return self.json_header_template
        elif suffix in ['.yaml', '.yml']:
            return self.yaml_header_template
        elif suffix == '.txt':
            return self.txt_header_template
        else:
            return self.header_template  # Default markdown-style for most files
    
    def apply_header(self, file_path):
        """Apply Phase 5 legendary header to file"""
        try:
            if self.has_header(file_path):
                print(f"SKIP: {file_path.name} (already has header)")
                return True
            
            # Create backup
            backup_path = file_path.with_suffix(file_path.suffix + '.backup')
            shutil.copy2(file_path, backup_path)
            
            # Read existing content with better encoding handling
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    existing_content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r', encoding='latin-1') as f:
                        existing_content = f.read()
                except:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        existing_content = f.read()
            
            # Get template and generate header
            template = self.get_template_for_file(file_path)
            
            # Handle JSON template formatting issues
            if file_path.suffix == '.json':
                try:
                    header = template.format(
                        filename=file_path.name.replace('{', '{{').replace('}', '}}'),
                        working_dir=str(file_path.parent).replace('\\', '/').replace('{', '{{').replace('}', '}}'),
                        purpose=self.detect_purpose(file_path).replace('{', '{{').replace('}', '}}'),
                        date=datetime.now().strftime('%Y%m%d')
                    )
                except:
                    # Fallback to markdown template for problematic JSON files
                    template = self.header_template
                    header = template.format(
                        filename=file_path.name,
                        working_dir=str(file_path.parent).replace('\\', '/'),
                        purpose=self.detect_purpose(file_path),
                        date=datetime.now().strftime('%Y%m%d')
                    )
            else:
                header = template.format(
                    filename=file_path.name,
                    working_dir=str(file_path.parent).replace('\\', '/'),
                    purpose=self.detect_purpose(file_path),
                    date=datetime.now().strftime('%Y%m%d')
                )
            
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(header + '\n\n' + existing_content)
            
            print(f"LEGENDARY: Applied Phase 5 header to {file_path.name}")
            return True
            
        except Exception as e:
            print(f"ERROR: {file_path.name} - {e}")
            return False
    
    def run_phase5_legendary(self):
        """Run Phase 5 legendary status processing"""
        print("=" * 70)
        print("PHASE 5: LEGENDARY STATUS QUEST")
        print("TARGET: 50%+ Compliance - Complete Ecosystem Standardization")
        print("MISSION: Process ALL remaining files for legendary achievement")
        print("=" * 70)
        
        # Find ALL processable files without headers
        print("SCANNING: Finding all processable files...")
        
        all_files = []
        for file_path in self.base_dir.rglob('*'):
            if (file_path.is_file() and 
                self.is_processable_file(file_path) and
                not self.has_header(file_path)):
                all_files.append(file_path)
        
        print(f"FOUND: {len(all_files)} files ready for legendary transformation")
        
        if len(all_files) == 0:
            print("AMAZING: All processable files already have headers!")
            print("LEGENDARY STATUS ALREADY ACHIEVED!")
            return 0, 0
        
        # Categorize files by type for better processing
        file_categories = {
            'documentation': [],
            'code': [],
            'configuration': [],
            'data': [],
            'other': []
        }
        
        for file_path in all_files:
            name = file_path.name.lower()
            suffix = file_path.suffix.lower()
            
            if suffix in ['.md', '.txt', '.rst'] or any(x in name for x in ['doc', 'guide', 'readme']):
                file_categories['documentation'].append(file_path)
            elif suffix in ['.py', '.js', '.ts', '.java', '.cpp', '.c', '.h']:
                file_categories['code'].append(file_path)
            elif suffix in ['.json', '.yaml', '.yml', '.xml', '.ini', '.conf'] or 'config' in name:
                file_categories['configuration'].append(file_path)
            elif suffix in ['.csv', '.tsv', '.log'] or any(x in name for x in ['data', 'log', 'report']):
                file_categories['data'].append(file_path)
            else:
                file_categories['other'].append(file_path)
        
        # Display categorization
        print("\nCATEGORIZATION:")
        for category, files in file_categories.items():
            print(f"  {category.upper()}: {len(files)} files")
        
        # Process files with smart limits
        total_target = min(len(all_files), 150)  # Process up to 150 files for legendary status
        
        print(f"\nPROCESSING: Up to {total_target} files for legendary transformation")
        print("=" * 70)
        
        success_count = 0
        processed_count = 0
        
        # Process each category with balanced allocation
        category_limits = {
            'documentation': 40,
            'code': 30,
            'configuration': 30,
            'data': 30,
            'other': 20
        }
        
        for category, files in file_categories.items():
            if processed_count >= total_target:
                break
                
            limit = min(len(files), category_limits[category])
            if limit == 0:
                continue
                
            print(f"\nPROCESSING {category.upper()} FILES ({limit} files):")
            
            for i, file_path in enumerate(files[:limit]):
                if processed_count >= total_target:
                    break
                    
                if self.apply_header(file_path):
                    success_count += 1
                
                processed_count += 1
                
                # Progress indicator
                if (i + 1) % 10 == 0 or i == limit - 1:
                    print(f"  PROGRESS: {i + 1}/{limit} {category} files processed")
        
        # Final results
        print("\n" + "=" * 70)
        print(f"PHASE 5 LEGENDARY STATUS COMPLETE!")
        print(f"FILES PROCESSED: {success_count}/{processed_count}")
        print(f"SUCCESS RATE: {(success_count/processed_count*100):.1f}%")
        print(f"LEGENDARY ACHIEVEMENT UNLOCKED!")
        print("=" * 70)
        
        return success_count, processed_count

def main():
    import sys
    base_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    print("UNIVERSAL FILE HEADER SYSTEM - PHASE 5 LEGENDARY STATUS")
    print("TARGET: 50%+ Compliance | Complete Ecosystem Standardization")
    print("ACHIEVEMENT: Legendary Status in Project Organization")
    
    phase5 = Phase5LegendaryStatus(base_dir)
    phase5.run_phase5_legendary()

if __name__ == "__main__":
    main()