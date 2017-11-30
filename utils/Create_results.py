#!/usr/bin/env python
# This file finds all the results.xml files following a test run,
# combines them into a single xml file, and transforms this xml file
# into html using an xslt transform. The resulting html file is then 
# converted to pdf.

import os, os.path
import glob
import xmlcombine
import subprocess
import lxml.etree as ET

source_files = 'results.xml'
combined_file = 'combined.xml'
transform_file = 'utils/results.xsl'
html_file = 'combined_results.html'
pdf_file = 'Test_Results.pdf'


# Find all the results files.
results_files = []
for root, dirs, files in os.walk('.'):
  for f in files:
    fullpath = os.path.join(root, f)
    if f.endswith(source_files):
      results_files.append(fullpath)

# combine the files
with open (combined_file, 'w') as f:
  # write header, with link to xslt file
  f.write ('<?xml version="1.0" encoding="UTF-8"?> \
       <?xml-stylesheet type="text/xsl" href="results.xsl"?>')
  # write actual file
  f.write(xmlcombine.combine (results_files))

# convert to html.
dom = ET.parse(combined_file)
xslt = ET.parse(transform_file)
# do the transform
transform = ET.XSLT(xslt)
newdom = transform(dom)
# write out to html file
with open (html_file, 'w') as f:
  f.write (ET.tostring(newdom, pretty_print=True))

# convert to pdf
subprocess.call (['/usr/local/bin/wkhtmltopdf', html_file, pdf_file]) 
