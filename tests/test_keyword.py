# from keyword_extractor.keyword_extractor import extract_keywords

from keywords.keyword_extractor import extract_keywords

text = """
Artificial Intelligence and Machine Learning are transforming education.
Students can summarize notes and extract keywords using AI.
"""

keywords = extract_keywords(text)

print(keywords)