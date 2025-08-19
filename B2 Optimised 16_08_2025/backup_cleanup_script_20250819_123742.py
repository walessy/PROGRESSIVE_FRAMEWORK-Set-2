#!/usr/bin/env python3
"""
Automated Backup File Cleanup - Generated 2025-08-19 12:37:42
Removes only files confirmed as safe to remove.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

def cleanup_backup_files():
    base_dir = Path(r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025")
    cleanup_backup_dir = base_dir / "removed_backups"
    cleanup_backup_dir.mkdir(exist_ok=True)
    
    print("🧹 BACKUP FILE CLEANUP STARTING")
    print(f"📁 Backup directory: {cleanup_backup_dir}")
    print("🔒 Only removing files confirmed as safe")
    
    # Files confirmed as safe to remove
    safe_files = [
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\SIMPLE USER GUIDE\1 PROGRESSIVE_FRAMEWORK-Set-2  QUICK START GUIDE.md.backup_20250818_141129.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\Chat004_Directory-Lister-Script_20250818_143500.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\8 breathing_framework_automation.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\SIMPLE USER GUIDE\2 PKM PROGRESSIVE.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\2 pmcs_024_filename_correction_report_20250818_142338.md.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\3 PKM 5-Point Protocol XML Configuration.txt.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Templates\Evolutionary-Lesson-Template-Foundation.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\evolutionary_mapping_engine.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\cross_system_inheritance_engine.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\4 Optimized Progressive Systems Configuration JSON v4.0.txt.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\5 missing_files_fix.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\PDT-PLUS\First-5-PDT-PLUS-Evolutionary-Lessons-Proof-of-Concept.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\KNOWLEDGE-EVOLUTION-ENGINE_LESSON_20250818_162938_backup_044255.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\REQUIREMENTS-PRIME_LESSON_20250818_165411_backup_044219.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\CONTEXT-EVOLUTION-ENGINE_LESSON_20250818_165624_backup_044033.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\SECURITY-BUILD-FUSION\SECURITY-BUILD-FUSION_LESSON_20250818_165624.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PUXT-PLUS\PUXT-PLUS_LESSON_20250818_165826.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PAES\PAES_LESSON_20250818_165957.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\DPI\DPI_LESSON_20250818_170356.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PTODOS\PTODOS_LESSON_20250818_170356.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\DPI\DPI_LESSON_20250818_170452.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PDT-PLUS\PDT-PLUS_LESSON_20250818_170623.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\UNIVERSAL-ORCHESTRATION-PRIME\UNIVERSAL-ORCHESTRATION-PRIME_LESSON_20250818_170643.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PAES\PAES_LESSON_20250818_170647.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PUXT-PLUS\PUXT-PLUS_LESSON_20250818_171914.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PSO-PRIME\PSO-PRIME_LESSON_20250818_172055.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\REQUIREMENTS-PRIME_LESSON_20250818_172318_backup_043812.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\CONTEXT-EVOLUTION-ENGINE_LESSON_20250818_172549_backup_043923.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\DPI\DPI_LESSON_20250818_173355.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\PTODOS_LESSON_20250818_173456_backup_043847.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\PUXT-PLUS_LESSON_20250818_182515_backup_044108.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\PSO-PRIME_LESSON_20250818_182550_backup_043736.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\PERFORMANCE-AI-FUSION_LESSON_20250818_182845_backup_044144.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\DPI\DPI_LESSON_20250818_183217.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PSO-PRIME\PSO-PRIME_LESSON_20250818_200836.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\REQUIREMENTS-PRIME\REQUIREMENTS-PRIME_LESSON_20250818_200836.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\robustness_test_backups\BUSINESS-OPS-FUSION_LESSON_20250818_200836_backup_043958.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PERFORMANCE-AI-FUSION\PERFORMANCE-AI-FUSION_LESSON_20250818_200836.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\UNIVERSAL-ORCHESTRATION-PRIME\UNIVERSAL-ORCHESTRATION-PRIME_LESSON_20250818_200836.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PMCS-024\PMCS-024_LESSON_20250818_200836.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\DPI\DPI_LESSON_20250818_200836.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PDT-PLUS\PDT-PLUS_LESSON_20250818_201302.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\signal_validation_report_20250818_231341.json.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\11 615+ Test-to-Lesson Evolutionary Mapping Engine.md.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\10 15 Chat Startup Commands - 615+ Test-to-Lesson Evolutionary Mapping.md.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PTT-DOCS-FUSION\PTT-DOCS-FUSION_LESSON_20250818_162938.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PTT-DOCS-FUSION\PTT-DOCS-FUSION_LESSON_20250818_165333.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PTT-DOCS-FUSION\PTT-DOCS-FUSION_LESSON_20250818_165455.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PTT-DOCS-FUSION\PTT-DOCS-FUSION_LESSON_20250818_170629.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PTT-DOCS-FUSION\PTT-DOCS-FUSION_LESSON_20250818_172207.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PTT-DOCS-FUSION\PTT-DOCS-FUSION_LESSON_20250818_182625.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\PTT-DOCS-FUSION\PTT-DOCS-FUSION_LESSON_20250818_200836.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\signal_diagnostic_tool.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\signal_performance_validator.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\System_Specs\Education_Platform\Progressive-Framework-Academy-Complete-Specification.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\PKM 5-Point Protocol XML Configuration.txt.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\specification_evolution_report_20250819_042241.json.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\runtime_ideas_evolution_deployment.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\robustness_tester.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Active\REQUIREMENTS-PRIME\REQUIREMENTS-PRIME_LESSON_20250818_165411.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\robustness_test_report_20250819_044325.txt.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\signals_fix.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\lesson_monitor.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\7 evolutionary_mapping_update_report_20250818_160215.md.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\File_Header_Specification_v2.1_SignalBased.md.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\deployment_validation_checklist.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Lessons\Lessons-Index.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\Runtime_Ideas_Evolution_Architecture.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\Signal_Generation_Layer_v1.1_Implementation.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\SIMPLE USER GUIDE\1 PROGRESSIVE_FRAMEWORK-Set-2  QUICK START GUIDE.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\System Logic Testing Framework\Chat004_Framework-Set-2-Implementation-Roadmap_20250818_143500.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\System Logic Testing Framework\Chat004_Unified-Testing-Strategy-Framework-Set-2_20250818_143500.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Templates\Student-Progress-Protection-Template.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part2_template_generation_fix.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part2_template_generation_fix_corrected.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part2_clean.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part2_minimal.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\6 evolutionary_update_master.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\9 automated_lesson_triggers.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\batch_test_signal_trigger.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_diagnostic.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_header_manager.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part1_existing_files_header_fix.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\reathing_framework_diagnostic.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\signal_hooks_implementation.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\spec_evolution_automation.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_config_20250819_055926.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_integrator.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_integration_report_20250819_061054.md.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_integrator_fixed.py.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_integration_report_20250819_061743.md.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Logs\breathing_framework_integration_20250819_061743.log.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\universal_file_header_verification.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\universal_header_verification_report_20250819_062332.md.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Logs\universal_header_verification_20250819_062332.log.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\universal_file_header_verification_fixed.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\universal_header_verification_report_20250819_062710.md.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Logs\universal_header_verification_20250819_062709.log.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\batch_test_processing_report_20250818_232525.json.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part1_existing_files_header_report_20250819_053049.json.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\signal_validation_report_20250818_231312.json.backup.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\automated_header_applicator_phase3.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\automated_header_applicator.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\10 15 Chat Startup Commands - 615+ Test-to-Lesson Evolutionary Mapping.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\11 615+ Test-to-Lesson Evolutionary Mapping Engine.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\2 pmcs_024_filename_correction_report_20250818_142338.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\3 PKM 5-Point Protocol XML Configuration.txt.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\4 Optimized Progressive Systems Configuration JSON v4.0.txt.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\5 missing_files_fix.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\6 evolutionary_update_master.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\7 evolutionary_mapping_update_report_20250818_160215.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\8 breathing_framework_automation.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\9 automated_lesson_triggers.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\batch_test_processing_report_20250818_232525.json.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\batch_test_signal_trigger.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_config_20250819_055926.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_diagnostic.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_header_manager.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_integration_report_20250819_061054.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_integration_report_20250819_061743.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_integrator.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\breathing_framework_integrator_fixed.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\File_Header_Specification_v2.1_SignalBased.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part1_existing_files_header_fix.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part1_existing_files_header_report_20250819_053049.json.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part2_minimal.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part2_template_generation_fix.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part2_template_generation_fix_corrected.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\PKM 5-Point Protocol XML Configuration.txt.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\reathing_framework_diagnostic.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\robustness_test_report_20250819_044325.txt.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\signal_validation_report_20250818_231312.json.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\specification_evolution_report_20250819_042241.json.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\universal_header_verification_report_20250819_062332.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\universal_header_verification_report_20250819_062710.md.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\part2_clean.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\Chat004_Directory-Lister-Script_20250818_143500.py.backup.backup",
        r"C:\Users\Wales\OneDrive\Desktop\PROGRESSIVE_FRAMEWORK-Set-2\B2 Optimised 16_08_2025\Scripts\signal_validation_report_20250818_231341.json.backup.backup",
    ]
    
    removed_count = 0
    total_size_mb = 0
    
    for file_path_str in safe_files:
        file_path = Path(file_path_str)
        if file_path.exists():
            try:
                # Get file size before removal
                file_size = file_path.stat().st_size
                total_size_mb += file_size / (1024 * 1024)
                
                # Create backup copy before removal
                backup_name = f"{file_path.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                backup_path = cleanup_backup_dir / backup_name
                shutil.copy2(file_path, backup_path)
                
                # Remove original
                file_path.unlink()
                print(f"✅ Removed: {file_path.name}")
                removed_count += 1
                
            except Exception as e:
                print(f"❌ Error removing {file_path.name}: {e}")
    
    print(f"🎯 Cleanup complete:")
    print(f"   Files removed: {removed_count}")
    print(f"   Space freed: {total_size_mb:.1f} MB")
    print(f"   Backups saved: {cleanup_backup_dir}")

if __name__ == "__main__":
    print("🧹 PROGRESSIVE FRAMEWORK BACKUP CLEANUP")
    print("This will remove backup files confirmed as safe to remove.")
    print("All removed files will be backed up before deletion.")
    print("")
    confirm = input("Type 'YES' to proceed with backup cleanup: ")
    if confirm == 'YES':
        cleanup_backup_files()
    else:
        print("Cleanup cancelled.")
