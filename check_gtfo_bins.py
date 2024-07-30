import requests


filepath = 'text_gtfo_bins.txt'
#filepath = str(input("Enter full path of file name : "))


list_of_cmds = []
file = open(filepath, 'r')
lines = file.readlines()
for line in lines:
	single_line = line.rstrip()
	x = single_line.split("/")
	command = x[len(x)-1]
	list_of_cmds.append(command)
	


for i in list_of_cmds:
	URL = 'https://gtfobins.github.io/gtfobins/' + i + '/'
	r = requests.get(URL)
	if(r.status_code == 200):
		print(i + " commmand exist")


# Adding functionality that compares normal output of the find command to see if there are any custom scripts with SGID or SUID bit set

# find / -perm -u=s -type f 2>/dev/null
# 4000 is the bitmask for SetUID


# find / -perm /4000 2>/dev/null
# 2000 is the bitmask for SetGID
