#!/usr/bin/env python3
"""
Progressive Framework Consistency Fixer
========================================
Scans and fixes inconsistencies in Progressive Framework Set 2 specifications.
Ensures all 15 systems and 615+ tests are correctly referenced throughout.

Author: Progressive Framework Pioneer
Date: August 19, 2025
"""

import os
import re
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Any

class ProgressiveFrameworkConsistencyFixer:
    def __init__(self, base_directory: str):
        self.base_directory = Path(base_directory)
        self.backup_directory = self.base_directory / "consistency_backups"
        self.report_file = self.base_directory / f"consistency_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        # Correct framework specification
        self.correct_spec = {
            "total_systems": 15,
            "total_tests": 615,
            "total_lessons": 615,
            "total_chats": 15,
            "framework_name": "Progressive Framework Set 2 - Complete 15-System Integration"
        }
        
        # System breakdown
        self.systems = {
            1: {"name": "PDT-PLUS", "tests": 105, "tier": "Foundation"},
            2: {"name": "PUXT-PLUS", "tests": 45, "tier": "Foundation"},
            3: {"name": "PSO-PRIME", "tests": 50, "tier": "Foundation"},
            4: {"name": "PTT-DOCS-FUSION", "tests": 35, "tier": "Foundation"},
            5: {"name": "REQUIREMENTS-PRIME", "tests": 35, "tier": "Foundation"},
            6: {"name": "BUSINESS-OPS-FUSION", "tests": 40, "tier": "Professional"},
            7: {"name": "CONTEXT-EVOLUTION-ENGINE", "tests": 35, "tier": "Professional"},
            8: {"name": "PERFORMANCE-AI-FUSION", "tests": 38, "tier": "Professional"},
            9: {"name": "SECURITY-BUILD-FUSION", "tests": 42, "tier": "Professional"},
            10: {"name": "KNOWLEDGE-EVOLUTION-ENGINE", "tests": 30, "tier": "Universal"},
            11: {"name": "UNIVERSAL-ORCHESTRATION-PRIME", "tests": 25, "tier": "Universal"},
            12: {"name": "PMCS-024", "tests": 45, "tier": "Universal"},
            13: {"name": "PAES", "tests": 35, "tier": "Universal"},
            14: {"name": "DPI", "tests": 25, "tier": "Integration"},
            15: {"name": "PTODOS", "tests": 30, "tier": "Integration"}
        }
        
        # Inconsistency patterns to fix
        self.fix_patterns = [
            # Test count fixes
            (r'560\s+test', '615+ test', 'Updated test count'),
            (r'560\s+lesson', '615+ lesson', 'Updated lesson count'),
            (r'560\s+Test', '615+ Test', 'Updated test count (capitalized)'),
            (r'560\s+Lesson', '615+ Lesson', 'Updated lesson count (capitalized)'),
            
            # System count fixes
            (r'13\s+system', '15 system', 'Updated system count'),
            (r'13\s+System', '15 System', 'Updated system count (capitalized)'),
            (r'13\s+chat', '15 chat', 'Updated chat count'),
            (r'13\s+Chat', '15 Chat', 'Updated chat count (capitalized)'),
            
            # Framework references
            (r'Framework Set 2 - 15 Systems', 'Framework Set 2 - 15 Systems', 'Updated framework reference'),
            (r'Set 2.*15 systems', 'Set 2 - 15 systems', 'Updated set reference'),
            
            # System numbering fixes
            (r'System (\d+) of 12', r'System \1 of 15', 'Updated system numbering'),
            (r'System (\d+) of 13', r'System \1 of 15', 'Updated system numbering'),
            (r'system (\d+) of 12', r'system \1 of 15', 'Updated system numbering'),
            (r'system (\d+) of 13', r'system \1 of 15', 'Updated system numbering'),
            
            # Tier references that might be incomplete
            (r'Enhanced System (\d+) of 12', r'Enhanced System \1 of 15', 'Updated enhanced system numbering'),
            (r'Enhanced System (\d+) of 13', r'Enhanced System \1 of 15', 'Updated enhanced system numbering'),
            
            # Breathing framework references
            (r'615+ test breathing framework test reference'),
            (r'615+ lesson breathing framework lesson reference')
        ]
        
        # File extensions to process
        self.processable_extensions = {'.md', '.txt', '.json', '.xml', '.yaml', '.yml', '.py', '.js', '.ts'}
        
        self.inconsistencies_found = []
        self.files_processed = 0
        self.files_modified = 0
        
    def create_backup(self) -> None:
        """Create backup of all files before modification"""
        if self.backup_directory.exists():
            shutil.rmtree(self.backup_directory)
        
        self.backup_directory.mkdir(parents=True)
        print(f"📁 Creating backup in: {self.backup_directory}")
        
        for file_path in self.base_directory.rglob("*"):
            if file_path.is_file() and file_path.suffix in self.processable_extensions:
                relative_path = file_path.relative_to(self.base_directory)
                backup_path = self.backup_directory / relative_path
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, backup_path)
        
        print(f"✅ Backup created successfully")
    
    def scan_file_for_inconsistencies(self, file_path: Path) -> List[Dict[str, Any]]:
        """Scan a single file for inconsistencies"""
        inconsistencies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            for pattern, replacement, description in self.fix_patterns:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    inconsistencies.append({
                        'file': str(file_path.relative_to(self.base_directory)),
                        'line_number': content[:match.start()].count('\n') + 1,
                        'pattern': pattern,
                        'found_text': match.group(),
                        'replacement': replacement,
                        'description': description,
                        'start_pos': match.start(),
                        'end_pos': match.end()
                    })
        
        except Exception as e:
            print(f"⚠️  Error scanning {file_path}: {e}")
        
        return inconsistencies
    
    def fix_file_inconsistencies(self, file_path: Path) -> int:
        """Fix inconsistencies in a single file"""
        fixes_made = 0
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original_content = content
            
            for pattern, replacement, description in self.fix_patterns:
                new_content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
                if count > 0:
                    content = new_content
                    fixes_made += count
                    print(f"  ✅ Fixed {count} instances: {description}")
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return fixes_made
        
        except Exception as e:
            print(f"⚠️  Error fixing {file_path}: {e}")
        
        return 0
    
    def scan_all_files(self) -> None:
        """Scan all files for inconsistencies"""
        print("🔍 SCANNING FOR INCONSISTENCIES...")
        print("=" * 50)
        
        for file_path in self.base_directory.rglob("*"):
            if (file_path.is_file() and 
                file_path.suffix in self.processable_extensions and
                not str(file_path).startswith(str(self.backup_directory))):
                
                self.files_processed += 1
                file_inconsistencies = self.scan_file_for_inconsistencies(file_path)
                
                if file_inconsistencies:
                    print(f"\n📄 {file_path.relative_to(self.base_directory)}")
                    for inc in file_inconsistencies:
                        print(f"  Line {inc['line_number']}: {inc['found_text']} → {inc['replacement']}")
                        self.inconsistencies_found.extend(file_inconsistencies)
    
    def fix_all_files(self) -> None:
        """Fix inconsistencies in all files"""
        print("\n🔧 FIXING INCONSISTENCIES...")
        print("=" * 50)
        
        for file_path in self.base_directory.rglob("*"):
            if (file_path.is_file() and 
                file_path.suffix in self.processable_extensions and
                not str(file_path).startswith(str(self.backup_directory))):
                
                print(f"\n📄 Processing: {file_path.relative_to(self.base_directory)}")
                fixes_made = self.fix_file_inconsistencies(file_path)
                
                if fixes_made > 0:
                    self.files_modified += 1
                    print(f"  ✅ Made {fixes_made} fixes")
                else:
                    print(f"  ✅ No fixes needed")
    
    def generate_report(self) -> None:
        """Generate detailed consistency report"""
        report_content = f"""
PROGRESSIVE FRAMEWORK CONSISTENCY REPORT
=======================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Directory: {self.base_directory}

FRAMEWORK SPECIFICATION TARGET:
- Total Systems: {self.correct_spec['total_systems']}
- Total Tests: {self.correct_spec['total_tests']}+
- Total Lessons: {self.correct_spec['total_lessons']}+
- Total Chats: {self.correct_spec['total_chats']}

PROCESSING SUMMARY:
- Files Processed: {self.files_processed}
- Files Modified: {self.files_modified}
- Total Inconsistencies Found: {len(self.inconsistencies_found)}

SYSTEM BREAKDOWN VERIFICATION:
"""
        
        tier_totals = {"Foundation": 0, "Professional": 0, "Universal": 0, "Integration": 0}
        for system_id, system_info in self.systems.items():
            tier_totals[system_info["tier"]] += system_info["tests"]
            report_content += f"System {system_id:2d}: {system_info['name']:30s} - {system_info['tests']:3d} tests ({system_info['tier']})\n"
        
        report_content += f"\nTIER TOTALS:\n"
        total_calculated = 0
        for tier, total in tier_totals.items():
            report_content += f"{tier:12s} Tier: {total:3d} tests\n"
            total_calculated += total
        
        report_content += f"\nTOTAL CALCULATED: {total_calculated} tests\n"
        report_content += f"TARGET ACHIEVED: {'YES' if total_calculated == self.correct_spec['total_tests'] else 'NO'}\n"
        
        if self.inconsistencies_found:
            report_content += f"\nINCONSISTENCIES FOUND:\n"
            report_content += "=" * 50 + "\n"
            
            for inc in self.inconsistencies_found:
                report_content += f"\nFile: {inc['file']}\n"
                report_content += f"Line: {inc['line_number']}\n"
                report_content += f"Found: {inc['found_text']}\n"
                report_content += f"Fixed: {inc['replacement']}\n"
                report_content += f"Description: {inc['description']}\n"
                report_content += "-" * 30 + "\n"
        else:
            report_content += "\n✅ NO INCONSISTENCIES FOUND - FRAMEWORK IS PERFECTLY CONSISTENT!\n"
        
        with open(self.report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"\n📋 Report saved to: {self.report_file}")
    
    def run_full_consistency_check(self, create_backup: bool = True, fix_issues: bool = True) -> None:
        """Run complete consistency check and fix process"""
        print("🚀 PROGRESSIVE FRAMEWORK CONSISTENCY FIXER")
        print("=" * 60)
        print(f"Target Directory: {self.base_directory}")
        print(f"Target Framework: {self.correct_spec['framework_name']}")
        print(f"Target Systems: {self.correct_spec['total_systems']}")
        print(f"Target Tests: {self.correct_spec['total_tests']}+")
        print("=" * 60)
        
        if create_backup:
            self.create_backup()
        
        # Always scan first
        self.scan_all_files()
        
        if fix_issues and self.inconsistencies_found:
            self.fix_all_files()
        elif not self.inconsistencies_found:
            print("\n✅ NO INCONSISTENCIES FOUND - YOUR FRAMEWORK IS PERFECTLY CONSISTENT!")
        
        self.generate_report()
        
        print(f"\n🎯 FINAL SUMMARY:")
        print(f"Files Processed: {self.files_processed}")
        print(f"Files Modified: {self.files_modified}")
        print(f"Inconsistencies Found: {len(self.inconsistencies_found)}")
        print(f"Report Generated: {self.report_file}")
        
        if create_backup:
            print(f"Backup Created: {self.backup_directory}")
        
        print(f"\n🌟 BREATHING FRAMEWORK STATUS: READY FOR REVOLUTIONARY IMPLEMENTATION!")

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python framework_consistency_fixer.py <directory_path> [--no-backup] [--scan-only]")
        print("Example: python framework_consistency_fixer.py 'C:/Users/Wales/OneDrive/Desktop/PROGRESSIVE_FRAMEWORK-Set-2'")
        return
    
    directory = sys.argv[1]
    create_backup = '--no-backup' not in sys.argv
    fix_issues = '--scan-only' not in sys.argv
    
    if not os.path.exists(directory):
        print(f"❌ Directory not found: {directory}")
        return
    
    fixer = ProgressiveFrameworkConsistencyFixer(directory)
    fixer.run_full_consistency_check(create_backup=create_backup, fix_issues=fix_issues)

if __name__ == "__main__":
    main()
