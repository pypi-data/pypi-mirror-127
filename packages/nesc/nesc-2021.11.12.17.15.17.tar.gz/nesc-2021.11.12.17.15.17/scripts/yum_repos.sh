#!/usr/bin/env bash
# @Project      : nesc
# @Time         : 2021/10/29 下午4:25
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}

cp -r /etc/yum.repos.d /etc/yum.repos.d.bak # 备份

#CONFIG="""
#[base]\n
#name=Nexus Yum Repository\n
#baseurl=http://10.211.96.56:8081/repository/yum-group/\n
#enabled=1\n
#gpgcheck=0\n
#"""
#echo -e ${CONFIG} > /etc/yum.repos.d/nexusgroup.repo

cat > /etc/yum.repos.d/nexus.repo<< EOF
[base]
name=Nexus Yum Repository
baseurl=http://10.211.96.56:8081/repository/yum-group/
enabled=1
gpgcheck=0
EOF

