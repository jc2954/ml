import os
import xml.etree.ElementTree as ET
import csv
import pandas as pd
import glob

for f in glob.glob('annotations' + '/*.xml'):
    tree = ET.parse(f)
    root = tree.getroot()
    xml_list = []
    filename = root.find("filename").text

    for size in root.findall('size'):
        width = size.find("width").text
        height = size.find('height').text
        print(width)
    for i in root.findall('object'):
        classname = i.find("name").text
    for n in i.findall("bndbox"):
        xmin = n.find("xmin").text
        ymin = n.find("ymin").text
        xmax = n.find("xmax").text
        ymax = n.find("ymax").text

    print(xmin)

    column_name = ['filename', 'width', 'height',
                    'class', 'xmin', 'ymin', 'xmax', 'ymax']

    value = (filename,int(width),int(height),classname,int(xmin),int(ymin),int(xmax),int(ymax))

    xml_list.append(value)

xml_df = pd.DataFrame(xml_list, columns=column_name)

xml_df.to_csv('labels.csv', index=None)

