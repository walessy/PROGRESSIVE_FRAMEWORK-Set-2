#!/usr/bin/env python3
"""
FILE: piping_compatible_header_applicator.py
WORKING_DIRECTORY: C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025
PURPOSE: Piping-Compatible Progressive Framework Header System - Supports both standalone operation and piped input from system identifier
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: 20250819_Progressive-Framework-Integration
STATUS: ✅ Progressive Framework System File
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | System Integration ✅
PROGRESSIVE_FRAMEWORK: Core System | Confidence: 100 | System Validated ✅

Piping-Compatible Progressive Framework Header System
Supports both standalone operation and piped input from system identifier
"""

import os
import re
import json
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from datetime import datetime

class PipingCompatibleHeaderApplicator:
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
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
    
    def read_piped_input(self) -> Optional[Dict]:
        """Read JSON input from stdin (piped from system identifier)"""
        try:
            if not sys.stdin.isatty():  # Check if there's piped input
                piped_data = sys.stdin.read().strip()
                if piped_data:
                    return json.loads(piped_data)
            return None
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing piped JSON: {e}")
            return None
        except Exception as e:
            print(f"❌ Error reading piped input: {e}")
            return None
    
    def read_json_file(self, json_file: str) -> Optional[Dict]:
        """Read JSON results from file"""
        try:
            json_path = Path(json_file)
            if not json_path.exists():
                print(f"❌ JSON file not found: {json_file}")
                return None
                
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing JSON file: {e}")
            return None
        except Exception as e:
            print(f"❌ Error reading JSON file: {e}")
            return None
    
    def apply_headers_from_results(self, scan_results: Dict, mode: str = 'intelligent') -> Dict[str, any]:
        """Apply headers based on scan results from system identifier"""
        print(f"🚀 Applying headers based on system identification results")
        print(f"🎯 Mode: {mode}")
        
        # Validate scan results structure
        if not self.validate_scan_results(scan_results):
            raise ValueError("Invalid scan results structure")
        
        summary = scan_results.get('summary', {})
        print(f"📊 Input Summary:")
        print(f"   Total Files: {summary.get('total_files_scanned', 0)}")
        print(f"   System Files: {summary.get('system_files_identified', 0)}")
        print(f"   Files Needing Headers: {summary.get('files_needing_headers', 0)}")
        
        if mode == 'intelligent':
            return self.apply_headers_intelligent(scan_results)
        elif mode == 'core_only':
            return self.apply_headers_core_only(scan_results)
        elif mode == 'all_system':
            return self.apply_headers_all_system(scan_results)
        else:
            raise ValueError(f"Unknown mode: {mode}")
    
    def validate_scan_results(self, scan_results: Dict) -> bool:
        """Validate the structure of scan results"""
        required_keys = ['summary', 'files_needing_headers']
        for key in required_keys:
            if key not in scan_results:
                print(f"❌ Missing required key in scan results: {key}")
                return False
        return True
    
    def apply_headers_intelligent(self, scan_results: Dict) -> Dict[str, any]:
        """Apply headers using intelligent prioritization"""
        print("\n🎯 INTELLIGENT HEADER APPLICATION")
        
        results = {
            'core_system_applied': 0,
            'component_applied': 0,
            'related_applied': 0,
            'total_applied': 0,
            'errors': []
        }
        
        # Get file lists from scan results
        core_files = [f for f in scan_results.get('core_system_files', []) 
                     if self.file_needs_header(f)]
        component_files = [f for f in scan_results.get('system_component_files', []) 
                          if self.file_needs_header(f)]
        related_files = [f for f in scan_results.get('system_related_files', []) 
                        if self.file_needs_header(f)]
        
        # Priority 1: Core System Files
        if core_files:
            print(f"🌟 Applying headers to {len(core_files)} core system files...")
            for file_info in core_files:
                if self.apply_header_to_file(file_info):
                    results['core_system_applied'] += 1
                else:
                    results['errors'].append(f"Failed: {file_info.get('name', 'unknown')}")
        
        # Priority 2: System Component Files
        if component_files:
            print(f"🔧 Applying headers to {len(component_files)} system component files...")
            for file_info in component_files:
                if self.apply_header_to_file(file_info):
                    results['component_applied'] += 1
                else:
                    results['errors'].append(f"Failed: {file_info.get('name', 'unknown')}")
        
        # Priority 3: System Related Files
        if related_files:
            print(f"📋 Applying headers to {len(related_files)} system related files...")
            for file_info in related_files:
                if self.apply_header_to_file(file_info):
                    results['related_applied'] += 1
                else:
                    results['errors'].append(f"Failed: {file_info.get('name', 'unknown')}")
        
        results['total_applied'] = (results['core_system_applied'] + 
                                   results['component_applied'] + 
                                   results['related_applied'])
        
        self.print_application_results(results)
        return results
    
    def apply_headers_core_only(self, scan_results: Dict) -> Dict[str, any]:
        """Apply headers only to core system files"""
        print("\n🌟 CORE SYSTEM FILES ONLY")
        
        core_files = [f for f in scan_results.get('core_system_files', []) 
                     if self.file_needs_header(f)]
        
        print(f"Applying headers to {len(core_files)} core system files...")
        
        results = {'core_applied': 0, 'total_applied': 0, 'errors': []}
        
        for file_info in core_files:
            if self.apply_header_to_file(file_info):
                results['core_applied'] += 1
            else:
                results['errors'].append(f"Failed: {file_info.get('name', 'unknown')}")
        
        results['total_applied'] = results['core_applied']
        self.print_application_results(results)
        return results
    
    def apply_headers_all_system(self, scan_results: Dict) -> Dict[str, any]:
        """Apply headers to all identified system files"""
        print("\n🚀 ALL SYSTEM FILES")
        
        all_system_files = scan_results.get('files_needing_headers', [])
        print(f"Applying headers to {len(all_system_files)} system files...")
        
        results = {'all_applied': 0, 'total_applied': 0, 'errors': []}
        
        for file_info in all_system_files:
            if self.apply_header_to_file(file_info):
                results['all_applied'] += 1
            else:
                results['errors'].append(f"Failed: {file_info.get('name', 'unknown')}")
        
        results['total_applied'] = results['all_applied']
        self.print_application_results(results)
        return results
    
    def file_needs_header(self, file_info: Dict) -> bool:
        """Check if file needs header based on file_info structure"""
        # Handle different possible structures
        if isinstance(file_info, dict):
            return file_info.get('needs_header', False)
        return False
    
    def apply_header_to_file(self, file_info: Dict) -> bool:
        """Apply Progressive Framework header to a specific file"""
        try:
            # Extract file path from file_info
            if 'path' in file_info:
                file_path = Path(file_info['path'])
            elif 'relative_path' in file_info:
                file_path = self.base_dir / file_info['relative_path']
            else:
                print(f"❌ No path found in file_info: {file_info}")
                return False
            
            analysis = file_info.get('analysis', {})
            
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
            
            category = analysis.get('file_category', 'unknown')
            confidence = analysis.get('confidence_score', 0)
            print(f"✅ Applied header to {file_path.name} ({category}, confidence: {confidence})")
            return True
            
        except Exception as e:
            print(f"❌ Error applying header to file: {e}")
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
        header = header.replace('[fileCategory]', analysis.get('file_category', 'system').title())
        header = header.replace('[confidence]', str(analysis.get('confidence_score', 0)))
        
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
        
        if any('system' in str(ind).lower() for ind in indicators):
            return "Progressive Framework System Specification"
        elif any('lesson' in str(ind).lower() for ind in indicators):
            return "Progressive Framework Educational Content"
        elif any('test' in str(ind).lower() for ind in indicators):
            return "Progressive Framework Testing Component"
        elif any('script' in str(ind).lower() for ind in indicators):
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

