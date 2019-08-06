import os
import time
import sys


def generate_traffic(time_count):
    print "--- Generate Traffic For %dth Munites ---" % time_count
    for i in range(time_count):
        # print "generate %d th workloads" % i
        start_time = time.time()
        value = i % 72
        cmd = "python ./run_ab.py %d &" % (value)
        ret = os.system(cmd)
        count = 0
        while True:
            end_time = time.time()
            if end_time - start_time > 60:
                # print ("go to next interval...")
                break
            count += 1
            # print "wait 5 seconds", count
            time.sleep(5)


def main(time_count):
    total_start_time = time.time()
    print "=== Generate Traffic for %d Minutes ===" % time_count
    generate_traffic(time_count)
    total_end_time = time.time()
    print "completed!!!", (total_end_time - total_start_time)/60, "minutes"


if __name__ == "__main__":
    try:
        time_count = int(os.environ.get("WORKLOAD_DURATION"))
        main(time_count)
    except Exception as e:
        print "failed to generate traffic: %s" % str(e)
