import re

txt = open(r"C:\Users\Fujitsu\Desktop\text.txt")
for line in txt :
    line = line.rstrip()
    if re.search("And",line):
        print(line)
    
