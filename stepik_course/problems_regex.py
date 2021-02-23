import re

pattern = r"[([АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}([АВЕКМНОРСТУХ]{2}\d{3}\d{2,3})]"

print(re.match(pattern, input()))
