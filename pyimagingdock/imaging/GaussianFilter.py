import SimpleITK as sitk

from ..describe import describe, Description
from ..io import readSitkImage, writeSitkImage,writeSitkToPng

@describe(
    Description('GaussianFilter', 'Performs a gaussian smoothing operation on an image', dockerImage='pyimagingdock')
        .input('image', 'The input image', type='file', deserialize=readSitkImage)
        .input('sigma', 'spread (sigma) value', type='number', required=False)
        .output('output', 'The output image', type='new-file', serialize=writeSitkImage)
)

def GaussianFilter(image, sigma):
    print 'Gaussian filter was executed!'
    print 'received image of size:', image.GetSize()
    blurFilter = sitk.SmoothingRecursiveGaussianImageFilter()
    blurFilter.SetSigma(float(sigma))
    outimage = blurFilter.Execute(image)
    
  # Covert the real output image back to the original pixel type, to
  # make writing easier, as many file formats don't support real
  # pixels.
    
    caster = sitk.CastImageFilter()
    caster.SetOutputPixelType(image.GetPixelID())
    outimage=caster.Execute(outimage)

    return outimage
