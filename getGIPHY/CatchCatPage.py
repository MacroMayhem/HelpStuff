import urllib2
from bs4 import BeautifulSoup
import sys
import threading
from Queue import Queue
import logging

# THE CLASS FOR GETTING THE CATEGORY FROM A FILE -> DOWNLOADING THE WEBPAGE CORRESPONDING TO IT -> GETTING TAGS ON THE WEBPAGE

class CatchCatPage:
  def __init__(self,fName=None):
    self.fileName=fName
    self.catList=[]
    self.exDic={}
    self.exFile="exclude.txt"
    self.parentSite="http://www.giphy.com"
    print "CatchCatPage Object Created"

# Open the file which has list of categories from which the tags are needed to be extracted. Category->actions, music etc.
  def readCatFile(self):
    print "Reading file for category names"
    fileObj = open(self.fileName,'r')
    for line in fileObj.read().split('\n'):
      if len(line) > 0:
        self.catList.append(line)
    print "Reading Completed"
    exclHandle = open(self.exFile,"r")
    for line in exclHandle.read().split("\n"):
      if len(line)>0:
        self.exDic[line]=1
        print "To exclude: ",line
# For each category down the webpage and extract the Tags present there. tag Page = http://www.giphy.com/categories/example
# categoryName : name of the current category ex:actions
# tagList: an empty tagList to populate from the webpage of categoryName
  def getTags(self,categoryName=None,tagList=[]):
      print "Retrieving Tags for ",categoryName
      categoryHandle = urllib2.urlopen(self.parentSite+"/categories/"+categoryName)
      categoryPage = BeautifulSoup(categoryHandle.read())
      rawTagList = categoryPage.findAll('div',{'class':'grid_9 omega tag-list'})
      rawTagList = BeautifulSoup(str(rawTagList))
      Tags = rawTagList.findAll('a')
      for tagLink in Tags:
        tagVal = tagLink.string.replace(' ','+').replace('#','')
        if tagVal in self.exDic:
          print "Skipping: ",tagVal
        else:
          tagList.append(tagLink.string)
      print "Tags retrieval completed for ",categoryName
 
#For each gif page retrieve all the tags present there.  
# webPage: link to the webpage of a GIF
# tagList: empty List to populate with additional tags present there
  def getTagsForVids(self,webPage,tagList=[]): 
    pageHandle = urllib2.urlopen(webPage)
    pageContent = BeautifulSoup(pageHandle.read())
    rawTagList = pageContent.findAll('div',{'id':'tags'})
    rawTagList = BeautifulSoup(str(rawTagList))
    Tags = rawTagList.findAll('a')
    for TagLink in Tags:
      tagList.append(TagLink['href'].split("/")[-2])    
