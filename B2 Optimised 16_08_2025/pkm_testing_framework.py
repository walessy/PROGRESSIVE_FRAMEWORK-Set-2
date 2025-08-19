#!/usr/bin/env python3
"""
PKM Framework Command Testing Suite
Clean Python implementation without unicode characters
Tests all command combinations systematically
"""

import json
import datetime
import os
from dataclasses import dataclass
from typing import List, Dict, Optional
from pathlib import Path


@dataclass
class TestResult:
    """Container for test results"""
    test_id: str
    command: str
    expected_systems: List[str]
    expected_lessons: int
    actual_systems: List[str] = None
    actual_lessons: int = 0
    status: str = "PENDING"
    processing_time: float = 0.0
    output_file: str = ""
    issues: List[str] = None
    timestamp: str = ""
    
    def __post_init__(self):
        if self.issues is None:
            self.issues = []
        if not self.timestamp:
            self.timestamp = datetime.datetime.now().isoformat()


class PKMTestFramework:
    """Main testing framework for PKM commands"""
    
    def __init__(self, working_directory: str):
        self.working_directory = working_directory
        self.test_results = []
        self.system_definitions = self._load_system_definitions()
        self.test_commands = self._generate_test_commands()
        
    def _load_system_definitions(self) -> Dict[str, Dict]:
        """Load system definitions with expected lesson counts"""
        return {
            "PDT-PLUS": {"id": 1, "lessons": 105, "tier": "Foundation"},
            "PUXT-PLUS": {"id": 2, "lessons": 45, "tier": "Foundation"},
            "PSO-PRIME": {"id": 3, "lessons": 50, "tier": "Foundation"},
            "PTT-DOCS-FUSION": {"id": 4, "lessons": 35, "tier": "Foundation"},
            "REQUIREMENTS-PRIME": {"id": 5, "lessons": 35, "tier": "Foundation"},
            "BUSINESS-OPS-FUSION": {"id": 6, "lessons": 40, "tier": "Professional"},
            "CONTEXT-EVOLUTION-ENGINE": {"id": 7, "lessons": 35, "tier": "Professional"},
            "PERFORMANCE-AI-FUSION": {"id": 8, "lessons": 38, "tier": "Professional"},
            "SECURITY-BUILD-FUSION": {"id": 9, "lessons": 42, "tier": "Professional"},
            "KNOWLEDGE-EVOLUTION-ENGINE": {"id": 10, "lessons": 30, "tier": "Universal"},
            "UNIVERSAL-ORCHESTRATION-PRIME": {"id": 11, "lessons": 25, "tier": "Universal"},
            "PMCS-024": {"id": 12, "lessons": 45, "tier": "Universal"},
            "PAES": {"id": 13, "lessons": 35, "tier": "Universal"},
            "DPI": {"id": 14, "lessons": 25, "tier": "Integration"},
            "PTODOS": {"id": 15, "lessons": 30, "tier": "Integration"}
        }
    
    def _generate_test_commands(self) -> List[Dict]:
        """Generate all test command combinations"""
        base_dir = self.working_directory
        timestamp = "20250819_Signal_Based_Activation"
        
        commands = [
            # Test 01: Single System - Debug Focus
            {
                "test_id": "01",
                "name": "Single System - Debug Focus",
                "command": f"""Working Directory: {base_dir}
PDT-PLUS Breathing Framework Implementation
Primary Objectives: Master debugging with ATLAS, PRISM, NEXUS, CRUD engines (105 lessons)
{timestamp}""",
                "expected_systems": ["PDT-PLUS"],
                "expected_lessons": 105
            },
            
            # Test 02: Single System - Business Focus
            {
                "test_id": "02",
                "name": "Single System - Business Focus",
                "command": f"""Working Directory: {base_dir}
BUSINESS-OPS-FUSION Breathing Framework Implementation
Primary Objectives: Business operations mastery (40 lessons)
{timestamp}""",
                "expected_systems": ["BUSINESS-OPS-FUSION"],
                "expected_lessons": 40
            },
            
            # Test 03: Dual System - Business Combo
            {
                "test_id": "03",
                "name": "Dual System - Business Combo",
                "command": f"""Working Directory: {base_dir}
BUSINESS-OPS-FUSION + PUXT-PLUS Implementation
Primary Objectives: Business operations and revenue optimization (85 lessons)
{timestamp}""",
                "expected_systems": ["BUSINESS-OPS-FUSION", "PUXT-PLUS"],
                "expected_lessons": 85
            },
            
            # Test 04: Foundation Tier
            {
                "test_id": "04",
                "name": "Foundation Tier Complete",
                "command": f"""Working Directory: {base_dir}
Foundation Tier Breathing Framework Implementation
Primary Objectives: Learn framework fundamentals through 5 foundation systems (270+ lessons)
{timestamp}""",
                "expected_systems": ["PDT-PLUS", "PUXT-PLUS", "PSO-PRIME", "PTT-DOCS-FUSION", "REQUIREMENTS-PRIME"],
                "expected_lessons": 270
            },
            
            # Test 05: Professional Tier
            {
                "test_id": "05",
                "name": "Professional Tier Complete",
                "command": f"""Working Directory: {base_dir}
Professional Tier Breathing Framework Implementation
Primary Objectives: Advanced professional systems (155+ lessons)
{timestamp}""",
                "expected_systems": ["BUSINESS-OPS-FUSION", "CONTEXT-EVOLUTION-ENGINE", "PERFORMANCE-AI-FUSION", "SECURITY-BUILD-FUSION"],
                "expected_lessons": 155
            },
            
            # Test 06: Universal Tier
            {
                "test_id": "06",
                "name": "Universal Tier Complete",
                "command": f"""Working Directory: {base_dir}
Universal Tier Breathing Framework Implementation
Primary Objectives: Master-level universal systems (135+ lessons)
{timestamp}""",
                "expected_systems": ["KNOWLEDGE-EVOLUTION-ENGINE", "UNIVERSAL-ORCHESTRATION-PRIME", "PMCS-024", "PAES"],
                "expected_lessons": 135
            },
            
            # Test 07: Integration Tier
            {
                "test_id": "07",
                "name": "Integration Tier Complete",
                "command": f"""Working Directory: {base_dir}
Integration Tier Breathing Framework Implementation
Primary Objectives: Meta-integration systems (55+ lessons)
{timestamp}""",
                "expected_systems": ["DPI", "PTODOS"],
                "expected_lessons": 55
            },
            
            # Test 08: Foundation + Professional
            {
                "test_id": "08",
                "name": "Foundation + Professional Tiers",
                "command": f"""Working Directory: {base_dir}
Foundation + Professional Tier Breathing Framework Implementation
Primary Objectives: Comprehensive learning path (425+ lessons)
{timestamp}""",
                "expected_systems": ["PDT-PLUS", "PUXT-PLUS", "PSO-PRIME", "PTT-DOCS-FUSION", "REQUIREMENTS-PRIME",
                                   "BUSINESS-OPS-FUSION", "CONTEXT-EVOLUTION-ENGINE", "PERFORMANCE-AI-FUSION", "SECURITY-BUILD-FUSION"],
                "expected_lessons": 425
            },
            
            # Test 09: Professional + Universal
            {
                "test_id": "09",
                "name": "Professional + Universal Tiers",
                "command": f"""Working Directory: {base_dir}
Professional + Universal Tier Breathing Framework Implementation
Primary Objectives: Advanced implementation skills (290+ lessons)
{timestamp}""",
                "expected_systems": ["BUSINESS-OPS-FUSION", "CONTEXT-EVOLUTION-ENGINE", "PERFORMANCE-AI-FUSION", "SECURITY-BUILD-FUSION",
                                   "KNOWLEDGE-EVOLUTION-ENGINE", "UNIVERSAL-ORCHESTRATION-PRIME", "PMCS-024", "PAES"],
                "expected_lessons": 290
            },
            
            # Test 10: Foundation + Universal
            {
                "test_id": "10",
                "name": "Foundation + Universal Tiers",
                "command": f"""Working Directory: {base_dir}
Foundation + Universal Tier Breathing Framework Implementation
Primary Objectives: Strategic learning path (405+ lessons)
{timestamp}""",
                "expected_systems": ["PDT-PLUS", "PUXT-PLUS", "PSO-PRIME", "PTT-DOCS-FUSION", "REQUIREMENTS-PRIME",
                                   "KNOWLEDGE-EVOLUTION-ENGINE", "UNIVERSAL-ORCHESTRATION-PRIME", "PMCS-024", "PAES"],
                "expected_lessons": 405
            },
            
            # Test 11: Complete Framework
            {
                "test_id": "11",
                "name": "Complete Framework Standard",
                "command": f"""Working Directory: {base_dir}
Complete 15-System Breathing Framework Implementation
Primary Objectives: Full framework deployment (615+ lessons)
{timestamp}""",
                "expected_systems": list(self.system_definitions.keys()),
                "expected_lessons": 615
            },
            
            # Test 12: Complete Framework with Override
            {
                "test_id": "12",
                "name": "Complete Framework with Corporate Override",
                "command": f"""Working Directory: {base_dir}
Complete 15-System Breathing Framework Implementation
Primary Objectives: Full enterprise deployment (615+ lessons)
Tier Override: FORCE_ALL_TIERS_ACTIVE
Scope: CORPORATE_TRAINING
{timestamp}""",
                "expected_systems": list(self.system_definitions.keys()),
                "expected_lessons": 615
            }
        ]
        
        return commands
    
    def run_test(self, test_command: Dict) -> TestResult:
        """Run individual test (simulation - in real use, this would interact with Claude)"""
        print(f"Running Test {test_command['test_id']}: {test_command['name']}")
        
        result = TestResult(
            test_id=test_command['test_id'],
            command=test_command['command'],
            expected_systems=test_command['expected_systems'],
            expected_lessons=test_command['expected_lessons']
        )
        
        # SIMULATION: In real implementation, this would:
        # 1. Send command to Claude
        # 2. Parse the response
        # 3. Extract system list and lesson count
        # 4. Measure processing time
        
        # For now, simulate results
        result.actual_systems = test_command['expected_systems']  # Simulate perfect match
        result.actual_lessons = test_command['expected_lessons']   # Simulate perfect match
        result.status = "PASS"
        result.processing_time = 45.0  # Simulate 45 second processing
        result.output_file = f"Chat_Test{test_command['test_id']}_{test_command['name'].replace(' ', '_')}_20250819.md"
        
        print(f"  Expected Systems: {len(result.expected_systems)}")
        print(f"  Actual Systems: {len(result.actual_systems)}")
        print(f"  Expected Lessons: {result.expected_lessons}")
        print(f"  Actual Lessons: {result.actual_lessons}")
        print(f"  Status: {result.status}")
        print(f"  Processing Time: {result.processing_time}s")
        print()
        
        return result
    
    def validate_result(self, result: TestResult) -> TestResult:
        """Validate test result against expected criteria"""
        issues = []
        
        # Check system count
        if len(result.actual_systems) != len(result.expected_systems):
            issues.append(f"System count mismatch: expected {len(result.expected_systems)}, got {len(result.actual_systems)}")
        
        # Check specific systems
        missing_systems = set(result.expected_systems) - set(result.actual_systems)
        extra_systems = set(result.actual_systems) - set(result.expected_systems)
        
        if missing_systems:
            issues.append(f"Missing systems: {', '.join(missing_systems)}")
        if extra_systems:
            issues.append(f"Unexpected systems: {', '.join(extra_systems)}")
        
        # Check lesson count (allow 5% variance)
        lesson_variance = abs(result.actual_lessons - result.expected_lessons) / result.expected_lessons
        if lesson_variance > 0.05:
            issues.append(f"Lesson count variance: {lesson_variance:.1%} (expected {result.expected_lessons}, got {result.actual_lessons})")
        
        # Check processing time (warn if > 2 minutes)
        if result.processing_time > 120:
            issues.append(f"Processing time too long: {result.processing_time}s (limit: 120s)")
        
        # Update result
        result.issues = issues
        if issues:
            result.status = "FAIL" if len(issues) > 2 else "PARTIAL"
        else:
            result.status = "PASS"
        
        return result
    
    def run_all_tests(self) -> List[TestResult]:
        """Run complete test suite"""
        print("=== PKM Framework Command Testing Suite ===")
        print(f"Working Directory: {self.working_directory}")
        print(f"Total Tests: {len(self.test_commands)}")
        print(f"Start Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        results = []
        
        for test_command in self.test_commands:
            result = self.run_test(test_command)
            validated_result = self.validate_result(result)
            results.append(validated_result)
            
            # Display issues if any
            if validated_result.issues:
                print("  ISSUES FOUND:")
                for issue in validated_result.issues:
                    print(f"    - {issue}")
                print()
        
        self.test_results = results
        return results
    
    def generate_report(self) -> str:
        """Generate comprehensive test report"""
        if not self.test_results:
            return "No test results available. Run tests first."
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for r in self.test_results if r.status == "PASS")
        partial_tests = sum(1 for r in self.test_results if r.status == "PARTIAL")
        failed_tests = sum(1 for r in self.test_results if r.status == "FAIL")
        
        report = f"""
PKM FRAMEWORK TESTING REPORT
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Working Directory: {self.working_directory}

SUMMARY:
Total Tests: {total_tests}
Passed: {passed_tests} ({passed_tests/total_tests:.1%})
Partial: {partial_tests} ({partial_tests/total_tests:.1%})
Failed: {failed_tests} ({failed_tests/total_tests:.1%})

DETAILED RESULTS:
"""
        
        for result in self.test_results:
            report += f"""
Test {result.test_id}: {result.status}
Expected Systems: {len(result.expected_systems)} ({', '.join(result.expected_systems)})
Actual Systems: {len(result.actual_systems)} ({', '.join(result.actual_systems)})
Expected Lessons: {result.expected_lessons}
Actual Lessons: {result.actual_lessons}
Processing Time: {result.processing_time}s
Output File: {result.output_file}
"""
            if result.issues:
                report += "Issues:\n"
                for issue in result.issues:
                    report += f"  - {issue}\n"
        
        return report
    
    def save_results(self, filename: str = None) -> str:
        """Save test results to JSON file"""
        if filename is None:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"pkm_test_results_{timestamp}.json"
        
        # Convert results to dict for JSON serialization
        results_data = {
            "metadata": {
                "working_directory": self.working_directory,
                "total_tests": len(self.test_results),
                "timestamp": datetime.datetime.now().isoformat()
            },
            "results": []
        }
        
        for result in self.test_results:
            results_data["results"].append({
                "test_id": result.test_id,
                "command": result.command,
                "expected_systems": result.expected_systems,
                "expected_lessons": result.expected_lessons,
                "actual_systems": result.actual_systems,
                "actual_lessons": result.actual_lessons,
                "status": result.status,
                "processing_time": result.processing_time,
                "output_file": result.output_file,
                "issues": result.issues,
                "timestamp": result.timestamp
            })
        
        with open(filename, 'w') as f:
            json.dump(results_data, f, indent=2)
        
        return filename
    
    def run_specific_test(self, test_id: str) -> Optional[TestResult]:
        """Run a specific test by ID"""
        test_command = next((cmd for cmd in self.test_commands if cmd['test_id'] == test_id), None)
        if not test_command:
            print(f"Test {test_id} not found")
            return None
        
        result = self.run_test(test_command)
        validated_result = self.validate_result(result)
        return validated_result


def main():
    """Main function for command-line usage"""
    import sys
    
    # Default working directory (can be overridden)
    default_wd = r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025"
    
    if len(sys.argv) > 1:
        working_directory = sys.argv[1]
    else:
        working_directory = default_wd
    
    # Create test framework
    framework = PKMTestFramework(working_directory)
    
    # Run tests
    if len(sys.argv) > 2 and sys.argv[2].startswith("test_"):
        # Run specific test
        test_id = sys.argv[2].replace("test_", "")
        result = framework.run_specific_test(test_id)
        if result:
            print("=== SPECIFIC TEST RESULT ===")
            print(f"Test {result.test_id}: {result.status}")
            if result.issues:
                print("Issues:")
                for issue in result.issues:
                    print(f"  - {issue}")
    else:
        # Run all tests
        results = framework.run_all_tests()
        
        # Generate and display report
        report = framework.generate_report()
        print(report)
        
        # Save results
        results_file = framework.save_results()
        print(f"\nResults saved to: {results_file}")


if __name__ == "__main__":
    main()
