from evaluation.evaluator import evaluate_summary

original = """
Artificial Intelligence is transforming education.
Machine Learning helps computers learn from data.
Deep Learning is a subset of Machine Learning.
Natural Language Processing helps computers understand language.
"""

summary = """
Artificial Intelligence is transforming education.
Machine Learning helps computers learn from data.
Natural Language Processing helps computers understand language.
"""

results = evaluate_summary(original, summary)

print("\n===== EduAssist Evaluation =====\n")

for key, value in results.items():

    if key == "llm_evaluation":
        print("\nLLM Evaluation")
        print("-" * 40)
        print(value)

    else:
        print(f"{key}: {value}")