import pytest
from src.feedback_analysis import analyze_feedback

def test_analyze_feedback():
    feedback_text = "We need more parks"
    analysis = analyze_feedback(feedback_text)
    assert "sentiment" in analysis
    assert "score" in analysis
    assert analysis["text"] == feedback_text
