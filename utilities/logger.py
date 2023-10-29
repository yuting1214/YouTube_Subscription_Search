import json
import os
from datetime import datetime
from utilities.filesystem import ensure_directory_exists

class Logger:
    def __init__(self, log_dir='log', log_file_name='log.json'):
        self.log_dir = log_dir
        self.log_file = os.path.join(log_dir, log_file_name)
        
        # Ensure log directory exists
        ensure_directory_exists(self.log_dir)

        # If log file doesn't exist, initialize it
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)

    def add_log(self, message):
        # Load the existing log data
        with open(self.log_file, 'r') as f:
            logs = json.load(f)

        # Add the new log
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_data = {
            "timestamp": timestamp,
            "message": message
        }
        logs.append(log_data)

        # Save the updated logs
        with open(self.log_file, 'w') as f:
            json.dump(logs, f, indent=4)