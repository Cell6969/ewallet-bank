from datetime import datetime, timezone

def get_datetime_naive():
    return datetime.now(timezone.utc).replace(tzinfo=None)