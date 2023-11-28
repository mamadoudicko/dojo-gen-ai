import datetime


def get_current_time() -> str:
    """
    Get the current time
    """
    return datetime.datetime.now().strftime("%H:%M:%S")
