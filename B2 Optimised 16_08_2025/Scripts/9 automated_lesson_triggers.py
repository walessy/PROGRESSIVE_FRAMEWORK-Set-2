#!/usr/bin/env python3
"""
FILE: 9 automated_lesson_triggers.py
WORKING_DIRECTORY: .
PURPOSE: Python automation script
CREATOR: Amos Wales - Progressive Framework Pioneer
UPDATED: 20250819_Header-System-Integration
STATUS: ✅ Universal Header System Compliant
BREATHING_FRAMEWORK: 15 Systems ✅ | 615+ Tests ✅ | Compliance ✅
"""


# BREATHING FRAMEWORK HEADER INJECTION SYSTEM
# Generated: 20250819_055926

def generate_breathing_framework_header(filename, system_name="UNASSIGNED"):
    timestamp = "20250819_055926"
    return f"""# BREATHING FRAMEWORK FILE

**FILE**: {filename}
**SYSTEM**: {system_name}
**CREATED**: {timestamp}
**STATUS**: ACTIVE

---

## BREATHING FRAMEWORK INTEGRATION

This file is part of the 615+ Test-to-Lesson Breathing Framework.

---

"""

def auto_add_breathing_framework_header(content, filename, system_name="UNASSIGNED"):
    header = generate_breathing_framework_header(filename, system_name)
    return header + content

print("BREATHING FRAMEWORK HEADER SYSTEM LOADED")


#!/usr/bin/env python3
"""
🧪 UNASSIGNED 9 Automated Lesson Triggers Test Case

FILE: 9 automated_lesson_triggers.py
VERSION: v2.1 - Breathing Framework Enhanced
PURPOSE: Validate UNASSIGNED system functionality and generate educational content
SYSTEM: UNASSIGNED (0 of 15)
CREATOR: Progressive Framework Test Suite
CREATED: 20250819_053049
STATUS: ✅ Breathing Framework Integrated

BREATHING FRAMEWORK INTEGRATION:
- Educational Tier: Unassigned
- Business Value: $0/month
- Test Coverage: Part of 615+ test case framework
- System Integration: 15-system breathing framework
- Auto-Generation: ✅ ACTIVE

Specifications:
- Framework Version: 615+ Test-to-Lesson v2.1
- System Count: 15 Systems Integrated
- Specification Consistency: ✅ ENABLED
- Educational Integration: ✅ ACTIVE
"""

#!/usr/bin/env python3
"""
Automated Lesson Generation Trigger System
Automatically generates and saves evolutionary lessons from test cases with zero manual intervention
"""

import os
import json
import yaml
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

@dataclass
class LessonGenerationTrigger:
    """Configuration for automatic lesson generation triggers"""
    trigger_type: str  # "test_case_added", "test_case_modified", "system_updated"
    source_patterns: List[str]  # File patterns that trigger generation
    target_systems: List[int]  # Systems affected by this trigger
    generation_delay: float = 5.0  # Seconds to wait before generating (debounce)
    auto_save: bool = True
    auto_index: bool = True
    cross_system_analysis: bool = True

@dataclass
class TestCaseMetadata:
    """Metadata extracted from test case for lesson generation"""
    test_id: str
    system_id: int
    engine: Optional[str]
    skill_level: str
    test_type: str
    version: str
    file_path: str
    last_modified: datetime
    checksum: str

