import re

txt = 'a abc abcd abcde abcdef abcdefg abcdefgh eeeeee gh bii opop kk plp cxyz uvw'
line = re.findall("[a-c]+",txt) #Starts with at least one letter between a to c, then one more any letter, then as many letters
print(line) # findall() returns a list of string
    
