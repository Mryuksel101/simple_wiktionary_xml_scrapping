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
    word: ....
    [
        [
            {   
                des : ...
                sentences : [
                
                ]
            }
        ]
        type: .......
    ]
}

for i, item in enumerate(noun_sections, 1):
    print(f"== Noun {i} ==\n{item}\n")

pattern = re.compile(r'== Noun ==(.+?)\n\n', re.DOTALL)
noun_sections = pattern.findall(text)
""" 

import xml.etree.ElementTree as ET
import re
with open('dic.xml', 'r') as file:
    xml_data = file.read()

# XML metnini ayrıştırma
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

word = root.find('title').text
text = root.find('.//text').text

# 'Noun' bölümünü
desPattern = re.compile(r'#(.+?)\n', re.DOTALL)
sentencesPattern = re.compile(r'#:(.+?)\n', re.DOTALL)
des = desPattern.search(text).group(1)
sentences = sentencesPattern.findall(text)

for i in sentences:
    print(i)









