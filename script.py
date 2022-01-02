import xml.etree.ElementTree as ET

tree = ET.parse('cripto.xml')
root = tree.getroot()

# print(ET.tostring(root))
# coin = root.get('coin')
# print(f'${coin}')

# set 'launched' attribute
# root.set('launched', '20211231')
# print(root.attrib)

# Save updated XML
# tree.write('cripto.xml')

# Add 'id' attribute to each investor
# id = 1 
# for investor in tree.findall('investor'):
#     investor.set('id', str(id))
#     id += 1
#tree.write('cripto.xml')

# Delete 'id' attributes
# for investor in tree.findall('investor'):
#     del(investor.attrib['id'])

# tree.write('cripto.xml')

#Add investor #1
# investor1 = ET.fromstring('<investor>Allen Duffy</investor>')
# root.append(investor1)
# tree.write('cripto.xml')

#Add investor #2 
# investor2 = ET.Element('investor')
# investor2.text = 'Karl Amber'
# root.append(investor2)

#Add ids once more
# for(id,investor) in enumerate(root.findall('investor')):
#     investor.set('id', str(id))

#Select investor 4
investor = root.find(".//investor[@id='4']")
print(investor.text)


#tree.write('cripto.xml')