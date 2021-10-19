def clock_angle(time):
    time_in_int_dict = dict(zip(['hour', 'minute'], list(map(int, time.split(':')))))
    minute_angle = (360/60)*time_in_int_dict['minute']
    hour_angle = (360/12)*(time_in_int_dict['hour']%12) + (minute_angle/360)*30
    final_angle = min(360 - abs(minute_angle-hour_angle), abs(minute_angle-hour_angle))
    print(time_in_int_dict, ' hour_angle: ', hour_angle, ' minute_angle:', minute_angle, ' final_angle:', final_angle)
    return final_angle

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"