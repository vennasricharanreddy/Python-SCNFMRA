from datetime import datetime

class Booking:
    def __init__(self, facility_id, purpose, start_time, end_time):
        self.facility_id = facility_id
        self.purpose = purpose
        self.start_time = datetime.fromisoformat(start_time)
        self.end_time = datetime.fromisoformat(end_time)

    def conflicts(self, other):
        return self.facility_id == other.facility_id and not (
            self.end_time <= other.start_time or self.start_time >= other.end_time
        )