#!/usr/bin/env python3
"""
Recursive File and Folder Lister
Lists all folders, subfolders, and files recursively with detailed information
"""

import os
from pathlib import Path
from datetime import datetime
import json

class RecursiveFileLister:
    def __init__(self, base_directory: str):
        self.base_directory = Path(base_directory)
        self.file_count = 0
        self.folder_count = 0
        self.total_size = 0
        
    def get_file_size_readable(self, size_bytes: int) -> str:
        """Convert bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def list_directory_contents(self, directory: Path, level: int = 0) -> list:
        """Recursively list directory contents with tree structure"""
        items = []
        indent = "  " * level
        
        try:
            # Get all items in directory
            directory_items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
            
            for item in directory_items:
                if item.is_file():
                    self.file_count += 1
                    file_size = item.stat().st_size
                    self.total_size += file_size
                    file_info = {
                        "type": "file",
                        "name": item.name,
                        "path": str(item.relative_to(self.base_directory)),
                        "size": file_size,
                        "size_readable": self.get_file_size_readable(file_size),
                        "extension": item.suffix,
                        "level": level
                    }
                    items.append(file_info)
                    print(f"{indent}📄 {item.name} ({self.get_file_size_readable(file_size)})")
                    
                elif item.is_dir():
                    self.folder_count += 1
                    folder_info = {
                        "type": "folder",
                        "name": item.name,
                        "path": str(item.relative_to(self.base_directory)),
                        "level": level
                    }
                    items.append(folder_info)
                    print(f"{indent}📁 {item.name}/")
                    
                    # Recursively list subdirectory contents
                    sub_items = self.list_directory_contents(item, level + 1)
                    items.extend(sub_items)
                    
        except PermissionError:
            print(f"{indent}❌ Permission denied: {directory}")
        except Exception as e:
            print(f"{indent}❌ Error accessing {directory}: {e}")
            
        return items
    
    def find_files_by_pattern(self, pattern: str) -> list:
        """Find files matching a specific pattern"""
        matching_files = []
        for file_path in self.base_directory.rglob(pattern):
            if file_path.is_file():
                matching_files.append({
                    "name": file_path.name,
                    "path": str(file_path.relative_to(self.base_directory)),
                    "full_path": str(file_path),
                    "size": file_path.stat().st_size
                })
        return matching_files
    
    def analyze_file_types(self, items: list) -> dict:
        """Analyze file types and extensions"""
        extension_counts = {}
        file_items = [item for item in items if item["type"] == "file"]
        
        for item in file_items:
            ext = item["extension"].lower() if item["extension"] else "no_extension"
            extension_counts[ext] = extension_counts.get(ext, 0) + 1
            
        return extension_counts
    
    def search_for_system_files(self) -> dict:
        """Search specifically for Progressive Framework system files"""
        system_files = {
            "markdown_files": self.find_files_by_pattern("*.md"),
            "json_files": self.find_files_by_pattern("*.json"),
            "xml_files": self.find_files_by_pattern("*.xml"),
            "progressive_files": [],
            "system_files": [],
            "pmcs_files": []
        }
        
        # Search for specific patterns
        all_files = system_files["markdown_files"] + system_files["json_files"] + system_files["xml_files"]
        
        for file_info in all_files:
            filename = file_info["name"].lower()
            
            if "progressive" in filename:
                system_files["progressive_files"].append(file_info)
            if "system" in filename:
                system_files["system_files"].append(file_info)
            if "pmcs" in filename:
                system_files["pmcs_files"].append(file_info)
                
        return system_files
    
    def generate_comprehensive_report(self, items: list) -> str:
        """Generate a comprehensive directory report"""
        extension_analysis = self.analyze_file_types(items)
        system_files = self.search_for_system_files()
        
        report = f"""
# 📁 COMPREHENSIVE DIRECTORY ANALYSIS

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Base Directory**: {self.base_directory}
**Total Folders**: {self.folder_count}
**Total Files**: {self.file_count}
**Total Size**: {self.get_file_size_readable(self.total_size)}

