import re


with open("/Users/younglee/Documents/github/leetcode/scratch/google_list.txt", "r") as f:
    file = f.readlines()

l = []
for item in file:
    if re.match("\d+\n", item):
        #print(item)
        l.append(int(item))

for item in l:
    print("[ ]", item, "<br />")




#[ ] 4<br />
