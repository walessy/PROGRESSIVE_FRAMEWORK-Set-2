#!/usr/bin/env python3
"""
Content Modification Signal Trigger
PURPOSE: Actually modify file content to guarantee signal generation
APPROACH: Add timestamp comments to trigger real file changes
"""

import os
import time
from pathlib import Path
from datetime import datetime

class ContentModificationTrigger:
    """Modify file content to guarantee signal generation"""
    
    def __init__(self, working_directory: str):
        self.working_directory = Path(working_directory)
        self.signals_folder = self.working_directory / "signals"
        self.modifications_made = 0
        self.signals_generated = 0
        
    def modify_file_content(self, file_path: Path):
        """Actually modify file content to trigger signals"""
        try:
            # Read current content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add timestamp comment at the end
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            modification_comment = f"\n<!-- Signal Trigger: {timestamp} -->\n"
            
            # Write back with modification
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content + modification_comment)
            
            self.modifications_made += 1
            print(f"  ✅ Modified: {file_path.name}")
            return True
            
        except Exception as e:
            print(f"  ❌ Error modifying {file_path.name}: {e}")
            return False
    
    def monitor_signal_generation(self, wait_seconds: int = 5):
        """Monitor for signal generation after modifications"""
        print(f"\n⏳ Waiting {wait_seconds} seconds for signal generation...")
        time.sleep(wait_seconds)
        
        if not self.signals_folder.exists():
            print("❌ Signals folder not found!")
            return 0
            
        total_signals = 0
        signal_subfolders = ["test_cases", "systems", "debug", "coordination"]
        
        print("📡 CHECKING SIGNAL GENERATION:")
        for subfolder in signal_subfolders:
            folder_path = self.signals_folder / subfolder
            if folder_path.exists():
                signals = list(folder_path.glob("*.signal"))
                folder_signals = len(signals)
                total_signals += folder_signals
                
                print(f"  📊 {subfolder}: {folder_signals} signals")
                
                # Show most recent signals
                if signals:
                    recent_signals = sorted(signals, key=lambda x: x.stat().st_mtime, reverse=True)[:2]
                    for signal_file in recent_signals:
                        mod_time = datetime.fromtimestamp(signal_file.stat().st_mtime)
                        print(f"    - {signal_file.name} ({mod_time.strftime('%H:%M:%S')})")
        
        self.signals_generated = total_signals
        print(f"\n📊 TOTAL SIGNALS: {total_signals}")
        return total_signals
    
    def test_single_file_modification(self):
        """Test modification of a single file to verify signal generation"""
        print("🧪 TESTING SINGLE FILE MODIFICATION")
        print("=" * 50)
        
        # Find a system specification file to test
        system_specs = list(self.working_directory.glob("**/PROGRESSIVEPROJECT-SYSTEM-*.md"))
        
        if not system_specs:
            print("❌ No system specification files found for testing")
            return False
            
        test_file = system_specs[0]
        print(f"📁 Testing with file: {test_file.name}")
        
        # Modify the file
        success = self.modify_file_content(test_file)
        
        if success:
            # Monitor for signal generation
            signals_generated = self.monitor_signal_generation(10)
            
            if signals_generated > 0:
                print("✅ SUCCESS: Signal generation confirmed!")
                return True
            else:
                print("❌ FAILURE: No signals generated")
                return False
        else:
            print("❌ FAILURE: Could not modify test file")
            return False
    
    def modify_all_system_files(self):
        """Modify all system specification files to trigger mass signal generation"""
        print("🚀 MODIFYING ALL SYSTEM SPECIFICATION FILES")
        print("=" * 50)
        
        # Find all system specification files
        system_files = []
        
        # System specifications
        system_specs = list(self.working_directory.glob("**/PROGRESSIVEPROJECT-SYSTEM-*.md"))
        system_files.extend(system_specs)
        
        # Configuration files
        config_files = list(self.working_directory.glob("**/*Config*.md"))
        system_files.extend(config_files)
        
        # Chat command files
        chat_files = list(self.working_directory.glob("**/*Chat*Commands*.md"))
        system_files.extend(chat_files)
        
        # Framework files
        framework_files = list(self.working_directory.glob("**/*Framework*.md"))
        system_files.extend(framework_files)
        
        # Remove duplicates
        system_files = list(set(system_files))
        
        print(f"📁 Found {len(system_files)} files to modify")
        
        if not system_files:
            print("❌ No files found to modify!")
            return
        
        # Modify files in batches
        batch_size = 5
        batches = [system_files[i:i + batch_size] for i in range(0, len(system_files), batch_size)]
        
        for batch_num, batch_files in enumerate(batches, 1):
            print(f"\n📦 BATCH {batch_num}/{len(batches)} - Modifying {len(batch_files)} files:")
            
            for file_path in batch_files:
                self.modify_file_content(file_path)
                time.sleep(0.5)  # Small delay between modifications
            
            # Check for signals after each batch
            print(f"⏳ Checking signals after batch {batch_num}...")
            signals_in_batch = self.monitor_signal_generation(3)
            
            if signals_in_batch > 0:
                print(f"✅ Batch {batch_num}: {signals_in_batch} signals generated!")
            else:
                print(f"⚠️ Batch {batch_num}: No signals detected yet")
        
        # Final signal check
        print("\n🔍 FINAL SIGNAL GENERATION CHECK:")
        final_signals = self.monitor_signal_generation(5)
        
        print(f"\n📊 FINAL RESULTS:")
        print(f"📁 Files Modified: {self.modifications_made}")
        print(f"📡 Signals Generated: {final_signals}")
        
        if final_signals > 0:
            print("🎉 SUCCESS: Signal-based processing is working!")
            signal_rate = (final_signals / max(self.modifications_made, 1)) * 100
            print(f"📈 Signal Generation Rate: {signal_rate:.1f}%")
        else:
            print("❌ ISSUE: No signals generated despite file modifications")
            print("🔧 Troubleshooting needed for signal detection system")


def main():
    """Main function to test and trigger signal generation"""
    print("CONTENT MODIFICATION SIGNAL TRIGGER")
    print("=" * 50)
    print("PURPOSE: Modify file content to guarantee signal generation")
    
    # Get working directory
    working_dir = input("📁 Enter your working directory path: ").strip()
    if not working_dir:
        working_dir = os.getcwd()
        print(f"📁 Using current directory: {working_dir}")
    
    # Initialize trigger
    trigger = ContentModificationTrigger(working_dir)
    
    # Ask user what to do
    print("\nOPTIONS:")
    print("1. Test single file modification (recommended first)")
    print("2. Modify all system files for mass signal generation")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        trigger.test_single_file_modification()
    elif choice == "2":
        trigger.modify_all_system_files()
    else:
        print("Invalid choice. Testing single file...")
        trigger.test_single_file_modification()


if __name__ == "__main__":
    main()