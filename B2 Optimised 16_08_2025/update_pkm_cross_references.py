#!/usr/bin/env python3
"""
FILENAME: update_pkm_cross_references.py
PKM Configuration Cross-Reference Update Script
Progressive Framework Set 2 - Automated Configuration Enhancement

Purpose: Automatically update existing PKM and Progressive Systems configuration files 
         to add proper cross-references for v5.1 session state management
Version: 5.1_state_aware
Author: Progressive Framework Development Team
Created: 2025-08-20

Working Directory: C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\

Updates:
✅ Adds cross-references to PKM-5Point-Protocol-v5.0.xml
✅ Adds PKM integration section to Progressive-Systems-Config-v2.3-SignalBased.json
✅ Creates PKM-5Point-Protocol-v5.1-StateAware.json with proper references
✅ Validates all cross-references work correctly
✅ Creates backup copies before making changes
"""

import os
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import shutil
from pathlib import Path

class PKMConfigUpdater:
    def __init__(self, working_directory):
        self.working_dir = Path(working_directory)
        self.backup_dir = self.working_dir / "config-backups" / f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # File paths
        self.pkm_xml_path = self.working_dir / "PKM-5Point-Protocol-v5.0.xml"
        self.progressive_json_path = self.working_dir / "Progressive-Systems-Config-v2.3-SignalBased.json"
        self.session_json_path = self.working_dir / "progressive-config" / "PKM-5Point-Protocol-v5.1-StateAware.json"
        
        print(f"🚀 PKM Configuration Cross-Reference Updater")
        print(f"📁 Working Directory: {self.working_dir}")
        print(f"💾 Backup Directory: {self.backup_dir}")
        
    def create_backups(self):
        """Create backup copies of existing configuration files"""
        print(f"\n💾 Creating backup copies...")
        
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        files_to_backup = [
            (self.pkm_xml_path, "PKM-5Point-Protocol-v5.0.xml"),
            (self.progressive_json_path, "Progressive-Systems-Config-v2.3-SignalBased.json")
        ]
        
        for source_path, filename in files_to_backup:
            if source_path.exists():
                backup_path = self.backup_dir / filename
                shutil.copy2(source_path, backup_path)
                print(f"   ✅ Backed up: {filename}")
            else:
                print(f"   ⚠️ File not found: {filename}")
        
        print(f"✅ Backups created in: {self.backup_dir}")
    
    def update_pkm_xml(self):
        """Update PKM-5Point-Protocol-v5.0.xml to reference v5.1 session state file"""
        print(f"\n📝 Updating PKM-5Point-Protocol-v5.0.xml...")
        
        if not self.pkm_xml_path.exists():
            print(f"❌ PKM XML file not found: {self.pkm_xml_path}")
            return False
        
        try:
            # Parse existing XML
            tree = ET.parse(self.pkm_xml_path)
            root = tree.getroot()
            
            # Check if EnhancedFeatures section already exists
            enhanced_features = root.find('EnhancedFeatures')
            if enhanced_features is not None:
                print(f"   ⚠️ EnhancedFeatures section already exists - skipping XML update")
                return True
            
            # Create EnhancedFeatures section
            enhanced_features = ET.SubElement(root, 'EnhancedFeatures')
            
            # Add SessionStateManagement section
            session_mgmt = ET.SubElement(enhanced_features, 'SessionStateManagement')
            
            config_file = ET.SubElement(session_mgmt, 'ConfigurationFile')
            config_file.text = "progressive-config/PKM-5Point-Protocol-v5.1-StateAware.json"
            
            description = ET.SubElement(session_mgmt, 'Description')
            description.text = "Enhanced session state management for chat numbering and initialization control"
            
            features = ET.SubElement(session_mgmt, 'Features')
            feature_list = [
                "Sequential chat numbering",
                "Conditional display modes", 
                "Session state persistence",
                "Redundancy elimination"
            ]
            
            for feature_text in feature_list:
                feature = ET.SubElement(features, 'Feature')
                feature.text = feature_text
            
            # Add ProgressiveSystemsIntegration section
            progressive_integration = ET.SubElement(enhanced_features, 'ProgressiveSystemsIntegration')
            
            progressive_config_file = ET.SubElement(progressive_integration, 'ConfigurationFile')
            progressive_config_file.text = "Progressive-Systems-Config-v2.3-SignalBased.json"
            
            progressive_description = ET.SubElement(progressive_integration, 'Description')
            progressive_description.text = "15-system Progressive Framework coordination"
            
            # Add VersionHistory section
            version_history = ET.SubElement(enhanced_features, 'VersionHistory')
            
            version_50 = ET.SubElement(version_history, 'Version', number="5.0")
            version_50.text = "Base PKM Protocol implementation"
            
            version_51 = ET.SubElement(version_history, 'Version', number="5.1")
            version_51.text = "Added session state management and conditional displays"
            
            # Write updated XML
            tree.write(self.pkm_xml_path, encoding='utf-8', xml_declaration=True)
            
            print(f"   ✅ Added EnhancedFeatures section with cross-references")
            print(f"   ✅ Referenced: PKM-5Point-Protocol-v5.1-StateAware.json")
            print(f"   ✅ Referenced: Progressive-Systems-Config-v2.3-SignalBased.json")
            return True
            
        except Exception as e:
            print(f"   ❌ Error updating PKM XML: {e}")
            return False
    
    def update_progressive_systems_json(self):
        """Update Progressive-Systems-Config-v2.3-SignalBased.json to reference PKM integration"""
        print(f"\n📝 Updating Progressive-Systems-Config-v2.3-SignalBased.json...")
        
        if not self.progressive_json_path.exists():
            print(f"❌ Progressive Systems JSON file not found: {self.progressive_json_path}")
            return False
        
        try:
            # Load existing JSON
            with open(self.progressive_json_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Check if PKM integration already exists
            if 'pkm_integration' in config:
                print(f"   ⚠️ PKM integration section already exists - skipping JSON update")
                return True
            
            # Add PKM integration section
            config['pkm_integration'] = {
                "version": "5.1_state_aware",
                "description": "PKM 5-Point Protocol session state management integration",
                "configuration_files": {
                    "base_protocol": "PKM-5Point-Protocol-v5.0.xml",
                    "session_state": "progressive-config/PKM-5Point-Protocol-v5.1-StateAware.json"
                },
                "features": {
                    "sequential_chat_numbering": True,
                    "conditional_display_modes": True,
                    "session_state_persistence": True,
                    "redundancy_elimination": True
                },
                "coordination": {
                    "with_15_systems": True,
                    "breathing_framework_integration": True,
                    "signal_based_architecture": True
                },
                "last_updated": datetime.now().isoformat()
            }
            
            # Write updated JSON
            with open(self.progressive_json_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print(f"   ✅ Added pkm_integration section")
            print(f"   ✅ Referenced: PKM-5Point-Protocol-v5.0.xml")
            print(f"   ✅ Referenced: PKM-5Point-Protocol-v5.1-StateAware.json")
            return True
            
        except Exception as e:
            print(f"   ❌ Error updating Progressive Systems JSON: {e}")
            return False
    
    def create_session_state_json(self):
        """Create PKM-5Point-Protocol-v5.1-StateAware.json with proper cross-references"""
        print(f"\n📝 Creating PKM-5Point-Protocol-v5.1-StateAware.json...")
        
        # Ensure progressive-config directory exists
        self.session_json_path.parent.mkdir(parents=True, exist_ok=True)
        
        if self.session_json_path.exists():
            print(f"   ⚠️ Session state JSON already exists - skipping creation")
            return True
        
        try:
            session_config = {
                "pkm_protocol": {
                    "version": "5.1_state_aware",
                    "description": "PKM 5-Point Protocol with session state management - Enhanced from v5.0",
                    "extends_configuration": "PKM-5Point-Protocol-v5.0.xml",
                    "integrates_with": "Progressive-Systems-Config-v2.3-SignalBased.json",
                    "working_directory": str(self.working_dir).replace('\\', '\\\\'),
                    
                    "session_management": {
                        "track_initialization": True,
                        "persistent_chat_numbering": True,
                        "conditional_display": True,
                        "state_persistence": "session_level"
                    },
                    
                    "chat_numbering": {
                        "format": "Chat{###}_ProgressiveProject_{timestamp}",
                        "increment_rule": "new_session_only",
                        "validation": "ensure_uniqueness_across_project",
                        "current_counter": 28,
                        "last_session_id": None
                    },
                    
                    "display_modes": {
                        "first_time": {
                            "template": "full_protocol",
                            "description": "Complete 15-system initialization display",
                            "trigger": "user_message == 'Hello' AND session_state.initialized == false"
                        },
                        "continuation": {
                            "template": "brief_status", 
                            "description": "Abbreviated status for ongoing sessions",
                            "trigger": "user_message == 'Hello' AND session_state.initialized == true"
                        },
                        "refresh": {
                            "template": "confirmation_only",
                            "description": "Status confirmation on request",
                            "trigger": "user_message contains 'PKM status' OR 'show full'"
                        },
                        "none": {
                            "template": "no_display",
                            "description": "Normal conversation, no PKM display",
                            "trigger": "default"
                        }
                    },
                    
                    "progressive_systems": {
                        "count": 15,
                        "source_configuration": "Progressive-Systems-Config-v2.3-SignalBased.json",
                        "foundation_tier": [
                            {"id": 1, "name": "PDT-PLUS", "value": "$57,400+/month"},
                            {"id": 2, "name": "PUXT-PLUS", "value": "$31,500/month"},
                            {"id": 3, "name": "PSO-PRIME", "value": "$74,800+/month"},
                            {"id": 4, "name": "PTT-DOCS-FUSION", "value": "$76,700+/month"},
                            {"id": 5, "name": "REQUIREMENTS-PRIME", "value": "$59,400+/month"}
                        ],
                        "professional_tier": [
                            {"id": 6, "name": "BUSINESS-OPS-FUSION", "value": "$87,300+/month"},
                            {"id": 7, "name": "CONTEXT-EVOLUTION-ENGINE", "value": "$38,600/month"},
                            {"id": 8, "name": "PERFORMANCE-AI-FUSION", "value": "$45,200/month"},
                            {"id": 9, "name": "SECURITY-BUILD-FUSION", "value": "$41,800/month"}
                        ],
                        "universal_tier": [
                            {"id": 10, "name": "KNOWLEDGE-EVOLUTION-ENGINE", "value": "$36,700/month"},
                            {"id": 11, "name": "UNIVERSAL-ORCHESTRATION-PRIME", "value": "$48,200/month"},
                            {"id": 12, "name": "PMCS-024", "value": "$67,300/month"},
                            {"id": 13, "name": "PAES", "value": "$52,700/month"}
                        ],
                        "integration_tier": [
                            {"id": 14, "name": "DPI", "value": "$25,000+/month"},
                            {"id": 15, "name": "PTODOS", "value": "$30,000+/month"}
                        ]
                    },
                    
                    "breathing_framework": {
                        "educational_triggers": 615,
                        "real_time_lessons": True,
                        "cross_system_coordination": True,
                        "signal_based_architecture": True,
                        "source_configuration": "Progressive-Systems-Config-v2.3-SignalBased.json"
                    },
                    
                    "debug_engines": {
                        "ATLAS": "Analytics & Learning - Pattern recognition + educational scenarios",
                        "PRISM": "Prevention & Risk - Risk management + educational prevention", 
                        "NEXUS": "Network & Execution - Coordination + educational management",
                        "CRUD": "Correction & Recovery - Solutions + educational automation"
                    },
                    
                    "total_business_value": "$800,000+/month",
                    "created": datetime.now().isoformat(),
                    "last_updated": datetime.now().isoformat()
                }
            }
            
            # Write session state JSON
            with open(self.session_json_path, 'w', encoding='utf-8') as f:
                json.dump(session_config, f, indent=2, ensure_ascii=False)
            
            print(f"   ✅ Created session state configuration file")
            print(f"   ✅ Added cross-references to PKM v5.0 XML and Progressive Systems v2.3 JSON")
            return True
            
        except Exception as e:
            print(f"   ❌ Error creating session state JSON: {e}")
            return False
    
    def validate_cross_references(self):
        """Validate that all configuration files properly reference each other"""
        print(f"\n🔍 Validating cross-references...")
        
        validation_results = {
            "pkm_xml_exists": self.pkm_xml_path.exists(),
            "progressive_json_exists": self.progressive_json_path.exists(),
            "session_json_exists": self.session_json_path.exists(),
            "xml_references_session": False,
            "json_references_pkm": False,
            "session_references_both": False
        }
        
        # Check PKM XML references
        if validation_results["pkm_xml_exists"]:
            try:
                tree = ET.parse(self.pkm_xml_path)
                root = tree.getroot()
                session_ref = root.find('.//SessionStateManagement/ConfigurationFile')
                if session_ref is not None and 'PKM-5Point-Protocol-v5.1-StateAware.json' in session_ref.text:
                    validation_results["xml_references_session"] = True
            except Exception:
                pass
        
        # Check Progressive Systems JSON references
        if validation_results["progressive_json_exists"]:
            try:
                with open(self.progressive_json_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                if 'pkm_integration' in config:
                    validation_results["json_references_pkm"] = True
            except Exception:
                pass
        
        # Check Session JSON references
        if validation_results["session_json_exists"]:
            try:
                with open(self.session_json_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                pkm_protocol = config.get('pkm_protocol', {})
                if ('extends_configuration' in pkm_protocol and 
                    'integrates_with' in pkm_protocol):
                    validation_results["session_references_both"] = True
            except Exception:
                pass
        
        # Report validation results
        print(f"   📁 File Existence:")
        print(f"      PKM XML: {'✅' if validation_results['pkm_xml_exists'] else '❌'}")
        print(f"      Progressive JSON: {'✅' if validation_results['progressive_json_exists'] else '❌'}")
        print(f"      Session JSON: {'✅' if validation_results['session_json_exists'] else '❌'}")
        
        print(f"   🔗 Cross-References:")
        print(f"      XML → Session: {'✅' if validation_results['xml_references_session'] else '❌'}")
        print(f"      Progressive → PKM: {'✅' if validation_results['json_references_pkm'] else '❌'}")
        print(f"      Session → Both: {'✅' if validation_results['session_references_both'] else '❌'}")
        
        all_valid = all(validation_results.values())
        print(f"\n{'🎉 All cross-references validated successfully!' if all_valid else '⚠️ Some cross-references missing or invalid'}")
        
        return validation_results
    
    def run_update(self):
        """Run the complete configuration update process"""
        print(f"\n🚀 Starting PKM Configuration Cross-Reference Update Process")
        print(f"=" * 70)
        
        # Step 1: Create backups
        self.create_backups()
        
        # Step 2: Update PKM XML
        xml_success = self.update_pkm_xml()
        
        # Step 3: Update Progressive Systems JSON
        json_success = self.update_progressive_systems_json()
        
        # Step 4: Create session state JSON
        session_success = self.create_session_state_json()
        
        # Step 5: Validate cross-references
        validation_results = self.validate_cross_references()
        
        # Summary
        print(f"\n📊 Update Summary:")
        print(f"=" * 30)
        print(f"   PKM XML Update: {'✅' if xml_success else '❌'}")
        print(f"   Progressive JSON Update: {'✅' if json_success else '❌'}")
        print(f"   Session JSON Creation: {'✅' if session_success else '❌'}")
        print(f"   Cross-Reference Validation: {'✅' if all(validation_results.values()) else '❌'}")
        
        if xml_success and json_success and session_success:
            print(f"\n🎉 PKM Configuration Update SUCCESSFUL!")
            print(f"   All files have been updated with proper cross-references")
            print(f"   Backup copies saved to: {self.backup_dir}")
            print(f"   Ready for PKM 5.1 session state management!")
        else:
            print(f"\n⚠️ PKM Configuration Update had issues")
            print(f"   Check error messages above for details")
            print(f"   Backup copies available in: {self.backup_dir}")

def main():
    """Main function to run the PKM configuration updater"""
    
    # Default working directory - update this path as needed
    working_directory = r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025"
    
    # Allow user to specify different directory
    if len(os.sys.argv) > 1:
        working_directory = os.sys.argv[1]
    
    # Create and run updater
    updater = PKMConfigUpdater(working_directory)
    updater.run_update()

if __name__ == "__main__":
    main()