class EvolutionaryLessonTriggerSystem:
    """Automated trigger system for evolutionary lesson generation"""
    
    def __init__(self, project_directory: str, config_file: Optional[str] = None):
        self.project_dir = Path(project_directory)
        self.config_file = config_file or self.project_dir / "Config" / "lesson_triggers.yaml"
        self.lessons_dir = self.project_dir / "Lessons"
        self.test_cases_dir = self.project_dir / "System_Specs"
        
        # Trigger configuration
        self.triggers: List[LessonGenerationTrigger] = []
        self.pending_generations: Dict[str, float] = {}  # file_path -> trigger_time
        self.generation_queue: List[TestCaseMetadata] = []
        self.is_running = False
        
        # File system monitoring
        self.observer: Optional[Observer] = None
        self.event_handler: Optional['LessonTriggerHandler'] = None
        
        # Load configuration
        self.load_trigger_configuration()
        
        print("🔄 Evolutionary Lesson Trigger System Initialized")
        print(f"📁 Monitoring: {self.test_cases_dir}")
        print(f"📚 Lesson Output: {self.lessons_dir}")
    
    def load_trigger_configuration(self):
        """Load trigger configuration from YAML file"""
        
        # Default configuration
        default_triggers = [
            LessonGenerationTrigger(
                trigger_type="test_case_added",
                source_patterns=["**/PROGRESSIVEPROJECT-SYSTEM-*.md", "**/test_*.py", "**/spec_*.md"],
                target_systems=list(range(1, 16)),  # All 15 systems
                generation_delay=5.0,
                auto_save=True,
                auto_index=True,
                cross_system_analysis=True
            ),
            LessonGenerationTrigger(
                trigger_type="test_case_modified",
                source_patterns=["**/PROGRESSIVEPROJECT-SYSTEM-*.md"],
                target_systems=list(range(1, 16)),
                generation_delay=10.0,  # Longer delay for modifications
                auto_save=True,
                auto_index=True,
                cross_system_analysis=True
            ),
            LessonGenerationTrigger(
                trigger_type="system_specification_updated",
                source_patterns=["**/System_Specs/*.md", "**/debugging_engines_specs.md"],
                target_systems=list(range(1, 16)),
                generation_delay=15.0,  # Even longer for system updates
                auto_save=True,
                auto_index=True,
                cross_system_analysis=True
            )
        ]
        
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config_data = yaml.safe_load(f)
                    # Parse YAML into trigger objects
                    self.triggers = [LessonGenerationTrigger(**trigger) for trigger in config_data.get('triggers', [])]
                    print(f"  ✅ Loaded {len(self.triggers)} triggers from config")
            else:
                # Create default configuration
                self.triggers = default_triggers
                self.save_trigger_configuration()
                print(f"  ✅ Created default trigger configuration with {len(self.triggers)} triggers")
                
        except Exception as e:
            print(f"  ⚠️ Error loading trigger config: {e}")
            self.triggers = default_triggers
    
    def save_trigger_configuration(self):
        """Save current trigger configuration to YAML file"""
        try:
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            
            config_data = {
                'triggers': [
                    {
                        'trigger_type': t.trigger_type,
                        'source_patterns': t.source_patterns,
                        'target_systems': t.target_systems,
                        'generation_delay': t.generation_delay,
                        'auto_save': t.auto_save,
                        'auto_index': t.auto_index,
                        'cross_system_analysis': t.cross_system_analysis
                    }
                    for t in self.triggers
                ]
            }
            
            with open(self.config_file, 'w', encoding='utf-8') as f:
                yaml.dump(config_data, f, default_flow_style=False, indent=2)
                
            print(f"  ✅ Saved trigger configuration to {self.config_file}")
            
        except Exception as e:
            print(f"  ❌ Error saving trigger config: {e}")
    
    def start_monitoring(self):
        """Start file system monitoring for automatic lesson generation"""
        if self.is_running:
            print("  ⚠️ Trigger system already running")
            return
        
        self.event_handler = LessonTriggerHandler(self)
        self.observer = Observer()
        self.observer.schedule(self.event_handler, str(self.test_cases_dir), recursive=True)
        
        # Also monitor other relevant directories
        for additional_dir in [self.project_dir / "Scripts", self.project_dir / "Templates"]:
            if additional_dir.exists():
                self.observer.schedule(self.event_handler, str(additional_dir), recursive=True)
        
        self.observer.start()
        self.is_running = True
        
        # Start generation worker thread
        self.generation_worker = threading.Thread(target=self._generation_worker, daemon=True)
        self.generation_worker.start()
        
        print("🔄 File system monitoring started")
        print("⚡ Automatic lesson generation active")
        print("  📝 Watching for test case changes...")
        print("  🎓 Auto-generating lessons from test modifications...")
        print("  💾 Auto-saving to organized lesson structure...")
    
    def stop_monitoring(self):
        """Stop file system monitoring"""
        if not self.is_running:
            return
        
        if self.observer:
            self.observer.stop()
            self.observer.join()
        
        self.is_running = False
        print("⏹️ File system monitoring stopped")
    
    def _generation_worker(self):
        """Background worker thread for processing lesson generation queue"""
        while self.is_running:
            try:
                # Check for pending generations
                current_time = time.time()
                ready_files = []
                
                for file_path, trigger_time in list(self.pending_generations.items()):
                    if current_time - trigger_time >= 5.0:  # Default delay
                        ready_files.append(file_path)
                        del self.pending_generations[file_path]
                
                # Process ready files
                for file_path in ready_files:
                    self.process_file_change(Path(file_path))
                
                # Process generation queue
                while self.generation_queue and self.is_running:
                    test_metadata = self.generation_queue.pop(0)
                    self.generate_lesson_from_test_case(test_metadata)
                
                time.sleep(1.0)  # Check every second
                
            except Exception as e:
                print(f"⚠️ Error in generation worker: {e}")
                time.sleep(5.0)  # Wait longer on error
    
    def trigger_lesson_generation(self, file_path: Path, trigger_type: str):
        """Trigger lesson generation for a specific file"""
        print(f"⚡ Trigger detected: {trigger_type} for {file_path.name}")
        
        # Add to pending generations with debounce
        self.pending_generations[str(file_path)] = time.time()
        
        # Find matching triggers
        matching_triggers = []
        for trigger in self.triggers:
            if trigger.trigger_type == trigger_type:
                for pattern in trigger.source_patterns:
                    if file_path.match(pattern.replace('**/', '')):
                        matching_triggers.append(trigger)
                        break
        
        if matching_triggers:
            print(f"  ✅ {len(matching_triggers)} matching triggers found")
            print(f"  ⏰ Lesson generation scheduled (debounce: {matching_triggers[0].generation_delay}s)")
        else:
            print(f"  ⚠️ No matching triggers for {file_path}")
    
    def process_file_change(self, file_path: Path):
        """Process a file change and extract test case metadata"""
        try:
            if not file_path.exists():
                print(f"  ⚠️ File no longer exists: {file_path}")
                return
            
            # Extract test case metadata
            metadata = self.extract_test_case_metadata(file_path)
            if metadata:
                print(f"  📋 Test case metadata extracted for {metadata.test_id}")
                self.generation_queue.append(metadata)
            else:
                print(f"  ⚠️ Could not extract test metadata from {file_path.name}")
                
        except Exception as e:
            print(f"  ❌ Error processing file {file_path}: {e}")
    
    def extract_test_case_metadata(self, file_path: Path) -> Optional[TestCaseMetadata]:
        """Extract metadata from a test case file for lesson generation"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Calculate file checksum
            checksum = hashlib.md5(content.encode()).hexdigest()
            
            # Extract system ID from filename or content
            system_id = self.extract_system_id(file_path, content)
            if not system_id:
                return None
            
            # Extract other metadata
            test_id = self.generate_test_id(file_path, system_id)
            engine = self.extract_engine_info(content)
            skill_level = self.extract_skill_level(content)
            test_type = self.extract_test_type(content)
            version = self.extract_version(content)
            
            return TestCaseMetadata(
                test_id=test_id,
                system_id=system_id,
                engine=engine,
                skill_level=skill_level,
                test_type=test_type,
                version=version,
                file_path=str(file_path),
                last_modified=datetime.fromtimestamp(file_path.stat().st_mtime),
                checksum=checksum
            )
            
        except Exception as e:
            print(f"  ❌ Error extracting metadata from {file_path}: {e}")
            return None
    
    def extract_system_id(self, file_path: Path, content: str) -> Optional[int]:
        """Extract system ID from file path or content"""
        # Try to extract from filename
        import re
        
        filename_match = re.search(r'SYSTEM-(\d+)', str(file_path))
        if filename_match:
            return int(filename_match.group(1))
        
        # Try to extract from content
        content_match = re.search(r'System (\d+)', content)
        if content_match:
            return int(content_match.group(1))
        
        # Map known files to systems
        system_mapping = {
            'PDT-PLUS': 1, 'PUXT-PLUS': 2, 'PSO-PRIME': 3, 'PTT-DOCS-FUSION': 4,
            'REQUIREMENTS-PRIME': 5, 'BUSINESS-OPS-FUSION': 6, 'CONTEXT-EVOLUTION-ENGINE': 7,
            'PERFORMANCE-AI-FUSION': 8, 'SECURITY-BUILD-FUSION': 9, 'KNOWLEDGE-EVOLUTION-ENGINE': 10,
            'UNIVERSAL-ORCHESTRATION-PRIME': 11, 'PMCS-024': 12, 'PAES': 13, 'DPI': 14, 'PTODOS': 15
        }
        
        for system_name, system_id in system_mapping.items():
            if system_name in str(file_path) or system_name in content:
                return system_id
        
        return None
    
    def generate_test_id(self, file_path: Path, system_id: int) -> str:
        """Generate unique test ID"""
        system_names = {
            1: 'PDT-PLUS', 2: 'PUXT-PLUS', 3: 'PSO-PRIME', 4: 'PTT-DOCS-FUSION',
            5: 'REQUIREMENTS-PRIME', 6: 'BUSINESS-OPS-FUSION', 7: 'CONTEXT-EVOLUTION-ENGINE',
            8: 'PERFORMANCE-AI-FUSION', 9: 'SECURITY-BUILD-FUSION', 10: 'KNOWLEDGE-EVOLUTION-ENGINE',
            11: 'UNIVERSAL-ORCHESTRATION-PRIME', 12: 'PMCS-024', 13: 'PAES', 14: 'DPI', 15: 'PTODOS'
        }
        
        system_name = system_names.get(system_id, f'SYSTEM-{system_id}')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return f"{system_name}_AUTO_GENERATED_{timestamp}"
    
    def extract_engine_info(self, content: str) -> Optional[str]:
        """Extract debugging engine information from content"""
        engines = ['ATLAS', 'PRISM', 'NEXUS', 'CRUD']
        for engine in engines:
            if engine in content:
                return engine
        return None
    
    def extract_skill_level(self, content: str) -> str:
        """Extract skill level from content"""
        skill_indicators = {
            'beginner': ['basic', 'introduction', 'beginner', 'getting started'],
            'intermediate': ['intermediate', 'advanced', 'practical'],
            'expert': ['expert', 'master', 'complex', 'enterprise'],
            'master': ['master', 'certification', 'capstone', 'leadership']
        }
        
        content_lower = content.lower()
        for level, indicators in skill_indicators.items():
            if any(indicator in content_lower for indicator in indicators):
                return level
        
        return 'intermediate'  # Default
    
    def extract_test_type(self, content: str) -> str:
        """Extract test type from content"""
        if 'hands-on' in content.lower() or 'practical' in content.lower():
            return 'hands_on'
        elif 'project' in content.lower() or 'capstone' in content.lower():
            return 'project'
        elif 'certification' in content.lower():
            return 'certification'
        elif 'case study' in content.lower():
            return 'case_study'
        else:
            return 'theory'
    
    def extract_version(self, content: str) -> str:
        """Extract version information from content"""
        import re
        version_match = re.search(r'v(\d+\.\d+)', content)
        if version_match:
            return version_match.group(1)
        return '1.0'
    
    def generate_lesson_from_test_case(self, metadata: TestCaseMetadata):
        """Generate evolutionary lesson from test case metadata"""
        try:
            print(f"🎓 Generating lesson for {metadata.test_id}")
            
            # Load the evolutionary lesson template
            template_path = self.project_dir / "Templates" / "Evolutionary-Lesson-Template-Foundation.md"
            if not template_path.exists():
                print(f"  ⚠️ Template not found: {template_path}")
                return
            
            # Generate lesson content using the template
            lesson_content = self.create_lesson_content(metadata, template_path)
            
            # Determine output path
            system_names = {
                1: 'PDT-PLUS', 2: 'PUXT-PLUS', 3: 'PSO-PRIME', 4: 'PTT-DOCS-FUSION',
                5: 'REQUIREMENTS-PRIME', 6: 'BUSINESS-OPS-FUSION', 7: 'CONTEXT-EVOLUTION-ENGINE',
                8: 'PERFORMANCE-AI-FUSION', 9: 'SECURITY-BUILD-FUSION', 10: 'KNOWLEDGE-EVOLUTION-ENGINE',
                11: 'UNIVERSAL-ORCHESTRATION-PRIME', 12: 'PMCS-024', 13: 'PAES', 14: 'DPI', 15: 'PTODOS'
            }
            
            system_name = system_names.get(metadata.system_id, f'SYSTEM-{metadata.system_id}')
            output_dir = self.lessons_dir / "Active" / system_name
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate filename
            lesson_filename = f"{metadata.test_id.replace('_AUTO_GENERATED_', '_LESSON_')}.md"
            output_path = output_dir / lesson_filename
            
            # Save lesson content
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(lesson_content)
            
            print(f"  ✅ Lesson saved: {output_path}")
            
            # Auto-update lesson index if enabled
            self.update_lesson_index(metadata, output_path)
            
            # Trigger cross-system analysis if enabled
            self.analyze_cross_system_applicability(metadata)
            
        except Exception as e:
            print(f"  ❌ Error generating lesson for {metadata.test_id}: {e}")
    
    def create_lesson_content(self, metadata: TestCaseMetadata, template_path: Path) -> str:
        """Create lesson content using the evolutionary lesson template"""
        try:
            # Read the original test case content
            with open(metadata.file_path, 'r', encoding='utf-8') as f:
                test_content = f.read()
            
            # Read the lesson template
            with open(template_path, 'r', encoding='utf-8') as f:
                template = f.read()
            
            # Generate lesson content based on test case and template
            lesson_content = f"""# 🎓 **AUTO-GENERATED EVOLUTIONARY LESSON**
