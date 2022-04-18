#!/usr/bin/python3
import random
import string

N_KEYS = 80000
KEY_LEN = 128

data = {}


for _ in range(N_KEYS):
	k = ''.join(random.choices(string.ascii_uppercase + string.digits, k=KEY_LEN))
	v = ''.join(random.choices(string.ascii_uppercase + string.digits, k=KEY_LEN))
	data[k] = v

with open('data.json', 'w') as f:
	f.write(str(data))
with open('data.hset', 'w') as f:
	command = 'HSET myhset ' + ' '.join([key + ' ' + value for key, value in data.items()])
	f.write(command)
with open('data.zset', 'w') as f:
	command = 'ZADD myzset ' + ' '.join(['1 ' + key for key in data.keys()])
	f.write(command)
with open('data.list', 'w') as f:
	command = 'LPUSH mylist ' + ' '.join([value for value in data.values()])
	f.write(command)

