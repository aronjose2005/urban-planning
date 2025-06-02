import pytest
from src.urban_planning import generate_urban_planning_recommendation

def test_generate_urban_planning_recommendation():
    feedback = {"sentiment": "positive", "score": 0.9, "text": "More green spaces needed"}
    recommendation = generate_urban_planning_recommendation(feedback)
    assert isinstance(recommendation, str)
    assert len(recommendation) > 0
