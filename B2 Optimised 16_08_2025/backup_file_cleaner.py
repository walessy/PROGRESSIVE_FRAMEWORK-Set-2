#!/usr/bin/env python3
"""
FILE: backup_file_cleaner.py
WORKING_DIRECTORY: Progressive Framework Base Directory
PURPOSE: Remove backup files safely from Progressive Framework directory
CREATOR: Amos Wales - Progressive Framework Pioneer
CREATED: 20250819_114500
STATUS: Backup File Cleanup Tool - Ready for Framework Cleanup
BREATHING_FRAMEWORK: File Organization and Cleanup Management
PROGRESSIVE_ACADEMY: Clean Directory Structure Standards
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

class BackupFileCleaner:
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        self.backup_patterns = [
            # Common backup suffixes
            r'\.backup$',
            r'\.backup\.\w+$',
            r'\.bak$', 
            r'\.old$',
            r'\.orig$',
            r'_backup$',
            r'_backup\.\w+$',
            r'_bak$',
            r'_old$',
            r'_BACKUP$',
            r'_BAK$',
            r'_OLD$',
            
            # Timestamp backup patterns
            r'\.backup_\d{8}$',
            r'\.backup_\d{8}_\d{6}$',
            r'_backup_\d{8}$',
            r'_backup_\d{8}_\d{6}$',
            
            # Copy patterns
            r'_copy$',
            r'_copy\.\w+$',
            r'_COPY$',
            r'\.copy$',
            
            # Version patterns
            r'\s*\(1\)$',
            r'\s*\(2\)$',
            r'\s*\(3\)$',
            r'\s*\(4\)$',
            r'\s*\(5\)$',
            
            # Progressive Framework specific backups
            r'\.backup\.backup$',
            r'\.backup\.backup\.backup$',
        ]
    
    def scan_backup_files(self) -> Dict[str, List[Path]]:
        """Scan directory for backup files"""
        print("🔍 SCANNING FOR BACKUP FILES")
        print("=" * 50)
        
        backup_files = {
            'backup_suffix': [],
            'timestamp_backup': [],
            'copy_files': [],
            'version_copies': [],
            'progressive_backups': [],
            'other_backups': []
        }
        
        total_scanned = 0
        
        # Scan all files recursively
        for file_path in self.base_dir.rglob('*'):
            if file_path.is_file():
                total_scanned += 1
                filename = file_path.name
                
                # Check against backup patterns
                backup_type = self.categorize_backup_file(filename)
                if backup_type:
                    backup_files[backup_type].append(file_path)
                
                if total_scanned % 100 == 0:
                    print(f"   Scanned {total_scanned} files...")
        
        total_backups = sum(len(files) for files in backup_files.values())
        print(f"✅ Scan complete: {total_scanned} files scanned, {total_backups} backup files found")
        
        return backup_files
    
    def categorize_backup_file(self, filename: str) -> str:
        """Categorize backup file by type"""
        filename_lower = filename.lower()
        
        # Progressive Framework specific backups (multiple .backup extensions)
        if '.backup.backup' in filename_lower:
            return 'progressive_backups'
        
        # Timestamp backups
        if re.search(r'backup_\d{8}', filename_lower):
            return 'timestamp_backup'
        
        # Copy files
        if re.search(r'[_\s]copy[\s\.]|\.copy$', filename_lower):
            return 'copy_files'
        
        # Version copies (1), (2), etc.
        if re.search(r'\s*\(\d+\)$', filename):
            return 'version_copies'
        
        # Standard backup suffixes
        for pattern in self.backup_patterns:
            if re.search(pattern, filename, re.IGNORECASE):
                return 'backup_suffix'
        
        return None
    
    def analyze_backup_safety(self, backup_files: Dict[str, List[Path]]) -> Dict[str, Dict]:
        """Analyze which backups are safe to remove"""
        analysis = {}
        
        for category, files in backup_files.items():
            if not files:
                continue
                
            safety_analysis = {
                'total_files': len(files),
                'total_size_mb': 0,
                'safe_to_remove': [],
                'review_needed': [],
                'oldest_file': None,
                'newest_file': None
            }
            
            file_stats = []
            for file_path in files:
                try:
                    stat = file_path.stat()
                    file_info = {
                        'path': file_path,
                        'size': stat.st_size,
                        'modified': datetime.fromtimestamp(stat.st_mtime)
                    }
                    file_stats.append(file_info)
                    safety_analysis['total_size_mb'] += stat.st_size / (1024 * 1024)
                except:
                    pass
            
            if file_stats:
                # Sort by modification time
                file_stats.sort(key=lambda x: x['modified'])
                safety_analysis['oldest_file'] = file_stats[0]['modified']
                safety_analysis['newest_file'] = file_stats[-1]['modified']
                
                # Determine safety based on category and age
                for file_info in file_stats:
                    if self.is_safe_to_remove(file_info, category):
                        safety_analysis['safe_to_remove'].append(file_info['path'])
                    else:
                        safety_analysis['review_needed'].append(file_info['path'])
            
            analysis[category] = safety_analysis
        
        return analysis
    
    def is_safe_to_remove(self, file_info: Dict, category: str) -> bool:
        """Determine if a backup file is safe to remove"""
        age_days = (datetime.now() - file_info['modified']).days
        size_mb = file_info['size'] / (1024 * 1024)
        
        # Very old backups (over 30 days) are usually safe
        if age_days > 30:
            return True
        
        # Progressive Framework multiple backups (.backup.backup.backup)
        if category == 'progressive_backups':
            return True  # These are definitely safe from our recent work
        
        # Very small backup files (under 1MB and over 7 days old)
        if size_mb < 1 and age_days > 7:
            return True
        
        # Copy files and version copies over 14 days old
        if category in ['copy_files', 'version_copies'] and age_days > 14:
            return True
        
        # Timestamp backups over 14 days old
        if category == 'timestamp_backup' and age_days > 14:
            return True
        
        return False
    
    def generate_cleanup_report(self, analysis: Dict) -> str:
        """Generate detailed cleanup report"""
        report = f"""# BACKUP FILE CLEANUP REPORT

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Base Directory**: {self.base_dir}

