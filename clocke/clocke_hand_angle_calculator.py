def calculate_hand_angle_difference(time_input: str) -> float:
    hours, minutes = parse_time_string(time_input)
    hour_hand_angle = calculate_hour_hand_angle(hours, minutes)
    minute_hand_angle = calculate_minute_hand_angle(minutes)

    if hour_hand_angle <= minute_hand_angle:
        return minute_hand_angle - hour_hand_angle
    else:
        return 360 - hour_hand_angle + minute_hand_angle


def calculate_minute_hand_angle(minutes: int) -> float:
    return minutes * 360 / 60


def calculate_hour_hand_angle(hours: int, minutes: int) -> float:
    return (hours % 12) * 360 / 12 + minutes * 30 / 60


def parse_time_string(time_string: str) -> tuple[int, int]:
    if len(time_string) != 4:
        raise ValueError("time string must be 4 characters [hh:mm]")

    hours = int(time_string[:2])
    if hours < 0 or hours > 23:
        raise ValueError("hours must be between 0 - 24")

    minutes = int(time_string[2:])
    if minutes < 0 or minutes > 59:
        raise ValueError("minutes must be between 0 - 59")

    return hours, minutes
