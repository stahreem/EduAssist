import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from translation.translator import translate_text

print(
    translate_text(
        "Artificial Intelligence is transforming education.",
        "Spanish"
    )
)