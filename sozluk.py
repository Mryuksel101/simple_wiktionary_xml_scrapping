""" 
{
    word: ....
    [
        {   
            definition : ....
            sentences :
                [         
                    
                ]
            type: .......
        }
    ]
}

{
  words:  [
        {
            word: ....
                
                definitions: [
                    {   bizde aynı partOfSpeech'in birden fazla tanımları ve cümle örnekleri olabilir
                
                        properties [
                            property : {
                                definition : ...
                                sentences : [
                                
                                ]
                            }
                        ]
                        partOfSpeech: .......
                    }
                    
                    }
                        properties [
                            {
                                definition : ...
                                sentences : [
                                
                                ]
                            }
                        ]
                        partOfSpeech: .......
                    }
                ]
            ]
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

wordMeaning["words"][0]["definitions"].appned({})
""" 

import xml.etree.ElementTree as ET
import re

def sectionParse(value, word: str, wordMeaning: str, sectionName: str):
    section_name = "== " + sectionName + " =="
    if section_name in value:
        wordMeaning["words"][0]["definitions"].append({})
        wordMeaning["words"][0]["definitions"][-1]["partOfSpeech"] = sectionName
        wordMeaning["words"][0]["definitions"][-1]["properties"] = []
        print("found {} in words".format(sectionName)) 
        prepositionSectionPattern = re.compile(f'== {sectionName} ==(.+?)\n\n', re.DOTALL)
        prepositionText = prepositionSectionPattern.search(value).group(1)
        prepositionSectionItemsPattern = re.compile(r'#.*?(?=\n|$)', re.DOTALL)
        items = prepositionSectionItemsPattern.findall(prepositionText)
        #print(items)
        for i in items:
            if ":" in i:
                #print("var", i)
                wordMeaning["words"][0]["definitions"][-1]["properties"][-1]["sentences"].append(i)
            else:
                #definition kısmına ekle çıkan şeyi
                """ 
                1. item ({{P+NP}}, ''after the noun'' & {{P-comp}}) If A is '''above''' B, A is [[higher]] than or [[before]] B, but not touching B.
                2. item : ''In a newspaper, the title of a story is usually '''above''' the story.''
                eğer başlangıçta ":" yoksa diziye yeni bir property map eklenmeli
                    map'ın "definition" key'i doldurulmalı
                    map'ın "sentences" key'i doldurulmalı

                """ 
                #print("yok", i)
                wordMeaning["words"][0]["definitions"][-1]["properties"].append({})
                wordMeaning["words"][0]["definitions"][-1]["properties"][-1]["definition"] = i
                wordMeaning["words"][0]["definitions"][-1]["properties"][-1]["sentences"] = []

        



    else:
        print("nor founds {} in words".format(sectionName)) 

with open('dic.xml', 'r') as file:
    xml_data = file.read()

# XML metnini ayrıştırma
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

wordMeaning = {}

word = root.find('title').text
text = root.find('.//text').text

wordMeaning["words"] = []
wordMeaning["words"].append({})

wordMeaning["words"][0]["word"] = word
wordMeaning["words"][0]["definitions"]=[]

# 'Noun' bölümünü
prepositionSectionPattern =  re.compile(r'== Preposition ==(.+?)\n\n', re.DOTALL)
definitionPattern = re.compile(r'#(.+?)\n', re.DOTALL)
sentencesPattern = re.compile(r'#:(.+?)\n', re.DOTALL)
definition = definitionPattern.search(text).group(1)
sentences = sentencesPattern.findall(text)
prepositionSection = prepositionSectionPattern.search(text).group(1)

sectionParse(text, word, wordMeaning, "Preposition")
sectionParse(text, word, wordMeaning, "Noun")
sectionParse(text, word, wordMeaning, "Subordinator")
sectionParse(text, word, wordMeaning, "Verb")

print(wordMeaning)







