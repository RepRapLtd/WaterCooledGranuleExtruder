# FreeCAD program to generate a 3D-printable sieve with a certain mesh size.

# Adrian Bowyer
#
# RepRap Ltd
# https://reprapltd.com
#
# 13 November 2021
#
# Licence: GPL


# All dimensions in mm.

# The size of the mesh holes

holeDiameter = 2.0

# Overall diameter

bigDiameter = 60.0

# Overall depth

depth = 50.0

# Wall thickness

wallThickness = 4.0

# Base thickness

baseThickness = 1.0

#********************************************************************************************************

import Part, FreeCAD, math
from FreeCAD import Base
import math as maths


sieve = Part.makeCylinder(bigDiameter*0.5, depth, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1))
innerR = bigDiameter/2 - wallThickness
sieve = sieve.cut(Part.makeCylinder(innerR, depth, Base.Vector(0, 0, baseThickness), Base.Vector(0, 0, 1)))

innerR -= 1.5*holeDiameter
r = holeDiameter*0.5
xHalfSquareSide = round(innerR/(3*r))
yHalfSquareSide = round(innerR/(3*r*maths.sqrt(3)*0.5))
innerR2 = innerR*innerR

for y in range(-yHalfSquareSide, yHalfSquareSide+1):
 yc = y*r*3.0*maths.sqrt(3)*0.5
 if y%2 == 0:
  xOff = 1.5*r
 else:
  xOff = 0
 for x in range(-xHalfSquareSide, xHalfSquareSide+1):
  xc = x*r*3.0 + xOff
  r2 = xc*xc + yc*yc
  if r2 < innerR2:
   sieve = sieve.cut(Part.makeCylinder(r, baseThickness*4.0, Base.Vector(xc, yc, -baseThickness), Base.Vector(0, 0, 1)))

Part.show(sieve)
