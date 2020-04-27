import xml.etree.ElementTree as ET


def get_attr(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for country in root.findall('country'):
        # get element from sub tag
        name = country.get('name')
        # get attr from sub tag
        rank = country.find('rank').text
        print(name, rank)


if __name__ == '__main__':
    file = open("../../res/example.xml", "r")
    get_attr(file)
