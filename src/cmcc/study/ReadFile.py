#####################################
'''读取文件'''

import codecs
import  re
import  os

def removeAnswer(inFile,outFile):
    with codecs.open(inFile,'r',encoding='UTF-8') as fin:
        contents = fin.readlines()

    with codecs.open(outFile,'w',encoding='UTF-8') as fout:
        for line in contents:
            tmp=re.sub(r'\([ABCD  ]*\)','()',line)
            tmp=re.sub(r'（[ABCD  ]*）','()',tmp)
            fout.write(tmp)


inDir="txt"
outDir="out"
for inFileName in os.listdir(inDir):
    removeAnswer(inDir+"/"+inFileName,outDir+"/"+inFileName)
print('over!')