from random import randint
import time


res_negativ = ["Ай, блять!!!", "Ну, камон!", "Хватит!!!"]
res_positive = ["О, да!!!", "Ещё!!!", "Жоще!!!"]

sponk_count = 0

sponk_time_start = 0


def sponk():

    global sponk_count
    global sponk_time_start

    sponk_time_start = time.perf_counter() + 15
    delta_sponk_time = time.perf_counter()

    while delta_sponk_time > 0:

        delta_sponk_time = sponk_time_start - time.perf_counter()

    sponk_count = 0

    return "Боже, моя жопа!!!"


def resuls_sponks():

    global sponk_count
    global sponk_time_start

    if sponk_count < 7:

        sponk_count += 1

        res = [sponk_negative(), sponk_negativ_img()]

        sponk_time_start = time.perf_counter() + 15

    else:

        res = [sponk_positive(), sponk_positiv_img()]

        sponk_time_start = time.perf_counter() + 15

    return res


def sponk_negative():

    return res_negativ[randint(0, 2)]


def sponk_positive():

    return res_positive[randint(0, 2)]


def sponk_negativ_img():

    return f"cat ({randint(1, 5)})"


def sponk_positiv_img():

    return f"ahegao ({randint(1, 5)})"
