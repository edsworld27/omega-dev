#!/usr/bin/env python3
"""
OMEGA INSTALLER - CLI Kit Installation Tool
Omega Constitution V14

Install kits from omega-store to your project's plug-and-play directory.

Usage:
    python omega_installer.py list                    # List available kits
    python omega_installer.py info <kit-name>         # Show kit details
    python omega_installer.py install <kit-name>      # Install a kit
    python omega_installer.py installed               # List installed kits

Examples:
    python omega_installer.py list
    python omega_installer.py install website
    python omega_installer.py info saas
"""

import os
import sys
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List

# Configuration
STORE_DIR = os.path.expanduser(
    os.getenv("OMEGA_STORE_DIR",
              "~/Documents/Omega Constitution Pack/Omega DEV Panel/06_Full_System/omega-store")
)
DEFAULT_PROJECT_DIR = os.path.expanduser(
    os.getenv("OMEGA_PROJECT_DIR",
              "~/Documents/Omega Constitution Pack/Omega System Public/Constution V13/USER SPACE")
)

KITS_DIR = os.path.join(STORE_DIR, "kits")
PLUG_AND_PLAY_DIR = os.path.join(DEFAULT_PROJECT_DIR, "dev-work/plug-and-play")


class OmegaInstaller:
    """Kit installation manager for Omega Constitution."""

    def __init__(self, store_dir: str = STORE_DIR, project_dir: str = DEFAULT_PROJECT_DIR):
        self.store_dir = os.path.expanduser(store_dir)
        self.project_dir = os.path.expanduser(project_dir)
        self.kits_dir = os.path.join(self.store_dir, "kits")
        self.plug_and_play_dir = os.path.join(self.project_dir, "dev-work/plug-and-play")

    def list_available_kits(self) -> List[Dict]:
        """List all available kits in the store."""
        kits = []

        if not os.path.exists(self.kits_dir):
            return kits

        for kit_name in os.listdir(self.kits_dir):
            kit_path = os.path.join(self.kits_dir, kit_name)

            # Skip non-directories and templates
            if not os.path.isdir(kit_path) or kit_name.startswith("_"):
                continue

            # Check for kit.config.md
            config_path = os.path.join(kit_path, "kit.config.md")
            if not os.path.exists(config_path):
                continue

            # Parse kit info
            kit_info = self._parse_kit_config(config_path)
            kit_info["name"] = kit_name
            kit_info["path"] = kit_path
            kits.append(kit_info)

        return kits

    def _parse_kit_config(self, config_path: str) -> Dict:
        """Parse kit.config.md for basic info."""
        info = {
            "description": "No description",
            "version": "unknown",
            "project_types": []
        }

        try:
            with open(config_path, 'r') as f:
                content = f.read()

            # Extract description (first non-header paragraph)
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip() and not line.startswith('#') and not line.startswith('-'):
                    info["description"] = line.strip()[:100]
                    break

            # Extract project types from activation rules
            if "project_types" in content.lower() or "activates for" in content.lower():
                for line in lines:
                    if "website" in line.lower():
                        info["project_types"].append("website")
                    if "web-app" in line.lower() or "webapp" in line.lower():
                        info["project_types"].append("web-app")
                    if "saas" in line.lower():
                        info["project_types"].append("saas")
                    if "api" in line.lower():
                        info["project_types"].append("api")

        except Exception:
            pass

        return info

    def get_kit_info(self, kit_name: str) -> Optional[Dict]:
        """Get detailed information about a specific kit."""
        kit_path = os.path.join(self.kits_dir, kit_name)

        if not os.path.exists(kit_path):
            return None

        info = {
            "name": kit_name,
            "path": kit_path,
            "files": [],
            "readme": None,
            "config": None,
            "prompter": None
        }

        # List files
        for f in os.listdir(kit_path):
            info["files"].append(f)

        # Read README if exists
        readme_path = os.path.join(kit_path, "README.md")
        if os.path.exists(readme_path):
            with open(readme_path, 'r') as f:
                info["readme"] = f.read()[:500] + "..." if len(f.read()) > 500 else f.read()
                f.seek(0)
                info["readme"] = f.read()[:500]

        # Read config
        config_path = os.path.join(kit_path, "kit.config.md")
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                info["config"] = f.read()[:1000]

        # Check for PROMPTER
        prompter_path = os.path.join(kit_path, "PROMPTER.md")
        info["has_prompter"] = os.path.exists(prompter_path)

        return info

    def install_kit(self, kit_name: str, target_dir: str = None) -> Dict:
        """Install a kit to the plug-and-play directory."""
        kit_path = os.path.join(self.kits_dir, kit_name)

        if not os.path.exists(kit_path):
            return {
                "success": False,
                "message": f"Kit '{kit_name}' not found in store"
            }

        # Determine target directory
        if target_dir:
            dest_dir = os.path.expanduser(target_dir)
        else:
            dest_dir = os.path.join(self.plug_and_play_dir, kit_name)

        # Check if already installed
        if os.path.exists(dest_dir):
            return {
                "success": False,
                "message": f"Kit '{kit_name}' already installed at {dest_dir}"
            }

        # Create plug-and-play directory if needed
        Path(self.plug_and_play_dir).mkdir(parents=True, exist_ok=True)

        # Copy kit
        try:
            shutil.copytree(kit_path, dest_dir)

            # Create installation manifest
            manifest = {
                "kit_name": kit_name,
                "installed_at": datetime.now().isoformat(),
                "source": kit_path,
                "destination": dest_dir
            }

            manifest_path = os.path.join(dest_dir, ".omega_install.json")
            with open(manifest_path, 'w') as f:
                json.dump(manifest, f, indent=2)

            return {
                "success": True,
                "message": f"Kit '{kit_name}' installed to {dest_dir}",
                "path": dest_dir,
                "files": os.listdir(dest_dir)
            }

        except Exception as e:
            return {
                "success": False,
                "message": f"Failed to install kit: {str(e)}"
            }

    def list_installed_kits(self) -> List[Dict]:
        """List all installed kits in plug-and-play."""
        installed = []

        if not os.path.exists(self.plug_and_play_dir):
            return installed

        for item in os.listdir(self.plug_and_play_dir):
            item_path = os.path.join(self.plug_and_play_dir, item)

            if not os.path.isdir(item_path):
                continue

            # Check for installation manifest
            manifest_path = os.path.join(item_path, ".omega_install.json")
            if os.path.exists(manifest_path):
                with open(manifest_path, 'r') as f:
                    manifest = json.load(f)
                manifest["current_path"] = item_path
                installed.append(manifest)
            else:
                # Legacy installation (no manifest)
                installed.append({
                    "kit_name": item,
                    "installed_at": "unknown",
                    "current_path": item_path,
                    "legacy": True
                })

        return installed

    def uninstall_kit(self, kit_name: str) -> Dict:
        """Remove an installed kit."""
        kit_path = os.path.join(self.plug_and_play_dir, kit_name)

        if not os.path.exists(kit_path):
            return {
                "success": False,
                "message": f"Kit '{kit_name}' not found in plug-and-play"
            }

        try:
            shutil.rmtree(kit_path)
            return {
                "success": True,
                "message": f"Kit '{kit_name}' uninstalled"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Failed to uninstall: {str(e)}"
            }


