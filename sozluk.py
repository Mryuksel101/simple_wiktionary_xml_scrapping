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
match = pattern.search(wordMeaningAll)

# Sonuçları alıyoruz
if match:
    noun_section = match.group(2)
    print(noun_section)
else:
    print("Bölüm bulunamadı.")






