import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from flashcards.flashcard_generator import generate_flashcards
from flashcards.parser import parse_flashcards


sample = """
Artificial Intelligence is transforming education.
Machine learning enables computers to learn from data.
Deep learning is a subset of machine learning.
Natural Language Processing helps computers understand human language.
"""

raw = generate_flashcards(sample)

cards = parse_flashcards(raw)

print("\nGenerated Flashcards:\n")
print(type(cards))
print(cards)

for i, card in enumerate(cards, 1):
    print(f"{i}.")
    print("Q:", card["question"])
    print("A:", card["answer"])
    print("-" * 40)