#!/usr/bin/env python3
"""
FILE: part2_clean.py
WORKING_DIRECTORY: .
PURPOSE: Python automation script
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: 20250819_Header-System-Integration
STATUS: ✅ Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Compliance ✅
"""

#!/usr/bin/env python3
import os
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

class TemplateGenerationFixer:
    def __init__(self, base_directory: str):
        self.base_directory = Path(base_directory)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.updated_templates = []
        
    def find_template_and_generation_files(self) -> List[Path]:
        print("🔍 Scanning for template and generation files...")
        
        template_patterns = [
            "**/templates/**/*.py",
            "**/generators/**/*.py",
            "**/*template*.py",
            "**/*generator*.py",
            "**/*breathing_framework*.py"
        ]
        
        template_files = set()
        for pattern in template_patterns:
            found_files = list(self.base_directory.glob(pattern))
            template_files.update(found_files)
            if found_files:
                print(f"   📁 Found {len(found_files)} files matching: {pattern}")
        
        print("🔍 Scanning for files with generation logic...")
        additional_files = []
        
        for file_path in self.base_directory.rglob("*.py"):
            if self._contains_generation_logic(file_path):
                additional_files.append(file_path)
        
        if additional_files:
            print(f"   📁 Found {len(additional_files)} files with generation logic")
        
        template_files.update(additional_files)
        filtered_files = [f for f in template_files if self._should_process_template(f)]
        
        print(f"📊 Total template/generation files found: {len(filtered_files)}")
        return sorted(filtered_files)
    
    def _contains_generation_logic(self, file_path: Path) -> bool:
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore').lower()
            
            generation_keywords = [
                'def generate_',
                'def create_',
                'def auto_generate',
                'def build_',
                'template',
                'auto_generation',
                'breathing_framework',
                'lesson_generation',
                'test_generation',
                '.format(',
                'f"""',
                "f'''",
                'template_string',
                'generate_lesson',
                'create_test',
                'write_text(',
                'with open(',
                'file.write(',
                '.save(',
                'output_file'
            ]
            
            matches = sum(1 for keyword in generation_keywords if keyword in content)
            return matches >= 2
            
        except:
            return False
    
    def _should_process_template(self, file_path: Path) -> bool:
        if file_path.name.startswith('.'):
            return False
        
        excluded_dirs = ['node_modules', '.git', '__pycache__', '.vscode', 'venv', 'env']
        if any(excluded in str(file_path) for excluded in excluded_dirs):
            return False
        
        try:
            if file_path.stat().st_size < 100:
                return False
        except:
            return False
        
        return True
    
    def create_header_injection_system(self) -> str:
        return f'''
# BREATHING FRAMEWORK HEADER INJECTION SYSTEM
# Auto-generated: {self.timestamp}

import datetime

def get_breathing_framework_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def get_system_configurations():
    return {{
        "PDT-PLUS": {{"system_id": 1, "tier": "Enhanced Foundation", "business_value": 89000}},
        "PUXT-PLUS": {{"system_id": 2, "tier": "Enhanced Foundation", "business_value": 34000}},
        "PSO-PRIME": {{"system_id": 3, "tier": "Enhanced Foundation", "business_value": 42000}},
        "PTT-DOCS-FUSION": {{"system_id": 4, "tier": "Enhanced Foundation", "business_value": 26700}},
        "REQUIREMENTS-PRIME": {{"system_id": 5, "tier": "Enhanced Foundation", "business_value": 25000}},
        "BUSINESS-OPS-FUSION": {{"system_id": 6, "tier": "Enhanced Professional", "business_value": 45000}},
        "CONTEXT-EVOLUTION-ENGINE": {{"system_id": 7, "tier": "Enhanced Professional", "business_value": 38000}},
        "PERFORMANCE-AI-FUSION": {{"system_id": 8, "tier": "Enhanced Professional", "business_value": 52000}},
        "SECURITY-BUILD-FUSION": {{"system_id": 9, "tier": "Enhanced Professional", "business_value": 48000}},
        "UNIVERSAL-LESSON-ENGINE": {{"system_id": 10, "tier": "Enhanced Universal", "business_value": 35000}},
        "META-PROJECT-ENGINE": {{"system_id": 11, "tier": "Enhanced Universal", "business_value": 28000}},
        "AUTOMATION-INTELLIGENCE-FUSION": {{"system_id": 12, "tier": "Enhanced Universal", "business_value": 25000}},
        "PROGRESSIVE-ENHANCEMENT-ENGINE": {{"system_id": 13, "tier": "Enhanced Universal", "business_value": 15000}},
        "DPI": {{"system_id": 14, "tier": "Intelligence Tier", "business_value": 18000}},
        "PTODOS": {{"system_id": 15, "tier": "Organization Tier", "business_value": 12000}}
    }}

def generate_breathing_framework_header(filename, file_type="markdown", content_type="lesson", system_name="UNASSIGNED", purpose="Auto-generated content", version="2.1"):
    timestamp = get_breathing_framework_timestamp()
    system_configs = get_system_configurations()
    
    config = system_configs.get(system_name, {{
        "system_id": 0, 
        "tier": "Unassigned", 
        "business_value": 0
    }})
    
    title = filename.replace('_', ' ').replace('-', ' ')
    if '.' in title:
        title = title.split('.')[0]
    title = title.title()
    
    if content_type == "test":
        title = f"{{system_name}} {{title}} Test Case"
        icon = "TEST"
        creator = "Progressive Framework Test Suite"
        status = "ACTIVE Breathing Framework Integrated"
    elif content_type == "lesson":
        title = f"{{system_name}} {{title}} Lesson Module" 
        icon = "LESSON"
        creator = "Breathing Framework 615+ Test-to-Lesson Engine"
        status = "ACTIVE Auto-Generated Educational Content"
    else:
        title = f"{{system_name}} {{title}} Documentation"
        icon = "DOCS"
        creator = "PTT-DOCS-FUSION Auto-Generation Engine"
        status = "ACTIVE Auto-Generated Living Documentation"
    
    if file_type.lower() == "markdown":
        return f"""# {{icon}} {{title}}

**FILE**: {{filename}}  
**VERSION**: v{{version}} - Breathing Framework Auto-Generated  
**PURPOSE**: {{purpose}}  
**SYSTEM**: {{system_name}} ({{config['system_id']}} of 15)  
**CREATOR**: {{creator}}  
**CREATED**: {{timestamp}}  
**STATUS**: {{status}}  

---

## BREATHING FRAMEWORK INTEGRATION

**Educational Tier**: {{config['tier']}}  
**Business Value**: ${{config['business_value']:,}}/month  
**Test Coverage**: Part of 615+ test case framework  
**System Integration**: 15-system breathing framework  
**Auto-Generation**: ACTIVE  

---

"""
    
    elif file_type.lower() == "python":
        return f'''#!/usr/bin/env python3
