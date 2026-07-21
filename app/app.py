print("1")

import sys
from pathlib import Path

print("2")

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

print("3")

from ui.dashboard import run_dashboard

print("4")

run_dashboard()

print("5")