import uuid
from threading import Lock

class TimingCollector:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._init_singleton()
            return cls._instance

    def _init_singleton(self):
        self.run_id = str(uuid.uuid4())
        self.events = []

    def record_event(self, event_name, event_start, event_end):
        # Convert to milliseconds, no decimals
        event_start_ms = int(event_start * 1000)
        event_end_ms = int(event_end * 1000)
        elapsed_time_ms = event_end_ms - event_start_ms
        self.events.append({
            'run_id': self.run_id,
            'event_name': event_name,
            'event_start': event_start_ms,
            'event_end': event_end_ms,
            'elapsed_time': elapsed_time_ms
        })

    def print_events(self):
        for event in self.events:
            print(event)
