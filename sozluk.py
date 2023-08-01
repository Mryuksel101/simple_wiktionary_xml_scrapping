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
  silitem:  [
        {
            word: ....
            silkanka: [
                {   
                    des : ...
                    sentences : [
                    
                    ]
                }
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

if "== Preposition ==" in text:

wordMeaning["silitem"][0]["silkanka"].appned({})
""" 

import xml.etree.ElementTree as ET
import re

def prepositionSectionParse(value, word, wordMeaning):
    if "== Preposition ==" in value:
        print("metinde prepositionSectionParse bulundu")
        prepositionSectionPattern = re.compile(r'== Preposition ==(.+?)\n\n', re.DOTALL)
        prepositionText = prepositionSectionPattern.search(value).group(1)
        wordMeaning["silitem"][0]["type"] = "Preposition"
        

        prepositionSectionItemsPattern = re.compile(r'#(.+?)\n', re.DOTALL)
        items = prepositionSectionItemsPattern.findall(prepositionText)
        for i in items:
            if ":" in i:
                wordMeaning["silitem"][0]["silkanka"][-1]["sentences"].append(i)
            else:
                #des kısmına ekle çıkan şeyi
                """ 
                1. item ({{P+NP}}, ''after the noun'' & {{P-comp}}) If A is '''above''' B, A is [[higher]] than or [[before]] B, but not touching B.
                2. item : ''In a newspaper, the title of a story is usually '''above''' the story.''
                eğer başlangıçta ":" yoksa diziye yeni bir map eklenmeli
                    map'ın "des" key'i doldurulmalı
                    map'ın "sentences" key'i doldurulmalı

                """ 
                print("yok", i)
                wordMeaning["silitem"][0]["silkanka"].append({})
                wordMeaning["silitem"][0]["silkanka"][-1]["des"] = i
                wordMeaning["silitem"][0]["silkanka"][-1]["sentences"] = []





    else:
        print("metinde prepositionSectionParse bulunmadı")

with open('dic.xml', 'r') as file:
    xml_data = file.read()

# XML metnini ayrıştırma
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

wordMeaning = {}

word = root.find('title').text
text = root.find('.//text').text

wordMeaning["silitem"] = []
wordMeaning["silitem"].append({})

wordMeaning["silitem"][0]["word"] = word
wordMeaning["silitem"][0]["silkanka"]=[]

# 'Noun' bölümünü
prepositionSectionPattern =  re.compile(r'== Preposition ==(.+?)\n\n', re.DOTALL)
desPattern = re.compile(r'#(.+?)\n', re.DOTALL)
sentencesPattern = re.compile(r'#:(.+?)\n', re.DOTALL)
des = desPattern.search(text).group(1)
sentences = sentencesPattern.findall(text)
prepositionSection = prepositionSectionPattern.search(text).group(1)

prepositionSectionParse(text, word, wordMeaning)

print(wordMeaning)







