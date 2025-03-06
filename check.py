def check(avaiable_hours, user_hours):
    matching_slots = []
    for user_date, user_hour in user_hours:
        for slot in avaiable_hours:
            if slot["date"] == user_date and slot["time"] == user_hour:
                matching_slots.append((user_date, user_hour))

    return matching_slots
