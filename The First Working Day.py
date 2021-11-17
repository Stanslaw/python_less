from datetime import datetime, timedelta

def vacation(date, days):
    #replace this for solution

    date_dt = datetime.strptime(date, '%Y-%m-%d')

    # print(str(date_dt.date() + timedelta(days=days)))

    if (date_dt.date() + timedelta(days=days)).weekday() == 6:
        return str(date_dt.date() + timedelta(days=days + 1))
    elif (date_dt.date() + timedelta(days=days)).weekday() == 5:
        return str(date_dt.date() + timedelta(days=days + 2))
    else:
        return str(date_dt.date() + timedelta(days=days))


    return 0

if __name__ == '__main__':
    # print("Example:")
    # print(vacation('2018-07-01', 14))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert vacation('2018-07-01', 14) == '2018-07-16'
    assert vacation('2018-02-19', 10) == '2018-03-01'
    assert vacation('2000-02-28', 5) == '2000-03-06'
    assert vacation('1999-12-20', 14) == '2000-01-03'
    print("Coding complete? Click 'Check' to earn cool rewards!")
