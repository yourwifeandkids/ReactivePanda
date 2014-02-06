import g
import math
from panda3d.core import Quat, Vbase3
from Types import *

class SHPR:
  def __init__(self, h, p, r):
    self.h = h
    self.p = p
    self.r = r
    self.type = HPRType
  def __str__(self):
      return "HPR(%7.2f, %7.2f, %7.2f)" % ( self.h, self.p, self.r)
  def __add__(self, y):
      return g.add(self, y)
  def __sub__(self, y):
      return g.sub(self, y)
  def __rsub__(self, y):
          return g.sub(y, self)
  def __mul__(self, y):
          return g.mul(self, y)
  def __rmul__(self, s):
      return g.mul(s, self)
  def __neg__(self):
          return g.mul(self, -1)
  def interp(self, t, p2):
          return SHPR(staticLerpA(t, self.h, p2.h),
                      staticLerpA(t, self.p, p2.p),
                      staticLerpA(t, self.r, p2.r))

def addHPR(a,b):
    return SHPR(a.h+b.h, a.p+b.p, a.r+b.r)

def subHPR(a,b):
    return SHPR(a.h-b.h, a.p-b.p, a.r-b.r)

def scaleHPR(s,a):
    return SHPR(a.h*s, a.p*s, a.r*s)

def getUpHPR(hpr):
    q = Quat()
    q.setHpr(VBase3(math.degrees(hpr.h), math.degrees(hpr.p), math.degrees(hpr.r)))
    v = q.getUp()
    return SP3(v.x, v.y, v.z)

HPRType.encode = lambda p:str(p.h)+","+str(p.p)+","+str(p.r)
def readHPR(str):
    nums = parseNumbers(str)
    return SHPR(nums[0],nums[1], nums[2])

HPRType.decode = readHPR