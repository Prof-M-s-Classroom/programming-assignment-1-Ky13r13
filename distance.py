from datetime import datetime


class Distance:
    """
    Class to represent a distance measurement with timestamp.
    """
    def __init__(self, distance = None):
        """Initialize the Distance object with distance and timestamp."""

        self.distance = float(distance) if distance else None
        self.timestamp = datetime.now()


    def __str__(self):
        """Return a formatted string representation of the Distance object."""
        return f"Distance(distance={self.distance} cm, timestamp={self.timestamp})"

