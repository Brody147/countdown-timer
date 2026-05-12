# COUNTDOWN TIMER

import time

countdown_timer_list = [24, 0, 0]

# Print the starting value of 24:0:0
print("24:00:00")

while True:
    time.sleep(1)
    countdown_timer_list[2] -= 1
    if countdown_timer_list[2] < 0:
        countdown_timer_list[2] = 59
        countdown_timer_list[1] -= 1
        if countdown_timer_list[1] < 0:
            countdown_timer_list[1] = 59
            countdown_timer_list[0] -= 1
            if countdown_timer_list[0] < 0:
                countdown_timer_list = [24, 0, 0]
                print("Finished one!")
                time.sleep(2)

    if len(str(countdown_timer_list[0])) == 1:
        print("0" + str(countdown_timer_list[0]) + ":" + str(
            countdown_timer_list[1]) + ":" + str(countdown_timer_list[2]))

    elif len(str(countdown_timer_list[1])) == 1:
        print(str(countdown_timer_list[0]) + ":0" + str(
            countdown_timer_list[1]) + ":" + str(countdown_timer_list[2]))

    elif len(str(countdown_timer_list[2])) == 1:
        print(str(countdown_timer_list[0]) + ":" + str(
            countdown_timer_list[1]) + ":0" + str(countdown_timer_list[2]))

    else:
        print(str(countdown_timer_list[0]) + ":" + str(
            countdown_timer_list[1]) + ":" + str(countdown_timer_list[2]))
