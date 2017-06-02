import SimpleITK as sitk

from ..describe import describe, Description
from ..io import readSitkImage, writeSitkImage,writeSitkToPng

@describe(
    Description('PassThroughFilter', 'Passes an image through unchanged', dockerImage='pyimagingdock')
        .input('image', 'The input image', type='file', deserialize=readSitkImage)
        .output('output', 'The output image', type='new-file', serialize=writeSitkImage)
)

def ImagePassThroughFilter(image):
    outImage = image
    return outImage
