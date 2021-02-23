from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()

print(root)
print(root.tag, root.attrib)

for child in root:
    print(child.tag, child.attrib)
print(root[0][0].text)

for element in root.iter("scores"): # root.iter - перебор всех интересующих элементов в поддереве
                                    # root.findall() - перебор только лишь среди детей
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)



greg = root[0]
module1 = next(greg.iter("module1"))
print(module1, module1.text)
module1.text = str(float(module1.text) + 30)

tree = ElementTree.parse("example_modified.xml")
root = tree.getroot()
greg = root[0]

description = ElementTree.Element("description")
description.text = "Showed excellent skills during the course" # add tag
greg.append(description)

description = greg.find("description")
greg.remove(description) # remove tag

certificate = greg[2]
certificate.set("type", "with distinction")
tree.write("example_modified.xml") # точная копия нашего дерева