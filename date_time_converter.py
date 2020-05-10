from datetime import datetime
def date_time(time: str) -> str:
    #replace this for solution

    my_dict = {" 00 ":" 0 ",
               " 01 ":" 1 ",
               " 02 ":" 2 ",
               " 03 ":" 3 ",
               " 04 ":" 4 ",
               " 05 ":" 5 ",
               " 06 ":" 6 ",
               " 07 ":" 7 ",
               " 08 ":" 8 ",
               " 09 ":" 9 "}

    date_cust = datetime.strptime(time, "%d.%m.%Y %H:%M")
    if date_cust.hour == 1:
        hour_cust = "hour"
    else:
        hour_cust = "hours"

    if date_cust.minute == 1:
        minute_cust = "minute"
    else:
        minute_cust = "minutes"

    # print(hour_cust, minute_cust)
    # print("!!!", date_cust)
    # print(date_cust.date())
    date_cust_new = date_cust.strftime(f"%d %B %Y year %H {hour_cust} %M {minute_cust}")

    for k, v in my_dict.items():
        # print(k, v)
        date_cust_new = date_cust_new.replace(k, v)

    # print(date_cust_new[1:])

    if date_cust_new[0] == "0":
        date_cust_new = date_cust_new[1:]

    print(date_cust_new)

    return date_cust_new

if __name__ == '__main__':
    # print("Example:")
    # print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    assert date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute"
    print("Coding complete? Click 'Check' to earn cool rewards!")
