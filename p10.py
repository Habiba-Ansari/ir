import xml.etree.ElementTree as ET
from openpyxl import Workbook

# Step 1: read XML file
tree = ET.parse("input.xml")
root = tree.getroot()

# Step 2: create excel file
wb = Workbook()
ws = wb.active
ws.append(["Source", "Target"])  # headers

# Step 3: extract links
for page in root.findall("page"):
    source = page.get("url")

    for link in page.findall("link"):
        target = link.text
        ws.append([source, target])

# Step 4: save excel
wb.save("output.xlsx")

print("Web graph saved to Excel!")
