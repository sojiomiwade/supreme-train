'''
Given a file of strings, sometimes there's a " character. Remove all such, and then remove the duplicate files
abc
def
abc
github

read it all into a string, then use a set to ignore something if it already exists
optimize: read one string at a time, to avoid memory issues



'''
import sys


def remove_duplicates(file_obj) -> None:
    res = set()
    for line in file_obj:
        res.add(line.replace('"','').replace('\n',''))
    
    for item in res:
        print(item)

with open(sys.argv[1]) as openfileobject:
    remove_duplicates(openfileobject)
