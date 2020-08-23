LINKS:
Blog: https://blog.jamesfheath.com/2020/08/python-library-xml-with-lxml.html
Code: https://github.com/JamesFHeath/jamesfheathblog_code/blob/master/Python%20Libraries/xml_with_lxml.py
lxml: https://lxml.de/
XPath Tutorial: https://www.w3schools.com/xml/xpath_intro.asp

# Intro
Hi Everyone, SearingFrost here in the Python Library.
Today we'll be checking out the lxml library, which is a 3rd party library for working with XML. 
XML stands for eXtensible Markup Language, and it's a base for defining other markup languages.
HTML is the most well known XML, being the basis for all webpages. 
Python has a standard xml library, but lxml has some nice features such as full XPath support and nice factory functions that make it a better choice. 
This video will go over not only lxml, but XML in general. 

# Element Tree
The goal of lxml is to work with XML using the ElementTree API, stored in lxml.etree.
Every XML tag is an element in the tree, and each element contains a name and potentially attributes, child elements, and text. 
Element tree attributes work like Python dictionaries, and child elements are in a Python list. 
This allows for standard Python syntax to work seamlessly with etree elements. 

# Parsing and Serializing XML
lxml can read from files or string objects of XML and parse them into etree elements. 
Let's take this simple XML string and put it into an etree element using the fromstring fuction.
Be sure to define the string as binary if you have the xml declaration tag
The store elemnt refers to the root of our xml document. 

 <?xml version="1.0" encoding="UTF-8"?>
 <store>
    <inventory>
        <apples count="5">Golden Delicious</apples>
        <oranges count="0"/>
    </inventory>
    <employees>
        <employee title="writer">SearingFrost</employee>
    </employees>
 </store>

xml_string = '<?xml version="1.0" encoding="UTF-8"?><store><inventory><apples count="5">Golden Delicious</apples><oranges count="0"/></inventory><employees><employee title="writer">SearingFrost</employee></employees></store>'

store = etree.fromstring(xml_string)

XML travels in string format, so the ability to transform **lxml** elements into strings is vital. 
Luckily, it is very simple with the tostring function. 
tostring just reverses the fromstring function. 
We can choose the encoding, and whether we want an xml declaration or pretty printing.

etree.tostring(store, encoding='utf-8', xml_declaration=True, pretty_print=True)


# Searching and Modifying XML 
The most effective way to search for XML Elements is with XPath.
XPath is fully implemented in lxml, and if you know what tags you are searching for XPath is the way to go.
Give the XPath expression to the element you wish to search using the element's xpath method. 
Note that the xpath method always returns a list of results, even if no elements or only one element is found. 
Let's use some xpaths on our store elements. 
We can get the store elemenent by accessing it directly. 
Or we can get all of store's children using a wildcard. 
Check the link in the video description for the W3School's xpath tutorial if you aren't familiar with the syntax. 

store.xpath('/store')
store.xpath('/store/*')

Searching can also be accomplished using iterators with the iterwalk class. 
iterwalk is part of etree that and it takes an Element and iterate through the Element's tree. 
The iterator returns tuples of events and elements.
When elements are encountered, they can be mutated as needed. 
Let's Iterate through the store returning start and end events
We can see the SearingFrost is changed to NewName 

for event, element in etree.iterwalk(store, events=('start', 'end')):
    print(event, element)
    print(element.text)
    if element.text == 'SearingFrost':
        element.text = 'NewName'

# Creating XML objects 
lxml also makes it possible to build your own XML trees from scratch. 
After you start with a root element the XML tree is built mostly with calls to etree.subelement.
The subelement factory takes a parent element, tag name, an optional attribute dictionary, and extra keyword arguments if necessary. 
Let's recreate the store XML document using subelements. 
We will start with the store element.
Then inventory.
Then we can add the apples and oranges elements with their text
Then the employee searingfrost
It's just as simple as that

from lxml import etree

