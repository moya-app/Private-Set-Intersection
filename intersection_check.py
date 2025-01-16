c = open('client_set', 'r')
client_set_entries = c.readlines()
client_set_entries = [value.strip() for value in client_set_entries]

s = open('server_set', 'r')
server_set_entries = s.readlines()
server_set_entries = [value.strip() for value in server_set_entries]

print(sum(1 for value in client_set_entries if value in server_set_entries))