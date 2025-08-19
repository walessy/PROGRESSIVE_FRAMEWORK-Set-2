#!/usr/bin/env python3
r"""
FILE: progressive_framework_system_identifier.py
WORKING_DIRECTORY: C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025
PURPOSE: Progressive Framework System File Identifier - Intelligently identifies which files are actually part of the Progressive Framework system vs. random files
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: 20250819_Progressive-Framework-Integration
STATUS: ✅ Progressive Framework System File
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | System Integration ✅
PROGRESSIVE_FRAMEWORK: Core System | Confidence: 100 | System Validated ✅

Progressive Framework System File Identifier
Intelligently identifies which files are actually part of the Progressive Framework system
vs. random files that happen to be in the directory
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class ProgressiveFrameworkSystemIdentifier:
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        
        # Core Progressive Framework system indicators
        self.system_indicators = {
            'progressive_keywords': [
                'progressive', 'framework', 'breathing', 'evolutionary',
                'pdt-plus', 'puxt-plus', 'pso-prime', 'pmcs-024', 'paes',
                'atlas', 'prism', 'nexus', 'crud', 'dpi', 'ptodos'
            ],
            'system_file_patterns': [
                r'PROGRESSIVEPROJECT-SYSTEM-\d+',
                r'Chat\d+.*Progressive',
                r'.*breathing.*framework',
                r'.*progressive.*academy',
                r'.*evolutionary.*mapping'
            ],
            'framework_directories': [
                'System_Specs', 'Scripts', 'Templates', 'Automation',
                'Educational_Content', 'Academy', 'Config', 'Lessons'
            ],
            'critical_files': [
                'Progressive Systems Config',
                'Breathing Framework',
                'PKM 5-Point Protocol',
                'Complete 15-System Deployment',
                'Unified Testing Strategy'
            ]
        }
        
        # Reference tracking - files that reference other system files
        self.reference_patterns = [
            r'C:\\Users\\Wales\\OneDrive\\Desktop\\PROGRESSIVE_FRAMEWORK',
            r'System_Specs\\',
            r'Scripts\\',
            r'PROGRESSIVEPROJECT-SYSTEM',
            r'breathing.*framework',
            r'615\+?\s*test',
            r'15\s*system',
            r'Framework Set 2'
        ]
    
    def analyze_file_content(self, file_path: Path) -> Dict[str, any]:
        """Analyze file content to determine system relevance"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(2000)  # Read first 2000 chars for analysis
                
            analysis = {
                'is_system_file': False,
                'confidence_score': 0,
                'indicators_found': [],
                'references_found': [],
                'file_category': 'unknown',
                'should_have_header': False
            }
            
            # Check for Progressive Framework keywords
            keyword_matches = 0
            for keyword in self.system_indicators['progressive_keywords']:
                if keyword.lower() in content.lower():
                    keyword_matches += 1
                    analysis['indicators_found'].append(f"keyword: {keyword}")
            
            # Check for system file patterns
            pattern_matches = 0
            for pattern in self.system_indicators['system_file_patterns']:
                if re.search(pattern, content, re.IGNORECASE):
                    pattern_matches += 1
                    analysis['indicators_found'].append(f"pattern: {pattern}")
            
            # Check for framework references
            reference_matches = 0
            for ref_pattern in self.reference_patterns:
                matches = re.findall(ref_pattern, content, re.IGNORECASE)
                if matches:
                    reference_matches += len(matches)
                    analysis['references_found'].extend(matches)
            
            # Calculate confidence score
            confidence = 0
            confidence += keyword_matches * 10  # Keywords worth 10 points each
            confidence += pattern_matches * 20  # Patterns worth 20 points each
            confidence += reference_matches * 5  # References worth 5 points each
            
            # Boost for critical file names
            for critical_file in self.system_indicators['critical_files']:
                if critical_file.lower() in file_path.name.lower():
                    confidence += 50
                    analysis['indicators_found'].append(f"critical_file: {critical_file}")
            
            # Boost for framework directories
            for framework_dir in self.system_indicators['framework_directories']:
                if framework_dir in str(file_path):
                    confidence += 15
                    analysis['indicators_found'].append(f"framework_dir: {framework_dir}")
            
            analysis['confidence_score'] = confidence
            
            # Determine if it's a system file (confidence threshold: 20)
            if confidence >= 20:
                analysis['is_system_file'] = True
                analysis['should_have_header'] = True
                
                # Categorize system files
                if confidence >= 50:
                    analysis['file_category'] = 'core_system'
                elif confidence >= 35:
                    analysis['file_category'] = 'system_component'
                else:
                    analysis['file_category'] = 'system_related'
            
            return analysis
            
        except Exception as e:
            return {
                'is_system_file': False,
                'confidence_score': 0,
                'indicators_found': [f"error: {str(e)}"],
                'references_found': [],
                'file_category': 'error',
                'should_have_header': False
            }
    
    def has_header(self, file_path: Path) -> bool:
        """Check if file already has a Progressive Framework header"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                first_lines = f.read(800)
                
            header_indicators = [
                'FILE:', 'WORKING_DIRECTORY:', 'PURPOSE:', 
                'CREATOR:', 'UPDATED:', 'STATUS:',
                'BREATHING_FRAMEWORK:', 'PROGRESSIVE'
            ]
            
            found_indicators = sum(1 for indicator in header_indicators if indicator in first_lines)
            return found_indicators >= 4
            
        except Exception:
            return False
    
    def scan_all_files(self) -> Dict[str, List[Dict]]:
        """Scan all files and categorize them"""
        results = {
            'core_system_files': [],
            'system_component_files': [],
            'system_related_files': [],
            'non_system_files': [],
            'files_needing_headers': [],
            'files_already_compliant': []
        }
        
        print("Scanning all files for Progressive Framework system identification...")
        
        total_files = 0
        system_files = 0
        
        for file_path in self.base_dir.rglob('*'):
            if file_path.is_file() and not file_path.name.startswith('.'):
                # Skip backup files from analysis
                if self.is_backup_file(file_path):
                    continue
                    
                total_files += 1
                
                analysis = self.analyze_file_content(file_path)
                has_header = self.has_header(file_path)
                
                file_info = {
                    'path': file_path,
                    'name': file_path.name,
                    'relative_path': file_path.relative_to(self.base_dir),
                    'analysis': analysis,
                    'has_header': has_header,
                    'needs_header': analysis['should_have_header'] and not has_header
                }
                
                # Categorize files
                if analysis['is_system_file']:
                    system_files += 1
                    
                    if analysis['file_category'] == 'core_system':
                        results['core_system_files'].append(file_info)
                    elif analysis['file_category'] == 'system_component':
                        results['system_component_files'].append(file_info)
                    else:
                        results['system_related_files'].append(file_info)
                    
                    if file_info['needs_header']:
                        results['files_needing_headers'].append(file_info)
                    elif has_header:
                        results['files_already_compliant'].append(file_info)
                else:
                    results['non_system_files'].append(file_info)
        
        # Generate summary
        results['summary'] = {
            'total_files_scanned': total_files,
            'system_files_identified': system_files,
            'non_system_files': len(results['non_system_files']),
            'files_needing_headers': len(results['files_needing_headers']),
            'files_already_compliant': len(results['files_already_compliant']),
            'system_file_percentage': (system_files / total_files * 100) if total_files > 0 else 0
        }
        
        return results
    
    def is_backup_file(self, file_path: Path) -> bool:
        """Check if file is a backup file that should be excluded"""
        name = file_path.name.lower()
        return (name.endswith('.backup') or 
                '.backup.' in name or
                name.endswith('.bak') or
                '.bak.' in name)
    
    def generate_report(self, results: Dict) -> str:
        """Generate comprehensive system identification report"""
        report = f"""
