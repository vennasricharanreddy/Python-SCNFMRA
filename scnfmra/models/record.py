from datetime import datetime

class Record:
    def __init__(self):
        self._created_at = datetime.now()
        self._updated_at = datetime.now()

    def update_timestamp(self):
        self._updated_at = datetime.now()