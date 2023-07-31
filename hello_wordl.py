import xml.etree.ElementTree as ET
with open("C:/Users/Mustafa Yüksel/Desktop/python/dic.xml", "r") as file:
    xml_text = file.read()
root = ET.fromstring(xml_text)

allText = root.find(".//text").text

if allText.find("== Noun ==")!=-1:
    print("kelime var")
    
else:
    print("kelime yok")