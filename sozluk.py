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

dictionary["words"][0]["definitions"].appned({})
""" 

import xml.etree.ElementTree as ET
import re

def specialCase(index: int, firsItem, dictionary: str):
   if index == 1:
       parsedText = re.sub(r"#: |''(.*?)''|#", r"\1", firsItem) #regex parse
       dictionary["words"][-1]["definitions"][-1]["properties"].append({})
       dictionary["words"][-1]["definitions"][-1]["properties"][-1]["sentences"] = []
       dictionary["words"][-1]["definitions"][-1]["properties"][-1]["sentences"].append(parsedText)
       

def sectionParse(value, word: str, dictionary: str, sectionName: str):
    print("f sectionParse fonksiyonumuz açıldıı. kelimemiz:" + word)
    section_name = "== " + sectionName + " =="
    value = value + "\n\n"
    if section_name in value:
        index = 0
        dictionary["words"][-1]["definitions"].append({})
        dictionary["words"][-1]["definitions"][-1]["partOfSpeech"] = sectionName
        dictionary["words"][-1]["definitions"][-1]["properties"] = []
        print("found {} in words".format(sectionName)) 
        prepositionSectionPattern = re.compile(f'== {sectionName} ==(.+?)\n\n', re.DOTALL)
        prepositionText = prepositionSectionPattern.search(value).group(1)
        prepositionSectionItemsPattern = re.compile(r'#.*?(?=\n|$)', re.DOTALL)
        items = prepositionSectionItemsPattern.findall(prepositionText)
        #print(items)
        for i in items:
            index = index + 1
            if "#:" in i:
                if index == 1:
                    specialCase(index, i, dictionary)
                else:
                    print("bakılan", i)
                    parsedText = re.sub(r"#: |''(.*?)''|#", r"\1", i) #regex parse
                    print("parsed text:", parsedText)
                    dictionary["words"][-1]["definitions"][-1]["properties"][-1]["sentences"].append(parsedText)
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
                parsedText = re.sub(r"#: |''(.*?)''|#", r"\1", i) #regex parce
                dictionary["words"][-1]["definitions"][-1]["properties"].append({})
                dictionary["words"][-1]["definitions"][-1]["properties"][-1]["definition"] = parsedText
                dictionary["words"][-1]["definitions"][-1]["properties"][-1]["sentences"] = []

        
        



    else:
        print("nor founds {} in words".format(sectionName)) 

with open('simplewiktionary-20230701-pages-articles-multistream.xml', 'r',  encoding='utf-8') as file:
    xml_data = file.read()

# XML metnini ayrıştırma
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

dictionary = {}
dictionary["words"] = []
textElements = root.findall('.//page')
print(len(textElements))
for i in textElements:
    word = i.find('title').text
    text = i.find('.//text').text
    dictionary["words"].append({})
    dictionary["words"][-1]["word"] = word
    dictionary["words"][-1]["definitions"]=[]

    sectionParse(text, word, dictionary, "Preposition")
    sectionParse(text, word, dictionary, "Noun")
    sectionParse(text, word, dictionary, "Subordinator")
    sectionParse(text, word, dictionary, "Verb")
    sectionParse(text, word, dictionary, "Determiner")
    sectionParse(text, word, dictionary, "Adjective")
    sectionParse(text, word, dictionary, "Interjection")
    sectionParse(text, word, dictionary, "Symbol")

    sectionParse(text, word, dictionary, "Expression")
    sectionParse(text, word, dictionary, "Proper noun")
    sectionParse(text, word, dictionary, "Abbreviation")
    sectionParse(text, word, dictionary, "Adverbs")


print(dictionary)














