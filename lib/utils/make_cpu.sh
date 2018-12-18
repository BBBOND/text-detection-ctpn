#!/usr/bin/env bash

export CFLAGS=-I/Users/bbbond/Documents/ENV/venv-py2-tf-cpu/lib/python2.7/site-packages/numpy/core/include

python setup_cpu.py build

cp ./build/lib.*/lib/utils/*.so ./

echo "复制成功"