import datetime
from datetime import timedelta


def week_no(target_day: datetime) -> int:
    """연월일을 입력받아 해당 요일의 주차를 얻는 함수

    Args:
       target_day : 변환해야하는 날
    Return:
        int - 해당 요일의 주
    """
    # weekday
    # 0이 월요일 6이 일요일
    firstday = datetime.datetime.strptime(target_day, "%Y-%m-%d").replace(day=1)  # 5
    target_day = datetime.datetime.strptime(
        target_day, "%Y-%m-%d"
    ) - datetime.timedelta(
        days=datetime.datetime.strptime(target_day, "%Y-%m-%d").weekday()
    )

    firstday = target_day.replace(day=1)  # 5
    if firstday.weekday() == 0:
        origin = firstday
    elif firstday.weekday() < 3:
        origin = firstday - timedelta(days=firstday.weekday() + 1)
    else:
        origin = firstday + timedelta(days=5 - firstday.weekday())
    return (target_day - origin).days // 7 + 1


print(week_no("2022-05-01"))
