import rake
import re
import operator

def KeywordsExtra(text):
    tags=[]
    lentext=len(text)
    if lentext==0:
        tags.append("there")
    else:
        RAKE=rake.Rake("SmartStoplist.txt",3,3,1)
        tags=RAKE.run(text)
    return(tags)
  
             
            
    