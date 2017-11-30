#!/usr/bin/env python
import sys
import os
from xml.etree import ElementTree

def combine(files):
    first = None
    total_skips = 0
    total_tests = 0
    total_errors = 0
    total_failures = 0

    # loop through input files
    for filename in files:
        testset = str(os.path.abspath(filename))
        testset = testset.encode("string_escape").rsplit('/', 2)[1]
        # the incoming xml
        data = ElementTree.parse(filename).getroot()
        # create a new element for each testset
        e = ElementTree.Element("testset")

        # get test result data from the input file
        skips = int(data.attrib.get('skips'))
        tests = int(data.attrib.get('tests'))
        errors = int(data.attrib.get('errors'))
        failures = int(data.attrib.get('failures'))

        # set the value in the new "testset" element
        e.set('tests', str(tests))
        e.set('skips', str(skips))
        e.set('errors', str(errors))
        e.set('failures', str(failures))
        e.set('passes', str(tests - skips - failures))
        e.set('name', testset)

        # collate totals
        total_skips = total_skips + skips
        total_tests = total_tests + tests
        total_errors = total_errors + errors
        total_failures = total_failures + failures

        # if the file has a properties element append it to new element, 
        # then remove it from existing element
        for properties in data.findall('properties'):
            e.append(properties)
            data.remove(properties)

        # if the file has a testcase element append it to new element, 
        # then remove it from existing element
        for testcase in data.findall('testcase'):
            e.append(testcase)
            data.remove(testcase)

        # add our new element to the output.
        data.append(e)

        # if the first element hasn't been written to yet, add our data element to it.
        # if it has, append our latest data element
        if first is None:
            first = data
        else:
            first.extend(data)
    # append the totals to the file if it's not empty
    if first is not None:
        first.set('tests', str(total_tests))
        first.set('skips', str(total_skips))
        first.set('errors', str(total_errors))
        first.set('failures', str(total_failures))
        first.set('passes', str(total_tests - total_skips - total_failures))
        return ElementTree.tostring(first)

if __name__ == "__main__":
    combine(sys.argv[1:])
