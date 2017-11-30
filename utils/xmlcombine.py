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

    for filename in files:
        testset = str(os.path.abspath(filename))
        testset = testset.encode("string_escape").rsplit('/', 2)[1]
        e = ElementTree.Element("testset")
        data = ElementTree.parse(filename).getroot()

        skips = int(data.attrib.get('skips'))
        tests = int(data.attrib.get('tests'))
        errors = int(data.attrib.get('errors'))
        failures = int(data.attrib.get('failures'))

        e.set('tests', str(tests))
        e.set('skips', str(skips))
        e.set('errors', str(errors))
        e.set('failures', str(failures))
        e.set('passes', str(tests - skips - failures))
        e.set('name', testset)

        total_skips = total_skips + skips
        total_tests = total_tests + tests
        total_errors = total_errors + errors
        total_failures = total_failures + failures

        for properties in data.findall('properties'):
            e.append(properties)
            data.remove(properties)

        for testcase in data.findall('testcase'):
            e.append(testcase)
            data.remove(testcase)

        data.append(e)

        if first is None:
            first = data
        else:
            first.extend(data)
    if first is not None:
        first.set('tests', str(total_tests))
        first.set('skips', str(total_skips))
        first.set('errors', str(total_errors))
        first.set('failures', str(total_failures))
        first.set('passes', str(total_tests - total_skips - total_failures))
        return ElementTree.tostring(first)

if __name__ == "__main__":
    combine(sys.argv[1:])
