#!/usr/bin/env python
"""
 This file finds all the results.xml files following a test run,
 combines them into a single xml file, and transforms this xml file
 into html using an xslt transform. The resulting html file is then 
 converted to pdf.
"""

import os, os.path
import xmlcombine
import subprocess
import lxml.etree as ET

source_files = 'results.xml'
combined_file = 'combined.xml'
transform_file = 'utils/results.xsl'
html_file = 'combined_results.html'
pdf_file = 'Test_Results.pdf'


### check all the files exist
def FileExists(fileName):
  if os.path.isfile(fileName):
    return True
  else:
    return False


### Find all the results files.
def GetResultsFiles():
  print "Find all results files"
  results_files = []

  for root, dirs, files in os.walk('.'):
    for f in files:
      fullpath = os.path.join(root, f)
      if f.endswith(source_files):
        results_files.append(fullpath)
  print "found " + str(len(results_files)) + " results files"
  if len(results_files) == 0:
    print "Error: No results files found! Exiting"
    exit(-1)
  return results_files


### combine the files
def CombineResultsFiles(results_files):
  print "Combine the results files"
  with open (combined_file, 'w') as f:
    # write header, with link to xslt file
    f.write ('<?xml version="1.0" encoding="UTF-8"?> \
         <?xml-stylesheet type="text/xsl" href="results.xsl"?>')
    # write actual file
    f.write(xmlcombine.combine (results_files))
  if not FileExists(combined_file):
    print "Error: Failed to create combined xml file."
    exit(-1)

### convert to html.
def ConvertToHtml():
  print "Transform xml to html"
  if not FileExists(transform_file):
    print "Transform file not found!"
    exit(-1)

  dom = ET.parse(combined_file)
  xslt = ET.parse(transform_file)
  # do the transform
  transform = ET.XSLT(xslt)
  newdom = transform(dom)
  # write out to html file
  with open (html_file, 'w') as f:
    f.write (ET.tostring(newdom, pretty_print=True))

  if not FileExists(html_file):
    print "Failed to created html file"
    exit(-1)

### convert to pdf
def ConvertToPdf():
  print "convert to pdf for publishing"
  subprocess.call (['/usr/local/bin/wkhtmltopdf', html_file, pdf_file]) 
  if not FileExists(pdf_file):
    print "Failed to Create pdf file"
    exit(-1)

######
CombineResultsFiles(GetResultsFiles())
ConvertToHtml()
ConvertToPdf()
exit(0)

