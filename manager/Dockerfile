FROM centos:7.6.1810

ENV APPHOME=/opt/prophetstor/federatorai/demo \
    APP_DEBUG=0

WORKDIR ${APPHOME}

COPY . /tmp/src

RUN echo \
    && mkdir -p ${APPHOME} \
    && cd /tmp/src/; cp -fv install.sh generate_traffic.py run_ab.py transaction.txt ${APPHOME}/; cd - \
    && cd ${APPHOME} && sh -x ./install.sh \
    && cp -fv /tmp/src/init.sh /init.sh && chmod 755 /init.sh \
    && cp -fv /tmp/src/tini /sbin/tini && chmod 755 /sbin/tini \
    && rm -rf /tmp/src \
    && yum clean all

RUN cd ${APPHOME}
ENTRYPOINT ["/sbin/tini","-v", "--"]
CMD ["/init.sh"]