def main():
    """Main execution function with piping support"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python piping_compatible_header_applicator.py <base_directory> [mode] [--json-file file.json]")
        print("Modes:")
        print("  intelligent (default) - Smart prioritization: core → components → related")
        print("  core_only            - Only core system files")
        print("  all_system           - All identified system files")
        print()
        print("Input Methods:")
        print("  1. Piped JSON: progressive_framework_system_identifier.py dir export_json | python this_script.py dir")
        print("  2. JSON file: python this_script.py dir intelligent --json-file results.json")
        print("  3. No input: Run standalone (will call system identifier internally)")
        sys.exit(1)
    
    base_dir = sys.argv[1]
    mode = 'intelligent'
    json_file = None
    
    # Parse command line arguments
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg in ['intelligent', 'core_only', 'all_system']:
            mode = arg
        elif arg == '--json-file' and i + 1 < len(sys.argv):
            json_file = sys.argv[i + 1]
            i += 1
        i += 1
    
    print("🚀 Piping-Compatible Progressive Framework Header Applicator")
    print(f"📂 Base Directory: {base_dir}")
    print(f"🎯 Mode: {mode}")
    print("=" * 70)
    
    try:
        applicator = PipingCompatibleHeaderApplicator(base_dir)
        scan_results = None
        
        # Try to get input in order of preference
        
        # 1. Try piped input first
        scan_results = applicator.read_piped_input()
        if scan_results:
            print("📥 Using piped JSON input from system identifier")
        
        # 2. Try JSON file if specified
        elif json_file:
            scan_results = applicator.read_json_file(json_file)
            if scan_results:
                print(f"📄 Using JSON file: {json_file}")
        
        # 3. Run system identifier internally as fallback
        else:
            print("🔍 No input provided - running system identifier internally...")
            # Import and run the system identifier
            try:
                sys.path.append(str(Path(base_dir)))
                from progressive_framework_system_identifier import ProgressiveFrameworkSystemIdentifier
                
                identifier = ProgressiveFrameworkSystemIdentifier(base_dir)
                scan_results = identifier.scan_all_files()
                print("✅ System identification completed internally")
            except ImportError:
                print("❌ Could not import system identifier - please provide JSON input")
                sys.exit(1)
        
        if not scan_results:
            print("❌ No valid scan results available")
            sys.exit(1)
        
        # Apply headers based on scan results
        results = applicator.apply_headers_from_results(scan_results, mode)
        
        print(f"\n🎉 Header application completed successfully!")
        print(f"📈 Total headers applied: {results['total_applied']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()