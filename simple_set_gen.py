from random import sample
from parameters import server_size, client_size, intersection_size

#set elements can be integers < order of the generator of the elliptic curve (192 bits integers if P192 is used); 'sample' works only for a maximum of 63 bits integers.
server_set =  sample(range(2700000000,2799999999), 1000000)
client_set = sample(range(2700000000,2799999999), 100000)

f = open('server_set', 'w')
for item in server_set:
	f.write(str(item) + '\n')
f.close()

g = open('client_set', 'w')
for item in client_set:
	g.write(str(item) + '\n')
g.close()

# Removed intersection set as not needed