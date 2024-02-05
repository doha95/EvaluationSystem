from datetime import datetime


def is_ordered_by_date(dates):
    """Check if the given list of date strings is ordered by date.

    Args:
        dates (list): List of date strings in the format "Month Year".

    Returns:
        bool: True if the list is ordered by date, False otherwise.
    """
    # Convert the first date to a datetime object
    prev_date = datetime.strptime(dates[0], "%B %Y")

    # Iterate over the remaining dates and check if they are in order
    for current_date in dates[1:]:
        current_datetime = datetime.strptime(current_date, "%B %Y")
        if current_datetime >= prev_date:
            return False
        prev_date = current_datetime

    return True
