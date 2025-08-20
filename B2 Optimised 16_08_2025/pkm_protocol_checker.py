#!/usr/bin/env python3
"""
PKM 5-Point Protocol Configuration Checker
Analyzes PKM configuration and validates setup for auto-activation
"""

import os
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

class PKMProtocolChecker:
    def __init__(self, base_directory: str):
        self.base_directory = Path(base_directory)
        self.system_specs_dir = self.base_directory / "System_Specs"
        self.analysis_results = {}
        
    def check_pkm_xml_configuration(self) -> Dict:
        """Check PKM XML protocol configuration"""
        pkm_xml_path = self.system_specs_dir / "PKM-5Point-Protocol-v5.0.xml"
        
        config_status = {
            "file_exists": pkm_xml_path.exists(),
            "file_path": str(pkm_xml_path),
            "file_size": 0,
            "auto_activate": None,
            "version": None,
            "breathing_framework": None,
            "framework_reference": None,
            "working_directory_handling": None,
            "system_integration": None,
            "valid_xml": False,
            "configuration_issues": []
        }
        
        if not pkm_xml_path.exists():
            config_status["configuration_issues"].append("PKM XML file not found")
            return config_status
            
        try:
            config_status["file_size"] = pkm_xml_path.stat().st_size
            
            # Read and parse XML
            with open(pkm_xml_path, 'r', encoding='utf-8') as f:
                xml_content = f.read()
                
            # Check for key configuration elements
            if 'auto_activate="true"' in xml_content:
                config_status["auto_activate"] = True
            elif 'auto_activate="false"' in xml_content:
                config_status["auto_activate"] = False
            else:
                config_status["configuration_issues"].append("auto_activate attribute not found")
                
            if 'breathing_framework' in xml_content.lower():
                config_status["breathing_framework"] = True
            else:
                config_status["configuration_issues"].append("breathing_framework reference not found")
                
            if 'ProgressiveProject' in xml_content or 'Progressive Framework' in xml_content:
                config_status["framework_reference"] = True
            else:
                config_status["configuration_issues"].append("Progressive Framework reference not found")
                
            if 'Working Directory' in xml_content or 'working_directory' in xml_content:
                config_status["working_directory_handling"] = True
            else:
                config_status["configuration_issues"].append("Working directory handling not found")
                
            # Try to parse as XML
            try:
                root = ET.fromstring(xml_content)
                config_status["valid_xml"] = True
                config_status["version"] = root.get("version", "Unknown")
            except ET.ParseError as e:
                config_status["configuration_issues"].append(f"XML parsing error: {e}")
                
        except Exception as e:
            config_status["configuration_issues"].append(f"Error reading XML: {e}")
            
        return config_status
    
    def check_progressive_systems_config(self) -> Dict:
        """Check Progressive Systems Configuration JSON"""
        json_path = self.system_specs_dir / "Progressive-Systems-Config-v2.3-SignalBased.json"
        
        json_status = {
            "file_exists": json_path.exists(),
            "file_path": str(json_path),
            "file_size": 0,
            "valid_json": False,
            "systems_count": 0,
            "signal_based": None,
            "breathing_framework": None,
            "educational_integration": None,
            "system_file_references": [],
            "configuration_issues": []
        }
        
        if not json_path.exists():
            json_status["configuration_issues"].append("Progressive Systems Config JSON not found")
            return json_status
            
        try:
            json_status["file_size"] = json_path.stat().st_size
            
            with open(json_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                json_status["valid_json"] = True
                
                # Check for signal-based architecture
                if 'signal' in str(config_data).lower():
                    json_status["signal_based"] = True
                    
                # Check for breathing framework
                if 'breathing' in str(config_data).lower():
                    json_status["breathing_framework"] = True
                    
                # Check for educational integration
                if 'education' in str(config_data).lower() or 'lesson' in str(config_data).lower():
                    json_status["educational_integration"] = True
                    
                # Count systems
                systems_found = 0
                for key, value in config_data.items():
                    if 'system' in key.lower() and isinstance(value, dict):
                        if 'systems' in value:
                            systems_found += len(value['systems'])
                            
                json_status["systems_count"] = systems_found
                
        except json.JSONDecodeError as e:
            json_status["configuration_issues"].append(f"JSON parsing error: {e}")
        except Exception as e:
            json_status["configuration_issues"].append(f"Error reading JSON: {e}")
            
        return json_status
    
    def check_system_specification_files(self) -> Dict:
        """Check all 15 system specification files"""
        expected_systems = {
            1: "PDT-PLUS",
            2: "PUXT-PLUS", 
            3: "PSO-PRIME",
            4: "PTT-DOCS-FUSION",
            5: "REQUIREMENTS-PRIME",
            6: "BUSINESS-OPS-FUSION",
            7: "CONTEXT-EVOLUTION-ENGINE",
            8: "PERFORMANCE-AI-FUSION",
            9: "SECURITY-BUILD-FUSION",
            10: "KNOWLEDGE-EVOLUTION-ENGINE",
            11: "UNIVERSAL-ORCHESTRATION-PRIME",
            12: "PMCS-024",
            13: "PAES",
            14: "DPI",
            15: "PTODOS"
        }
        
        system_status = {
            "total_expected": 15,
            "total_found": 0,
            "missing_systems": [],
            "found_systems": [],
            "naming_issues": [],
            "breathing_framework_integration": 0
        }
        
        for system_id, system_name in expected_systems.items():
            expected_filename = f"PROGRESSIVEPROJECT-SYSTEM-{system_id:02d}-{system_name}.md"
            file_path = self.system_specs_dir / expected_filename
            
            if file_path.exists():
                system_status["total_found"] += 1
                file_info = {
                    "system_id": system_id,
                    "system_name": system_name,
                    "filename": expected_filename,
                    "size": file_path.stat().st_size,
                    "breathing_framework": False
                }
                
                # Check for breathing framework integration
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'breathing framework' in content.lower() or 'educational' in content.lower():
                            file_info["breathing_framework"] = True
                            system_status["breathing_framework_integration"] += 1
                except:
                    pass
                    
                system_status["found_systems"].append(file_info)
            else:
                system_status["missing_systems"].append({
                    "system_id": system_id,
                    "system_name": system_name,
                    "expected_filename": expected_filename
                })
                
        return system_status
    
    def check_breathing_framework_lessons(self) -> Dict:
        """Check breathing framework lesson generation"""
        lessons_dir = self.base_directory / "Lessons" / "Active"
        
        lessons_status = {
            "lessons_directory_exists": lessons_dir.exists(),
            "total_lesson_folders": 0,
            "total_lessons": 0,
            "systems_with_lessons": [],
            "lessons_by_system": {}
        }
        
        if lessons_dir.exists():
            for system_folder in lessons_dir.iterdir():
                if system_folder.is_dir():
                    lessons_status["total_lesson_folders"] += 1
                    system_name = system_folder.name
                    
                    lesson_files = list(system_folder.glob("*.md"))
                    lesson_count = len(lesson_files)
                    lessons_status["total_lessons"] += lesson_count
                    
                    if lesson_count > 0:
                        lessons_status["systems_with_lessons"].append(system_name)
                        lessons_status["lessons_by_system"][system_name] = {
                            "lesson_count": lesson_count,
                            "latest_lesson": max(lesson_files, key=lambda x: x.stat().st_mtime).name if lesson_files else None
                        }
                        
        return lessons_status
    
    def generate_comprehensive_analysis(self) -> str:
        """Generate comprehensive PKM protocol analysis"""
        print("🔍 Analyzing PKM 5-Point Protocol Configuration...")
        
        # Run all checks
        pkm_config = self.check_pkm_xml_configuration()
        json_config = self.check_progressive_systems_config()
        system_files = self.check_system_specification_files()
        lessons_status = self.check_breathing_framework_lessons()
        
        # Calculate overall status
        total_issues = len(pkm_config.get("configuration_issues", [])) + len(json_config.get("configuration_issues", []))
        pkm_ready = (pkm_config.get("auto_activate") and 
                    json_config.get("valid_json") and 
                    system_files.get("total_found", 0) == 15)
        
        report = f"""
# 🔍 PKM 5-POINT PROTOCOL ANALYSIS REPORT

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Base Directory**: {self.base_directory}
**Analysis Status**: {'✅ READY' if pkm_ready else '⚠️ ISSUES FOUND'}

## 📋 PKM XML PROTOCOL STATUS

**File**: {pkm_config['file_path']}
**Exists**: {'✅ YES' if pkm_config['file_exists'] else '❌ NO'}
**Size**: {pkm_config['file_size']} bytes
**Valid XML**: {'✅ YES' if pkm_config['valid_xml'] else '❌ NO'}
**Auto-Activate**: {'✅ ENABLED' if pkm_config['auto_activate'] else '❌ DISABLED' if pkm_config['auto_activate'] is False else '⚠️ NOT SET'}
**Breathing Framework**: {'✅ INTEGRATED' if pkm_config['breathing_framework'] else '❌ NOT FOUND'}
**Working Directory**: {'✅ CONFIGURED' if pkm_config['working_directory_handling'] else '❌ NOT CONFIGURED'}

### Configuration Issues:
"""
        
        if pkm_config['configuration_issues']:
            for issue in pkm_config['configuration_issues']:
                report += f"- ❌ {issue}\n"
        else:
            report += "- ✅ No configuration issues found\n"
        
        report += f"""

## ⚙️ PROGRESSIVE SYSTEMS CONFIG STATUS

**File**: {json_config['file_path']}
**Exists**: {'✅ YES' if json_config['file_exists'] else '❌ NO'}
**Size**: {json_config['file_size']} bytes
**Valid JSON**: {'✅ YES' if json_config['valid_json'] else '❌ NO'}
**Systems Found**: {json_config['systems_count']}/15
**Signal-Based**: {'✅ ENABLED' if json_config['signal_based'] else '❌ NOT FOUND'}
**Breathing Framework**: {'✅ INTEGRATED' if json_config['breathing_framework'] else '❌ NOT FOUND'}
**Educational Integration**: {'✅ ACTIVE' if json_config['educational_integration'] else '❌ NOT FOUND'}

### JSON Configuration Issues:
"""
        
        if json_config['configuration_issues']:
            for issue in json_config['configuration_issues']:
                report += f"- ❌ {issue}\n"
        else:
            report += "- ✅ No JSON configuration issues found\n"
        
        report += f"""

## 📁 SYSTEM SPECIFICATION FILES STATUS

**Expected Systems**: {system_files['total_expected']}
**Found Systems**: {system_files['total_found']}
**Breathing Framework Integration**: {system_files['breathing_framework_integration']}/15 systems
**Completion Rate**: {(system_files['total_found']/system_files['total_expected']*100):.1f}%

### Found Systems:
"""
        
        for system in system_files['found_systems']:
            bf_status = '✅ BF' if system['breathing_framework'] else '❌ No BF'
            report += f"- ✅ System {system['system_id']:02d}: {system['system_name']} ({system['size']} bytes) {bf_status}\n"
        
        if system_files['missing_systems']:
            report += "\n### Missing Systems:\n"
            for system in system_files['missing_systems']:
                report += f"- ❌ System {system['system_id']:02d}: {system['system_name']} ({system['expected_filename']})\n"
        
        report += f"""

## 📚 BREATHING FRAMEWORK LESSONS STATUS

**Lessons Directory**: {'✅ EXISTS' if lessons_status['lessons_directory_exists'] else '❌ NOT FOUND'}
**System Folders**: {lessons_status['total_lesson_folders']}
**Total Lessons**: {lessons_status['total_lessons']}
**Systems with Lessons**: {len(lessons_status['systems_with_lessons'])}/15

### Lessons by System:
"""
        
        for system_name, info in lessons_status['lessons_by_system'].items():
            report += f"- ✅ {system_name}: {info['lesson_count']} lessons (Latest: {info['latest_lesson']})\n"
        
        report += f"""

## 🎯 PKM 5-POINT PROTOCOL READINESS

### Overall Status: {'✅ READY FOR AUTO-ACTIVATION' if pkm_ready else '⚠️ CONFIGURATION ISSUES FOUND'}

### Readiness Checklist:
- PKM XML Auto-Activate: {'✅' if pkm_config.get('auto_activate') else '❌'}
- Progressive Systems Config: {'✅' if json_config.get('valid_json') else '❌'}
- All 15 Systems Present: {'✅' if system_files.get('total_found') == 15 else '❌'}
- Breathing Framework: {'✅' if pkm_config.get('breathing_framework') and json_config.get('breathing_framework') else '❌'}
- Educational Lessons: {'✅' if lessons_status.get('total_lessons', 0) > 0 else '❌'}

### Configuration Issues Found: {total_issues}

## 🚀 RECOMMENDED ACTIONS

"""
        
        if pkm_ready:
            report += """
✅ **PKM Protocol is READY!**
- Start a new chat with your working directory specification
- PKM should auto-activate and load all 15 systems
- Breathing framework should provide educational content generation
- All systems should be accessible through project knowledge

**Test Command**: 
```
Working Directory: C:\\Users\\Wales\\OneDrive\\Desktop\\PROGRESSIVE_FRAMEWORK-Set-2\\B2 Optimised 16_08_2025\\
Chat003 - PKM Protocol Test
Primary Objectives: Test PKM auto-activation
20250820_PKM_Test
```
"""
        else:
            report += """
⚠️ **Configuration Issues Need Resolution**

**Priority Fixes:**
"""
            if not pkm_config.get('auto_activate'):
                report += "1. Enable auto_activate in PKM XML protocol\n"
            if not json_config.get('valid_json'):
                report += "2. Fix Progressive Systems Config JSON syntax\n"
            if system_files.get('total_found', 0) < 15:
                report += f"3. Add missing {15 - system_files.get('total_found', 0)} system specification files\n"
            if total_issues > 0:
                report += "4. Resolve configuration issues listed above\n"
        
        return report
    
    def run_complete_analysis(self):
        """Run complete PKM protocol analysis"""
        report = self.generate_comprehensive_analysis()
        
        # Save report
        report_path = self.base_directory / "PKM-Protocol-Analysis-Report.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📋 PKM Analysis Complete!")
        print(f"📄 Report saved: {report_path}")
        print(f"\n{report}")

# Usage Example
if __name__ == "__main__":
    # Replace with your actual working directory
    working_dir = r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025"
    
    checker = PKMProtocolChecker(working_dir)
    checker.run_complete_analysis()
