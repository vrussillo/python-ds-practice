def weekday_name(day_of_week):
    weekdays = ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day_of_week < 1 or day_of_week > 7:
        return None
    return weekdays[day_of_week -1]
 