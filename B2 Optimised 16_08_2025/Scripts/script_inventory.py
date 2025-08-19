#!/usr/bin/env python3
"""
Complete Script Inventory Tool
Provides comprehensive listing of ALL scripts for manual review
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

class ScriptInventory:
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        
    def scan_all_scripts(self) -> Dict[str, List[Dict]]:
        """Scan and catalog every script file in the framework"""
        script_extensions = {'.py', '.bat', '.ps1', '.sh', '.cmd', '.vbs', '.ps'}
        
        inventory = {
            'root_scripts': [],
            'scripts_directory': [],
            'devscripts_directory': [],
            'other_locations': []
        }
        
        print("🔍 SCANNING ALL SCRIPT FILES")
        print("=" * 50)
        
        # Scan root directory (non-recursive)
        print("📁 Scanning root directory...")
        for file_path in self.base_dir.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in script_extensions:
                script_info = self.analyze_script_file(file_path)
                inventory['root_scripts'].append(script_info)
        
        # Scan scripts directory (recursive)
        scripts_dir = self.base_dir / 'scripts'
        if scripts_dir.exists():
            print("📁 Scanning scripts directory...")
            for file_path in scripts_dir.rglob('*'):
                if file_path.is_file() and file_path.suffix.lower() in script_extensions:
                    script_info = self.analyze_script_file(file_path)
                    inventory['scripts_directory'].append(script_info)
        
        # Scan devscripts directory (recursive)
        devscripts_dir = self.base_dir / 'devscripts'
        if devscripts_dir.exists():
            print("📁 Scanning devscripts directory...")
            for file_path in devscripts_dir.rglob('*'):
                if file_path.is_file() and file_path.suffix.lower() in script_extensions:
                    script_info = self.analyze_script_file(file_path)
                    inventory['devscripts_directory'].append(script_info)
        
        # Scan all other locations (recursive from root, excluding already scanned)
        print("📁 Scanning other locations...")
        exclude_dirs = {'scripts', 'devscripts', '.git', '__pycache__', '.vscode', 'node_modules'}
        
        for file_path in self.base_dir.rglob('*'):
            if (file_path.is_file() and 
                file_path.suffix.lower() in script_extensions and
                file_path.parent != self.base_dir and  # Not in root
                not any(excluded in file_path.parts for excluded in exclude_dirs)):
                
                script_info = self.analyze_script_file(file_path)
                inventory['other_locations'].append(script_info)
        
        return inventory
    
    def analyze_script_file(self, file_path: Path) -> Dict:
        """Analyze individual script file"""
        try:
            stats = file_path.stat()
            
            # Basic file info
            script_info = {
                'name': file_path.name,
                'path': str(file_path.relative_to(self.base_dir)),
                'full_path': str(file_path),
                'size_bytes': stats.st_size,
                'size_kb': round(stats.st_size / 1024, 2),
                'modified': datetime.fromtimestamp(stats.st_mtime),
                'extension': file_path.suffix,
                'directory': str(file_path.parent.relative_to(self.base_dir))
            }
            
            # Content analysis
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                script_info.update(self.analyze_content(content, file_path))
                
            except Exception as e:
                script_info['content_error'] = str(e)
                script_info['content_preview'] = "Could not read file"
                script_info['purpose_guess'] = "Unknown (unreadable)"
        
        except Exception as e:
            script_info = {
                'name': file_path.name,
                'path': str(file_path.relative_to(self.base_dir)),
                'error': str(e)
            }
        
        return script_info
    
    def analyze_content(self, content: str, file_path: Path) -> Dict:
        """Analyze script content for purpose and characteristics"""
        analysis = {}
        
        # Basic content stats
        lines = content.split('\n')
        analysis['line_count'] = len(lines)
        analysis['content_preview'] = '\n'.join(lines[:5])  # First 5 lines
        
        # Content indicators
        content_lower = content.lower()
        indicators = []
        
        # Framework-specific indicators
        if 'progressive framework' in content_lower:
            indicators.append('Progressive Framework')
        if 'breathing framework' in content_lower:
            indicators.append('Breathing Framework')
        if 'header' in content_lower and 'applicator' in content_lower:
            indicators.append('Header Management')
        if 'lesson' in content_lower:
            indicators.append('Educational/Lessons')
        if 'academy' in content_lower:
            indicators.append('Progressive Academy')
        if 'debugging' in content_lower:
            indicators.append('Debugging')
        if 'automation' in content_lower:
            indicators.append('Automation')
        if 'test' in content_lower:
            indicators.append('Testing')
        if 'backup' in content_lower:
            indicators.append('Backup/Utility')
        if 'cleanup' in content_lower or 'clean' in content_lower:
            indicators.append('Cleanup/Maintenance')
        if 'evolutionary' in content_lower:
            indicators.append('Evolutionary Mapping')
        if 'orchestration' in content_lower:
            indicators.append('System Orchestration')
        if 'specification' in content_lower:
            indicators.append('Specifications')
        
        analysis['content_indicators'] = indicators
        
        # Python-specific analysis
        if file_path.suffix == '.py':
            # Extract imports
            imports = re.findall(r'^(?:from\s+(\S+)\s+)?import\s+(.+)', content, re.MULTILINE)
            analysis['imports'] = [imp[1] if imp[0] == '' else f"{imp[0]}.{imp[1]}" for imp in imports]
            
            # Extract functions
            functions = re.findall(r'^def\s+(\w+)', content, re.MULTILINE)
            analysis['functions'] = functions[:10]  # First 10 functions
            analysis['function_count'] = len(functions)
            
            # Extract classes
            classes = re.findall(r'^class\s+(\w+)', content, re.MULTILINE)
            analysis['classes'] = classes
        
        # Purpose guessing
        filename = file_path.name.lower()
        purpose_clues = []
        
        if 'progressive' in filename:
            purpose_clues.append('Progressive Framework component')
        if 'breathing' in filename:
            purpose_clues.append('Breathing Framework automation')
        if 'header' in filename:
            purpose_clues.append('Header management system')
        if 'lesson' in filename:
            purpose_clues.append('Educational content system')
        if 'test' in filename:
            purpose_clues.append('Testing/validation script')
        if 'backup' in filename or 'temp' in filename:
            purpose_clues.append('Temporary/backup utility')
        if 'cleanup' in filename or 'clean' in filename:
            purpose_clues.append('Cleanup/maintenance tool')
        if 'automation' in filename or 'auto' in filename:
            purpose_clues.append('Automation script')
        if 'diagnostic' in filename or 'debug' in filename:
            purpose_clues.append('Diagnostic/debugging tool')
        if 'evolutionary' in filename:
            purpose_clues.append('Evolutionary mapping system')
        if 'orchestration' in filename:
            purpose_clues.append('System orchestration')
        if 'specification' in filename or 'spec' in filename:
            purpose_clues.append('Specification management')
        
        analysis['purpose_guess'] = '; '.join(purpose_clues) if purpose_clues else 'General utility/unknown'
        
        return analysis
    
    def generate_inventory_report(self, inventory: Dict) -> str:
        """Generate comprehensive inventory report"""
        report = f"""# COMPLETE SCRIPT INVENTORY REPORT

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Base Directory**: {self.base_dir}

