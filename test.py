import datetime

cur_wd = datetime.datetime.weekday(datetime.datetime.now())
dif = 3 - cur_wd
if dif == 1:
    ans = f"До ЧСЧ осталось {dif} день"
if dif > 1 and dif < 5:
    ans = f"До ЧСЧ осталось {dif} дня"
if dif > 5:
    ans = f"До ЧСЧ осталось {dif} дней"
elif dif < 0:
    ans = f"До ЧСЧ осталось {7 - dif} дней"
elif dif == 0:
    ans = f"ЧСЧ по плану сегодня!!! Не забудь!"
print(ans)
print(dif)
print(cur_wd)
