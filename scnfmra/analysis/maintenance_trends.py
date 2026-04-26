import pandas as pd

def complaint_analysis(complaints):
    if not complaints:
        return pd.Series()

    data = []

    for c in complaints:
        data.append({
            "facility_id": c.facility_id,
            "severity": c.severity
        })

    df = pd.DataFrame(data)

    return df.groupby("facility_id").size()