import os
import time
import sys
autoscale_type = sys.argv[1]


def generate_traffic(time_count):
    print "--- Generate %s Traffic For %d Munites ---" % (autoscale_type, time_count)
    for i in range(time_count):
        # print "generate %d th workloads" % i
        start_time = time.time()
        value = i % 72
        day_count = (i/60) % 24
        cmd = "python ./run_ab.py %s %d 0 %d &" % (autoscale_type, value, day_count)
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
    print "=== Generate %s Traffic For %d Minutes ===" % (autoscale_type, time_count)
    generate_traffic(time_count)
    total_end_time = time.time()
    print "completed!!!", (total_end_time - total_start_time)/60, "minutes"


if __name__ == "__main__":
    if autoscale_type == "hpa" and not os.environ.get("WORKLOAD_HPA_DURATION"):
        print "Skip hpa job due to environment variable WORKLOAD_HPA_DURATION is not specified"
        sys.exit()
    if autoscale_type == "vpa" and not os.environ.get("WORKLOAD_VPA_DURATION"):
        print "Skip vpa job due to environment variable WORKLOAD_VPA_DURATION is not specified"
        sys.exit()
    time_count = int(os.environ.get("WORKLOAD_HPA_DURATION"))
    try:
        if autoscale_type == "vpa":
            time_count = int(os.environ.get("WORKLOAD_VPA_DURATION"))
        main(time_count)
    except Exception as e:
        print "failed to generate traffic: %s" % str(e)
        sys.exit()
