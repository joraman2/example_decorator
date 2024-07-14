#!/usr/bin/env python3.10
from time import sleep 
from lib import timer

@timer.timer
def main():
    short_wait()
    longer_wait()

@timer.timer
def short_wait():
    sleep(1)
    return True

@timer.timer
def longer_wait():
    sleep(3)

if __name__ == "__main__":
    main()