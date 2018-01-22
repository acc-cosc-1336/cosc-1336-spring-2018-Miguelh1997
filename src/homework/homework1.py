def get_hours_since_midnight(seconds):

    return seconds // 3600

def get_minutes(seconds):

    return (seconds % 3600) // 60

def get_seconds(seconds):

    return (seconds % 3600) % 60
