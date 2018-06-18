
import json

mapping = {}

f = open('in_out_ip_map', 'r')

for line in f:
    line_list = line.split()
    print("{\"%s\": \"%s\"}, " % (line_list[0], line_list[1]))


