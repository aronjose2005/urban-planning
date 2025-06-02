from urban_planning import generate_urban_planning_recommendation
from feedback_analysis import fetch_community_feedback, analyze_feedback

def main():
    # Fetch and analyze community feedback
    feedback_text = fetch_community_feedback()
    print(f"Community Feedback: {feedback_text}")
    feedback_analysis = analyze_feedback(feedback_text)
    print(f"Feedback Analysis: {feedback_analysis}")

    # Generate urban planning recommendation
    recommendation = generate_urban_planning_recommendation(feedback_analysis)
    print(f"Urban Planning Recommendation: {recommendation}")

if __name__ == "__main__":
    main()
