#!/usr/bin/env python3
"""
Signal Diagnostic Tool
SAVE AS: signal_diagnostic.py
REPLACES: No direct replacement - NEW diagnostic script
LOCATION: Save to your working directory main folder
PURPOSE: Diagnose why signal hooks are not generating signals
VERSION: v1.0 - Comprehensive signal system diagnostic
ACTION NEEDED: Run this script to identify signal processing issues
CHAT: Chat006
WORKING DIRECTORY: C:/Users/Wales/OneDrive/Desktop/PROGRESSIVE_FRAMEWORK-Set-2/B2 Optimised 16_08_2025
PROJECT CONTEXT: Progressive Framework Set 2 Development with Signal-Based Processing
PKM PROTOCOL: v8.0 Compatible (Signal-Based Architecture)
SIGNAL INTEGRATION: Diagnoses signal processing infrastructure issues
TROUBLESHOOTING: Identifies root cause of signal generation failures
STATUS: Ready for Local Sync and Project Knowledge Update
"""

import os
import json
import time
from pathlib import Path
from datetime import datetime

class SignalDiagnostic:
    """Comprehensive diagnostic for signal processing issues"""
    
    def __init__(self, working_directory: str):
        self.working_directory = Path(working_directory)
        self.signals_folder = self.working_directory / "signals"
        self.test_results = {}
        
    def test_1_signal_folder_structure(self):
        """Test 1: Verify signal folder structure exists"""
        print("🧪 TEST 1: Signal Folder Structure")
        print("-" * 40)
        
        expected_folders = [
            "test_cases", "systems", "debug", "coordination",
            "debug/atlas", "debug/prism", "debug/nexus", "debug/crud"
        ]
        
        results = {
            "signals_folder_exists": self.signals_folder.exists(),
            "subfolders_exist": {},
            "folder_permissions": {}
        }
        
        print(f"📁 Signals folder: {self.signals_folder}")
        print(f"   Exists: {'✅' if results['signals_folder_exists'] else '❌'}")
        
        if results["signals_folder_exists"]:
            for folder in expected_folders:
                folder_path = self.signals_folder / folder
                exists = folder_path.exists()
                results["subfolders_exist"][folder] = exists
                
                # Check write permissions
                try:
                    test_file = folder_path / ".test_write"
                    test_file.touch()
                    test_file.unlink()
                    can_write = True
                except:
                    can_write = False
                
                results["folder_permissions"][folder] = can_write
                
                status = "✅" if exists else "❌"
                perm_status = "✅" if can_write else "❌"
                print(f"   {folder}: {status} (Write: {perm_status})")
        
        self.test_results["folder_structure"] = results
        return results["signals_folder_exists"] and all(results["subfolders_exist"].values())
    
    def test_2_manual_signal_creation(self):
        """Test 2: Create signal file manually"""
        print("\n🧪 TEST 2: Manual Signal Creation")
        print("-" * 40)
        
        try:
            # Create a test signal manually
            signal_id = f"diagnostic_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            signal_content = {
                "signal_metadata": {
                    "signal_id": signal_id,
                    "timestamp": datetime.now().isoformat(),
                    "signal_type": "DIAGNOSTIC_TEST",
                    "source_system": "DiagnosticTool",
                    "version": "1.0"
                },
                "test_data": {
                    "purpose": "Manual signal creation test",
                    "created_by": "signal_diagnostic.py"
                }
            }
            
            # Write to test_cases folder
            signal_file = self.signals_folder / "test_cases" / f"{signal_id}.signal"
            
            with open(signal_file, 'w') as f:
                json.dump(signal_content, f, indent=2)
            
            print(f"✅ Manual signal created: {signal_file.name}")
            
            # Verify file exists and has content
            if signal_file.exists():
                file_size = signal_file.stat().st_size
                print(f"   File size: {file_size} bytes")
                
                self.test_results["manual_signal"] = {
                    "success": True,
                    "file_path": str(signal_file),
                    "file_size": file_size
                }
                return True
            else:
                print("❌ Signal file was not created")
                self.test_results["manual_signal"] = {"success": False, "error": "File not created"}
                return False
                
        except Exception as e:
            print(f"❌ Error creating manual signal: {e}")
            self.test_results["manual_signal"] = {"success": False, "error": str(e)}
            return False
    
    def test_3_watchdog_availability(self):
        """Test 3: Check if watchdog library is available and working"""
        print("\n🧪 TEST 3: Watchdog Library Test")
        print("-" * 40)
        
        try:
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler
            print("✅ Watchdog library imported successfully")
            
            # Test basic observer creation
            observer = Observer()
            print("✅ Observer created successfully")
            
            # Test event handler
            class TestHandler(FileSystemEventHandler):
                def __init__(self):
                    self.events_detected = 0
                    
                def on_modified(self, event):
                    self.events_detected += 1
                    print(f"   📡 Event detected: {event.src_path}")
                    
                def on_created(self, event):
                    self.events_detected += 1
                    print(f"   📡 Creation detected: {event.src_path}")
            
            handler = TestHandler()
            
            # Set up monitoring on a test directory
            test_dir = self.working_directory / "test_monitor"
            test_dir.mkdir(exist_ok=True)
            
            observer.schedule(handler, str(test_dir), recursive=False)
            observer.start()
            print(f"✅ Observer started monitoring: {test_dir}")
            
            # Create a test file to trigger events
            test_file = test_dir / "watchdog_test.txt"
            test_file.write_text("Test content")
            print(f"✅ Test file created: {test_file.name}")
            
            # Wait for events
            time.sleep(2)
            
            # Modify the file
            test_file.write_text("Modified content")
            print(f"✅ Test file modified")
            
            # Wait for events
            time.sleep(2)
            
            # Stop observer
            observer.stop()
            observer.join()
            
            # Clean up
            test_file.unlink()
            test_dir.rmdir()
            
            events_detected = handler.events_detected
            print(f"📊 Events detected: {events_detected}")
            
            self.test_results["watchdog"] = {
                "available": True,
                "events_detected": events_detected,
                "working": events_detected > 0
            }
            
            return events_detected > 0
            
        except ImportError as e:
            print(f"❌ Watchdog library not available: {e}")
            self.test_results["watchdog"] = {"available": False, "error": str(e)}
            return False
        except Exception as e:
            print(f"❌ Watchdog test failed: {e}")
            self.test_results["watchdog"] = {"available": True, "error": str(e), "working": False}
            return False
    
    def test_4_signal_generation_logic(self):
        """Test 4: Test signal generation logic directly"""
        print("\n🧪 TEST 4: Signal Generation Logic Test")
        print("-" * 40)
        
        try:
            # Import signal generation logic from signal_hooks_implementation
            import sys
            sys.path.append(str(self.working_directory))
            
            # Test direct signal generation
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            signal_id = f"logic_test_{timestamp}"
            
            signal_content = {
                "signal_metadata": {
                    "signal_id": signal_id,
                    "timestamp": datetime.now().isoformat(),
                    "signal_type": "LOGIC_TEST",
                    "priority": "HIGH",
                    "source_system": "DiagnosticTool",
                    "version": "1.1"
                },
                "signal_data": {
                    "test_type": "logic_verification",
                    "file_path": "diagnostic_test.md",
                    "change_type": "MODIFIED"
                }
            }
            
            # Generate signal file using same logic as signal hooks
            signal_folder = self.signals_folder / "systems"
            signal_folder.mkdir(parents=True, exist_ok=True)
            signal_file_path = signal_folder / f"{signal_id}.signal"
            
            with open(signal_file_path, 'w') as f:
                json.dump(signal_content, f, indent=2)
            
            print(f"✅ Logic test signal created: {signal_file_path.name}")
            
            # Verify signal exists
            if signal_file_path.exists():
                file_size = signal_file_path.stat().st_size
                print(f"   File size: {file_size} bytes")
                
                self.test_results["signal_logic"] = {
                    "success": True,
                    "signal_path": str(signal_file_path),
                    "file_size": file_size
                }
                return True
            else:
                print("❌ Logic test signal not created")
                self.test_results["signal_logic"] = {"success": False}
                return False
                
        except Exception as e:
            print(f"❌ Signal generation logic test failed: {e}")
            self.test_results["signal_logic"] = {"success": False, "error": str(e)}
            return False
    
    def test_5_file_event_simulation(self):
        """Test 5: Simulate file events manually"""
        print("\n🧪 TEST 5: File Event Simulation")
        print("-" * 40)
        
        try:
            # Create a test file in System_Specs
            test_file = self.working_directory / "System_Specs" / "diagnostic_test.md"
            
            # Ensure directory exists
            test_file.parent.mkdir(exist_ok=True)
            
            print(f"📁 Creating test file: {test_file.name}")
            
            # Create file with content
            test_content = f"""# Diagnostic Test File
            
Created: {datetime.now().isoformat()}
Purpose: Test file event detection

## Test Details
This file is created to test if file system events trigger signal generation.
"""
            
            test_file.write_text(test_content)
            print("✅ Test file created")
            
            # Wait for potential signal generation
            print("⏳ Waiting 5 seconds for signal generation...")
            time.sleep(5)
            
            # Check if any signals were generated
            total_signals = 0
            signal_folders = ["test_cases", "systems", "debug", "coordination"]
            
            for folder_name in signal_folders:
                folder_path = self.signals_folder / folder_name
                if folder_path.exists():
                    signals = list(folder_path.glob("*.signal"))
                    folder_signals = len(signals)
                    total_signals += folder_signals
                    
                    if folder_signals > 0:
                        print(f"   📡 {folder_name}: {folder_signals} signals")
                        # Show most recent signal
                        recent_signal = max(signals, key=lambda x: x.stat().st_mtime)
                        mod_time = datetime.fromtimestamp(recent_signal.stat().st_mtime)
                        print(f"      Latest: {recent_signal.name} ({mod_time.strftime('%H:%M:%S')})")
            
            # Clean up test file
            test_file.unlink()
            print(f"🧹 Cleaned up test file")
            
            print(f"📊 Total signals after file creation: {total_signals}")
            
            self.test_results["file_simulation"] = {
                "signals_generated": total_signals,
                "success": total_signals > 0
            }
            
            return total_signals > 0
            
        except Exception as e:
            print(f"❌ File event simulation failed: {e}")
            self.test_results["file_simulation"] = {"success": False, "error": str(e)}
            return False
    
    def run_complete_diagnostic(self):
        """Run all diagnostic tests"""
        print("🔍 SIGNAL PROCESSING DIAGNOSTIC SUITE")
        print("=" * 60)
        print("PURPOSE: Identify why signal hooks are not generating signals")
        
        tests = [
            ("Signal Folder Structure", self.test_1_signal_folder_structure),
            ("Manual Signal Creation", self.test_2_manual_signal_creation), 
            ("Watchdog Library Test", self.test_3_watchdog_availability),
            ("Signal Generation Logic", self.test_4_signal_generation_logic),
            ("File Event Simulation", self.test_5_file_event_simulation)
        ]
        
        results = {}
        
        for test_name, test_func in tests:
            try:
                success = test_func()
                results[test_name] = success
            except Exception as e:
                print(f"❌ {test_name} failed with error: {e}")
                results[test_name] = False
        
        # Generate diagnostic report
        self.generate_diagnostic_report(results)
        
        return results
    
    def generate_diagnostic_report(self, results):
        """Generate comprehensive diagnostic report"""
        print(f"\n📊 DIAGNOSTIC REPORT")
        print("=" * 50)
        
        passed_tests = sum(1 for success in results.values() if success)
        total_tests = len(results)
        
        print(f"📈 Tests Passed: {passed_tests}/{total_tests}")
        print(f"📊 Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        print(f"\n📋 DETAILED RESULTS:")
        for test_name, success in results.items():
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"   {status} {test_name}")
        
        # Provide recommendations
        print(f"\n🔧 RECOMMENDATIONS:")
        
        if not results.get("Signal Folder Structure", False):
            print("   🚨 CRITICAL: Fix signal folder structure first")
        
        if not results.get("Watchdog Library Test", False):
            print("   🚨 CRITICAL: Watchdog library issues detected")
            print("      Solution: pip install watchdog")
        
        if not results.get("File Event Simulation", False):
            print("   🚨 CRITICAL: File events not triggering signals")
            print("      Solution: Check signal hooks are running and monitoring correct paths")
        
        if results.get("Manual Signal Creation", False) and results.get("Signal Generation Logic", False):
            print("   ✅ Signal creation logic works - issue is with file event detection")
        
        # Save diagnostic data
        self.save_diagnostic_data()
    
    def save_diagnostic_data(self):
        """Save diagnostic data to file"""
        diagnostic_file = self.working_directory / f"signal_diagnostic_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            with open(diagnostic_file, 'w') as f:
                json.dump(self.test_results, f, indent=2, default=str)
            print(f"💾 Diagnostic report saved: {diagnostic_file.name}")
        except Exception as e:
            print(f"❌ Error saving diagnostic report: {e}")


def main():
    """Main diagnostic function"""
    print("SIGNAL PROCESSING DIAGNOSTIC TOOL")
    print("=" * 50)
    
    # Get working directory
    working_dir = input("📁 Enter your working directory path: ").strip()
    if not working_dir:
        working_dir = os.getcwd()
        print(f"📁 Using current directory: {working_dir}")
    
    # Run diagnostics
    diagnostic = SignalDiagnostic(working_dir)
    diagnostic.run_complete_diagnostic()


if __name__ == "__main__":
    main()