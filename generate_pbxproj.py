import os

def create_pbxproj():
    proj_dir = r"C:\Users\vasil\OneDrive\Рабочий стол\gemini lite\GeminiLite.xcodeproj"
    os.makedirs(proj_dir, exist_ok=True)
    
    workspace_dir = os.path.join(proj_dir, "project.xcworkspace")
    os.makedirs(workspace_dir, exist_ok=True)
    
    # Write contents.xcworkspacedata
    with open(os.path.join(workspace_dir, "contents.xcworkspacedata"), "w", encoding="utf-8") as f:
        f.write('''<?xml version="1.0" encoding="UTF-8"?>
<Workspace
   version = "1.0">
   <FileRef
      location = "self:">
   </FileRef>
</Workspace>
''')

    # Files to include in compilation
    sources = [
        ("GeminiLiteApp.swift", "GeminiLite/App/GeminiLiteApp.swift"),
        ("ChatMessage.swift", "GeminiLite/Models/ChatMessage.swift"),
        ("AppSettings.swift", "GeminiLite/Models/AppSettings.swift"),
        ("GeminiAPI.swift", "GeminiLite/Models/GeminiAPI.swift"),
        ("GeminiService.swift", "GeminiLite/Services/GeminiService.swift"),
        ("SlateTheme.swift", "GeminiLite/Theme/SlateTheme.swift"),
        ("ChatView.swift", "GeminiLite/Views/ChatView.swift"),
        ("MessageBubbleView.swift", "GeminiLite/Views/MessageBubbleView.swift"),
        ("SettingsView.swift", "GeminiLite/Views/SettingsView.swift"),
        ("ImagePicker.swift", "GeminiLite/Views/ImagePicker.swift"),
        ("QuickPromptBar.swift", "GeminiLite/Views/QuickPromptBar.swift"),
    ]
    
    resources = [
        ("Assets.xcassets", "GeminiLite/Assets.xcassets", "folder"),
    ]
    
    # ID generator with deterministic IDs based on index
    def id_file(i): return f"F000000000000000000000{i:02X}"
    def id_build(i): return f"B000000000000000000000{i:02X}"
    
    id_infoplist = "F00000000000000000000099"
    id_res_assets_file = "F00000000000000000000080"
    id_res_assets_build = "B00000000000000000000080"

    # Groups
    id_main_group = "000000000000000000000001"
    id_geminilite_group = "000000000000000000000002"
    id_app_group = "000000000000000000000003"
    id_models_group = "000000000000000000000004"
    id_services_group = "000000000000000000000005"
    id_theme_group = "000000000000000000000006"
    id_views_group = "000000000000000000000007"
    id_products_group = "000000000000000000000008"
    
    # Products
    id_product_app = "P000000000000000000000001"
    
    # Phases
    id_sources_phase = "100000000000000000000001"
    id_frameworks_phase = "100000000000000000000002"
    id_resources_phase = "100000000000000000000003"
    
    # Target & Project
    id_target = "200000000000000000000001"
    id_project = "300000000000000000000001"
    
    # Configs
    id_conf_debug = "C00000000000000000000001"
    id_conf_release = "C00000000000000000000002"
    id_conf_list_proj = "C00000000000000000000003"
    id_conf_target_debug = "C00000000000000000000004"
    id_conf_target_release = "C00000000000000000000005"
    id_conf_list_target = "C00000000000000000000006"

    lines = []
    lines.append("// !$*UTF8*$!")
    lines.append("{")
    lines.append("\tarchiveVersion = 1;")
    lines.append("\tclasses = {")
    lines.append("\t};")
    lines.append("\tobjectVersion = 54;")
    lines.append("\tobjects = {")
    lines.append("")
    
    # PBXBuildFile
    lines.append("/* Begin PBXBuildFile section */")
    for i, (name, path) in enumerate(sources):
        lines.append(f"\t\t{id_build(i)} /* {name} in Sources */ = {{isa = PBXBuildFile; fileRef = {id_file(i)} /* {name} */; }};")
    lines.append(f"\t\t{id_res_assets_build} /* Assets.xcassets in Resources */ = {{isa = PBXBuildFile; fileRef = {id_res_assets_file} /* Assets.xcassets */; }};")
    lines.append("/* End PBXBuildFile section */")
    lines.append("")

    # PBXFileReference
    lines.append("/* Begin PBXFileReference section */")
    lines.append(f"\t\t{id_product_app} /* GeminiLite.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = GeminiLite.app; sourceTree = BUILT_PRODUCTS_DIR; }};")
    for i, (name, path) in enumerate(sources):
        fname = os.path.basename(path)
        lines.append(f"\t\t{id_file(i)} /* {fname} */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = {fname}; sourceTree = \"<group>\"; }};")
    lines.append(f"\t\t{id_res_assets_file} /* Assets.xcassets */ = {{isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = \"<group>\"; }};")
    lines.append(f"\t\t{id_infoplist} /* Info.plist */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = \"<group>\"; }};")
    lines.append("/* End PBXFileReference section */")
    lines.append("")

    # PBXFrameworksBuildPhase
    lines.append("/* Begin PBXFrameworksBuildPhase section */")
    lines.append(f"\t\t{id_frameworks_phase} /* Frameworks */ = {{")
    lines.append("\t\t\tisa = PBXFrameworksBuildPhase;")
    lines.append("\t\t\tbuildActionMask = 2147483647;")
    lines.append("\t\t\tfiles = (")
    lines.append("\t\t\t);")
    lines.append("\t\t\trunOnlyForDeploymentPostprocessing = 0;")
    lines.append("\t\t};")
    lines.append("/* End PBXFrameworksBuildPhase section */")
    lines.append("")

    # PBXGroup
    lines.append("/* Begin PBXGroup section */")
    lines.append(f"\t\t{id_main_group} = {{")
    lines.append("\t\t\tisa = PBXGroup;")
    lines.append("\t\t\tchildren = (")
    lines.append(f"\t\t\t\t{id_geminilite_group} /* GeminiLite */,")
    lines.append(f"\t\t\t\t{id_products_group} /* Products */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tsourceTree = \"<group>\";")
    lines.append("\t\t};")
    
    lines.append(f"\t\t{id_products_group} /* Products */ = {{")
    lines.append("\t\t\tisa = PBXGroup;")
    lines.append("\t\t\tchildren = (")
    lines.append(f"\t\t\t\t{id_product_app} /* GeminiLite.app */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tname = Products;")
    lines.append("\t\t\tsourceTree = \"<group>\";")
    lines.append("\t\t};")

    lines.append(f"\t\t{id_geminilite_group} /* GeminiLite */ = {{")
    lines.append("\t\t\tisa = PBXGroup;")
    lines.append("\t\t\tchildren = (")
    lines.append(f"\t\t\t\t{id_app_group} /* App */,")
    lines.append(f"\t\t\t\t{id_models_group} /* Models */,")
    lines.append(f"\t\t\t\t{id_services_group} /* Services */,")
    lines.append(f"\t\t\t\t{id_theme_group} /* Theme */,")
    lines.append(f"\t\t\t\t{id_views_group} /* Views */,")
    lines.append(f"\t\t\t\t{id_res_assets_file} /* Assets.xcassets */,")
    lines.append(f"\t\t\t\t{id_infoplist} /* Info.plist */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tpath = GeminiLite;")
    lines.append("\t\t\tsourceTree = \"<group>\";")
    lines.append("\t\t};")

    # Subgroups
    lines.append(f"\t\t{id_app_group} /* App */ = {{")
    lines.append("\t\t\tisa = PBXGroup;")
    lines.append("\t\t\tchildren = (")
    lines.append(f"\t\t\t\t{id_file(0)} /* GeminiLiteApp.swift */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tpath = App;")
    lines.append("\t\t\tsourceTree = \"<group>\";")
    lines.append("\t\t};")

    lines.append(f"\t\t{id_models_group} /* Models */ = {{")
    lines.append("\t\t\tisa = PBXGroup;")
    lines.append("\t\t\tchildren = (")
    lines.append(f"\t\t\t\t{id_file(1)} /* ChatMessage.swift */,")
    lines.append(f"\t\t\t\t{id_file(2)} /* AppSettings.swift */,")
    lines.append(f"\t\t\t\t{id_file(3)} /* GeminiAPI.swift */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tpath = Models;")
    lines.append("\t\t\tsourceTree = \"<group>\";")
    lines.append("\t\t};")

    lines.append(f"\t\t{id_services_group} /* Services */ = {{")
    lines.append("\t\t\tisa = PBXGroup;")
    lines.append("\t\t\tchildren = (")
    lines.append(f"\t\t\t\t{id_file(4)} /* GeminiService.swift */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tpath = Services;")
    lines.append("\t\t\tsourceTree = \"<group>\";")
    lines.append("\t\t};")

    lines.append(f"\t\t{id_theme_group} /* Theme */ = {{")
    lines.append("\t\t\tisa = PBXGroup;")
    lines.append("\t\t\tchildren = (")
    lines.append(f"\t\t\t\t{id_file(5)} /* SlateTheme.swift */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tpath = Theme;")
    lines.append("\t\t\tsourceTree = \"<group>\";")
    lines.append("\t\t};")

    lines.append(f"\t\t{id_views_group} /* Views */ = {{")
    lines.append("\t\t\tisa = PBXGroup;")
    lines.append("\t\t\tchildren = (")
    lines.append(f"\t\t\t\t{id_file(6)} /* ChatView.swift */,")
    lines.append(f"\t\t\t\t{id_file(7)} /* MessageBubbleView.swift */,")
    lines.append(f"\t\t\t\t{id_file(8)} /* SettingsView.swift */,")
    lines.append(f"\t\t\t\t{id_file(9)} /* ImagePicker.swift */,")
    lines.append(f"\t\t\t\t{id_file(10)} /* QuickPromptBar.swift */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tpath = Views;")
    lines.append("\t\t\tsourceTree = \"<group>\";")
    lines.append("\t\t};")
    lines.append("/* End PBXGroup section */")
    lines.append("")

    # PBXNativeTarget
    lines.append("/* Begin PBXNativeTarget section */")
    lines.append(f"\t\t{id_target} /* GeminiLite */ = {{")
    lines.append("\t\t\tisa = PBXNativeTarget;")
    lines.append(f"\t\t\tbuildConfigurationList = {id_conf_list_target} /* Build configuration list for PBXNativeTarget \"GeminiLite\" */;")
    lines.append("\t\t\tbuildPhases = (")
    lines.append(f"\t\t\t\t{id_sources_phase} /* Sources */,")
    lines.append(f"\t\t\t\t{id_frameworks_phase} /* Frameworks */,")
    lines.append(f"\t\t\t\t{id_resources_phase} /* Resources */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tbuildRules = (")
    lines.append("\t\t\t);")
    lines.append("\t\t\tdependencies = (")
    lines.append("\t\t\t);")
    lines.append("\t\t\tname = GeminiLite;")
    lines.append(f"\t\t\tproductName = GeminiLite;")
    lines.append(f"\t\t\tproductReference = {id_product_app} /* GeminiLite.app */;")
    lines.append("\t\t\tproductType = \"com.apple.product-type.application\";")
    lines.append("\t\t};")
    lines.append("/* End PBXNativeTarget section */")
    lines.append("")

    # PBXProject
    lines.append("/* Begin PBXProject section */")
    lines.append(f"\t\t{id_project} /* Project object */ = {{")
    lines.append("\t\t\tisa = PBXProject;")
    lines.append("\t\t\tattributes = {")
    lines.append("\t\t\t\tBuildIndependentTargetsInParallel = 1;")
    lines.append("\t\t\t\tLastSwiftUpdateCheck = 1500;")
    lines.append("\t\t\t\tLastUpgradeCheck = 1500;")
    lines.append("\t\t\t\tTargetAttributes = {")
    lines.append(f"\t\t\t\t\t{id_target} = {{")
    lines.append("\t\t\t\t\t\tCreatedOnToolsVersion = 15.0;")
    lines.append("\t\t\t\t\t};")
    lines.append("\t\t\t\t};")
    lines.append("\t\t\t};")
    lines.append(f"\t\t\tbuildConfigurationList = {id_conf_list_proj} /* Build configuration list for PBXProject \"GeminiLite\" */;")
    lines.append("\t\t\tcompatibilityVersion = \"Xcode 14.0\";")
    lines.append("\t\t\tdevelopmentRegion = ru;")
    lines.append("\t\t\thasScannedForEncodings = 0;")
    lines.append("\t\t\tknownRegions = (")
    lines.append("\t\t\t\tru,")
    lines.append("\t\t\t\tBase,")
    lines.append("\t\t\t);")
    lines.append(f"\t\t\tmainGroup = {id_main_group};")
    lines.append(f"\t\t\tproductRefGroup = {id_products_group} /* Products */;")
    lines.append("\t\t\tprojectDirPath = \"\";")
    lines.append("\t\t\tprojectRoot = \"\";")
    lines.append("\t\t\ttargets = (")
    lines.append(f"\t\t\t\t{id_target} /* GeminiLite */,")
    lines.append("\t\t\t);")
    lines.append("\t\t};")
    lines.append("/* End PBXProject section */")
    lines.append("")

    # PBXResourcesBuildPhase
    lines.append("/* Begin PBXResourcesBuildPhase section */")
    lines.append(f"\t\t{id_resources_phase} /* Resources */ = {{")
    lines.append("\t\t\tisa = PBXResourcesBuildPhase;")
    lines.append("\t\t\tbuildActionMask = 2147483647;")
    lines.append("\t\t\tfiles = (")
    lines.append(f"\t\t\t\t{id_res_assets_build} /* Assets.xcassets in Resources */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\trunOnlyForDeploymentPostprocessing = 0;")
    lines.append("\t\t};")
    lines.append("/* End PBXResourcesBuildPhase section */")
    lines.append("")

    # PBXSourcesBuildPhase
    lines.append("/* Begin PBXSourcesBuildPhase section */")
    lines.append(f"\t\t{id_sources_phase} /* Sources */ = {{")
    lines.append("\t\t\tisa = PBXSourcesBuildPhase;")
    lines.append("\t\t\tbuildActionMask = 2147483647;")
    lines.append("\t\t\tfiles = (")
    for i, (name, path) in enumerate(sources):
        lines.append(f"\t\t\t\t{id_build(i)} /* {name} in Sources */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\trunOnlyForDeploymentPostprocessing = 0;")
    lines.append("\t\t};")
    lines.append("/* End PBXSourcesBuildPhase section */")
    lines.append("")

    # XCBuildConfiguration
    lines.append("/* Begin XCBuildConfiguration section */")
    # Proj Debug
    lines.append(f"\t\t{id_conf_debug} /* Debug */ = {{")
    lines.append("\t\t\tisa = XCBuildConfiguration;")
    lines.append("\t\t\tbuildSettings = {")
    lines.append("\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;")
    lines.append("\t\t\t\tCLANG_ANALYZER_NONNULL = YES;")
    lines.append("\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = \"gnu++20\";")
    lines.append("\t\t\t\tCLANG_ENABLE_MODULES = YES;")
    lines.append("\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;")
    lines.append("\t\t\t\tCOPY_PHASE_STRIP = NO;")
    lines.append("\t\t\t\tDEBUG_INFORMATION_FORMAT = dwarf;")
    lines.append("\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;")
    lines.append("\t\t\t\tENABLE_TESTABILITY = YES;")
    lines.append("\t\t\t\tGCC_DYNAMIC_NO_PIC = NO;")
    lines.append("\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;")
    lines.append("\t\t\t\tGCC_OPTIMIZATION_LEVEL = 0;")
    lines.append("\t\t\t\tGCC_PREPROCESSOR_DEFINITIONS = (")
    lines.append("\t\t\t\t\t\"DEBUG=1\",")
    lines.append("\t\t\t\t\t\"$(inherited)\",")
    lines.append("\t\t\t\t);")
    lines.append("\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 15.0;")
    lines.append("\t\t\t\tMTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;")
    lines.append("\t\t\t\tONLY_ACTIVE_ARCH = YES;")
    lines.append("\t\t\t\tSDKROOT = iphoneos;")
    lines.append("\t\t\t\tSWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;")
    lines.append("\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = \"-Onone\";")
    lines.append("\t\t\t};")
    lines.append("\t\t\tname = Debug;")
    lines.append("\t\t};")

    # Proj Release
    lines.append(f"\t\t{id_conf_release} /* Release */ = {{")
    lines.append("\t\t\tisa = XCBuildConfiguration;")
    lines.append("\t\t\tbuildSettings = {")
    lines.append("\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;")
    lines.append("\t\t\t\tCLANG_ANALYZER_NONNULL = YES;")
    lines.append("\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = \"gnu++20\";")
    lines.append("\t\t\t\tCLANG_ENABLE_MODULES = YES;")
    lines.append("\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;")
    lines.append("\t\t\t\tCOPY_PHASE_STRIP = NO;")
    lines.append("\t\t\t\tDEBUG_INFORMATION_FORMAT = \"dwarf-with-dsym\";")
    lines.append("\t\t\t\tENABLE_NS_ASSERTIONS = NO;")
    lines.append("\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;")
    lines.append("\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;")
    lines.append("\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 15.0;")
    lines.append("\t\t\t\tMTL_ENABLE_DEBUG_INFO = NO;")
    lines.append("\t\t\t\tSDKROOT = iphoneos;")
    lines.append("\t\t\t\tSWIFT_COMPILATION_MODE = \"wholemodule\";")
    lines.append("\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = \"-O\";")
    lines.append("\t\t\t\tVALIDATE_PRODUCT = YES;")
    lines.append("\t\t\t};")
    lines.append("\t\t\tname = Release;")
    lines.append("\t\t};")

    # Target Debug
    lines.append(f"\t\t{id_conf_target_debug} /* Debug */ = {{")
    lines.append("\t\t\tisa = XCBuildConfiguration;")
    lines.append("\t\t\tbuildSettings = {")
    lines.append("\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;")
    lines.append("\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;")
    lines.append("\t\t\t\tCODE_SIGN_STYLE = Automatic;")
    lines.append("\t\t\t\tCURRENT_PROJECT_VERSION = 1;")
    lines.append("\t\t\t\tGENERATE_INFOPLIST_FILE = NO;")
    lines.append("\t\t\t\tINFOPLIST_FILE = GeminiLite/Info.plist;")
    lines.append("\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 15.0;")
    lines.append("\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (")
    lines.append("\t\t\t\t\t\"$(inherited)\",")
    lines.append("\t\t\t\t\t\"@executable_path/Frameworks\",")
    lines.append("\t\t\t\t);")
    lines.append("\t\t\t\tMARKETING_VERSION = 1.0.0;")
    lines.append("\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.vasil.geminilite;")
    lines.append("\t\t\t\tPRODUCT_NAME = \"$(TARGET_NAME)\";")
    lines.append("\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;")
    lines.append("\t\t\t\tSWIFT_VERSION = 5.0;")
    lines.append("\t\t\t\tTARGETED_DEVICE_FAMILY = \"1\";") # 1 = iPhone
    lines.append("\t\t\t};")
    lines.append("\t\t\tname = Debug;")
    lines.append("\t\t};")

    # Target Release
    lines.append(f"\t\t{id_conf_target_release} /* Release */ = {{")
    lines.append("\t\t\tisa = XCBuildConfiguration;")
    lines.append("\t\t\tbuildSettings = {")
    lines.append("\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;")
    lines.append("\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;")
    lines.append("\t\t\t\tCODE_SIGN_STYLE = Automatic;")
    lines.append("\t\t\t\tCURRENT_PROJECT_VERSION = 1;")
    lines.append("\t\t\t\tGENERATE_INFOPLIST_FILE = NO;")
    lines.append("\t\t\t\tINFOPLIST_FILE = GeminiLite/Info.plist;")
    lines.append("\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 15.0;")
    lines.append("\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (")
    lines.append("\t\t\t\t\t\"$(inherited)\",")
    lines.append("\t\t\t\t\t\"@executable_path/Frameworks\",")
    lines.append("\t\t\t\t);")
    lines.append("\t\t\t\tMARKETING_VERSION = 1.0.0;")
    lines.append("\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.vasil.geminilite;")
    lines.append("\t\t\t\tPRODUCT_NAME = \"$(TARGET_NAME)\";")
    lines.append("\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;")
    lines.append("\t\t\t\tSWIFT_VERSION = 5.0;")
    lines.append("\t\t\t\tTARGETED_DEVICE_FAMILY = \"1\";")
    lines.append("\t\t\t};")
    lines.append("\t\t\tname = Release;")
    lines.append("\t\t};")
    lines.append("/* End XCBuildConfiguration section */")
    lines.append("")

    # XCConfigurationList
    lines.append("/* Begin XCConfigurationList section */")
    lines.append(f"\t\t{id_conf_list_proj} /* Build configuration list for PBXProject \"GeminiLite\" */ = {{")
    lines.append("\t\t\tisa = XCConfigurationList;")
    lines.append("\t\t\tbuildConfigurations = (")
    lines.append(f"\t\t\t\t{id_conf_debug} /* Debug */,")
    lines.append(f"\t\t\t\t{id_conf_release} /* Release */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tdefaultConfigurationIsVisible = 0;")
    lines.append("\t\t\tdefaultConfigurationName = Release;")
    lines.append("\t\t};")

    lines.append(f"\t\t{id_conf_list_target} /* Build configuration list for PBXNativeTarget \"GeminiLite\" */ = {{")
    lines.append("\t\t\tisa = XCConfigurationList;")
    lines.append("\t\t\tbuildConfigurations = (")
    lines.append(f"\t\t\t\t{id_conf_target_debug} /* Debug */,")
    lines.append(f"\t\t\t\t{id_conf_target_release} /* Release */,")
    lines.append("\t\t\t);")
    lines.append("\t\t\tdefaultConfigurationIsVisible = 0;")
    lines.append("\t\t\tdefaultConfigurationName = Release;")
    lines.append("\t\t};")
    lines.append("/* End XCConfigurationList section */")
    lines.append("")

    lines.append("\t};")
    lines.append(f"\trootObject = {id_project} /* Project object */;")
    lines.append("}")
    
    with open(os.path.join(proj_dir, "project.pbxproj"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
        
    print("Successfully generated GeminiLite.xcodeproj/project.pbxproj!")

if __name__ == "__main__":
    create_pbxproj()
