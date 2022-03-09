from time import sleep


def buff(t=0.5):
    buf = True
    while buf:
        sleep(t)
        buf = False
    return 0