## SUMMARY

"""
        
        total_files = sum(cat['total_files'] for cat in analysis.values())
        total_size = sum(cat['total_size_mb'] for cat in analysis.values())
        total_safe = sum(len(cat['safe_to_remove']) for cat in analysis.values())
        total_review = sum(len(cat['review_needed']) for cat in analysis.values())
        
        report += f"- **Total Backup Files**: {total_files}\n"
        report += f"- **Total Size**: {total_size:.1f} MB\n"
        report += f"- **Safe to Remove**: {total_safe} files\n"
        report += f"- **Review Needed**: {total_review} files\n\n"
        
        # Detailed breakdown
        for category, data in analysis.items():
            if data['total_files'] == 0:
                continue
                
            report += f"## {category.replace('_', ' ').title()}\n\n"
            report += f"- **Total Files**: {data['total_files']}\n"
            report += f"- **Total Size**: {data['total_size_mb']:.1f} MB\n"
            report += f"- **Safe to Remove**: {len(data['safe_to_remove'])}\n"
            report += f"- **Review Needed**: {len(data['review_needed'])}\n"
            
            if data['oldest_file'] and data['newest_file']:
                report += f"- **Date Range**: {data['oldest_file'].strftime('%Y-%m-%d')} to {data['newest_file'].strftime('%Y-%m-%d')}\n"
            
            report += "\n"
            
            # Show some examples of safe to remove
            if data['safe_to_remove']:
                report += f"### Safe to Remove Examples:\n"
                for file_path in data['safe_to_remove'][:5]:
                    relative_path = file_path.relative_to(self.base_dir)
                    report += f"- `{relative_path}`\n"
                if len(data['safe_to_remove']) > 5:
                    report += f"- ... and {len(data['safe_to_remove']) - 5} more\n"
                report += "\n"
        
        # Cleanup recommendations
        report += """## CLEANUP RECOMMENDATIONS

### ✅ SAFE TO REMOVE
- Progressive Framework multiple backups (.backup.backup.backup)
- Backup files older than 30 days
- Small backup files (< 1MB) older than 7 days
- Copy files and version copies older than 14 days
- Timestamp backups older than 14 days

### ⚠️ REVIEW MANUALLY
- Recent backup files (< 7 days old)
- Large backup files (> 10MB)
- Backup files in critical system directories

### 🔒 NEVER REMOVE
- Original files (without backup extensions)
- Active configuration files
- Recently modified important documents

## CLEANUP COMMANDS

### Safe Cleanup (Recommended)
Run the generated cleanup script to remove only confirmed safe files.

