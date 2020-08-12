LINKS:
Blog: https://blog.jamesfheath.com/2020/08/python-library-xml-with-lxml.html
Code:
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

Searching can also be accomplished using iterators to go through elements until you find what you need. 
iterwalk is a class and part of etree that will take an Element and iterate through the Element's tree. 
**iterwalk**'s iterator returns tuples of events and elements.
When elements are encountered, they can be mutated as needed. 
let's Iterate through the store returning start and end events
We can see the SearingFrost is changed to NewName 

for event, element in etree.iterwalk(store, events=('start', 'end')):
    print(event, element)
    if element.tag == 'SearingFrost':
        element.tag = 'NewName'

# Creating XML objects 
lxml also makes it possible to build your own XML trees from scratch. 
After you start with a root element the XML tree is built mostly with calls to **etree.subelement**. 
The [subelement factory](http://effbot.org/zone/pythondoc-elementtree-ElementTree.htm#elementtree.ElementTree.SubElement-function) takes a parent, tag name, an optional attribute dictionary, and extra keyword arguments if necessary. Let's recreate the store XML document using subelements. 
{% highlight python %}
from lxml import etree

store = etree.Element('store')
inventory = etree.SubElement(store, 'inventory')
# Be mindful when adding assigning variables after
# the .text on SubElement call, as it will return 
# the text and not the Element
etree.SubElement(inventory, 'apples', {'count': '5'}).text = 'Golden Delicious'
etree.SubElement(inventory, 'oranges', {'count': '0'})
employees = etree.SubElement(store, 'employees')
etree.SubElement(employees, 'SearingFrost', {'title': 'writer'})

print(etree.tostring(store, encoding='utf-8', xml_declaration=True, pretty_print=True))
# b'<?xml version=\'1.0\' encoding=\'utf-8\'?><store><inventory>...</store>'
{% endhighlight %}

# Namespaces
Finally, we're going to dig into namespaces with a fair amount of detail. 
[Namespaces](https://www.w3.org/TR/REC-xml-names/#sec-namespaces) are an important part of XML, and **lxml** provides full utility to work with them. 
Namespaces are prefixes for tag names to avoid tag names clashing.
Namespaces use [URI's](https://www.rfc-editor.org/rfc/rfc3986.txt), which are essentially more generic URL's, in that URI's do not need to describe how to locate a resource. 
Namespaces are defined in the root attributes of XML elements that use that namespace (often the root element of an XML document will contain all the namespaces used).
Declarations use a special attribute name **xmlns:**namespace="URI/of/namespace".
Remember, the URI doesn't necessarily have to point to anything real, it just needs to be unique so it doesn't clash with other namespaces. 
{% highlight xml %}
<root xmlns:searing="https://www.jamesfheath.com/xmlnamespaces" xmlns:frost="https://www.jamesfheath.com/xmlnamespaces">
    <searing:store>store with the searing namespace</searing:store>
    <frost:store>store with the frost namespace</frost:store>
</root>
{% endhighlight %}

**lxml** uses *fully qualified* namespaces on etree elements and not just *prefixes* in order to avoid ambiguity and make code easier to write. 
When the final XML document is seraialized, it simply translates back into the prefix as expected.  

| lxml QName | Prefix |
|:-----|:-----|
| {https://www.jamesfheath.com/xmlnamespaces}*tagname* | searing |

**lxml** [stores namespaces in dictionaries](https://lxml.de/tutorial.html#namespaces) in the *nsmap* attribute. 

{% highlight python %}
namespace_xml_string = '<root xmlns:searing="https://www.jamesfheath.com/xmlnamespace1" xmlns:frost="https://www.jamesfheath.com/xmlnamespace2"><searing:store>store with the searing namespace</searing:store><frost:store>store with the frost namespace</frost:store></root>'

namespace_xml_root = etree.fromstring(namespace_xml_string)

print(namespace_xml_root.nsmap)
# {'searing': 'https://www.jamesfheath.com/xmlnamespace1',
#  'frost': 'https://www.jamesfheath.com/xmlnamespace2'}

for e in namespace_xml_root:
    print(e.tag)
    print(e.prefix)
# {https://www.jamesfheath.com/xmlnamespace1}store
# searing
# {https://www.jamesfheath.com/xmlnamespace2}store
# frost
{% endhighlight %}

To create XML elements with namespaces, you can add the full qualified string as a tag, though this is a lot of typing. 

{% highlight python %}
nsmap = {'searing': 'https://www.jamesfheath.com/xmlnamespace1', 'frost': 'https://www.jamesfheath.com/xmlnamespace2'}

root = etree.Element('root', nsmap=nsmap)
searing_store = etree.SubElement(root, '{https://www.jamesfheath.com/xmlnamespace1}store')
frost_store = etree.SubElement(root, '{https://www.jamesfheath.com/xmlnamespace2}store')

print(etree.tostring(root, pretty_print=True))
# <root xmlns:searing="https://www.jamesfheath.com/xmlnamespace1" xmlns:frost="https://www.jamesfheath.com/xmlnamespace2">
#    <searing:store/>
#    <frost:store/>
# </root>
{% endhighlight %}

Using [**etree.QName**](https://lxml.de/api/lxml.etree.QName-class.html) constructors, it's easy to build qualified names using your namespace map. 

{% highlight python %}
nsmap = {'searing': 'https://www.jamesfheath.com/xmlnamespace1', 'frost': 'https://www.jamesfheath.com/xmlnamespace2'}

root = etree.Element('root', nsmap=nsmap)
searing_store = etree.SubElement(root, etree.QName(nsmap['searing'], 'store'))
frost_store = etree.SubElement(root, etree.QName(nsmap['frost'], 'store'))

print(etree.tostring(root, pretty_print=True))
# <root xmlns:searing="https://www.jamesfheath.com/xmlnamespace1" xmlns:frost="https://www.jamesfheath.com/xmlnamespace2">
#    <searing:store/>
#    <frost:store/>
# </root>

{% endhighlight %}

# Conclusion
XML is a complicated topic, and there are a lot of details with stylesheets that need to be accounted for when working with complex elements. 
**lxml** will give you the tools to operate on XML, and we've gone over most of the tools you will need for 90% of you XML work. 

# Thanks for Watching
Thanks for watching this quick introduction to Types and Variables in Python. 
Python's type system is incredibly flexible and we've only scratched the surface here. 
Links to the code and my blog post on types and variables are in the description. 
I'll see everyone next time. 