def format_kit_list(kits: List[Dict]) -> str:
    """Format kit list for display."""
    if not kits:
        return "No kits found."

    output = "\n  AVAILABLE KITS\n"
    output += "  " + "=" * 50 + "\n\n"

    for kit in kits:
        output += f"  {kit['name']}\n"
        output += f"    {kit.get('description', 'No description')}\n"
        if kit.get('project_types'):
            output += f"    Types: {', '.join(set(kit['project_types']))}\n"
        output += "\n"

    output += "  " + "-" * 50 + "\n"
    output += f"  Total: {len(kits)} kits\n"
    output += "  Install: python omega_installer.py install <kit-name>\n"

    return output


def format_kit_info(info: Dict) -> str:
    """Format kit info for display."""
    if not info:
        return "Kit not found."

    output = f"\n  KIT: {info['name']}\n"
    output += "  " + "=" * 50 + "\n\n"

    output += f"  Path: {info['path']}\n"
    output += f"  Has PROMPTER: {'Yes' if info.get('has_prompter') else 'No'}\n\n"

    output += "  Files:\n"
    for f in info.get('files', []):
        output += f"    - {f}\n"

    if info.get('config'):
        output += "\n  Configuration (excerpt):\n"
        output += "  " + "-" * 40 + "\n"
        for line in info['config'].split('\n')[:10]:
            output += f"  {line}\n"

    return output


def format_installed_list(kits: List[Dict]) -> str:
    """Format installed kit list."""
    if not kits:
        return "No kits installed in plug-and-play."

    output = "\n  INSTALLED KITS\n"
    output += "  " + "=" * 50 + "\n\n"

    for kit in kits:
        output += f"  {kit['kit_name']}\n"
        output += f"    Installed: {kit.get('installed_at', 'unknown')}\n"
        output += f"    Path: {kit.get('current_path', 'unknown')}\n"
        if kit.get('legacy'):
            output += "    (Legacy installation - no manifest)\n"
        output += "\n"

    return output


# CLI Interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Omega Kit Installer - Install kits from omega-store",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python omega_installer.py list                  # List available kits
  python omega_installer.py install website       # Install the website kit
  python omega_installer.py info saas             # Show SaaS kit details
  python omega_installer.py installed             # Show installed kits
  python omega_installer.py uninstall website     # Remove a kit
        """
    )

    parser.add_argument("command", choices=[
        "list", "info", "install", "installed", "uninstall"
    ], help="Command to execute")

    parser.add_argument("kit_name", nargs="?", help="Kit name for info/install/uninstall")
    parser.add_argument("--store", help="Path to omega-store directory")
    parser.add_argument("--project", help="Path to project USER SPACE directory")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")

    args = parser.parse_args()

    # Initialize installer
    store_dir = args.store if args.store else STORE_DIR
    project_dir = args.project if args.project else DEFAULT_PROJECT_DIR
    installer = OmegaInstaller(store_dir, project_dir)

    result = None

    if args.command == "list":
        kits = installer.list_available_kits()
        if args.json:
            print(json.dumps(kits, indent=2))
        else:
            print(format_kit_list(kits))

    elif args.command == "info":
        if not args.kit_name:
            parser.error("info requires a kit name")
        info = installer.get_kit_info(args.kit_name)
        if args.json:
            print(json.dumps(info, indent=2))
        else:
            print(format_kit_info(info))

    elif args.command == "install":
        if not args.kit_name:
            parser.error("install requires a kit name")
        result = installer.install_kit(args.kit_name)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(result["message"])

    elif args.command == "installed":
        kits = installer.list_installed_kits()
        if args.json:
            print(json.dumps(kits, indent=2))
        else:
            print(format_installed_list(kits))

    elif args.command == "uninstall":
        if not args.kit_name:
            parser.error("uninstall requires a kit name")
        result = installer.uninstall_kit(args.kit_name)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(result["message"])

    # Exit code
    if result and "success" in result:
        sys.exit(0 if result["success"] else 1)
    else:
        sys.exit(0)
