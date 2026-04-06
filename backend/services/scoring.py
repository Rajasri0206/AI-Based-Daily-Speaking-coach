def calculate_score(wpm: float, grammar_accuracy: float) -> dict:
    """
    Calculate fluency, grammar, and overall score
    """

    try:
        # 🎯 Ideal WPM range: 120–160
        ideal_wpm = 140

        # Fluency score based on distance from ideal
        fluency_score = max(0, 100 - abs(ideal_wpm - wpm))

        # Grammar score (already computed)
        grammar_score = grammar_accuracy

        # Overall weighted score
        overall_score = (0.6 * fluency_score) + (0.4 * grammar_score)

        return {
            "fluency_score": round(fluency_score, 2),
            "grammar_score": round(grammar_score, 2),
            "overall_score": round(overall_score, 2)
        }

    except Exception as e:
        raise Exception(f"Scoring Error: {str(e)}")