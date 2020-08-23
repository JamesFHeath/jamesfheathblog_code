from lxml import etree

# Parsing and Serializing XML
xml_string = '<?xml version="1.0" encoding="UTF-8"?><store><inventory><apples count="5">Golden Delicious</apples><oranges count="0"/></inventory><employees><employee title="writer">SearingFrost</employee></employees></store>'

store = etree.fromstring(xml_string)

etree.tostring(store, encoding='utf-8', xml_declaration=True, pretty_print=True)


# Searching and Modifying XML 
store.xpath('/store')
store.xpath('/store/*')

for event, element in etree.iterwalk(store, events=('start', 'end')):
    print(event, element)
    print(element.text)
    if element.text == 'SearingFrost':
        element.text = 'NewName'

# Creating XML objects 
store = etree.Element('store')
inventory = etree.SubElement(store, 'inventory')
etree.SubElement(inventory, 'apples', {'count': '5'}).text = 'Golden Delicious'
etree.SubElement(inventory, 'oranges', {'count': '0'})
employees = etree.SubElement(store, 'employees')
etree.SubElement(employees, 'SearingFrost', {'title': 'writer'})

print(etree.tostring(store, encoding='utf-8', xml_declaration=True, pretty_print=True))

# Namespaces
namespace_xml_string = '<root xmlns:searing="https://www.jamesfheath.com/xmlnamespace1" xmlns:frost="https://www.jamesfheath.com/xmlnamespace2"><searing:store>store with the searing namespace</searing:store><frost:store>store with the frost namespace</frost:store></root>'

namespace_xml_root = etree.fromstring(namespace_xml_string)

namespace_xml_root.nsmap

for e in namespace_xml_root:
    print(f'Tag: {e.tag}')
    print(f'Prefix: {e.prefix}')


nsmap = {'searing': 'https://www.jamesfheath.com/xmlnamespace1', 'frost': 'https://www.jamesfheath.com/xmlnamespace2'}

root = etree.Element('root', nsmap=nsmap)
searing_store = etree.SubElement(root, '{https://www.jamesfheath.com/xmlnamespace1}store')
frost_store = etree.SubElement(root, '{https://www.jamesfheath.com/xmlnamespace2}store')

etree.tostring(root, pretty_print=True)

# QName constructors
nsmap = {'searing': 'https://www.jamesfheath.com/xmlnamespace1', 'frost': 'https://www.jamesfheath.com/xmlnamespace2'}

root = etree.Element('root', nsmap=nsmap)
searing_store = etree.SubElement(root, etree.QName(nsmap['searing'], 'store'))
frost_store = etree.SubElement(root, etree.QName(nsmap['frost'], 'store'))
