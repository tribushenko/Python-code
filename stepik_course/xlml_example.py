from lxml import etree
import requests

res = requests.get("https://docs.python.org/3/")
print(res.status_code, res.headers["Content-Type"], sep="\n")

parser = etree.HTMLParser()
root = etree.fromstring(res.text, parser)

for element in root.iter("a"):
    print(element, element.attrib)