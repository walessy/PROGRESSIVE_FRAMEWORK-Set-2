#!/usr/bin/env python3
"""
Breathing Framework Robustness Testing Tool
SAVE AS: robustness_tester.py
PURPOSE: Test breathing framework response to lesson file modifications
WORKING_DIRECTORY: C:/Users/Wales/OneDrive/Desktop/PROGRESSIVE_FRAMEWORK-Set-2/B2 Optimised 16_08_2025
"""

import os
import time
import random
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

class BreathingFrameworkRobustnessTester:
    """Test the robustness of the breathing framework by modifying lesson files"""
    
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        self.lessons_dir = self.base_dir / "Lessons"
        self.signals_dir = self.base_dir / "signals"
        self.test_results = []
        self.backup_dir = self.base_dir / "robustness_test_backups"
        
        print("🔄 BREATHING FRAMEWORK ROBUSTNESS TESTER INITIALIZED")
        print(f"📁 Base Directory: {self.base_dir}")
        print(f"📚 Lessons Directory: {self.lessons_dir}")
        print(f"📡 Signals Directory: {self.signals_dir}")
        
        # Create backup directory
        self.backup_dir.mkdir(exist_ok=True)
        
    def discover_lesson_structure(self) -> Dict:
        """Discover the current lesson folder structure"""
        print("\n🔍 DISCOVERING LESSON STRUCTURE...")
        
        structure = {}
        if not self.lessons_dir.exists():
            print(f"❌ Lessons directory not found: {self.lessons_dir}")
            return structure
            
        for system_folder in self.lessons_dir.iterdir():
            if system_folder.is_dir():
                system_name = system_folder.name
                structure[system_name] = []
                
                print(f"📁 Found system: {system_name}")
                
                # Find lesson files in this system
                for lesson_file in system_folder.rglob("*.md"):
                    structure[system_name].append(lesson_file)
                    print(f"  📄 Lesson: {lesson_file.name}")
                    
                # Find subfolders
                for subfolder in system_folder.iterdir():
                    if subfolder.is_dir():
                        print(f"  📁 Subfolder: {subfolder.name}")
                        for lesson_file in subfolder.rglob("*.md"):
                            structure[system_name].append(lesson_file)
                            print(f"    📄 Lesson: {lesson_file.name}")
        
        total_lessons = sum(len(lessons) for lessons in structure.values())
        print(f"\n📊 DISCOVERY COMPLETE: {len(structure)} systems, {total_lessons} lessons")
        return structure
        
    def backup_lesson_file(self, lesson_file: Path) -> Path:
        """Create backup of lesson file before modification"""
        backup_path = self.backup_dir / f"{lesson_file.stem}_backup_{datetime.now().strftime('%H%M%S')}.md"
        shutil.copy2(lesson_file, backup_path)
        return backup_path
        
    def touch_lesson_file(self, lesson_file: Path, modification_type: str) -> bool:
        """Modify lesson file to trigger breathing framework response"""
        try:
            # Backup original
            backup_path = self.backup_lesson_file(lesson_file)
            
            # Read current content
            content = lesson_file.read_text(encoding='utf-8')
            
            # Apply modification based on type
            if modification_type == "add_line":
                new_content = content + f"\n\n<!-- Robustness test modification: {datetime.now()} -->"
            elif modification_type == "modify_title":
                new_content = content.replace("# ", f"# [MODIFIED] ", 1)
            elif modification_type == "add_section":
                new_content = content + f"\n\n## Robustness Test Section\n\nAdded at {datetime.now()}"
            elif modification_type == "touch_timestamp":
                # Just touch the file to update timestamp
                lesson_file.touch()
                return True
            else:
                new_content = content + f"\n\n<!-- {modification_type}: {datetime.now()} -->"
            
            # Write modified content
            lesson_file.write_text(new_content, encoding='utf-8')
            
            print(f"✅ Modified {lesson_file.name} - {modification_type}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to modify {lesson_file.name}: {e}")
            return False
            
    def monitor_signals_response(self, timeout_seconds: int = 30) -> Dict:
        """Monitor signals directory for breathing framework response"""
        print(f"📡 Monitoring signals for {timeout_seconds} seconds...")
        
        initial_signals = self.count_signals()
        start_time = time.time()
        
        response_data = {
            "initial_signals": initial_signals,
            "final_signals": 0,
            "new_signals": 0,
            "response_time": 0,
            "signals_detected": []
        }
        
        while time.time() - start_time < timeout_seconds:
            current_signals = self.count_signals()
            if current_signals > initial_signals:
                response_data["response_time"] = time.time() - start_time
                response_data["new_signals"] = current_signals - initial_signals
                response_data["signals_detected"] = self.get_recent_signals(start_time)
                break
            time.sleep(0.5)
            
        response_data["final_signals"] = self.count_signals()
        return response_data
        
    def count_signals(self) -> int:
        """Count total signal files"""
        if not self.signals_dir.exists():
            return 0
        return sum(1 for _ in self.signals_dir.rglob("*.signal"))
        
    def get_recent_signals(self, since_time: float) -> List[str]:
        """Get list of signal files created since given time"""
        recent_signals = []
        if not self.signals_dir.exists():
            return recent_signals
            
        for signal_file in self.signals_dir.rglob("*.signal"):
            if signal_file.stat().st_mtime > since_time:
                recent_signals.append(signal_file.name)
        return recent_signals
        
    def run_single_robustness_test(self, lesson_file: Path, modification_type: str) -> Dict:
        """Run a single robustness test"""
        print(f"\n🧪 ROBUSTNESS TEST: {lesson_file.name}")
        print(f"🔧 Modification Type: {modification_type}")
        
        test_result = {
            "lesson_file": str(lesson_file),
            "modification_type": modification_type,
            "timestamp": datetime.now().isoformat(),
            "modification_success": False,
            "framework_response": {},
            "response_time": None,
            "signals_generated": 0
        }
        
        # Step 1: Modify the lesson file
        test_result["modification_success"] = self.touch_lesson_file(lesson_file, modification_type)
        
        if test_result["modification_success"]:
            # Step 2: Monitor for breathing framework response
            test_result["framework_response"] = self.monitor_signals_response()
            test_result["response_time"] = test_result["framework_response"]["response_time"]
            test_result["signals_generated"] = test_result["framework_response"]["new_signals"]
        
        # Step 3: Evaluate response
        self.evaluate_test_result(test_result)
        return test_result
        
    def evaluate_test_result(self, test_result: Dict):
        """Evaluate the test result and provide feedback"""
        print(f"\n📊 TEST EVALUATION:")
        print(f"  Modification Success: {'✅' if test_result['modification_success'] else '❌'}")
        
        if test_result["signals_generated"] > 0:
            print(f"  Framework Response: ✅ {test_result['signals_generated']} signals generated")
            print(f"  Response Time: ⚡ {test_result['response_time']:.2f} seconds")
        else:
            print(f"  Framework Response: ❌ No signals detected")
            
        # Performance evaluation
        if test_result["response_time"]:
            if test_result["response_time"] < 5:
                print(f"  Performance: 🚀 EXCELLENT (< 5s)")
            elif test_result["response_time"] < 15:
                print(f"  Performance: ✅ GOOD (< 15s)")
            elif test_result["response_time"] < 30:
                print(f"  Performance: ⚠️ ACCEPTABLE (< 30s)")
            else:
                print(f"  Performance: ❌ SLOW (> 30s)")
        
    def run_comprehensive_robustness_test(self, max_tests: int = 10):
        """Run comprehensive robustness testing across multiple lesson files"""
        print(f"\n🚀 STARTING COMPREHENSIVE ROBUSTNESS TEST")
        print(f"🎯 Maximum Tests: {max_tests}")
        
        # Discover lesson structure
        lesson_structure = self.discover_lesson_structure()
        
        if not lesson_structure:
            print("❌ No lessons found for testing")
            return
            
        # Collect all lesson files
        all_lessons = []
        for system_lessons in lesson_structure.values():
            all_lessons.extend(system_lessons)
            
        # Select random lessons for testing
        selected_lessons = random.sample(all_lessons, min(max_tests, len(all_lessons)))
        
        modification_types = ["add_line", "modify_title", "add_section", "touch_timestamp"]
        
        print(f"\n🧪 EXECUTING {len(selected_lessons)} ROBUSTNESS TESTS...")
        
        for i, lesson_file in enumerate(selected_lessons, 1):
            modification_type = random.choice(modification_types)
            
            print(f"\n" + "="*60)
            print(f"TEST {i}/{len(selected_lessons)}")
            
            test_result = self.run_single_robustness_test(lesson_file, modification_type)
            self.test_results.append(test_result)
            
            # Wait between tests to avoid overwhelming the system
            if i < len(selected_lessons):
                print(f"⏱️ Waiting 5 seconds before next test...")
                time.sleep(5)
                
        self.generate_robustness_report()
        
    def run_targeted_system_test(self, system_name: str):
        """Test robustness for a specific system"""
        print(f"\n🎯 TARGETED ROBUSTNESS TEST: {system_name}")
        
        lesson_structure = self.discover_lesson_structure()
        
        if system_name not in lesson_structure:
            print(f"❌ System not found: {system_name}")
            print(f"Available systems: {list(lesson_structure.keys())}")
            return
            
        system_lessons = lesson_structure[system_name]
        if not system_lessons:
            print(f"❌ No lessons found for system: {system_name}")
            return
            
        print(f"🧪 Testing {len(system_lessons)} lessons for {system_name}")
        
        modification_types = ["add_line", "modify_title", "add_section"]
        
        for i, lesson_file in enumerate(system_lessons, 1):
            modification_type = modification_types[i % len(modification_types)]
            
            print(f"\n" + "-"*40)
            print(f"SYSTEM TEST {i}/{len(system_lessons)}")
            
            test_result = self.run_single_robustness_test(lesson_file, modification_type)
            self.test_results.append(test_result)
            
            if i < len(system_lessons):
                time.sleep(3)
                
        self.generate_robustness_report()
        
    def generate_robustness_report(self):
        """Generate comprehensive robustness test report"""
        print(f"\n" + "="*60)
        print("📊 ROBUSTNESS TEST REPORT")
        print("="*60)
        
        if not self.test_results:
            print("❌ No test results available")
            return
            
        total_tests = len(self.test_results)
        successful_modifications = sum(1 for result in self.test_results if result["modification_success"])
        framework_responses = sum(1 for result in self.test_results if result["signals_generated"] > 0)
        
        print(f"📈 SUMMARY STATISTICS:")
        print(f"  Total Tests: {total_tests}")
        print(f"  Successful Modifications: {successful_modifications}/{total_tests} ({successful_modifications/total_tests*100:.1f}%)")
        print(f"  Framework Responses: {framework_responses}/{total_tests} ({framework_responses/total_tests*100:.1f}%)")
        
        # Response time analysis
        response_times = [result["response_time"] for result in self.test_results if result["response_time"]]
        if response_times:
            avg_response = sum(response_times) / len(response_times)
            min_response = min(response_times)
            max_response = max(response_times)
            
            print(f"\n⚡ RESPONSE TIME ANALYSIS:")
            print(f"  Average Response: {avg_response:.2f} seconds")
            print(f"  Fastest Response: {min_response:.2f} seconds")
            print(f"  Slowest Response: {max_response:.2f} seconds")
            
        # Performance grades
        excellent = sum(1 for t in response_times if t < 5)
        good = sum(1 for t in response_times if 5 <= t < 15)
        acceptable = sum(1 for t in response_times if 15 <= t < 30)
        slow = sum(1 for t in response_times if t >= 30)
        
        print(f"\n🎯 PERFORMANCE GRADES:")
        print(f"  🚀 Excellent (< 5s): {excellent}")
        print(f"  ✅ Good (5-15s): {good}")
        print(f"  ⚠️ Acceptable (15-30s): {acceptable}")
        print(f"  ❌ Slow (> 30s): {slow}")
        
        # Save detailed report
        self.save_detailed_report()
        
    def save_detailed_report(self):
        """Save detailed test report to file"""
        report_file = self.base_dir / f"robustness_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w') as f:
            f.write("BREATHING FRAMEWORK ROBUSTNESS TEST REPORT\n")
            f.write("="*50 + "\n\n")
            f.write(f"Test Date: {datetime.now()}\n")
            f.write(f"Total Tests: {len(self.test_results)}\n\n")
            
            for i, result in enumerate(self.test_results, 1):
                f.write(f"TEST {i}:\n")
                f.write(f"  Lesson: {result['lesson_file']}\n")
                f.write(f"  Modification: {result['modification_type']}\n")
                f.write(f"  Success: {result['modification_success']}\n")
                f.write(f"  Response Time: {result['response_time']}\n")
                f.write(f"  Signals Generated: {result['signals_generated']}\n")
                f.write(f"  Timestamp: {result['timestamp']}\n\n")
                
        print(f"📄 Detailed report saved: {report_file}")


