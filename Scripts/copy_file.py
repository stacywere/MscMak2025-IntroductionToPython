import sys
infilename = sys.argv[1]
outfilename = sys.argv[2]
""" Opens two files and copies one into the other line by line. """
infile = open("../Data/HumptyDumpty.txt", 'r')      #hardcoding -writing paths within program #avoid it
outfile = open("../Data/Newdumpty.txt",'w')

for x in infile:
    outfile.write(x)
    
infile.close()
outfile.close()