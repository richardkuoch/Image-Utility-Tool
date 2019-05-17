# s3563242

#!/usr/bin/python

import os 

# function to debug code
enableDebug = true

def debug(message):
  global enableDebug
  
  if enableDebug == true:
    print message  

def main():
  file = pickAFile()
  
  combineImage(file)
    

def combineImage(filename):
  global enableDebug
  enableDebug = false
  
  
  debug("The filename is" + str(filename))
  
  # find position of underscore in filename 
  filename_Index = filename.find('_')
  debug("The filename_Index occurs at position " + str(filename_Index))
  
  # mediaPath of file
  mediaPath = filename[:filename_Index]
  debug("The mediaPath of the file is "+ str(mediaPath))
  
  mainFilename = filename.split(os.sep)[-1]
  
  debug("The mainFilename is " + str(mainFilename))
  
  #find length of mainFilename
  length = len(mainFilename)
  debug("The length of mainFilename is " + str(length))
  
  # find position of dot found at the highest index
  dotIndex = mainFilename.rfind('.')
  debug("The first . in reverse find occurs at position " + str(dotIndex))
  
  # find position of underscore at the highest index
  r_Index = mainFilename.rfind('_')
  debug("The first _ in reverse find occurs at position " + str(r_Index))
  
  # find position of underscore at the lowest index    
  first_Index = mainFilename.find('_')
  debug("The first_Index occurs at position " + str(first_Index))
  
  # find position of the second underscore 
  second_Index = mainFilename.find('_',first_Index+1,length)
  debug("The second_Index occurs at position " + str(second_Index))
  
  # find position of the third underscore
  third_Index = mainFilename.find('_', second_Index+1,length)
  debug(" The third_Index occurs at position " + str(third_Index))
  
  # width of file
  sourceWidth = mainFilename[first_Index+1:second_Index]
  debug(" The width of the file is " + str(sourceWidth))
  
  # height of file
  sourceHeight = mainFilename[second_Index+1:third_Index]
  debug(" The height of the file is " + str(sourceHeight))
  
  # maxPieces of file
  maxPieces = mainFilename[r_Index+1:dotIndex]
  debug("The maxPieces of the file is " + str(maxPieces))
  
  # format of file
  extension = mainFilename[dotIndex+1:]
  debug(" The format of the file is " + str(extension))
  
  # pieceNo of file
  pieceNo = mainFilename[third_Index+1:r_Index]
  debug("The pieceNo of the file is "+ str(pieceNo))
  
  tempHeight = int(sourceHeight)/int(maxPieces)
  debug("The height of this part is " + str(tempHeight))  

  compositePic = makeEmptyPicture(int(sourceWidth),int(sourceHeight),white)
  
  targetRow = 0 
 
  for i in range(1,int(maxPieces)+1):
      tempPic = makePicture(mediaPath+'_'+ sourceWidth +'_'+ sourceHeight +'_'+ str(i) +'_'+ maxPieces +'.' + extension)
      print tempPic
      
      destCol = 0
      for col in range(int(sourceWidth)):
        destRow = targetRow
        for tempRow in range(int(tempHeight)):
          color = getColor(getPixel(tempPic,col,tempRow))
          setColor(getPixel(compositePic,destCol,destRow),color)
          destRow = destRow +1
        destCol = destCol +1 
      targetRow += tempHeight
  show(compositePic)
  writePictureTo(compositePic, mediaPath + '.' + extension)    
    

    