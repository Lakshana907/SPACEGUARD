from app.risk_engine import assess_risk

def test_close_approach_scores_higher():
    assert assess_risk(.2, 12)["score"] > assess_risk(20, 2)["score"]
def test_score_is_bounded():
    assert 0 <= assess_risk(0, 100)["score"] <= 100
def test_explanation_present():
    result = assess_risk(1, 10)
    assert result["level"] in {"CRITICAL","HIGH","MEDIUM","LOW"}
    assert result["factors"] and result["action"]
