#!/usr/bin/env python3
import time
import sys

def pomodoro(minutes):
    minutes = int(minutes)
    total_seconds = minutes * 60

    for s in range(total_seconds, -1, -1):
        mins = s // 60
        sec  = s % 60
        print(f"{mins:02d}:{sec:02d}")
        time.sleep(1)

if __name__ == "__main__":
    pomodoro(sys.argv[1])
