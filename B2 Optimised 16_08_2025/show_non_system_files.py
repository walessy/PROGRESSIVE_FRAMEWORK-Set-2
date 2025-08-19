#!/usr/bin/env python3
r"""
FILE: show_non_system_files.py
WORKING_DIRECTORY: C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025
PURPOSE: Show only non-system files that might be safe to remove
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: 20250819_Progressive-Framework-Integration
STATUS: ✅ Progressive Framework System File
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | System Integration ✅
PROGRESSIVE_FRAMEWORK: Core System | Confidence: 100 | System Validated ✅
"""

import sys
import json
from pathlib import Path

def show_non_system_files_only(base_dir: str):
    """Show only the non-system files in a clean format"""
    
    # Import the system identifier
    sys.path.append(str(Path(base_dir)))
    from progressive_framework_system_identifier import ProgressiveFrameworkSystemIdentifier
    
    print("Progressive Framework - Non-System Files Analysis")
    print(f"Directory: {base_dir}")
    print("=" * 60)
    
    # Run identification
    identifier = ProgressiveFrameworkSystemIdentifier(base_dir)
    results = identifier.scan_all_files()
    
    # Show summary
    summary = results['summary']
    print(f"\nSUMMARY (excluding backup files):")
    print(f"  Total Files Analyzed: {summary['total_files_scanned']}")
    print(f"  Progressive Framework Files: {summary['system_files_identified']}")
    print(f"  Non-System Files: {summary['non_system_files']}")
    print(f"  System File Coverage: {summary['system_file_percentage']:.1f}%")
    
    # Show non-system files
    non_system_files = results['non_system_files']
    
    if non_system_files:
        print(f"\nNON-SYSTEM FILES ({len(non_system_files)}):")
        print("These files were NOT identified as Progressive Framework components:")
        print()
        
        for i, file_info in enumerate(non_system_files, 1):
            confidence = file_info['analysis']['confidence_score']
            print(f"{i:2d}. {file_info['relative_path']}")
            print(f"    Confidence: {confidence} (below threshold of 20)")
            
            # Show what indicators were found (if any)
            indicators = file_info['analysis']['indicators_found']
            if indicators:
                print(f"    Found: {', '.join(indicators[:2])}")
            else:
                print(f"    Found: No Progressive Framework indicators")
            print()
            
        print("RECOMMENDATION:")
        print("These files appear to be non-Progressive Framework content.")
        print("Review them manually before considering removal.")
        
    else:
        print(f"\nEXCELLENT! No non-system files found.")
        print("All files in your directory are part of the Progressive Framework!")
    
    # Show backup file count
    backup_count = count_backup_files(Path(base_dir))
    if backup_count > 0:
        print(f"\nBACKUP FILES: {backup_count} backup files excluded from analysis")
        print("(These are automatically created safety copies)")

def count_backup_files(base_dir: Path) -> int:
    """Count backup files that were excluded"""
    count = 0
    for file_path in base_dir.rglob('*'):
        if file_path.is_file():
            name = file_path.name.lower()
            if (name.endswith('.backup') or '.backup.' in name or
                name.endswith('.bak') or '.bak.' in name):
                count += 1
    return count

def main():
    if len(sys.argv) < 2:
        print("Usage: python show_non_system_files.py <directory>")
        sys.exit(1)
    
    base_dir = sys.argv[1]
    show_non_system_files_only(base_dir)

if __name__ == "__main__":
    main()
