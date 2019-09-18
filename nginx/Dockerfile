FROM docker.io/nginx:1.16.0

RUN set -x \
    # support running as arbitrary user which belogs to the root group
    && mkdir -p /var/cache/nginx /var/run /var/log/nginx \
    && chmod -R 777 /var/cache/nginx /var/run /var/log/nginx \
    # non-root users are not allowed to listen on priviliged ports
    && sed -i.bak 's/listen\(.*\)80;/listen 8000;/' /etc/nginx/conf.d/default.conf \
    # comment user directive as master process may run as non-root user
    && sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf

EXPOSE 8000