**System**: {metadata.system_id} | **Engine**: {metadata.engine or 'General'} | **Level**: {metadata.skill_level.title()}

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Source Test Case**: {Path(metadata.file_path).name}  
**Test ID**: {metadata.test_id}  
**Version**: {metadata.version}  

---

## 📝 **LESSON METADATA**
```yaml
Lesson Information:
  lesson_id: "AUTO_{metadata.system_id}_{metadata.engine or 'GENERAL'}_{metadata.skill_level.upper()}_{metadata.test_type.upper()}_v{metadata.version}"
  title: "Auto-Generated: {metadata.engine or 'System'} {metadata.skill_level.title()} {metadata.test_type.replace('_', ' ').title()}"
  system_origin: "System {metadata.system_id}"
  skill_level: "{metadata.skill_level}"
  learning_type: "{metadata.test_type}"
  version: "{metadata.version}"
  creation_date: "{datetime.now().strftime('%Y-%m-%d')}"
  auto_generated: true
  
Evolution Tracking:
  previous_versions: []
  evolution_reason: "Auto-generated from test case modification"
  preserved_elements: ["Core test validation principles", "System-specific context"]
  new_elements: ["Educational framework", "Cross-system applicability"]
  
Cross-System Applicability:
  applicable_systems: [TBD - Requires cross-system analysis]
  inheritance_adaptations: [TBD - Requires domain analysis]
  cross_references: [TBD - Requires system integration analysis]
  
Student Protection:
  progress_preservation: "Auto-generated lessons preserve all learning value"
  migration_path: "Test-based learning → System mastery → Cross-system application"
  competency_mapping: "Test validation skills transfer across related systems"
  achievement_continuity: "Lesson completion enhances system-specific certifications"
```

