import argparse
from datetime import datetime
PROGRAMVERSION=0.1

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input", action="store", dest="inputfile", help="Name of the .csv-inputfile")
parser.add_argument("--output", action="store", dest="outputfile", help="Name of the outputfile, defaults to user_fix.dat", default="user_fix.dat")
parser.add_argument('--version', action='version', version='%(prog)s ' + str(PROGRAMVERSION))

try:
    arguments = parser.parse_args()
    print(arguments)
except IOError as msg:
    parser.error(str(msg))

# break, if no inputfile is given

if arguments.inputfile==None:
    print ("Inputfile is needed to process.")
    exit(1)

else:
    datei = open(arguments.inputfile,'r')
    #print (datei.read())

    #for zeile in datei:
     #   print(zeile)


    ausgabe=open(arguments.outputfile, "w")
    ausgabe.write("I\n")
    ausgabe.write("1101 Version - data cycle 2104, build 20210411, metadata FixXP1101. Copyright (c) 2021 Navigraph, Datasource Jeppesen\n\n")

    for zeile in datei:
        zelle=zeile.split(",")
        #for einezelle in zelle:
        #    print (einezelle)

        #print(zelle[0])
        verdichtet=zelle[2].replace(" ", "")
        airport= zelle[2][:4]
        fix= verdichtet[1:]

        ausgabe.write(" " + zelle[3] + " " + zelle[4] + " " + fix + " " + airport + " " + "ZZ 2115159\n")
    ausgabe.write("99\n")
    ausgabe.close()
    datei.close()

    
    
