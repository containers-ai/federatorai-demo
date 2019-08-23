#!/bin/sh
#
[ "${APPHOME}" = "" ] && export APPHOME=/opt/prophetstor/federatorai/demo

do_signal_term()
{
    echo "PID($$) - Shutdown services due to SIGTERM received."
    sleep 1
    exit 0
}

#
# Main
#
trap do_signal_term 15 # Trap SIGTERM

# start main service
cd ${APPHOME}
python generate_traffic.py hpa &
python generate_traffic.py vpa &
# Wait forever
while :; do
    [ -f /tmp/.pause ] && sleep 300 || sleep 30
done

exit 0
