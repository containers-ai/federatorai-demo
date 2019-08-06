#!/bin/bash
yum -y update
yum -y --enablerepo=extras install epel-release
yum install -y --enablerepo="epel" python-pip
yum install -y python2-devel
yum install -y gcc
yum -y install httpd
yum info python*-pip
yum install -y yum-utils
pip install subprocess32
pip install --upgrade pip
yum install -y freetype-devel
yum install -y libpng-devel
yum install -y python-yaml
pip install  matplotlib
