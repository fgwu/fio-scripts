#!/usr/bin/python

import argparse
import random
import sys

sys.path.append('..')

from lib import gen_trace

parser = argparse.ArgumentParser()
parser.add_argument("device")

args = parser.parse_args()

offset = 64*256*1024*1024
size = 1024*1024*1024
step = 136*1024
nr_ops = 134*1024

offsets = range(offset, offset + size, step)
random.shuffle(offsets)
offsets = offsets[:nr_ops]

gen_trace('write', args.device, offsets, step)