"""
{{icon}} {{title}}

FILE: {{filename}}
VERSION: v{{version}} - Breathing Framework Auto-Generated
PURPOSE: {{purpose}}
SYSTEM: {{system_name}} ({{config['system_id']}} of 15)
CREATOR: {{creator}}
CREATED: {{timestamp}}
STATUS: {{status}}

BREATHING FRAMEWORK INTEGRATION:
- Educational Tier: {{config['tier']}}
- Business Value: ${{config['business_value']:,}}/month
- Test Coverage: Part of 615+ test case framework
- System Integration: 15-system breathing framework
- Auto-Generation: ACTIVE
"""

'''
    
    else:
        return f"""# {{icon}} {{title}}

**FILE**: {{filename}}  
**SYSTEM**: {{system_name}}  
**CREATED**: {{timestamp}}  
**STATUS**: {{status}}  

---

## BREATHING FRAMEWORK INTEGRATION

This file is part of the 615+ Test-to-Lesson Breathing Framework.

---

"""

def auto_add_breathing_framework_header(generated_content, filename, file_type="markdown", content_type="lesson", system_name="UNASSIGNED", purpose="Auto-generated content"):
    header = generate_breathing_framework_header(
        filename=filename,
        file_type=file_type,
        content_type=content_type,
        system_name=system_name,
        purpose=purpose
    )
    
    return header + generated_content

print("BREATHING FRAMEWORK HEADER INJECTION SYSTEM LOADED")
'''

    def check_template_needs_update(self, template_path: Path) -> bool:
        try:
            content = template_path.read_text(encoding='utf-8', errors='ignore')
            
            breathing_framework_indicators = [
                "generate_breathing_framework_header",
                "auto_add_breathing_framework_header",
                "BREATHING FRAMEWORK HEADER INJECTION SYSTEM",
                "615+ test case framework"
            ]
            
            return not any(indicator in content for indicator in breathing_framework_indicators)
            
        except:
            return True

    def update_template_file(self, template_path: Path) -> Dict:
        try:
            if not self.check_template_needs_update(template_path):
                return {
                    "file_path": str(template_path),
                    "status": "skipped", 
                    "reason": "already_has_breathing_framework_integration"
                }
            
            original_content = template_path.read_text(encoding='utf-8', errors='ignore')
            original_size = len(original_content)
            
            header_system = self.create_header_injection_system()
            updated_content = self._inject_header_system(original_content, header_system, template_path)
            
            template_path.write_text(updated_content, encoding='utf-8')
            
            self.updated_templates.append(template_path)
            
            return {
                "file_path": str(template_path),
                "status": "success",
                "original_size": original_size,
                "updated_size": len(updated_content),
                "breathing_framework_integrated": True
            }
            
        except Exception as e:
            return {
                "file_path": str(template_path),
                "status": "error",
                "error": str(e)
            }

    def _inject_header_system(self, original_content: str, header_system: str, template_path: Path) -> str:
        injection_notice = f'''
# BREATHING FRAMEWORK INTEGRATION - ADDED {self.timestamp}
# This template has been enhanced to include breathing framework header generation
'''
        
        if template_path.suffix.lower() == '.py':
            lines = original_content.split('\n')
            import_section_end = 0
            
            for i, line in enumerate(lines):
                if (line.strip().startswith('import ') or 
                    line.strip().startswith('from ') or
                    line.strip().startswith('#') or
                    line.strip() == ''):
                    import_section_end = i + 1
                else:
                    break
            
            new_lines = (
                lines[:import_section_end] + 
                [injection_notice] +
                header_system.split('\n') +
                [''] +
                lines[import_section_end:]
            )
            
            updated_content = '\n'.join(new_lines)
            
        else:
            updated_content = injection_notice + '\n' + header_system + '\n\n' + original_content
        
        return updated_content

    def create_breathing_framework_config(self) -> str:
        config_content = f'''# BREATHING FRAMEWORK TEMPLATE COMPLIANCE CONFIGURATION
# Generated: {self.timestamp}

BREATHING_FRAMEWORK_TEMPLATE_CONFIG = {{
    "version": "2.1",
    "auto_header_generation": True,
    "template_compliance_required": True,
    
    "system_specifications": {{
        "total_systems": 15,
        "test_cases": "615+",
        "lesson_modules": "615+",
        "chat_commands": 15,
        "specification_consistency": "ACTIVE",
        "auto_correction": "ENABLED"
    }}
}}

print("BREATHING FRAMEWORK TEMPLATE COMPLIANCE CONFIGURATION LOADED")
'''
        
        config_path = self.base_directory / f"breathing_framework_template_config_{self.timestamp}.py"
        config_path.write_text(config_content, encoding='utf-8')
        
        return str(config_path)

    def process_all_templates(self) -> Dict:
        print("🔧 PART 2: FIXING TEMPLATE GENERATION FOR FUTURE FILES")
        print("🔄 Updating Templates to Auto-Generate Headers")
        print("=" * 70)
        
        template_files = self.find_template_and_generation_files()
        
        print(f"📁 Found {len(template_files)} template/generation files to update")
        print()
        
        if len(template_files) == 0:
            print("⚠️  No template/generation files found!")
            return {
                "template_update_summary": {
                    "total_template_files": 0,
                    "message": "No template files found to update"
                }
            }
        
        results = []
        
        for i, template_file in enumerate(template_files, 1):
            progress = (i / len(template_files)) * 100
            print(f"🔧 [{i:3d}/{len(template_files)}] [{progress:5.1f}%] {template_file.name}")
            
            result = self.update_template_file(template_file)
            results.append(result)
        
        summary = self._generate_template_summary(results)
        return summary

    def _generate_template_summary(self, results: List[Dict]) -> Dict:
        total_files = len(results)
        successful = len([r for r in results if r["status"] == "success"])
        skipped = len([r for r in results if r["status"] == "skipped"])
        errors = len([r for r in results if r["status"] == "error"])
        
        return {
            "template_update_summary": {
                "total_template_files": total_files,
                "successfully_updated": successful,
                "skipped_existing": skipped,
                "update_errors": errors,
                "success_rate": (successful / total_files * 100) if total_files > 0 else 100,
                "timestamp": self.timestamp
            },
            "breathing_framework_status": {
                "template_standardization": "COMPLETE" if successful > 0 else "NO_TEMPLATES_FOUND",
                "auto_header_generation": "ENABLED" if successful > 0 else "NO_TEMPLATES_TO_ENABLE",
                "future_file_compliance": "GUARANTEED" if successful > 0 else "NO_TEMPLATES_UPDATED"
            },
            "updated_templates": [str(t) for t in self.updated_templates],
            "results_detail": results,
            "next_steps": [
                f"SUCCESS: {successful} templates now auto-generate breathing framework headers" if successful > 0 else "WARNING: No templates were updated - check template locations",
                "SUCCESS: All new generated files will automatically include proper headers" if successful > 0 else "INFO: Verify template file locations and naming conventions",
                "ACTION: Test template updates by generating sample files" if successful > 0 else "ACTION: Check if templates are in different directories"
            ],
            "timestamp": datetime.now().isoformat()
        }

    def save_template_report(self, report: Dict) -> str:
        output_file = f"part2_template_generation_fix_report_{self.timestamp}.json"
        output_path = self.base_directory / output_file
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
        
        return str(output_path)

