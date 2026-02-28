#!/usr/bin/env python3
"""
OMEGA COMPILER — Project Handoff Tool

Exports the clean project folder to Desktop for sharing.
With the new structure, project/ is already clean — this just copies it out.
"""

import os
import shutil

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONSTITUTION_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(CONSTITUTION_DIR)
USER_SPACE = os.path.join(ROOT_DIR, "USER SPACE")
PROJECT_DIR = os.path.join(USER_SPACE, "project")
DEV_WORK_DIR = os.path.join(USER_SPACE, "dev-work")
DESKTOP_DIR = os.path.expanduser("~/Desktop")


def get_project_info():
    """Try to read project info from dev-work/seed/PROJECT.md"""
    project_md = os.path.join(DEV_WORK_DIR, "seed", "PROJECT.md")
    info = {"name": "Project", "description": ""}

    if os.path.exists(project_md):
        try:
            with open(project_md, 'r', encoding='utf-8') as f:
                content = f.read()
                for line in content.split('\n'):
                    if 'project name' in line.lower() and ':' in line:
                        info["name"] = line.split(':', 1)[1].strip()
                        break
                    if line.startswith('# '):
                        info["name"] = line[2:].strip()
                        break
        except Exception:
            pass

    return info


def count_files(directory):
    """Count files in a directory recursively."""
    count = 0
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        count += len([f for f in files if not f.startswith('.')])
    return count


def export_project(export_path, include_docs=False):
    """Copy project folder to export location."""

    exported_files = []

    # Copy project folder
    if os.path.exists(PROJECT_DIR):
        for root, dirs, files in os.walk(PROJECT_DIR):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__' and d != 'node_modules']

            rel_root = os.path.relpath(root, PROJECT_DIR)

            if rel_root == '.':
                dest_dir = export_path
            else:
                dest_dir = os.path.join(export_path, rel_root)

            for f in files:
                if f.startswith('.') or f == '.DS_Store':
                    continue

                src = os.path.join(root, f)
                os.makedirs(dest_dir, exist_ok=True)
                dst = os.path.join(dest_dir, f)
                shutil.copy2(src, dst)
                exported_files.append(os.path.relpath(dst, export_path))

    # Optionally include docs from dev-work
    if include_docs:
        docs_dir = os.path.join(DEV_WORK_DIR, "docs")
        if os.path.exists(docs_dir):
            dest_docs = os.path.join(export_path, "docs")
            os.makedirs(dest_docs, exist_ok=True)
            for f in os.listdir(docs_dir):
                if f.endswith('.md') and not f.startswith('.'):
                    src = os.path.join(docs_dir, f)
                    dst = os.path.join(dest_docs, f)
                    shutil.copy2(src, dst)
                    exported_files.append(os.path.join("docs", f))

    return exported_files


def generate_readme(export_path, project_name):
    """Generate README if one doesn't exist."""

    readme_path = os.path.join(export_path, "README.md")

    # Don't overwrite existing README
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Skip if it's not the placeholder
            if "replace with your project" not in content.lower():
                return

    # Detect project type
    has_package = os.path.exists(os.path.join(export_path, "package.json"))
    has_requirements = os.path.exists(os.path.join(export_path, "requirements.txt"))

    if has_package:
        setup = "npm install"
        run = "npm run dev"
    elif has_requirements:
        setup = "pip install -r requirements.txt"
        run = "python main.py"
    else:
        setup = "# Add setup command"
        run = "# Add run command"

    readme = f"""# {project_name}

## Quick Start

```bash
{setup}
{run}
```

## Project Structure

```
{project_name}/
├── src/          Source code
├── tests/        Tests
├── public/       Static assets
└── docs/         Documentation
```

---

*Built with [Omega Constitution](https://github.com/edsworld27/omega-constitution)*
"""

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme)


def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║             📦 OMEGA COMPILER — PROJECT HANDOFF           ║
╠═══════════════════════════════════════════════════════════╣
║         Exports your clean project folder to Desktop      ║
╚═══════════════════════════════════════════════════════════╝
""")

    # Check project folder exists
    if not os.path.exists(PROJECT_DIR):
        print("❌ Error: project/ folder not found in USER SPACE.")
        print(f"   Expected: {PROJECT_DIR}")
        return

    # Count files
    file_count = count_files(PROJECT_DIR)
    if file_count == 0:
        print("⚠️  Warning: project/ folder is empty.")
        print("   Build your project first, then run the compiler.")
        return

    # Get project info
    info = get_project_info()

    print(f"📁 Found {file_count} files in project/")
    project_name = input(f"\nProject name [{info['name']}]: ").strip()
    if not project_name:
        project_name = info['name']

    # Ask about docs
    include_docs = input("Include dev docs (PRD, specs)? [y/N]: ").strip().lower() == 'y'

    # Create export path
    safe_name = "".join(c if c.isalnum() or c in '-_' else '_' for c in project_name)
    export_path = os.path.join(DESKTOP_DIR, safe_name)

    # Check exists
    if os.path.exists(export_path):
        print(f"\n⚠️  Folder exists: {export_path}")
        if input("Overwrite? [y/N]: ").strip().lower() != 'y':
            print("🛑 Aborted.")
            return
        shutil.rmtree(export_path)

    # Export
    print(f"\n📦 Exporting '{project_name}'...")
    os.makedirs(export_path)

    exported_files = export_project(export_path, include_docs)
    generate_readme(export_path, project_name)

    print(f"""
╔═══════════════════════════════════════════════════════════╗
║                     ✅ EXPORT COMPLETE                    ║
╠═══════════════════════════════════════════════════════════╣
║  Files: {len(exported_files):<4}                                            ║
║  Location: ~/Desktop/{safe_name:<35} ║
╚═══════════════════════════════════════════════════════════╝

📁 {export_path}

Ready to share!
""")


if __name__ == "__main__":
    main()
