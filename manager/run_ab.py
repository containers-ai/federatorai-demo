import time
import os
import random
import sys


class Nginx:
    autoscale_type = "hpa"
    week_ratio_list = [0.7, 0.6, 0.9, 1.4, 1.6, 1.3, 0.8]

    def __init__(self, autoscale_type=""):
        if autoscale_type:
            self.autoscale_type = autoscale_type

    def run_cmd(self, cmd):
        ret = os.popen(cmd).read()
        return ret

    def wait_time(self, waittime):
        # print "wait %d time" % waittime
        time.sleep(waittime)

    def generate_nginx_traffic(self, count, ratio=0, day_count=0):
        cmd = ""

        traffic_ratio1 = os.environ.get("WORKLOAD_HPA_REQUEST_RATE")
        ip = os.environ.get("FEDERATORAI_DEMO_NGINX_HPA_SERVICE_HOST")
        port = os.environ.get("FEDERATORAI_DEMO_NGINX_HPA_SERVICE_PORT")
        if self.autoscale_type == "vpa":
            traffic_ratio1 = os.environ.get("WORKLOAD_VPA_REQUEST_RATE")
            ip = os.environ.get("FEDERATORAI_DEMO_NGINX_VPA_SERVICE_HOST")
            port = os.environ.get("FEDERATORAI_DEMO_NGINX_VPA_SERVICE_PORT")
        if ratio != 0:
            traffic_ratio1 = ratio
            print "traffic ratio = ", ratio
        weekly_ratio = self.week_ratio_list[day_count]
        transaction_list = self.get_transaction_list()
        transaction_num = int(int(transaction_list[count]) * int(traffic_ratio1) * weekly_ratio)
        cmd = "ab -c 100 -n %d -r http://%s:%s/index.html" % (transaction_num, ip, port)
        print "--- start 100 clients and %d transactions to host(%s:%s) by %s ---" % (transaction_num, ip, port, self.autoscale_type), weekly_ratio
        output = self.run_cmd(cmd)
        # print output
        return output

    def get_transaction_list(self):
        transaction_list = []
        fn = "./transaction.txt"
        with open(fn, "r") as f:
            output = f.read()
            for line in output.split("\n"):
                if line:
                    transaction = int(float(line.split()[0]))
                    transaction_list.append(transaction)
        return transaction_list


if __name__ == "__main__":
    autoscale_type = sys.argv[1]
    n = Nginx(autoscale_type)
    request_count = int(sys.argv[2])
    ratio = 0
    if len(sys.argv) > 3:
        ratio = int(sys.argv[3])
    day_count = 0
    if len(sys.argv[4]) > 4:
        day_count = int(sys.argv[4])
    n.generate_nginx_traffic(request_count, ratio, day_count)
