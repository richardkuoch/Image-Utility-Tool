#s3563242

#!/usr/bin/python

import os

# function to debug code
enableDebug = true

def debug(message):
  global enableDebug
  
  if enableDebug == true:
    print message  

def fileInfo(Image):
  # retrieve file size to determine if image needs to be split
  filestats = os.stat(Image)
  filesize = filestats.st_size
  
  print "the filesize of the image is",filesize, "bytes"
  
  return filesize


def main():  
  file = pickAFile()
  
  splitImage(file)
  
  
def splitImage(filename):
  global enableDebug
  
  enableDebug = false
  
  sourcePic = makePicture(filename)
  
  # find position of dot found at the highest index
  dotIndex = filename.rfind('.')
  debug("The first . in reverse find occurs at position" + str(dotIndex))
 
  # mediaPath
  mediaPath = filename[:dotIndex]
  
  debug("The mediaPath of the file is " + str(mediaPath))
 
  # format of file
  extension = filename[dotIndex:]
  
  debug("The format of the file is " + str(extension))
  
  fileSize = fileInfo(filename)
  
  noParts = fileSize/20000 + 1
  
  if fileSize > 20000:
    print "your image file needs to be split"
    print "the image file will be split into", noParts, "pieces"
    
    # dimensions of source pic
    sourceWidth = getWidth(sourcePic)
    debug("the width of the original image is " + str(sourceWidth))
  
    sourceHeight = getHeight(sourcePic)
    debug("the height of the original image is " + str(sourceHeight))
   
    # assign a pieceNo starting to each of the split files
    pieceNo = 1
  
    # startRow
    startRow = 0
  
    # noRows
    noRows = sourceHeight/noParts
    
    for i in range(1,noParts+1):
      copyPixels(sourcePic,startRow,noRows,sourceWidth,sourceHeight,mediaPath,pieceNo,noParts,extension)
      startRow += sourceHeight/noParts
      pieceNo += 1  
        
            
  else:
    print "your image file does not need to be split"   


def copyPixels(picture,startRow,noRows,width,height,mediaPath,pieceNo,noParts,extension):
  # make canvas
  newPic = makeEmptyPicture(getWidth(picture), noRows,white)
  
  destRow = 0
  
  for sourceRow in range(startRow, startRow + noRows):
      
      for col in range(getWidth(picture)):
      
        pixel = getPixel(picture,col,sourceRow)
        color = getColor(pixel)
      
        destPixel = getPixel(newPic,col,destRow)
        setColor(destPixel,color)
    
      destRow += 1 
  
  writePictureTo(newPic,mediaPath+'_'+ str(width)+"_"+ str(height)+"_"+ str(pieceNo)+ "_"+ str(noParts) + extension)
  
  show(newPic)
       




  