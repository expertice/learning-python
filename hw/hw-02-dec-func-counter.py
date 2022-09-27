"""+ Реализовать декоратор, который измеряет скорость выполнения функций.
"""
import time


def telemetry(func):
    def lets_measure():
        start = time.time()
        print(start)


telemetry(sum(2, 3))