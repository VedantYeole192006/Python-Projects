# Terminal Based
# Let user input time in seconds and count down to zero with a message or sound.
# time.sleep(), loops

import time
from plyer import notification

a = int(input("Enter time in seconds: "))
count = a

for i in range(a+1):
    time.sleep(1)
    print(count - i)
    if (count-i) == 0:
        print("Time up!")
        notification.notify(
            title = 'Time Up',
            message = f"Your time {a} sec are up.",
            app_icon = None,
            timeout = 10,
        )