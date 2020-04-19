import xml.etree.ElementTree as ET
tree = ET.parse('sample.xml')
root = tree.getroot()
books = list(root)
for book in books:
    check = book.find("hardcover")
    if check is None:
        root.remove(book)
tree.write("result.xml")