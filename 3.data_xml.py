from xml.etree import ElementTree as ET

# 直接解析xml文件
tree = ET.parse("data.xml")

# 获取xml文件的根节点
root = tree.getroot()
print(root)

