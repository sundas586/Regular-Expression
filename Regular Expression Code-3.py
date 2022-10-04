import re

txt = open(r"C:\Users\Fujitsu\Desktop\text.txt")
for line in txt :
    line = line.rstrip()
    if re.search(".*,",line): #Starts with at least one character, then as many characters, end with a comma
        print(line)
    
