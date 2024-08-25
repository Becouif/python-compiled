import re
from pickletools import long1

pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')

string= 'blessing@gmail.com'

a = pattern.search(string)

print(a)

# at least 8 char long
# contain any sort letters,numbers and symbols
