import json
import os

class UserManager:
    def __init__(self):
        self.preferences_file = "user_preferences.json"
        self.load_preferences()

    def load_preferences(self):
        """Load user preferences from JSON file."""
        if os.path.exists(self.preferences_file):
            with open(self.preferences_file, 'r') as f:
                self.preferences = json.load(f)
        else:
            self.preferences = {
                "topics": [],
                "history": []
            }

    def save_preferences(self):
        """Save user preferences to JSON file."""
        with open(self.preferences_file, 'w') as f:
            json.dump(self.preferences, f, indent=2)

    def add_topic(self, topic):
        """Add a topic to user preferences."""
        if topic not in self.preferences["topics"]:
            self.preferences["topics"].append(topic)
            self.save_preferences()

    def add_to_history(self, search_query):
        """Add search to history."""
        self.preferences["history"].append({
            "query": search_query,
            "timestamp": import_datetime.datetime.now().isoformat()
        })
        self.save_preferences()

    def get_topics(self):
        """Get user's preferred topics."""
        return self.preferences["topics"]

    def get_history(self):
        """Get user's search history."""
        return self.preferences["history"]