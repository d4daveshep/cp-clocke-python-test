import pytest

from clocke.clocke_hand_angle_calculator import calculate_hand_angle_difference, parse_time_string, \
    calculate_minute_hand_angle, calculate_hour_hand_angle

# test data list of tuple(time_string, angle_difference)
test_data = [("1230", 165),
             ("0245", 187.5),
             ("1445", 187.5),
             ("1754", 147),
             ("1710", 265),
             ("1200", 0)]


@pytest.mark.parametrize("time_string, angle_difference", test_data)
def test_hand_angle_difference(time_string, angle_difference):
    assert calculate_hand_angle_difference(time_string) == angle_difference


# hand angle test data tuple(time_string, minute_angle, hour_angle)
hand_angle_data = [
    ("0030", 180, 15),
    ("1230", 180, 15),
    ("0245", 270, 82.5),
    ("1445", 270, 82.5),
    ("0510", 60, 155),
    ("1710", 60, 155),
    ("0554", 324, 177),
    ("1754", 324, 177),
    ("0000", 0, 0),
    ("1200", 0, 0),
    ("0245", 270, 82.5),
    ("1445", 270, 82.5),
]


@pytest.mark.parametrize("time_string, minute_angle, hour_angle", hand_angle_data)
def test_minute_hand_angle(time_string, minute_angle, hour_angle):
    hours, minutes = parse_time_string(time_string)
    assert calculate_minute_hand_angle(minutes) == minute_angle


@pytest.mark.parametrize("time_string, minute_angle, hour_angle", hand_angle_data)
def test_hour_hand_angle(time_string, minute_angle, hour_angle):
    hours, minutes = parse_time_string(time_string)
    assert calculate_hour_hand_angle(hours, minutes) == hour_angle


def test_invalid_input_string():
    with pytest.raises(ValueError):
        calculate_hand_angle_difference("abcd")

    with pytest.raises(ValueError):
        calculate_hand_angle_difference("9999")


def test_parse_time_string():
    hours, minutes = parse_time_string("1230")
    assert hours == 12
    assert minutes == 30


def test_cant_parse_non_numeric_time_string():
    with pytest.raises(ValueError):
        parse_time_string("abcd")

    with pytest.raises(ValueError):
        parse_time_string("")


def test_cant_parse_wrong_length_time_string():
    with pytest.raises(ValueError):
        parse_time_string("123")

    with pytest.raises(ValueError):
        parse_time_string("12345")


def test_cant_parse_invalid_hours():
    with pytest.raises(ValueError):
        parse_time_string("2530")

    with pytest.raises(ValueError):
        parse_time_string("-230")


def test_cant_parse_invalid_minutes():
    with pytest.raises(ValueError):
        parse_time_string("1269")

    with pytest.raises(ValueError):
        parse_time_string("12-5")