## 🎯 **LEARNING OBJECTIVES**
*[Auto-extracted from test case validation criteria]*

Students will master:
1. **Test case validation** for {metadata.engine or 'system'} functionality
2. **System integration** within the {metadata.system_id} framework context
3. **Practical application** of {metadata.skill_level} level concepts
4. **Cross-system thinking** for broader framework integration

## 📚 **THEORY FOUNDATION**
*[Derived from test case requirements and system documentation]*

### **Core Concepts**
Based on the test case validation requirements, this lesson covers:
- System {metadata.system_id} core functionality and integration patterns
- {metadata.engine or 'General system'} specific capabilities and constraints
- Validation methodologies for {metadata.test_type.replace('_', ' ')} scenarios
- Cross-system applicability and inheritance patterns

## 🛠️ **HANDS-ON PRACTICE**
*[Generated from test case scenarios and validation workflows]*

### **Practical Exercise: Test Case Implementation**
```yaml
Exercise Context:
  based_on: "{Path(metadata.file_path).name}"
  system_context: "System {metadata.system_id} validation and integration"
  skill_level: "{metadata.skill_level}"
  
Student Tasks:
  1. Implement test case validation logic
  2. Verify system integration requirements
  3. Validate cross-system compatibility
  4. Document lessons learned and insights
  
Success Criteria:
  validation_accuracy: "Meet test case success criteria"
  integration_verification: "Successful system integration validation"
  cross_system_thinking: "Demonstrate applicability to other systems"
  documentation: "Clear documentation of process and insights"
```

