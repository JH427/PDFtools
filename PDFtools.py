import os, argparse
from PyPDF2 import PdfFileMerger, PdfFileReader

outputFilename = 'PDFTools_output'

path = os.getcwd()+'\\'

def mergePDF(mergeList=[]):
    merger = PdfFileMerger()
    try:
        for file in mergeList:
            merger.append(PdfFileReader(str(path+file), 'rb'))
        merger.write(path+outputFilename+'.pdf')
    except FileNotFoundError as err:
        print('merge: '+str(err))

parser = argparse.ArgumentParser(prog='PDFtools', description='command line pdf tools')
parser.add_argument('-m', '--merge', action='store', nargs='+', type=str, help='merge multiple pdfs')
parser.add_argument('-o', '--output', action='store', nargs=1, type=str, help='output filename')
parser.add_argument('-p', '--path', action='store', nargs=1, type=str, help='set the working directory (format: no trailing \\)')
args = parser.parse_args()
#parser.print_help()

if args.path:
    if os.path.isdir(args.path[0]+'\\'):
        try:
            path = str(args.path[0]+'\\')
        except FileNotFoundError as err:
            print('path: '+str(err))
    else:
        print('path: not a valid path')

if args.output:
    outputFilename = args.output[0]
    
if args.merge:
    argList = []
    for arg in args.merge:
        argList.append(arg)
    mergePDF(argList)


        