## OVERVIEW

"""
        
        # Calculate totals
        total_scripts = sum(len(scripts) for scripts in inventory.values())
        total_size = 0
        
        for location, scripts in inventory.items():
            count = len(scripts)
            size = sum(script.get('size_bytes', 0) for script in scripts)
            total_size += size
            
            report += f"- **{location.replace('_', ' ').title()}**: {count} scripts ({size/1024:.1f} KB)\n"
        
        report += f"- **Total**: {total_scripts} scripts ({total_size/1024:.1f} KB)\n\n"
        
        # Detailed listings
        for location, scripts in inventory.items():
            if not scripts:
                continue
                
            report += f"## {location.replace('_', ' ').upper()}\n\n"
            
            # Sort by modification date (newest first)
            sorted_scripts = sorted(scripts, 
                                  key=lambda x: x.get('modified', datetime.min), 
                                  reverse=True)
            
            for i, script in enumerate(sorted_scripts, 1):
                report += f"### {i}. {script['name']}\n\n"
                report += f"**Path**: `{script['path']}`\n"
                report += f"**Size**: {script.get('size_kb', 0)} KB ({script.get('line_count', 'Unknown')} lines)\n"
                report += f"**Modified**: {script.get('modified', 'Unknown').strftime('%Y-%m-%d %H:%M:%S') if isinstance(script.get('modified'), datetime) else 'Unknown'}\n"
                report += f"**Purpose**: {script.get('purpose_guess', 'Unknown')}\n"
                
                if script.get('content_indicators'):
                    report += f"**Contains**: {', '.join(script['content_indicators'])}\n"
                
                if script.get('functions'):
                    func_list = script['functions'][:5]  # First 5 functions
                    more_text = f" (+{len(script['functions']) - 5} more)" if len(script['functions']) > 5 else ""
                    report += f"**Functions**: {', '.join(func_list)}{more_text}\n"
                
                if script.get('imports'):
                    import_list = script['imports'][:3]  # First 3 imports
                    more_text = f" (+{len(script['imports']) - 3} more)" if len(script['imports']) > 3 else ""
                    report += f"**Key Imports**: {', '.join(import_list)}{more_text}\n"
                
                # Content preview
                if script.get('content_preview'):
                    preview = script['content_preview'][:200]  # First 200 chars
                    if len(script.get('content_preview', '')) > 200:
                        preview += "..."
                    report += f"**Preview**:\n```\n{preview}\n```\n"
                
                report += "\n---\n\n"
        
        # Summary recommendations
        report += "## REVIEW RECOMMENDATIONS\n\n"
        report += "### 🔍 MANUAL REVIEW NEEDED\n\n"
        
        # Group by likely importance
        framework_scripts = []
        utility_scripts = []
        unknown_scripts = []
        
        for location, scripts in inventory.items():
            for script in scripts:
                purpose = script.get('purpose_guess', '').lower()
                name = script['name'].lower()
                
                if any(keyword in purpose or keyword in name 
                       for keyword in ['progressive', 'breathing', 'framework', 'header', 'lesson']):
                    framework_scripts.append(script)
                elif any(keyword in purpose or keyword in name 
                         for keyword in ['test', 'backup', 'temp', 'cleanup', 'utility']):
                    utility_scripts.append(script)
                else:
                    unknown_scripts.append(script)
        
        report += f"**🔴 Likely Framework Scripts ({len(framework_scripts)})**: Review carefully, probably keep\n"
        report += f"**🟡 Likely Utility Scripts ({len(utility_scripts)})**: May be safe to clean if old\n"
        report += f"**⚪ Unknown Purpose Scripts ({len(unknown_scripts)})**: Need manual examination\n\n"
        
        report += "### ⚠️ CLEANUP SAFETY GUIDELINES\n\n"
        report += "1. **Never delete without backup** - Always create backups first\n"
        report += "2. **Test framework after cleanup** - Ensure everything still works\n"
        report += "3. **Keep recent files** - Scripts modified in last month are likely active\n"
        report += "4. **Preserve framework components** - Anything with 'progressive', 'breathing', 'framework'\n"
        report += "5. **Check dependencies** - Look for import statements and subprocess calls\n"
        
        return report
    
    def create_quick_summary(self, inventory: Dict) -> None:
        """Print quick summary to console"""
        print("\n" + "="*60)
        print("📊 SCRIPT INVENTORY SUMMARY")
        print("="*60)
        
        total_scripts = 0
        for location, scripts in inventory.items():
            count = len(scripts)
            total_scripts += count
            print(f"{location.replace('_', ' ').title():20}: {count:3} scripts")
        
        print(f"{'TOTAL':20}: {total_scripts:3} scripts")
        print("="*60)
        
        # Show some notable scripts
        all_scripts = []
        for scripts in inventory.values():
            all_scripts.extend(scripts)
        
        # Sort by size (largest first)
        largest = sorted(all_scripts, key=lambda x: x.get('size_bytes', 0), reverse=True)[:5]
        print("\n🔝 LARGEST SCRIPTS:")
        for script in largest:
            print(f"   {script['name']:30} ({script.get('size_kb', 0):6.1f} KB)")
        
        # Sort by modification (newest first)
        newest = sorted([s for s in all_scripts if s.get('modified')], 
                       key=lambda x: x['modified'], reverse=True)[:5]
        print("\n🆕 MOST RECENTLY MODIFIED:")
        for script in newest:
            mod_date = script['modified'].strftime('%Y-%m-%d') if script.get('modified') else 'Unknown'
            print(f"   {script['name']:30} ({mod_date})")
    
    def run_inventory(self) -> None:
        """Run complete script inventory"""
        print("🗂️ COMPLETE SCRIPT INVENTORY")
        print(f"📁 Base Directory: {self.base_dir}")
        print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Scan all scripts
        inventory = self.scan_all_scripts()
        
        # Generate quick summary
        self.create_quick_summary(inventory)
        
        # Generate detailed report
        report = self.generate_inventory_report(inventory)
        report_path = self.base_dir / f"complete_script_inventory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        report_path.write_text(report, encoding='utf-8')
        
        print(f"\n📄 Detailed report saved: {report_path.name}")
        print("🔍 Review the report to decide which scripts to keep/clean")

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
    
    inventory = ScriptInventory(base_dir)
    inventory.run_inventory()

if __name__ == "__main__":
    main()
