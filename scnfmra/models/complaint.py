from scnfmra.models.record import Record

class Complaint(Record):
    def __init__(self, cid, facility_id, issue, severity):
        super().__init__()
        self.cid = cid
        self.facility_id = facility_id
        self.issue = issue
        self.severity = severity
        self.status = "Open"
        self.assigned_to = None

    def assign(self, technician):
        self.assigned_to = technician
        self.status = "In Progress"

    def resolve(self, note):
        self.status = "Completed"
        self.resolution = note