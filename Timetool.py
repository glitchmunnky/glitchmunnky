import time
import threading
import datetime
import winsound

def clock():
    while True:
        now = datetime.datetime.now().strftime('%H:%M:%S')
        print("\rCurrent Time: " + now, end="")
        time.sleep(1)

def countdown_timer(duration):
    print(f"Countdown started for {duration} seconds.")
    for i in range(duration, 0, -1):
        print(f"\rCountdown: {i} seconds remaining", end="")
        time.sleep(1)
    print("\nTime's up!")

def stopwatch():
    print("Stopwatch started. Press Enter to split. Press Ctrl+C to stop.")
    start_time = time.time()
    splits = []
    
    try:
        while True:
            elapsed = time.time() - start_time
            print(f"\rElapsed Time: {elapsed:.2f} seconds", end="")
            input()  # Wait for Enter key to be pressed
            splits.append(elapsed)
            print(f"\nSplit at: {elapsed:.2f} seconds")
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")
        for i, split_time in enumerate(splits):
            print(f"Split {i + 1}: {split_time:.2f} seconds")

def set_alarm(alarm_time):
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == alarm_time:
            print(f"\nAlarm! It's {alarm_time}!")
            break
        time.sleep(10)  # Check every 10 seconds

def alarm_setup():
    alarms = []
    for i in range(5):
        alarm_time = input(f"Set alarm {i + 1} (HH:MM format): ")
        alarms.append(alarm_time)
        threading.Thread(target=set_alarm, args=(alarm_time,)).start()
    print("All alarms set.")

def main():
    print("Welcome to the Clock, Countdown Timer, Stopwatch, and Alarm Program!")
    print("Select an option:")
    print("1. Clock")
    print("2. Countdown Timer")
    print("3. Stopwatch")
    print("4. Set Alarms")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        clock()
    elif choice == '2':
        duration = int(input("Enter duration in seconds: "))
        countdown_timer(duration)
    elif choice == '3':
        stopwatch()
    elif choice == '4':
        alarm_setup()
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
