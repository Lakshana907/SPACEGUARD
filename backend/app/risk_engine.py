def assess_risk(separation_km: float, relative_speed_kms: float) -> dict:
    # Transparent heuristic for a synthetic demo, not a collision probability.
    sep = max(0.0, min(1.0, (10.0 - separation_km) / 10.0))
    speed = max(0.0, min(1.0, relative_speed_kms / 15.0))
    score = round(100 * (0.72 * sep + 0.28 * speed))
    level = "CRITICAL" if score >= 85 else "HIGH" if score >= 70 else "MEDIUM" if score >= 40 else "LOW"
    factors = []
    factors.append("Very low predicted separation" if separation_km < 1 else "Low predicted separation" if separation_km < 5 else "Moderate separation" if separation_km < 10 else "Separation above demo thresholds")
    factors.append("High relative velocity" if relative_speed_kms >= 10 else "Moderate relative velocity" if relative_speed_kms >= 5 else "Lower relative velocity in this demo")
    action = "Escalate for expert review; validate orbital data and uncertainty information." if level in ("CRITICAL","HIGH") else "Continue monitoring and reassess updated orbital data." if level == "MEDIUM" else "Routine monitoring; reassess when new data becomes available."
    return {"score": score, "level": level, "factors": factors, "action": action}
