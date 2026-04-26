import pandas as pd

def usage_analysis(bookings):
    if not bookings:
        return pd.Series()

    data = []

    for b in bookings:
        data.append({
            "facility_id": b.facility_id,
            "start": str(b.start_time),
            "end": str(b.end_time)
        })

    df = pd.DataFrame(data)

    return df.groupby("facility_id").size()