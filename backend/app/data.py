from .risk_engine import assess_risk

def make(identifier, primary, secondary, time, separation, speed):
    risk = assess_risk(separation, speed)
    return {"id":identifier,"primary":primary,"secondary":secondary,"time":time,"separation_km":separation,"relative_speed_kms":speed,**risk,"source":"Synthetic scenario"}

ENCOUNTERS = [
 make("SG-2048","SAT-1182","DEB-7741","00:18:42 UTC",.42,14.8),
 make("SG-2047","SAT-0731","DEB-2190","01:42:10 UTC",1.85,11.2),
 make("SG-2046","SAT-2055","DEB-8013","03:07:55 UTC",4.9,7.1),
 make("SG-2045","SAT-0914","DEB-4420","04:51:03 UTC",13.4,3.2),
 make("SG-2044","SAT-1450","DEB-0911","06:20:31 UTC",2.7,5.8),
]
def summary_for(items):
 return {"tracked_objects":1284,"monitored_encounters":len(items),"high_risk":sum(e["score"]>=70 for e in items),"alerts_today":sum(e["score"]>=65 for e in items)}
