#!/bin/sh


# Build the project
cython ./main.py --embed -3 -o main.c
PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags)
gcc -Os $(python3-config --includes) main.c -o down $(python3-config --ldflags) -l$PYTHONLIBVER
