from scnfmra.models.record import Record

class Asset(Record):
    def __init__(self, asset_id, category, building, room, warranty_expiry):
        super().__init__()
        self.asset_id = asset_id
        self.category = category
        self.building = building
        self.room = room
        self.warranty_expiry = warranty_expiry
        self.health_status = "Good"