# PROGRESSIVE FRAMEWORK SYSTEM FILE IDENTIFICATION REPORT

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Base Directory**: {self.base_dir}

## SCAN SUMMARY

- **Total Files Scanned**: {results['summary']['total_files_scanned']}
- **System Files Identified**: {results['summary']['system_files_identified']}
- **Non-System Files**: {results['summary']['non_system_files']}
- **System File Percentage**: {results['summary']['system_file_percentage']:.1f}%

## HEADER STATUS

- **Files Already Compliant**: {results['summary']['files_already_compliant']}
- **Files Needing Headers**: {results['summary']['files_needing_headers']}
- **Potential Header Compliance**: {((results['summary']['files_already_compliant'] + results['summary']['files_needing_headers']) / results['summary']['total_files_scanned'] * 100):.1f}%

## CORE SYSTEM FILES ({len(results['core_system_files'])})

These are definitely part of the Progressive Framework and MUST have headers:

"""
        
        for file_info in results['core_system_files']:
            status = "HAS HEADER" if file_info['has_header'] else "NEEDS HEADER"
            confidence = file_info['analysis']['confidence_score']
            report += f"- **{file_info['name']}** (Confidence: {confidence}) - {status}\n"
            if file_info['analysis']['indicators_found']:
                report += f"  - Indicators: {', '.join(file_info['analysis']['indicators_found'][:3])}\n"
        
        report += f"""
## SYSTEM COMPONENT FILES ({len(results['system_component_files'])})

These files are system components and should have headers:

"""
        
        for file_info in results['system_component_files']:
            status = "HAS HEADER" if file_info['has_header'] else "NEEDS HEADER"
            confidence = file_info['analysis']['confidence_score']
            report += f"- **{file_info['name']}** (Confidence: {confidence}) - {status}\n"
        
        report += f"""
## RECOMMENDED ACTION PLAN

### Priority 1: Core System Files Needing Headers
"""
        
        core_needing_headers = [f for f in results['core_system_files'] if f['needs_header']]
        for file_info in core_needing_headers:
            report += f"- `{file_info['relative_path']}`\n"
        
        report += f"""
### Priority 2: System Component Files Needing Headers
"""
        
        component_needing_headers = [f for f in results['system_component_files'] if f['needs_header']]
        for file_info in component_needing_headers:
            report += f"- `{file_info['relative_path']}`\n"
        
        report += f"""
