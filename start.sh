#!/bin/bash
cd LSHash_Master
pip install e .
echo "LSH installed"
cd ..
cd kdtree
pip install e .
echo "kdtree installed"
cd ..
echo "staring GUI"
python proto_top.py
