from datetime import timedelta, datetime
from time import sleep

from pyspectator.processor import Cpu


def generate_report(duration: timedelta):
    cpu = Cpu(monitoring_latency=0.1)
    measurements = []
    with cpu:
        end_time = datetime.now() + duration
        now = datetime.now()
        while now < end_time:
            measurements.append((now, cpu.load))
            now = datetime.now()
            sleep(0.2)

    return measurements