store = etree.Element('store')
inventory = etree.SubElement(store, 'inventory')
etree.SubElement(inventory, 'apples', {'count': '5'}).text = 'Golden Delicious'
etree.SubElement(inventory, 'oranges', {'count': '0'})
employees = etree.SubElement(store, 'employees')
etree.SubElement(employees, 'SearingFrost', {'title': 'writer'})

print(etree.tostring(store, encoding='utf-8', xml_declaration=True, pretty_print=True))

# Namespaces
Finally, we're going to dig into namespaces with a fair amount of detail. 
Namespaces are an important part of XML, and lxml provides full utility to work with them. 
Namespaces are prefixes for tag names to avoid tag names clashing.
They  are defined by URI's, which are essentially more generic URL's, in that URI's do not need to describe how to locate a resource. 
Namespaces are defined in the attribute of XML elements, usually at the root level.  
Namespace Declarations use a special attribute name xmlns:namespace="URI/of/namespace.
Remember, the URI doesn't necessarily have to point to anything real, it just needs to be unique so it doesn't clash with other namespaces. 


<root xmlns:searing="https://www.jamesfheath.com/xmlnamespace1" xmlns:frost="https://www.jamesfheath.com/xmlnamespace2">
    <searing:store>store with the searing namespace</searing:store>
    <frost:store>store with the frost namespace</frost:store>
</root>

lxml uses *fully qualified* namespaces on etree elements and not just *prefixes* in order to avoid ambiguity and make code easier to write. 
When the final XML document is seraialized, it simply translates back into the prefix as expected.  

| lxml QName | Prefix |
|:-----|:-----|
| {https://www.jamesfheath.com/xmlnamespace1}store | searing |
| {https://www.jamesfheath.com/xmlnamespace2}store | frost |

Let's look at how lxml works with namespaces. 
lxml stores namespaces in dictionaries in the *nsmap* attribute. 
We can see the nsmap matches the table we looked at earlier.
And when we iterate through the tags in our xml we see that tag and prefix

namespace_xml_string = '<root xmlns:searing="https://www.jamesfheath.com/xmlnamespace1" xmlns:frost="https://www.jamesfheath.com/xmlnamespace2"><searing:store>store with the searing namespace</searing:store><frost:store>store with the frost namespace</frost:store></root>'

namespace_xml_root = etree.fromstring(namespace_xml_string)

namespace_xml_root.nsmap

for e in namespace_xml_root:
    print(f'Tag: {e.tag}')
    print(f'Prefix: {e.prefix}')

To create XML elements with namespaces, you can add the full qualified string as a tag, though this is a lot of typing. 

nsmap = {'searing': 'https://www.jamesfheath.com/xmlnamespace1', 'frost': 'https://www.jamesfheath.com/xmlnamespace2'}

root = etree.Element('root', nsmap=nsmap)
searing_store = etree.SubElement(root, '{https://www.jamesfheath.com/xmlnamespace1}store')
frost_store = etree.SubElement(root, '{https://www.jamesfheath.com/xmlnamespace2}store')

etree.tostring(root, pretty_print=True)

Using etree.QName constructors, it's easy to build qualified names using your namespace map. 

nsmap = {'searing': 'https://www.jamesfheath.com/xmlnamespace1', 'frost': 'https://www.jamesfheath.com/xmlnamespace2'}

root = etree.Element('root', nsmap=nsmap)
searing_store = etree.SubElement(root, etree.QName(nsmap['searing'], 'store'))
frost_store = etree.SubElement(root, etree.QName(nsmap['frost'], 'store'))


# Thanks for Watching
Thanks for joining me in the python library to learn about LXML
XML is a complicated topic, and there are a lot of details with stylesheets that need to be accounted for when working with complex elements. 
lxml will give you the tools to operate on XML, and we've gone over most of the tools you will need for 90% of you XML work. 
Links to the code and my blog post on lxml are in the description. 
I'll see everyone next time. 