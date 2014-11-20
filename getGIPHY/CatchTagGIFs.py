from CatchCatPage import CatchCatPage
from bs4 import BeautifulSoup
import urllib2
import json
from collections import defaultdict
import os
import subprocess
class CatchTagGIFs:
# Initialisation of class visible to user
# fileName: Name of the file which contains list of categories to downlaod from
  def __init__(self,fileName=None):
    self.CatContent = CatchCatPage(fileName)
    self.tagInfo = {}    # Contains CategoryName and TagList pair.
    self.qPage = "http://api.giphy.com/v1/gifs/search?limit=30&q="
    self.Key = "&api_key=dc6zaTOxFJmzC"
  def readCatFile(self):
    self.CatContent.readCatFile()    # Read CategoryNames from the file
      

# For each Category Name get the Tags present on the website
  def getTagsFromCat(self):    
    self.tagInfo = {key:[] for key in self.CatContent.catList}
    for category in self.CatContent.catList:
      self.CatContent.getTags(category,self.tagInfo[category])

# For each category  for each Tag in it retrieve atmost 100 Tagged images.
  def getObj4Tags(self):
    for category in self.tagInfo:
     Catpath = "./"+category
     print "Current Working Category is",category
     if not os.path.exists(Catpath):
      os.makedirs(Catpath)
     for tag in self.tagInfo[category]:
      tag = tag.replace(" ","+").replace("#","");
      self.populateTag(category,tag)
        
# Getting the Tag make GIPHY API CALL DOWNLOAD GIFS AND TAGS
# categoryName : Name of the current Category
# tagName : current Tag to retrieve
  def populateTag(self,categoryName=None,tagName=None):
    print "Working to retrieve",tagName, "of",categoryName

# Create DIRs corresponding to /TAGS and /GIFS
    Tagpath = "./"+categoryName+"/"+tagName
    if not os.path.exists(Tagpath):
      os.makedirs(Tagpath)
    if not os.path.exists(Tagpath+"/GIFS"):
      os.makedirs(Tagpath+"/GIFS")
    if not os.path.exists(Tagpath+"/TAGS"):
      os.makedirs(Tagpath+"/TAGS")

# Make a QUERY and get the JSON object
    qString  = self.qPage+tagName+self.Key
    data = json.loads(urllib2.urlopen(qString).read())
    gifInt = 0
    gifJSON = {}

# Get the GIF details
    for jsonTag in data["data"]:
     gifID = data["data"][gifInt]["id"] 
     gifGIF = data["data"][gifInt]["images"]["original"]["url"]
     gifURL = data["data"][gifInt]["url"]
     gifInt = gifInt + 1
     gifTagPath = Tagpath +"/TAGS/"+gifID+".txt"
     gifFilePath = Tagpath+"/GIFS/"+gifID+".gif"
     gifFile = open(gifTagPath,"w+")
     print "Working On",tagName,categoryName,gifID,gifURL
     TagList = []
     self.CatContent.getTagsForVids(gifURL,TagList)
# WRITE SPAWN AND DOWNLOAD 
     for gifTag in TagList:
       gifFile.write(gifTag+"\n")
     gifFile.close() 
     args = ['wget','-O',gifFilePath,gifGIF] 
     output = subprocess.Popen(args,stdout=subprocess.PIPE)
     # ONE BY ONE
     #returnValue = os.system("wget -O "+gifFilePath+" "+gifGIF)     


     
