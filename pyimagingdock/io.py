import pandas as pd
import os
import six
from PIL import Image
import SimpleITK as sitk

def readCsv(fileName):
    data = pd.read_csv(fileName, nrows=1)
    indexCol = []
    for col in range(len(data.columns)):
        colName = data.columns[col]
        if colName.startswith('Unnamed') or colName.startswith('_') or isinstance(data.iloc[0, col], six.string_types):
            indexCol.append(col)
        else:
            break
    data = pd.read_csv(fileName, index_col=indexCol)

    def transformName(name):
        if name is None or name.startswith('_'):
            return name
        return '_' + name

    data.index.names = [transformName(name) for name in data.index.names]
    return data


# desearialization method for a dicom image. Placeholder that could be replaced with pyDicom methods
# if this is better.  Use SimpleITK reading for now, which gets only the pixels out
def readDicom(dicomFileName):
    image = sitk.ReadImage(dicomFileName)
    return image

    # desearialization method for an ITK image
def readSitkImage(imgFileName):
    if(os.path.isdir(imgFileName)==True):
        for file in os.listdir(imgFileName):
            imgPath =imgFileName+"/"+file
            print(imgPath)
            image = sitk.ReadImage(imgPath)
    else:
        image = sitk.ReadImage(imgFileName)
    return image

# this doesn't have the write arguments
def writeSitkImage(data,imageFileName):
    # WriteImage doesn't work because file type can't be discovered for an unknown reason
    #sitk.WriteImage(data,imageFileName)
    writer = sitk.ImageFileWriter()
    writer.SetFileName(imageFileName)
    writer.Execute(data)

# Here is a temporary workaround that converts 2D only ITK images to PNG output
def writeSitkToPng(data,imageFileName):
    imageSize = data.GetSize()
    tempImg = Image.new("L",imageSize)
    for i in range(imageSize[0]):
        for j in range(imageSize[1]):
            tempImg.putpixel([i,j],data[i,j])
	    #tempImg[i,j] = data[i,j]
    #now convert from PIL to PNG
    tempImg.save(imageFileName,"png")
