#!/usr/bin/env bash
# @Project      : nesc
# @Time         : 2021/10/27 下午7:04
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}
#生产环境：10.210.10.97:30002/library/deeplearning/docker-serving:v18
#开发环境：10.211.10.26:30002/library/deeplearning/docker-serving:v18
# 生产10.210.10.97:30002/library/deeplearning/docker-serving:v19
# 开发10.211.10.26:30002/library/deeplearning/docker-serving:v19

tar -cvf x.tar x


#FROM 10.210.10.97:30002/library/deeplearning/docker-serving:v19
#USER root
#
###################################################################
#RUN pip install -U --no-cache-dir appzoo -i http://192.18.26.222:8081/repository/pypiproxy/simple --trusted-host 192.18.26.222
###################################################################
#
#RUN rm -rf ~/.cache/pip/*
#RUN rm -rf /tmp/pip*


