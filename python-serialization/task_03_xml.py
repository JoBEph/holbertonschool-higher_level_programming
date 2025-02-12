#!/usr/bin/env python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):

    root = ET.element("data")
    
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()
