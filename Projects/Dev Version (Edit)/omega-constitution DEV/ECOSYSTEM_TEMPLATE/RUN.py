#!/usr/bin/env python3
"""
OMEGA SYSTEM - Quick Start
==========================

Run this to start the Omega System.

    python RUN.py           # Start
    python RUN.py --onboard # First-time setup
"""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "Omega Control" / "00 Rules" / "python" / "omega_run.py"

if __name__ == "__main__":
    subprocess.run([sys.executable, str(SCRIPT)] + sys.argv[1:])
