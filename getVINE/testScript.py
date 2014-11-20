from CatchTagVINES import CatchTagVINES
import sys
# COMMAND LINE ARGUMENT FOR THE LIST FOR MAJOR CATEGORY

fileName = sys.argv[1]
print "Reading categories from",fileName
actions = CatchTagVINES(fileName)
