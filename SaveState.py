'''
Created on Dec 21, 2018

@author: jack
'''
import os

def writeFile(outputFile, inputText):
    myfile = open(outputFile, 'w')
    myfile.write(inputText)
    myfile.close()

def readFile(inputFile):
    if not os.path.isfile(inputFile):
        print 'File does not exist.'
    else: 
        with open(inputFile) as f:
            content = f.read().splitlines()
            for line in content:
                print(line)
                f.close()     

def main():
    fileout = "/home/jack/newfile.txt"
    
    textMsg = {"name":"jsmith", "birthday": "2/19/1934"}

    writeFile("./outputFile.txt", str(textMsg))
    readFile("./outputFile.txt")

if __name__ == '__main__':
    main()