### Manual Review
Check the 'Review Needed' files manually before deciding to remove them.
"""
        
        return report
    
    def create_cleanup_script(self, analysis: Dict) -> str:
        """Create automated cleanup script"""
        cleanup_script = f"""#!/usr/bin/env python3
\"\"\"
Automated Backup File Cleanup - Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Removes only files confirmed as safe to remove.
\"\"\"

import os
import shutil
from pathlib import Path
from datetime import datetime

def cleanup_backup_files():
    base_dir = Path(r"{self.base_dir}")
    cleanup_backup_dir = base_dir / "removed_backups"
    cleanup_backup_dir.mkdir(exist_ok=True)
    
    print("🧹 BACKUP FILE CLEANUP STARTING")
    print(f"📁 Backup directory: {{cleanup_backup_dir}}")
    print("🔒 Only removing files confirmed as safe")
    
    # Files confirmed as safe to remove
    safe_files = [
"""
        
        # Add all safe-to-remove files
        for category, data in analysis.items():
            for file_path in data['safe_to_remove']:
                cleanup_script += f'        r"{file_path}",\n'
        
        cleanup_script += """    ]
    
    removed_count = 0
    total_size_mb = 0
    
    for file_path_str in safe_files:
        file_path = Path(file_path_str)
        if file_path.exists():
            try:
                # Get file size before removal
                file_size = file_path.stat().st_size
                total_size_mb += file_size / (1024 * 1024)
                
                # Create backup copy before removal
                backup_name = f"{file_path.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                backup_path = cleanup_backup_dir / backup_name
                shutil.copy2(file_path, backup_path)
                
                # Remove original
                file_path.unlink()
                print(f"✅ Removed: {file_path.name}")
                removed_count += 1
                
            except Exception as e:
                print(f"❌ Error removing {file_path.name}: {e}")
    
    print(f"🎯 Cleanup complete:")
    print(f"   Files removed: {removed_count}")
    print(f"   Space freed: {total_size_mb:.1f} MB")
    print(f"   Backups saved: {cleanup_backup_dir}")

if __name__ == "__main__":
    print("🧹 PROGRESSIVE FRAMEWORK BACKUP CLEANUP")
    print("This will remove backup files confirmed as safe to remove.")
    print("All removed files will be backed up before deletion.")
    print("")
    confirm = input("Type 'YES' to proceed with backup cleanup: ")
    if confirm == 'YES':
        cleanup_backup_files()
    else:
        print("Cleanup cancelled.")
"""
        
        return cleanup_script
    
    def run_analysis(self) -> None:
        """Run complete backup file analysis"""
        print("🧹 PROGRESSIVE FRAMEWORK BACKUP FILE CLEANUP")
        print(f"📁 Base Directory: {self.base_dir}")
        print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Scan for backup files
        backup_files = self.scan_backup_files()
        
        # Analyze safety
        analysis = self.analyze_backup_safety(backup_files)
        
        # Generate report
        report = self.generate_cleanup_report(analysis)
        report_path = self.base_dir / f"backup_cleanup_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        report_path.write_text(report, encoding='utf-8')
        
        # Generate cleanup script
        cleanup_script = self.create_cleanup_script(analysis)
        cleanup_path = self.base_dir / f"backup_cleanup_script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
        cleanup_path.write_text(cleanup_script, encoding='utf-8')
        
        # Print summary
        total_files = sum(len(files) for files in backup_files.values())
        total_safe = sum(len(cat['safe_to_remove']) for cat in analysis.values())
        total_size = sum(cat['total_size_mb'] for cat in analysis.values())
        
        print(f"\n📊 ANALYSIS COMPLETE")
        print(f"📄 Report: {report_path.name}")
        print(f"🧹 Cleanup script: {cleanup_path.name}")
        print(f"📁 Total backup files: {total_files}")
        print(f"✅ Safe to remove: {total_safe}")
        print(f"💾 Total size: {total_size:.1f} MB")

def main():
    """Main execution function"""
    import sys
    
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = input("📁 Enter base directory path (or press Enter for current): ").strip()
        if not base_dir:
            base_dir = os.getcwd()
    
    if not os.path.exists(base_dir):
        print(f"❌ Directory not found: {base_dir}")
        sys.exit(1)
    
    cleaner = BackupFileCleaner(base_dir)
    cleaner.run_analysis()

if __name__ == "__main__":
    main()
