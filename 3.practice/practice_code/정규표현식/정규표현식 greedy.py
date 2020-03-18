import re

s =  "<html><gead><title>Title</title>"
len(s)
print(re.match('<.*>',s).span())
print(re.match('<.*>',s).group())


print(re.match('<.+?>',s).group())
