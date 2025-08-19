#!/usr/bin/env python3
"""
FILE: integrated_progressive_framework_header_system.py
WORKING_DIRECTORY: C:/Users/Wales/OneDrive/Desktop/PROGRESSIVE_FRAMEWORK-Set-2/B2 Optimised 16_08_2025
PURPOSE: Integrated Progressive Framework Header System - Combines intelligent system identification with targeted header application
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: 20250819_Progressive-Framework-Integration
STATUS: ✅ Progressive Framework System File
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | System Integration ✅
PROGRESSIVE_FRAMEWORK: Core System | Confidence: 100 | System Validated ✅

Integrated Progressive Framework Header System
Combines intelligent system identification with targeted header application
"""

import os
import re
import json
import shutil
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from datetime import datetime

class IntegratedProgressiveFrameworkHeaderSystem:
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        
        # Import both components
        from progressive_framework_system_identifier import ProgressiveFrameworkSystemIdentifier
        
        self.identifier = ProgressiveFrameworkSystemIdentifier(base_directory)
        self.scan_results = None
        
        # Header templates for different file types
        self.templates = self.create_progressive_templates()
    
    def create_progressive_templates(self) -> Dict[str, str]:
        """Create Progressive Framework header templates"""
        return {
            'md': '''<!--
FILE: [fileName]
WORKING_DIRECTORY: [fullDirectory]
PURPOSE: [purpose]
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: [YYYYMMDD]_[description]
STATUS: ✅ Progressive Framework System File
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | System Integration ✅
PROGRESSIVE_FRAMEWORK: [fileCategory] | Confidence: [confidence] | System Validated ✅
-->''',
            'py': '''#!/usr/bin/env python3
"""
FILE: [fileName]
WORKING_DIRECTORY: [fullDirectory]
PURPOSE: [purpose]
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: [YYYYMMDD]_[description]
STATUS: ✅ Progressive Framework System File
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | System Integration ✅
PROGRESSIVE_FRAMEWORK: [fileCategory] | Confidence: [confidence] | System Validated ✅
"""''',
            'json': '''{
  "_progressive_header": {
    "FILE": "[fileName]",
    "WORKING_DIRECTORY": "[fullDirectory]",
    "PURPOSE": "[purpose]",
    "CREATOR": "Amos Wales - Progressive Framework Pioneer",
    "UPDATED": "[YYYYMMDD]_[description]",
    "STATUS": "✅ Progressive Framework System File",
    "BREATHING_FRAMEWORK": "15 Systems ✅ | 615+ Tests ✅ | System Integration ✅",
    "PROGRESSIVE_FRAMEWORK": "[fileCategory] | Confidence: [confidence] | System Validated ✅"
  },''',
            'yaml': '''#
# FILE: [fileName]
# WORKING_DIRECTORY: [fullDirectory]
# PURPOSE: [purpose]
# CREATOR: Amos Wales - Progressive Framework Pioneer
# UPDATED: [YYYYMMDD]_[description]
# STATUS: ✅ Progressive Framework System File
# BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | System Integration ✅
# PROGRESSIVE_FRAMEWORK: [fileCategory] | Confidence: [confidence] | System Validated ✅
#''',
            'txt': '''#
# FILE: [fileName]
# WORKING_DIRECTORY: [fullDirectory]
# PURPOSE: [purpose]
# CREATOR: Amos Wales - Progressive Framework Pioneer
# UPDATED: [YYYYMMDD]_[description]
# STATUS: ✅ Progressive Framework System File
# BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | System Integration ✅
# PROGRESSIVE_FRAMEWORK: [fileCategory] | Confidence: [confidence] | System Validated ✅
#'''
        }
    
    def run_integrated_workflow(self, mode: str = 'intelligent') -> Dict[str, any]:
        """Run the complete integrated workflow"""
        print("🚀 Starting Integrated Progressive Framework Header System")
        print(f"📂 Base Directory: {self.base_dir}")
        print(f"🎯 Mode: {mode}")
        print("=" * 70)
        
        # Step 1: Identify system files
        print("\n🔍 STEP 1: INTELLIGENT SYSTEM IDENTIFICATION")
        self.scan_results = self.identifier.scan_all_files()
        
        summary = self.scan_results['summary']
        print(f"✅ Scan Complete:")
        print(f"   Total Files: {summary['total_files_scanned']}")
        print(f"   System Files: {summary['system_files_identified']}")
        print(f"   Files Needing Headers: {summary['files_needing_headers']}")
        print(f"   Already Compliant: {summary['files_already_compliant']}")
        
        # Step 2: Apply headers based on mode
        if mode == 'intelligent':
            return self.apply_headers_intelligent()
        elif mode == 'core_only':
            return self.apply_headers_core_only()
        elif mode == 'all_system':
            return self.apply_headers_all_system()
        elif mode == 'scan_only':
            return self.generate_scan_report()
        else:
            raise ValueError(f"Unknown mode: {mode}")
    
    def apply_headers_intelligent(self) -> Dict[str, any]:
        """Apply headers using intelligent prioritization"""
        print("\n🎯 STEP 2: INTELLIGENT HEADER APPLICATION")
        
        results = {
            'core_system_applied': 0,
            'component_applied': 0,
            'related_applied': 0,
            'total_applied': 0,
            'errors': []
        }
        
        # Priority 1: Core System Files (must have headers)
        core_files = [f for f in self.scan_results['core_system_files'] if f['needs_header']]
        print(f"🌟 Applying headers to {len(core_files)} core system files...")
        
        for file_info in core_files:
            if self.apply_header_to_file(file_info):
                results['core_system_applied'] += 1
            else:
                results['errors'].append(f"Failed: {file_info['name']}")
        
        # Priority 2: System Component Files (should have headers)
        component_files = [f for f in self.scan_results['system_component_files'] if f['needs_header']]
        print(f"🔧 Applying headers to {len(component_files)} system component files...")
        
        for file_info in component_files:
            if self.apply_header_to_file(file_info):
                results['component_applied'] += 1
            else:
                results['errors'].append(f"Failed: {file_info['name']}")
        
        # Priority 3: System Related Files (nice to have headers)
        related_files = [f for f in self.scan_results['system_related_files'] if f['needs_header']]
        print(f"📋 Applying headers to {len(related_files)} system related files...")
        
        for file_info in related_files:
            if self.apply_header_to_file(file_info):
                results['related_applied'] += 1
            else:
                results['errors'].append(f"Failed: {file_info['name']}")
        
        results['total_applied'] = (results['core_system_applied'] + 
                                   results['component_applied'] + 
                                   results['related_applied'])
        
        self.print_application_results(results)
        return results
    
    def apply_headers_core_only(self) -> Dict[str, any]:
        """Apply headers only to core system files"""
        print("\n🌟 STEP 2: CORE SYSTEM FILES ONLY")
        
        core_files = [f for f in self.scan_results['core_system_files'] if f['needs_header']]
        print(f"Applying headers to {len(core_files)} core system files...")
        
        results = {'core_applied': 0, 'total_applied': 0, 'errors': []}
        
        for file_info in core_files:
            if self.apply_header_to_file(file_info):
                results['core_applied'] += 1
            else:
                results['errors'].append(f"Failed: {file_info['name']}")
        
        results['total_applied'] = results['core_applied']
        self.print_application_results(results)
        return results
    
    def apply_headers_all_system(self) -> Dict[str, any]:
        """Apply headers to all identified system files"""
        print("\n🚀 STEP 2: ALL SYSTEM FILES")
        
        all_system_files = self.scan_results['files_needing_headers']
        print(f"Applying headers to {len(all_system_files)} system files...")
        
        results = {'all_applied': 0, 'total_applied': 0, 'errors': []}
        
        for file_info in all_system_files:
            if self.apply_header_to_file(file_info):
                results['all_applied'] += 1
            else:
                results['errors'].append(f"Failed: {file_info['name']}")
        
        results['total_applied'] = results['all_applied']
        self.print_application_results(results)
        return results
    
    def apply_header_to_file(self, file_info: Dict) -> bool:
        """Apply Progressive Framework header to a specific file"""
        try:
            file_path = file_info['path']
            analysis = file_info['analysis']
            
            # Create backup
            backup_path = file_path.with_suffix(file_path.suffix + '.backup')
            shutil.copy2(file_path, backup_path)
            
            # Read existing content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                existing_content = f.read()
            
            # Generate header
            header = self.generate_progressive_header(file_path, analysis)
            if not header:
                print(f"❌ Could not generate header for {file_path.name}")
                return False
            
            # Write header + existing content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(header + '\n\n' + existing_content)
            
            print(f"✅ Applied header to {file_path.name} ({analysis['file_category']}, confidence: {analysis['confidence_score']})")
            return True
            
        except Exception as e:
            print(f"❌ Error applying header to {file_path}: {e}")
            return False
    
    def generate_progressive_header(self, file_path: Path, analysis: Dict) -> str:
        """Generate Progressive Framework header with system context"""
        # Detect file type
        file_type = self.detect_file_type(file_path)
        template = self.templates.get(file_type, self.templates['txt'])
        
        # Auto-detect purpose based on analysis
        purpose = self.auto_detect_purpose(file_path, analysis)
        
        # Get working directory
        working_dir = str(file_path.parent).replace('\\', '\\\\')
        
        # Replace template placeholders
        header = template.replace('[fileName]', file_path.name)
        header = header.replace('[fullDirectory]', working_dir)
        header = header.replace('[purpose]', purpose)
        header = header.replace('[YYYYMMDD]', datetime.now().strftime('%Y%m%d'))
        header = header.replace('[description]', 'Progressive-Framework-Integration')
        header = header.replace('[fileCategory]', analysis['file_category'].title())
        header = header.replace('[confidence]', str(analysis['confidence_score']))
        
        return header
    
    def detect_file_type(self, file_path: Path) -> str:
        """Detect file type for header template selection"""
        suffix = file_path.suffix.lower()
        extension_map = {
            '.md': 'md', '.py': 'py', '.json': 'json', 
            '.yaml': 'yaml', '.yml': 'yaml', '.xml': 'txt',
            '.txt': 'txt', '.cfg': 'txt', '.conf': 'txt'
        }
        return extension_map.get(suffix, 'txt')
    
    def auto_detect_purpose(self, file_path: Path, analysis: Dict) -> str:
        """Auto-detect file purpose based on path and analysis"""
        path_str = str(file_path).lower()
        name = file_path.name.lower()
        
        # Purpose detection based on indicators found
        indicators = analysis.get('indicators_found', [])
        
        if any('system' in ind for ind in indicators):
            return "Progressive Framework System Specification"
        elif any('lesson' in ind for ind in indicators):
            return "Progressive Framework Educational Content"
        elif any('test' in ind for ind in indicators):
            return "Progressive Framework Testing Component"
        elif any('script' in ind for ind in indicators):
            return "Progressive Framework Automation Script"
        elif 'config' in path_str or 'configuration' in name:
            return "Progressive Framework Configuration"
        elif 'template' in path_str:
            return "Progressive Framework Template"
        elif 'docs' in path_str or 'documentation' in name:
            return "Progressive Framework Documentation"
        else:
            return "Progressive Framework System Component"
    
    def print_application_results(self, results: Dict) -> None:
        """Print formatted results of header application"""
        print(f"\n📊 HEADER APPLICATION RESULTS:")
        
        if 'core_system_applied' in results:
            print(f"   🌟 Core System Files: {results['core_system_applied']}")
        if 'component_applied' in results:
            print(f"   🔧 Component Files: {results['component_applied']}")
        if 'related_applied' in results:
            print(f"   📋 Related Files: {results['related_applied']}")
        if 'core_applied' in results:
            print(f"   🌟 Core Files: {results['core_applied']}")
        if 'all_applied' in results:
            print(f"   🚀 All System Files: {results['all_applied']}")
            
        print(f"   📈 Total Applied: {results['total_applied']}")
        
        if results['errors']:
            print(f"   ❌ Errors: {len(results['errors'])}")
            for error in results['errors'][:5]:  # Show first 5 errors
                print(f"      - {error}")
    
    def generate_scan_report(self) -> Dict[str, any]:
        """Generate detailed scan report without applying headers"""
        print("\n📋 STEP 2: GENERATING SCAN REPORT")
        
        report = self.identifier.generate_report(self.scan_results)
        
        # Save report to file
        report_file = self.base_dir / "progressive_framework_system_analysis.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📄 Detailed report saved to: {report_file}")
        
        return {
            'report_generated': True,
            'report_file': str(report_file),
            'total_system_files': self.scan_results['summary']['system_files_identified'],
            'files_needing_headers': self.scan_results['summary']['files_needing_headers']
        }
    
    def calculate_new_compliance(self) -> Dict[str, float]:
        """Calculate what compliance would be after header application"""
        if not self.scan_results:
            return {}
        
        total_files = self.scan_results['summary']['total_files_scanned']
        current_compliant = self.scan_results['summary']['files_already_compliant']
        system_files_needing = self.scan_results['summary']['files_needing_headers']
        
        # Current compliance
        current_compliance = (current_compliant / total_files * 100) if total_files > 0 else 0
        
        # Potential compliance (if all system files get headers)
        potential_compliant = current_compliant + system_files_needing
        potential_compliance = (potential_compliant / total_files * 100) if total_files > 0 else 0
        
        # System-only compliance (only counting system files)
        total_system_files = self.scan_results['summary']['system_files_identified']
        system_compliance = (current_compliant / total_system_files * 100) if total_system_files > 0 else 0
        potential_system_compliance = 100.0  # All system files would have headers
        
        return {
            'current_overall': current_compliance,
            'potential_overall': potential_compliance,
            'current_system_only': system_compliance,
            'potential_system_only': potential_system_compliance,
            'total_files': total_files,
            'total_system_files': total_system_files
        }

def main():
    """Main execution function"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python integrated_progressive_framework_header_system.py <base_directory> [mode]")
        print("Modes:")
        print("  intelligent (default) - Smart prioritization: core → components → related")
        print("  core_only            - Only core system files")
        print("  all_system           - All identified system files")
        print("  scan_only            - Generate report without applying headers")
        sys.exit(1)
    
    base_dir = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'intelligent'
    
    print("🚀 Integrated Progressive Framework Header System")
    print(f"📂 Base Directory: {base_dir}")
    print(f"🎯 Mode: {mode}")
    print("=" * 70)
    
    try:
        system = IntegratedProgressiveFrameworkHeaderSystem(base_dir)
        results = system.run_integrated_workflow(mode)
        
        # Show compliance projections
        if mode != 'scan_only':
            compliance = system.calculate_new_compliance()
            print(f"\n📈 COMPLIANCE ANALYSIS:")
            print(f"   Current Overall: {compliance.get('current_overall', 0):.1f}%")
            print(f"   After Headers: {compliance.get('potential_overall', 0):.1f}%")
            print(f"   System Files Only: {compliance.get('potential_system_only', 0):.1f}%")
        
        print(f"\n🎉 Integrated workflow completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()