#! /usr/bin/python

import glob
import os
import os.path
import sys

HEADING_STR = '#!AMR\n'

def convert_aud_to_amr(in_fname):
  content = None
  with open(in_fname, 'rb') as f:
    content = f.read()
  out_fname = '%s.amr' %(os.path.basename(in_fname))
  print '%s --> %s' %(in_fname, out_fname)
  with open(out_fname, 'wb') as f:
    f.write(HEADING_STR)
    f.write(content)

def main():
  if len(sys.argv) < 2:
    in_files = glob.glob('*.aud')
    for in_file in in_files:
      convert_aud_to_amr(in_file)
  else:
    convert_aud_to_amr(sys.argv[1])

if __name__ == '__main__':
  main()
