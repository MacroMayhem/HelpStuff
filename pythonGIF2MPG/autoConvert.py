import os
import subprocess
import sys



# INPUT:
def toConvert(parentDir=None,tagName=None):
  gifFiles="./"+parentDir+"/"+tagName+"/GIFS"
  vidFiles="./"+parentDir+"/"+tagName+"/VIDS"
  
  if not os.path.exists(vidFiles):
    os.makedirs(vidFiles)
  fileList = os.listdir(gifFiles)
  for files in fileList:
    print "File under processing:",files
    gifPath = gifFiles+"/"+files
    gifName = files.split(".")[0]
    if os.path.isfile(gifPath):
      vidToWrite = vidFiles+"/"+gifName+".mpg"
      print "Initiating creation of",vidToWrite
     # args=["convert",gifPath,vidToWrite]
     # p = subprocess.Popen(args,stdout=subprocess.PIPE)
      result = os.system("convert "+gifPath+" "+vidToWrite)
      print "Conversion Complete"



# INPUT:
# argv[1] : Name of the parent category DIR example: actions etc
# argv[2] : Name of the file which contains list of TAGDIRs to convert
def main():
  parentDir = sys.argv[1]
  fileName  = sys.argv[2]
  fileObj   = open(fileName,"r")
  
  for line in fileObj.read().split("\n"):
    if(len(line)>0):
      print "To Convert: ",line
      toConvert(parentDir,line)

if __name__=="__main__":
  main()
