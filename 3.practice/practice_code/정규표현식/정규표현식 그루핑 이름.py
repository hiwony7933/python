

import re
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-7234-1234")
print(m.group("name"))

p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
p.search("Paris in the the spring").group()


