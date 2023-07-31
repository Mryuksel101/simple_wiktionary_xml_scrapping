import xml.etree.ElementTree as ET
import re
with open('dic.xml', 'r') as file:
    xml_data = file.read()

# XML metnini ayrıştırma
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

searchedWord = root.find('title').text
wordMeaningAll = root.find('.//text').text
# 'Noun' bölümünü arıyoruz
pattern = re.compile(r'== Noun ==(.+?)\n\n', re.DOTALL)
noun_sections = pattern.findall(wordMeaningAll)

for i, item in enumerate(noun_sections, 1):
    print(f"== Noun {i} ==\n{item}\n")






