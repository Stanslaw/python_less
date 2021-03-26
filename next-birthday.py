from typing import Dict, Tuple
import datetime

Date = Tuple[int, int, int]


def next_birthday(today: Date, birthdates: Dict[str, Date]) -> Tuple[int, Dict[str, int]]:

    # print(today)
    today_date = datetime.date(*today)
    print(today_date, end='\n\n')

    # print(today_date.day)

    for people in birthdates:

        birthsday_in_the_next_year = False

        who = people
        brs = datetime.date(*birthdates[people])

        delta_years = today_date.year - brs.year
        delta_months = today_date.month - brs.month
        delta_days = today_date.day - brs.day

        if delta_months < 0:
            # ДР только будет в этом году
            years = delta_years
            print("Years = ", years)
        elif delta_months == 0 and delta_days < 0:
            # ДР только будет через несколько дней
            years = delta_years
            print("Years = ", years)
        elif delta_months == 0 and delta_days == 0:
            # ДР сегодня
            years = delta_years
            print("Years now = ", years)
        else:
            # ДР будет через год
            years = delta_years + 1
            birthsday_in_the_next_year = True
            print("Years+1 =", years)


        if birthsday_in_the_next_year:
            # print("+", end=' ')
            # how_long_to_bsd = (datetime.date(today_date.year, brs.month, brs.day) - today_date) #+ datetime.timedelta(days=365)
            # how_many_days_in_next_year = datetime.date(today_date.year + 1, brs.month, brs.day) - datetime.date(today_date.year, brs.month, brs.day)

            # Пробуем вычисление даты - если выпадает ошибка значит это 29.02.хххх в невысокостном году. Меняем дату на первое марта
            try:
                date_brs_in_next_year = datetime.date(today_date.year + 1, brs.month, brs.day)
            except ValueError:
                date_brs_in_next_year = datetime.date(today_date.year + 1, 3, 1)

            try:
                date_brs_in_this_year = datetime.date(today_date.year, brs.month, brs.day)
            except ValueError:
                date_brs_in_this_year = datetime.date(today_date.year, 3, 1)

            how_many_days_in_next_year = date_brs_in_next_year - date_brs_in_this_year


            print("how_many_days_in_next_year =",  how_many_days_in_next_year.days)

            try:
                date_if_people_born_in_this_year = datetime.date(today_date.year, brs.month, brs.day)
            except ValueError:
                date_if_people_born_in_this_year = datetime.date(today_date.year, 3, 1)

            how_long_to_bsd = date_if_people_born_in_this_year - today_date + how_many_days_in_next_year

        else:
            # print("-", end=' ')
            how_long_to_bsd = datetime.date(today_date.year, brs.month, brs.day) - today_date


        print(who, brs, how_long_to_bsd.days, end='\n\n')



if __name__ == '__main__':
    FAMILY = {
        'Brian': (1967, 5, 31),
        'Léna': (1970, 10, 3),
        'Philippe': (1991, 6, 15),
        'Yasmine': (1996, 2, 29),
        'Emma': (2000, 12, 25),
    }

    TESTS = [
        # ((2020, 9, 8), (25, {'Léna': 50})),
        # ((2021, 10, 4), (82, {'Emma': 21})),
        ((2022, 3, 1), (0, {'Yasmine': 26})),
    ]

    for nb, (day, answer) in enumerate(TESTS, 1):
        user_result = tuple(next_birthday(day, FAMILY.copy()))
        if user_result != answer:
            print(f'You failed the test #{nb}.')
            print(f'Your result: {user_result}')
            print(f'Right result: {answer}')
            break
    else:
        print('Well done! Click on "Check" for real tests.')