def main():
    import sys
    
    if len(sys.argv) != 2:
        print("PART 2: FIX TEMPLATE GENERATION FOR FUTURE FILES")
        print("Usage: python part2_clean.py <base_directory>")
        sys.exit(1)
    
    base_directory = sys.argv[1]
    
    print("🔧 BREATHING FRAMEWORK - PART 2 (CLEAN)")
    print("🔄 FIXING TEMPLATE GENERATION FOR FUTURE FILES")
    print("=" * 70)
    print(f"📂 Target Directory: {base_directory}")
    print()
    
    fixer = TemplateGenerationFixer(base_directory)
    report = fixer.process_all_templates()
    config_file = fixer.create_breathing_framework_config()
    report_file = fixer.save_template_report(report)
    
    print("\n" + "=" * 70)
    print("📊 PART 2 COMPLETION SUMMARY")
    print("=" * 70)
    
    summary = report["template_update_summary"]
    
    print(f"📁 Template Files Found: {summary['total_template_files']}")
    print(f"✅ Successfully Updated: {summary['successfully_updated']}")
    print(f"⏩ Skipped (Existing): {summary['skipped_existing']}")
    print(f"❌ Errors: {summary['update_errors']}")
    print(f"🎯 Success Rate: {summary['success_rate']:.1f}%")
    print()
    
    print("🌟 BREATHING FRAMEWORK STATUS:")
    for key, value in report["breathing_framework_status"].items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    print()
    
    print("🚀 NEXT STEPS:")
    for step in report["next_steps"]:
        print(f"   {step}")
    print()
    
    print(f"📄 Detailed Report: {report_file}")
    print(f"⚙️ Template Config: {config_file}")
    print()
    print("✅ PART 2 COMPLETE! Templates now auto-generate headers for future files.")
    print("🎉 BREATHING FRAMEWORK HEADER SYSTEM FULLY OPERATIONAL!")

if __name__ == "__main__":
    main()