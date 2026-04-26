class Facility:
    def __init__(self, fid, building, room_type, capacity, floor, coordinates):
        self.fid = fid
        self.building = building
        self.room_type = room_type
        self.capacity = capacity
        self.floor = floor
        self.coordinates = coordinates

    def display(self):
        return f"{self.fid} | {self.building} | {self.room_type} | Cap:{self.capacity}"

    def to_dict(self):
        return self.__dict__