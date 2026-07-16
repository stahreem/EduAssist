import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from translation.translator import translate_text

text = """
Artificial Intelligence is transforming education.
Machine learning helps computers learn from data.
"""

translated = translate_text(
    text,
    "Malayalam"
)

print("\nTranslated Text:\n")
print(translated)