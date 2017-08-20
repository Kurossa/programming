#!/usr/bin/python3

import sys, getopt

def pirnt_help():
   print('Help:')
   print('test.py -i <inputfile> -o <outputfile>')

def parse_args(argv):
   try:
      opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
   except getopt.GetoptError:
      pirnt_help()
      sys.exit(2)

   is_input_file = False
   is_output_file = False

   inputfile = ''
   outputfile = ''

   for opt, arg in opts:
      if opt == '-h':
         pirnt_help()
         sys.exit()
      elif opt in ("-i", "--ifile"):
         is_input_file = True
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         is_output_file = True
         outputfile = arg

   return inputfile, outputfile, (is_output_file and is_input_file)

def main(argv):
   inputfile, outputfile, parse_ok = parse_args(argv)
   if (parse_ok):
      print('Input file is "', inputfile)
      print('Output file is "', outputfile)
   else:
      pirnt_help()


if __name__ == "__main__":
   main(sys.argv[1:])