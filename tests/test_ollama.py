from summarization import summarize_text

sample_text = """
Artificial Intelligence is the simulation of human intelligence by machines.
Machine Learning is a subset of AI.
Deep Learning is a subset of Machine Learning.
"""

summary = summarize_text(sample_text)

print(summary)