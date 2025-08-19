#!/usr/bin/env python3
"""
Quick fix for signals directory structure
SAVE AS: signals_fix.py
"""

import os
import json
from pathlib import Path
from datetime import datetime

def fix_signals_directory():
    """Fix the signals directory structure"""
    
    base_dir = Path.cwd()
    signals_dir = base_dir / "signals"
    
    print("🔧 FIXING SIGNALS DIRECTORY STRUCTURE")
    print(f"📁 Signals Directory: {signals_dir}")
    
    # Create lessons subfolder
    lessons_signals_dir = signals_dir / "lessons"
    lessons_signals_dir.mkdir(exist_ok=True)
    print(f"✅ Created: {lessons_signals_dir}")
    
    # Create README in lessons subfolder
    readme_path = lessons_signals_dir / "README.md"
    readme_content = """# Lessons Signals

Signals for lesson file modifications and updates.

## Signal File Format
Signal files follow the pattern: `lesson_{event_type}_{timestamp}.signal`

## Processing
These signals are processed by the breathing framework monitoring system.
"""
    readme_path.write_text(readme_content, encoding='utf-8')
    print(f"✅ Created README: {readme_path}")
    
    # Test signal generation
    test_signal_path = lessons_signals_dir / f"test_signal_{datetime.now().strftime('%H%M%S')}.signal"
    
    signal_content = {
        "event_type": "lesson_modified",
        "timestamp": datetime.now().isoformat(),
        "source": "signals_fix_tool",
        "lesson_file": "test_lesson.md",
        "modification_type": "directory_fix_test",
        "details": "Testing signal generation after directory fix"
    }
    
    try:
        test_signal_path.write_text(json.dumps(signal_content, indent=2), encoding='utf-8')
        print(f"✅ Test signal created: {test_signal_path.name}")
        
        # Verify signal exists
        if test_signal_path.exists():
            print(f"✅ Signal file verified: {test_signal_path.stat().st_size} bytes")
            print("✅ SIGNALS DIRECTORY FIX SUCCESSFUL!")
            return True
        else:
            print("❌ Signal file verification failed")
            return False
            
    except Exception as e:
        print(f"❌ Signal generation failed: {e}")
        return False

if __name__ == "__main__":
    fix_signals_directory()
    print("\n🚀 Now try running the diagnostic again:")
    print("python breathing_framework_diagnostic.py")