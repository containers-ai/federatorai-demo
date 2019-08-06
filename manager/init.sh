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
python generate_traffic.py

# Wait forever if environment variable APP_DEBUG=1
if [ "${APP_DEBUG}" = "1" ]; then
    while :; do
        [ -f /tmp/.pause ] && sleep 300 || sleep 30
    done
fi

exit 0
