# datetime, time, sound playback
# Ask the user to set a time, and when the time arrives, play a sound or print "Wake up!".
# Terminal based

import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"Current time: {current_time}")
        if current_time == alarm_time:
            print("Wake up!")
            winsound.Beep(440, 1000)
            break
        time.sleep(5)

def main():
    alarm_time = input("Set the alarm time (HH:MM): ")
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
        print(f"Alarm set for {alarm_time}.")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please use HH:MM.")

if __name__ == "__main__":
    main()
