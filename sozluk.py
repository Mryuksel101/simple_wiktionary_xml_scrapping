""" 
{
    word: ....
    [
        {   
            des : ....
            sentences :
                [         
                    
                ]
            type: .......
        }
    ]
}

{
    [
        {
            word: ....
            [
                {   
                    des : ...
                    sentences : [
                    
                    ]
                }
            ]
            type: .......
        }
    ]
}

for i, item in enumerate(noun_sections, 1):
    print(f"== Noun {i} ==\n{item}\n")

pattern = re.compile(r'== Noun ==(.+?)\n\n', re.DOTALL)
noun_sections = pattern.findall(text)

for i in sentences:
    print(i)
""" 

import xml.etree.ElementTree as ET
import re
with open('dic.xml', 'r') as file:
    xml_data = file.read()

# XML metnini ayrıştırma
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

wordMeaning = {}

word = root.find('title').text
text = root.find('.//text').text

wordMeaning["item"] = []
wordMeaning["item"].append({})

wordMeaning["item"][0]["word"] = word
# 'Noun' bölümünü
prepositionSectionPattern =  re.compile(r'== Preposition ==(.+?)\n\n', re.DOTALL)
desPattern = re.compile(r'#(.+?)\n', re.DOTALL)
sentencesPattern = re.compile(r'#:(.+?)\n', re.DOTALL)
des = desPattern.search(text).group(1)
sentences = sentencesPattern.findall(text)
prepositionSection = prepositionSectionPattern.search(text).group(1)

wordMeaning["item"][0]["silkanka"] = {}
print(wordMeaning)