## EXECUTION COMMAND

To apply headers to all identified system files:

```bash
# Apply headers to all Progressive Framework system files
python enhanced_automated_header_applicator_phase3.py "{self.base_dir}" system_files_only
```

**Total System Files Needing Headers**: {len(results['files_needing_headers'])}
**Estimated Header Compliance After Application**: {((results['summary']['files_already_compliant'] + results['summary']['files_needing_headers']) / results['summary']['total_files_scanned'] * 100):.1f}%
"""
        
        return report
    
    def export_system_file_list(self, results: Dict, output_file: str = None) -> Path:
        """Export list of system files for header application"""
        if not output_file:
            output_file = "progressive_framework_system_files.txt"
            
        output_path = self.base_dir / output_file
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Progressive Framework System Files Requiring Headers\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for file_info in results['files_needing_headers']:
                f.write(f"{file_info['relative_path']}\n")
        
        return output_path

    def export_json_results(self, results: Dict, output_file: str = None) -> Path:
        """Export complete results to JSON file"""
        import json
        
        if not output_file:
            output_file = "progressive_framework_scan_results.json"
            
        output_path = self.base_dir / output_file
        
        # Convert Path objects to strings for JSON serialization
        json_results = self.prepare_results_for_json(results)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(json_results, f, indent=2, ensure_ascii=False)
        
        return output_path
    
    def prepare_json_for_piping(self, results: Dict) -> str:
        """Prepare results as JSON string for piping"""
        import json
        
        json_results = self.prepare_results_for_json(results)
        return json.dumps(json_results, ensure_ascii=False)
    
    def prepare_results_for_json(self, results: Dict) -> Dict:
        """Convert results to JSON-serializable format"""
        import json
        
        def convert_file_info(file_info):
            """Convert file_info with Path objects to JSON-serializable format"""
            if isinstance(file_info, dict):
                converted = {}
                for key, value in file_info.items():
                    if key == 'path' and hasattr(value, '__fspath__'):
                        converted[key] = str(value)
                    elif key == 'relative_path' and hasattr(value, '__fspath__'):
                        converted[key] = str(value)
                    elif isinstance(value, dict):
                        converted[key] = convert_file_info(value)
                    elif isinstance(value, list):
                        converted[key] = [convert_file_info(item) if isinstance(item, dict) else item for item in value]
                    else:
                        converted[key] = value
                return converted
            return file_info
        
        json_results = {}
        for key, value in results.items():
            if isinstance(value, list):
                json_results[key] = [convert_file_info(item) for item in value]
            elif isinstance(value, dict):
                json_results[key] = convert_file_info(value)
            else:
                json_results[key] = value
        
        return json_results

def main():
    """Main execution function"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python progressive_framework_system_identifier.py <base_directory> [action]")
        print("Actions: scan (default), report, export, export_json, pipe_json")
        print()
        print("Piping Examples:")
        print("  # Export to JSON file")
        print("  python progressive_framework_system_identifier.py dir export_json")
        print("  # Pipe JSON to header applicator")
        print("  python progressive_framework_system_identifier.py dir pipe_json | python piping_compatible_header_applicator.py dir intelligent")
        sys.exit(1)
        
    base_dir = sys.argv[1]
    action = sys.argv[2] if len(sys.argv) > 2 else 'scan'
    
    if action != 'pipe_json':  # Don't print headers for pipe_json to keep output clean
        print("Progressive Framework System File Identifier", file=sys.stderr)
        print(f"Base Directory: {base_dir}", file=sys.stderr)
        print(f"Action: {action}", file=sys.stderr)
        print("=" * 70, file=sys.stderr)
    
    identifier = ProgressiveFrameworkSystemIdentifier(base_dir)
    
    if action in ['scan', 'report', 'export', 'export_json', 'pipe_json']:
        results = identifier.scan_all_files()
        
        if action != 'pipe_json':
            print(f"\nSCAN COMPLETE", file=sys.stderr)
            print(f"Total Files: {results['summary']['total_files_scanned']}", file=sys.stderr)
            print(f"System Files: {results['summary']['system_files_identified']}", file=sys.stderr)
            print(f"Files Needing Headers: {results['summary']['files_needing_headers']}", file=sys.stderr)
        
        if action == 'report':
            report = identifier.generate_report(results)
            print(report)
            
            # Save report to file
            report_file = identifier.base_dir / "system_identification_report.md"
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\nReport saved to: {report_file}")
        
        elif action == 'export':
            output_file = identifier.export_system_file_list(results)
            print(f"\nSystem file list exported to: {output_file}")
            
        elif action == 'export_json':
            # Export results to JSON file
            json_file = identifier.export_json_results(results)
            print(f"\nJSON results exported to: {json_file}", file=sys.stderr)
            
        elif action == 'pipe_json':
            # Output JSON to stdout for piping (no other output)
            json_output = identifier.prepare_json_for_piping(results)
            print(json_output)  # This goes to stdout for piping
    
    else:
        print(f"❌ Unknown action: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()