## 📊 FILE TYPE ANALYSIS

"""
        
        for ext, count in sorted(extension_analysis.items(), key=lambda x: x[1], reverse=True):
            report += f"**{ext}**: {count} files\n"
        
        report += f"""

## 🔍 PROGRESSIVE FRAMEWORK FILES FOUND

### Markdown Files ({len(system_files['markdown_files'])})
"""
        for file_info in system_files["markdown_files"]:
            report += f"- {file_info['path']} ({self.get_file_size_readable(file_info['size'])})\n"
        
        report += f"""

### JSON Configuration Files ({len(system_files['json_files'])})
"""
        for file_info in system_files["json_files"]:
            report += f"- {file_info['path']} ({self.get_file_size_readable(file_info['size'])})\n"
        
        report += f"""

### XML Configuration Files ({len(system_files['xml_files'])})
"""
        for file_info in system_files["xml_files"]:
            report += f"- {file_info['path']} ({self.get_file_size_readable(file_info['size'])})\n"
        
        report += f"""

## 🎯 PROGRESSIVE SYSTEM FILES

### Files with "Progressive" in name ({len(system_files['progressive_files'])})
"""
        for file_info in system_files["progressive_files"]:
            report += f"- {file_info['path']}\n"
        
        report += f"""

### Files with "System" in name ({len(system_files['system_files'])})
"""
        for file_info in system_files["system_files"]:
            report += f"- {file_info['path']}\n"
        
        report += f"""

### Files with "PMCS" in name ({len(system_files['pmcs_files'])})
"""
        for file_info in system_files["pmcs_files"]:
            report += f"- {file_info['path']}\n"
        
        return report
    
    def run_complete_analysis(self, save_json: bool = True, save_report: bool = True):
        """Run complete directory analysis"""
        print(f"🔍 Starting comprehensive directory analysis...")
        print(f"📁 Base Directory: {self.base_directory}")
        print(f"📊 Scanning all folders and files recursively...\n")
        
        # List all contents
        all_items = self.list_directory_contents(self.base_directory)
        
        print(f"\n📊 SUMMARY:")
        print(f"📁 Total Folders: {self.folder_count}")
        print(f"📄 Total Files: {self.file_count}")
        print(f"💾 Total Size: {self.get_file_size_readable(self.total_size)}")
        
        # Generate comprehensive report
        if save_report:
            report = self.generate_comprehensive_report(all_items)
            report_path = self.base_directory / "Directory-Analysis-Report.md"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"📋 Report saved: {report_path}")
        
        # Save JSON data
        if save_json:
            json_data = {
                "analysis_timestamp": datetime.now().isoformat(),
                "base_directory": str(self.base_directory),
                "summary": {
                    "total_folders": self.folder_count,
                    "total_files": self.file_count,
                    "total_size_bytes": self.total_size,
                    "total_size_readable": self.get_file_size_readable(self.total_size)
                },
                "all_items": all_items
            }
            
            json_path = self.base_directory / "directory_analysis.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2)
            print(f"💾 JSON data saved: {json_path}")
        
        # Search for Progressive Framework files
        system_files = self.search_for_system_files()
        print(f"\n🎯 PROGRESSIVE FRAMEWORK FILES FOUND:")
        print(f"📄 Markdown files: {len(system_files['markdown_files'])}")
        print(f"⚙️  JSON files: {len(system_files['json_files'])}")
        print(f"🔧 XML files: {len(system_files['xml_files'])}")
        print(f"🔍 'Progressive' files: {len(system_files['progressive_files'])}")
        print(f"🔍 'System' files: {len(system_files['system_files'])}")
        print(f"🔍 'PMCS' files: {len(system_files['pmcs_files'])}")

# Usage Example
if __name__ == "__main__":
    # Replace with your actual working directory
    working_dir = r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025"
    
    lister = RecursiveFileLister(working_dir)
    lister.run_complete_analysis()
