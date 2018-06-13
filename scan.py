#!/home/jcasper/python3/python
import re
import os.path
import sys
import csv
import itertools

"""
  Finds all function signatures in a file
  @param filename string
  @return dict with key className value set of function signatures
"""
def scanFile(filename):

  classPattern = re.compile(r'(?:class)\s+(\w+)')
  functionPattern = re.compile(r'(?:public|protected|private)?\s*(?:static\s+)?(?:function)\s+(\w+)\(')
  callPattern = re.compile(r'->(\w+)\(')
  functions = []
  calls = []
  className = None
  blockComment = 0
  with open(filename) as f:
    for line in f:
      if '/*' in line:
        blockComment += 1
      if '*/' in line:
        blockComment -= 1
      if blockComment > 0:
        continue
      if '//' in line:
        continue
      if className is None:
        className = classPattern.search(line)
      functionResult = functionPattern.search(line)
      callResult = callPattern.search(line)
      if functionResult:
        functions.append(functionResult.group(1))
      if callResult:
        calls.append(callResult.group(1))
  return {className.group(1) if className else None : [{f for f in functions}, {c for c in calls}]}

"""
  Writes data to a filename.csv
  @param data dict to be written
  @return void
"""
def writeCsv(data):

  with open(next(iter(data)) + '.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(data.keys())
    writer.writerows(itertools.zip_longest(*data.values()))

if __name__ == '__main__':
  try:
    result = scanFile(os.path.expanduser(sys.argv[1])) 
  except IsADirectoryError:
    print('is a dir but why? sys.argv[1]')
  writeCsv(result) 
