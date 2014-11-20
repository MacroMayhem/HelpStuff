from CatchCatPage import CatchCatPage
from bs4 import BeautifulSoup
import urllib2
import json
from collections import defaultdict
import os
import subprocess
class CatchTagVINES:
# fileName: READ tags to download
  def __init__(self,fileName=None):
    self.actionfile = fileName
    self.actionList =[]
    self.qPage = "https://api.vineapp.com/timelines/tags/"
    self.addHelp = "?page=3"
    self.Dict ={}
    self.readFile() 
  def readFile(self):
   fileObj = open(self.actionfile,'r')
   for line in fileObj.read().split('\n'):
     if(len(line)>0):
       self.actionList.append(line)
       print "-------storing--------",line
       self.populateVINES(line)
   
  
  def populateVINES(self,tagName=None):
    print "Working to retrieve",tagName
# Create DIRs corresponding to /TAGS and /VIDS
    Tagpath = "./VINE/"+tagName
    if not os.path.exists(Tagpath):
      os.makedirs(Tagpath)
    if not os.path.exists(Tagpath+"/VINES"):
      os.makedirs(Tagpath+"/VINES")
    if not os.path.exists(Tagpath+"/TAGS"):
      os.makedirs(Tagpath+"/TAGS")
    ovAll = 0
    for nos in range(1,7):
# Make a QUERY and get the JSON object
      qString  = self.qPage+tagName+"?page="+`nos`
      data = json.loads(urllib2.urlopen(qString).read())
      vineNos = 0;

# Get the VINE details
      for elements in data["data"]["records"]: 
        vineTAG = data["data"]["records"][vineNos]["tags"]
        vineDES = data["data"]["records"][vineNos]["description"]
        vineURL = data["data"]["records"][vineNos]["videoUrl"]
        vineNos = vineNos+1
        if vineURL not in self.Dict:
          self.Dict[vineURL]=vineDES
          vineTagPath = Tagpath +"/TAGS/"+tagName+`ovAll`+".txt"
          vineFilePath = Tagpath+"/VINES/"+tagName+`ovAll`+".mp4"
          ovAll = ovAll + 1
          vineFile = open(vineTagPath,"w+")
          for word in vineDES.split(' '):
            try:
              word.decode('ascii')
            except UnicodeEncodeError:
              print "Not an ascii encoded unicode string", word
            else:
              if( len(word) > 0 and word[0]=='#'):
                vineFile.write(word+'\n')
          vineFile.close() 
          #output = os.system("wget -O "+vineFilePath+" "+vineURL)     
          args = ['wget','-O',vineFilePath,vineURL] 
          output = subprocess.Popen(args,stdout=subprocess.PIPE)
    print len(self.Dict), "files in ",tagName
     

     