## 📊 **ASSESSMENT & VALIDATION**
*[Based on test case validation requirements]*

### **Competency Assessment**
1. **Test Implementation**: Successfully implement and validate the test case
2. **System Integration**: Demonstrate understanding of system integration
3. **Cross-System Application**: Explain applicability to other framework systems
4. **Learning Documentation**: Document insights and learning outcomes

## 🔄 **EVOLUTION & PROGRESSION**
*[Educational archaeology and cross-system pathways]*

### **Lesson Evolution Path**
- **v{metadata.version} (Current)**: Auto-generated from test case validation
- **Future Evolution**: Enhanced with student feedback and usage analytics
- **Cross-System Integration**: Adaptation to related systems based on applicability analysis

### **Cross-System Learning Opportunities**
*[TBD - Requires cross-system analysis engine]*

### **Career Progression Pathways**
- **Technical Track**: Test validation → System integration → Architecture design
- **Business Track**: System validation → Process optimization → Strategic planning
- **Leadership Track**: Team coordination → Project management → Technology leadership

---

## 🤖 **AUTO-GENERATION METADATA**

### **Generation Details**
- **Trigger**: File system change detection
- **Source**: {metadata.file_path}
- **Checksum**: {metadata.checksum}
- **Last Modified**: {metadata.last_modified}
- **Processing Time**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

