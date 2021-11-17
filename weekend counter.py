from datetime import date, timedelta


def checkio(from_date, to_date):
    """
        Count the days of rest
    """

    # print(from_date, to_date.weekday())

    full_days = (to_date - from_date).days
    full_wdays = (full_days//7)*2
    appendix_days = full_days % 7
    appendix_wdays = 0

    for i in range(appendix_days + 1):
        if (to_date - timedelta(days=i)).weekday() in [5, 6]:
            appendix_wdays += 1

    print(full_days, full_wdays, appendix_wdays)

    return full_wdays + appendix_wdays


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

