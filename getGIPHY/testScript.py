from CatchTagGIFs import CatchTagGIFs
from CatchCatPage import CatchCatPage
import sys


# COMMAND LINE ARGUMENT FOR THE LIST FOR MAJOR CATEGORY

fileName = sys.argv[1]
print "Reading categories from",fileName
categories = CatchTagGIFs(fileName)
categories.readCatFile()
categories.getTagsFromCat()
categories.getObj4Tags()
