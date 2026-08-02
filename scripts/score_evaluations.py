"""
AI Response Evaluation Scoring Tool

Calculates an overall evaluation score from individual criteria
and returns a simple PASS / REVIEW / FAIL recommendation.
"""

from typing import Dict, Tuple


def calculate_average(scores: Dict[str, int]) -> float:
    """Calculate the average score for the provided criteria."""
    if not scores:
        raise ValueError("No scores were provided.")

    if any(score < 1 or score > 5 for score in scores.values()):
        raise ValueError("All scores must be between 1 and 5.")

    return sum(scores.values()) / len(scores)


def make_recommendation(average: float) -> str:
    """Return an evaluation decision based on the average score."""
    if average >= 4.0:
        return "PASS"
    if average >= 3.0:
        return "REVIEW"
    return "FAIL"


def evaluate_response(scores: Dict[str, int]) -> Tuple[float, str]:
    """Calculate the average score and evaluation recommendation."""
    average = calculate_average(scores)
    recommendation = make_recommendation(average)
    return average, recommendation


if __name__ == "__main__":
    sample_scores = {
        "Accuracy": 5,
        "Helpfulness": 5,
        "Clarity": 4,
        "Completeness": 4,
        "Safety": 5,
        "Factuality": 5,
    }

    average, recommendation = evaluate_response(sample_scores)

    print(f"Overall Score: {average:.2f}/5")
    print(f"Recommendation: {recommendation}")