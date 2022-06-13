"""
PURPOSE:
Script to convert filtered .fits of an object and colorize it.

Austin Everman
Started on 6/2/2016
V1.0

Uses 'img_scale.py'
Written by Min-Su Shin
Department of Astronomy, University of Michigan (2009 - )
Department of Astrophysical Sciences, Princeton University (2005 - 2009)

Uses code by Jessica Lu, "http://www.astrobetter.com/blog/2010/10/22/making-rgb-images-from-fits-files-with-pythonmatplotlib/"

"""

import numpy as np
import pylab as py
import img_scale3converted as img_scale
from astropy.io import fits

VscaleMax = 30000
RscaleMax = 30000
BscaleMax = 30000

VscaleMin = 0
RscaleMin = 0
BscaleMin = 0

#Load the B, V, and R filtered .fits files, and one of their headers
hdulistB = fits.open('FITS/B.fts')
Bimg = hdulistB[0].data
#objName = hdulistB[0].header['OBJECT']
objName = "Dumbell Nebula"
hdulistB.close()

hdulistV = fits.open('FITS/V.fts')
Vimg = hdulistV[0].data
hdulistV.close()

hdulistR = fits.open('FITS/R.fts')
Rimg = hdulistR[0].data
hdulistR.close()

#Fill a 3D array, with its width and height the same as the .fits, and fill it with zeroes
img = np.zeros((Bimg.shape[0], Bimg.shape[1], 3), dtype=float)\

#Take the square root of the image data based on the scaling of the original data across the depth of the 3D array
img[:,:,0] = img_scale.sqrt(Vimg, scale_min = VscaleMin, scale_max = VscaleMax)
img[:,:,1] = img_scale.sqrt(Rimg, scale_min = RscaleMin, scale_max = RscaleMax)
img[:,:,2] = img_scale.sqrt(Bimg, scale_min = BscaleMin, scale_max = BscaleMax)

#Output and save the final image
py.clf()
py.imshow(img, aspect='equal')
py.title(objName)
py.savefig('Sqrt Final.png')

#Take the square root of the image data based on the scaling of the original data across the depth of the 3D array
img[:,:,0] = img_scale.linear(Vimg, scale_min = VscaleMin, scale_max = VscaleMax)
img[:,:,1] = img_scale.linear(Rimg, scale_min = RscaleMin, scale_max = RscaleMax)
img[:,:,2] = img_scale.linear(Bimg, scale_min = BscaleMin, scale_max = BscaleMax)

#Output and save the final image
py.clf()
py.imshow(img, aspect='equal')
py.title(objName)
py.savefig('Linear Final.png')

#Take the square root of the image data based on the scaling of the original data across the depth of the 3D array
img[:,:,0] = img_scale.log(Vimg, scale_min = VscaleMin, scale_max = VscaleMax)
img[:,:,1] = img_scale.log(Rimg, scale_min = RscaleMin, scale_max = RscaleMax)
img[:,:,2] = img_scale.log(Bimg, scale_min = BscaleMin, scale_max = BscaleMax)

#Output and save the final image
py.clf()
py.imshow(img, aspect='equal')
py.title(objName)
py.savefig('Log Final.png')

#Take the square root of the image data based on the scaling of the original data across the depth of the 3D array
img[:,:,0] = img_scale.asinh(Vimg, scale_min = VscaleMin, scale_max = VscaleMax)
img[:,:,1] = img_scale.asinh(Rimg, scale_min = RscaleMin, scale_max = RscaleMax)
img[:,:,2] = img_scale.asinh(Bimg, scale_min = BscaleMin, scale_max = BscaleMax)

#Output and save the final image
py.clf()
py.imshow(img, aspect='equal')
py.title(objName)
py.savefig('Asinh Final.png')