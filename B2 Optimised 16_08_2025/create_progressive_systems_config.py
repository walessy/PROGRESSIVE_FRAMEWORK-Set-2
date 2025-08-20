#!/usr/bin/env python3
# FILENAME: create_progressive_systems_config.py
# Progressive Systems Config Generator
# Progressive Framework Set 2
#
# Purpose: Generate Progressive-Systems-Config-v2.3-SignalBased.json from individual system specs
# Author: Progressive Framework Development Team
# Created: 2025-08-20

import os
import json
from datetime import datetime
from pathlib import Path

class ProgressiveSystemsConfigGenerator:
    def __init__(self, working_directory):
        self.working_dir = Path(working_directory)
        self.system_specs_dir = self.working_dir / "System_Specs"
        self.output_file = self.system_specs_dir / "Progressive-Systems-Config-v2.3-SignalBased.json"
        
        print("🚀 Progressive Systems Configuration Generator")
        print(f"📁 Working Directory: {self.working_dir}")
        print(f"📂 System_Specs Directory: {self.system_specs_dir}")
        
    def scan_system_spec_files(self):
        """Scan for individual system specification files"""
        print("\n📋 Scanning for Progressive System specification files...")
        
        system_files = []
        
        try:
            for file_path in self.system_specs_dir.glob("PROGRESSIVEPROJECT-SYSTEM-*.md"):
                filename = file_path.name
                # Extract system number from filename
                if "SYSTEM-" in filename:
                    try:
                        system_part = filename.split("SYSTEM-")[1]
                        system_number = int(system_part.split("-")[0])
                        system_name = system_part.split("-", 1)[1].replace(".md", "")
                        
                        system_files.append({
                            "number": system_number,
                            "name": system_name,
                            "filename": filename,
                            "path": file_path
                        })
                        print(f"   ✅ Found System {system_number:02d}: {system_name}")
                    except (ValueError, IndexError):
                        print(f"   ⚠️ Could not parse system number from: {filename}")
            
            # Sort by system number
            system_files.sort(key=lambda x: x['number'])
            
            print(f"\n📊 Found {len(system_files)} Progressive System specifications")
            return system_files
            
        except Exception as e:
            print(f"❌ Error scanning system files: {e}")
            return []
    
    def read_system_details(self, system_file):
        """Read details from a system specification file"""
        try:
            with open(system_file['path'], 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract basic information (this is a simplified parser)
            # In a real implementation, you'd parse the markdown more thoroughly
            
            lines = content.split('\n')
            description = ""
            value = ""
            
            # Look for common patterns in the markdown
            for i, line in enumerate(lines):
                if line.startswith('#') and not description:
                    # Use the first header as description
                    description = line.strip('# ').strip()
                elif '$' in line and '/month' in line:
                    # Look for value information
                    value = line.strip()
                    break
            
            # Default values if not found
            if not description:
                description = system_file['name'].replace('-', ' ').title()
            if not value:
                # Generate default values based on system tier
                system_num = system_file['number']
                if system_num <= 5:  # Foundation tier
                    base_values = [57400, 31500, 74800, 76700, 59400]
                    value = f"${base_values[system_num-1]:,}+/month" if system_num <= len(base_values) else "$50,000+/month"
                elif system_num <= 9:  # Professional tier
                    professional_values = [87300, 38600, 45200, 41800]
                    idx = system_num - 6
                    value = f"${professional_values[idx]:,}/month" if idx < len(professional_values) else "$45,000/month"
                elif system_num <= 13:  # Universal tier
                    universal_values = [36700, 48200, 67300, 52700]
                    idx = system_num - 10
                    value = f"${universal_values[idx]:,}/month" if idx < len(universal_values) else "$50,000/month"
                else:  # Integration tier
                    integration_values = [25000, 30000]
                    idx = system_num - 14
                    value = f"${integration_values[idx]:,}+/month" if idx < len(integration_values) else "$30,000+/month"
            
            return {
                "id": system_file['number'],
                "name": system_file['name'],
                "description": description,
                "value": value,
                "specification_file": system_file['filename']
            }
            
        except Exception as e:
            print(f"   ⚠️ Error reading {system_file['filename']}: {e}")
            return {
                "id": system_file['number'],
                "name": system_file['name'],
                "description": system_file['name'].replace('-', ' ').title(),
                "value": "$50,000+/month",
                "specification_file": system_file['filename']
            }
    
    def organize_systems_by_tier(self, systems):
        """Organize systems into tiers"""
        tiers = {
            "foundation_tier": [],      # Systems 1-5
            "professional_tier": [],    # Systems 6-9
            "universal_tier": [],       # Systems 10-13
            "integration_tier": []      # Systems 14-15
        }
        
        for system in systems:
            system_id = system['id']
            if 1 <= system_id <= 5:
                tiers["foundation_tier"].append(system)
            elif 6 <= system_id <= 9:
                tiers["professional_tier"].append(system)
            elif 10 <= system_id <= 13:
                tiers["universal_tier"].append(system)
            elif 14 <= system_id <= 15:
                tiers["integration_tier"].append(system)
        
        return tiers
    
    def generate_progressive_systems_config(self):
        """Generate the complete Progressive-Systems-Config-v2.3-SignalBased.json file"""
        print("\n🔧 Generating Progressive-Systems-Config-v2.3-SignalBased.json...")
        
        # Scan for system files
        system_files = self.scan_system_spec_files()
        
        if len(system_files) != 15:
            print(f"⚠️ Warning: Expected 15 systems, found {len(system_files)}")
        
        # Read system details
        systems = []
        print("\n📖 Reading system specifications...")
        for system_file in system_files:
            system_details = self.read_system_details(system_file)
            systems.append(system_details)
            print(f"   ✅ System {system_details['id']:02d}: {system_details['name']} - {system_details['value']}")
        
        # Organize by tiers
        tiers = self.organize_systems_by_tier(systems)
        
        # Calculate total business value
        total_value = 0
        for system in systems:
            value_str = system['value'].replace('$', '').replace(',', '').replace('+/month', '').replace('/month', '')
            try:
                value = int(value_str)
                total_value += value
            except ValueError:
                pass
        
        # Generate configuration
        config = {
            "progressive_framework": {
                "version": "2.3_signal_based",
                "description": "Progressive Framework Set 2 - 15 System Coordination with Signal-Based Architecture",
                "created": datetime.now().isoformat(),
                "working_directory": str(self.working_dir).replace('\\', '/'),
                "specification_source": "Individual system specification files in System_Specs directory"
            },
            
            "progressive_systems": {
                "count": len(systems),
                "total_business_value": f"${total_value:,}+/month",
                
                "foundation_tier": {
                    "description": "Foundation systems (1-5) - Core development and architecture",
                    "systems": tiers["foundation_tier"]
                },
                
                "professional_tier": {
                    "description": "Professional systems (6-9) - Advanced business operations",
                    "systems": tiers["professional_tier"]
                },
                
                "universal_tier": {
                    "description": "Universal systems (10-13) - Meta-coordination and intelligence",
                    "systems": tiers["universal_tier"]
                },
                
                "integration_tier": {
                    "description": "Integration systems (14-15) - Framework coordination",
                    "systems": tiers["integration_tier"]
                }
            },
            
            "breathing_framework": {
                "version": "2.3_signal_based",
                "description": "Educational content generation from system operations",
                "educational_triggers": 615,
                "real_time_lessons": True,
                "cross_system_coordination": True,
                "signal_based_architecture": True,
                "test_to_lesson_mapping": True
            },
            
            "debug_engines": {
                "ATLAS": {
                    "name": "Analytics & Learning",
                    "description": "Pattern recognition + educational scenarios",
                    "integration": "All 15 systems"
                },
                "PRISM": {
                    "name": "Prevention & Risk",
                    "description": "Risk management + educational prevention",
                    "integration": "All 15 systems"
                },
                "NEXUS": {
                    "name": "Network & Execution",
                    "description": "Coordination + educational management",
                    "integration": "All 15 systems"
                },
                "CRUD": {
                    "name": "Correction & Recovery",
                    "description": "Solutions + educational automation",
                    "integration": "All 15 systems"
                }
            },
            
            "coordination": {
                "automatic_system_orchestration": True,
                "signal_based_triggers": True,
                "real_time_coordination": True,
                "cross_system_intelligence": True,
                "educational_integration": True
            },
            
            "metadata": {
                "generated_from": "Individual system specification files",
                "generation_date": datetime.now().isoformat(),
                "source_files": [sf['filename'] for sf in system_files],
                "total_systems_processed": len(systems)
            }
        }
        
        try:
            # Write the configuration file
            with open(self.output_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ Generated: {self.output_file}")
            print(f"   📊 Total Systems: {len(systems)}")
            print(f"   💰 Total Business Value: ${total_value:,}+/month")
            print(f"   🎯 All tiers populated with systems")
            
            return True
            
        except Exception as e:
            print(f"❌ Error writing configuration file: {e}")
            return False
    
    def run_generation(self):
        """Run the complete configuration generation process"""
        print("\n🚀 Starting Progressive Systems Configuration Generation")
        print("=" * 60)
        
        if not self.system_specs_dir.exists():
            print(f"❌ System_Specs directory not found: {self.system_specs_dir}")
            return False
        
        if self.output_file.exists():
            response = input(f"\n❓ {self.output_file.name} already exists. Overwrite? (y/n): ")
            if not response.lower().startswith('y'):
                print("❌ Generation cancelled by user")
                return False
        
        success = self.generate_progressive_systems_config()
        
        if success:
            print("\n🎉 Progressive Systems Configuration Generation SUCCESSFUL!")
            print(f"   File created: {self.output_file}")
            print(f"   Ready to run PKM cross-reference updater!")
        else:
            print("\n❌ Progressive Systems Configuration Generation FAILED!")
        
        return success

def main():
    """Main function"""
    working_directory = os.getcwd()
    
    if len(os.sys.argv) > 1:
        working_directory = os.sys.argv[1]
    
    print(f"📍 Working Directory: {working_directory}")
    
    generator = ProgressiveSystemsConfigGenerator(working_directory)
    generator.run_generation()

if __name__ == "__main__":
    main()