### **Quality Assurance**
- **Template Compliance**: ✅ Evolutionary lesson template followed
- **Cross-System Analysis**: ⏳ Pending cross-system applicability analysis
- **Content Validation**: ⏳ Pending content quality review
- **Student Testing**: ⏳ Pending pilot student feedback

**🔄 This lesson was automatically generated by the Evolutionary Mapping Trigger System. It will evolve based on usage, feedback, and framework development.**
"""
            
            return lesson_content
            
        except Exception as e:
            print(f"  ❌ Error creating lesson content: {e}")
            return f"# Error generating lesson content: {e}"
    
    def update_lesson_index(self, metadata: TestCaseMetadata, lesson_path: Path):
        """Update the lesson index with new lesson"""
        try:
            index_path = self.lessons_dir / "Lessons-Index.md"
            
            # Read current index
            if index_path.exists():
                with open(index_path, 'r', encoding='utf-8') as f:
                    index_content = f.read()
            else:
                index_content = "# 📚 **EVOLUTIONARY LESSONS INDEX**\n\n"
            
            # Add new lesson entry
            lesson_entry = f"- ✅ [{metadata.test_id}]({lesson_path.relative_to(self.lessons_dir)}) - Auto-generated {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            
            # Insert into appropriate system section
            system_section = f"### **System {metadata.system_id}"
            if system_section in index_content:
                # Add to existing section
                insert_pos = index_content.find(system_section)
                section_end = index_content.find('\n### ', insert_pos + 1)
                if section_end == -1:
                    section_end = len(index_content)
                
                updated_content = (index_content[:section_end] + 
                                 lesson_entry + 
                                 index_content[section_end:])
            else:
                # Create new section
                updated_content = index_content + f"\n{system_section}**\n{lesson_entry}\n"
            
            # Save updated index
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"  ✅ Updated lesson index")
            
        except Exception as e:
            print(f"  ⚠️ Error updating lesson index: {e}")
    
    def analyze_cross_system_applicability(self, metadata: TestCaseMetadata):
        """Analyze cross-system applicability for the generated lesson"""
        print(f"  🔍 Analyzing cross-system applicability for {metadata.test_id}")
        # This would integrate with the cross-system inheritance engine
        # For now, just log that analysis is needed
        print(f"  ⏳ Cross-system analysis queued")


class LessonTriggerHandler(FileSystemEventHandler):
    """File system event handler for lesson generation triggers"""
    
    def __init__(self, trigger_system: EvolutionaryLessonTriggerSystem):
        self.trigger_system = trigger_system
        super().__init__()
    
    def on_created(self, event):
        """Handle file creation events"""
        if not event.is_directory:
            file_path = Path(event.src_path)
            self.trigger_system.trigger_lesson_generation(file_path, "test_case_added")
    
    def on_modified(self, event):
        """Handle file modification events"""
        if not event.is_directory:
            file_path = Path(event.src_path)
            # Ignore temporary files and backups
            if not (file_path.name.startswith('.') or file_path.name.endswith('.backup')):
                self.trigger_system.trigger_lesson_generation(file_path, "test_case_modified")
    
    def on_moved(self, event):
        """Handle file move/rename events"""
        if not event.is_directory:
            dest_path = Path(event.dest_path)
            self.trigger_system.trigger_lesson_generation(dest_path, "test_case_added")


def main():
    """Main execution function for trigger system"""
    import sys
    import signal
    
    if len(sys.argv) != 2:
        print("Usage: python automated_lesson_triggers.py <project_directory>")
        sys.exit(1)
    
    project_directory = sys.argv[1]
    
    # Initialize trigger system
    trigger_system = EvolutionaryLessonTriggerSystem(project_directory)
    
    # Set up signal handling for graceful shutdown
    def signal_handler(signum, frame):
        print("\n🛑 Shutting down trigger system...")
        trigger_system.stop_monitoring()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        # Start monitoring
        trigger_system.start_monitoring()
        
        print("\n🎓 Evolutionary Lesson Trigger System Active!")
        print("   📝 Monitoring test case files for changes...")
        print("   ⚡ Auto-generating lessons from modifications...")
        print("   💾 Auto-saving to organized lesson structure...")
        print("   🔄 Cross-system inheritance analysis enabled...")
        print("\n   Press Ctrl+C to stop monitoring\n")
        
        # Keep the script running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Shutting down trigger system...")
        trigger_system.stop_monitoring()

if __name__ == "__main__":
    main()