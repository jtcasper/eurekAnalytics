#!/home/jcasper/python3/python
import re
import os.path
import sys

"""
  Finds all function signatures in a file
  @param filename string
  @return dict with key className value set of function signatures
"""
def scanFile(filename):

  classPattern = re.compile(r'(?:class)\s+(\w+)')
  functionPattern = re.compile(r'(?:public|protected|private)?\s*(?:static\s+)?(?:function)\s+(\w+)\(')
  functions = []
  className = None
  with open(filename) as f:
    for line in f:
      if className is None:
        if '*' in line:
          continue
        className = classPattern.search(line)
      result = functionPattern.search(line)
      if result:
        functions.append(result.group(1))
  return {className.group(1) if className else None : {f for f in functions}}

if __name__ == '__main__':
  result = scanFile(os.path.expanduser(sys.argv[1])) 
  print(result)