def main():
    """Main function for interactive robustness testing"""
    print("🔄 BREATHING FRAMEWORK ROBUSTNESS TESTER")
    print("="*50)
    
    # Get working directory
    working_dir = input("📁 Enter working directory (or press Enter for current): ").strip()
    if not working_dir:
        working_dir = os.getcwd()
        
    tester = BreathingFrameworkRobustnessTester(working_dir)
    
    while True:
        print("\n🔧 ROBUSTNESS TESTING OPTIONS:")
        print("1. 🔍 Discover lesson structure")
        print("2. 🧪 Run single lesson test")
        print("3. 🚀 Run comprehensive test (10 random lessons)")
        print("4. 🎯 Run targeted system test")
        print("5. 📊 View test results")
        print("6. 🚪 Exit")
        
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == "1":
            tester.discover_lesson_structure()
            
        elif choice == "2":
            lesson_path = input("📄 Enter lesson file path: ").strip()
            if lesson_path and os.path.exists(lesson_path):
                mod_type = input("🔧 Modification type (add_line/modify_title/add_section/touch_timestamp): ").strip()
                if not mod_type:
                    mod_type = "add_line"
                tester.run_single_robustness_test(Path(lesson_path), mod_type)
            else:
                print("❌ Invalid lesson file path")
                
        elif choice == "3":
            max_tests = input("🎯 Max tests (default 10): ").strip()
            try:
                max_tests = int(max_tests) if max_tests else 10
            except ValueError:
                max_tests = 10
            tester.run_comprehensive_robustness_test(max_tests)
            
        elif choice == "4":
            system_name = input("🎯 System name (e.g., PDT-PLUS): ").strip()
            if system_name:
                tester.run_targeted_system_test(system_name)
            else:
                print("❌ System name required")
                
        elif choice == "5":
            tester.generate_robustness_report()
            
        elif choice == "6":
            print("👋 Exiting robustness tester")
            break
            
        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    main()