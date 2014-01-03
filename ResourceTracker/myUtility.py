#!/usr/bin/env python
import sys

debugFlag = False

def printf (format, *args):
  sys.stdout.write(format % args)

def setPrintDebugFlag (flag):
  global debugFlag
  debugFlag = flag

def dprintf (format, *args):
  global debugFlag
  if (debugFlag):
    printf (format, *args)

def fortune ():
  import random
  allFortunes = [
    "A life unexamined is not worth living.",
    "What the caterpillar calls the end of the world, the Master calls the butterfly.",
    "Life is a school to the wise man and an enemy to the fool.",
    "Every human being is a mirror through which God longs to see himself.",
    "It takes both rain and sunshine to make a rainbow."]
  return (random.sample(allFortunes,1)[0])

def distanceA (lat1,lon1,lat2,lon2):
  import math

  nautMilesPerLat = 60.000721
  nautMilesPerLon = 60.10793
  rad = math.pi/180.0
  kmetersPerNautMile = 1.852

  yDist = (lat2-lat1) * nautMilesPerLat
  xDist = (math.cos(lat1*rad) + math.cos(lat2*rad)) \
      * (lon2-lon1) * (nautMilesPerLon/2)
  distance = math.sqrt(yDist**2 + xDist**2)

  return distance * kmetersPerNautMile

def distanceB (lat1,lon1,lat2,lon2):
  import math

  R = 6371
  rad = math.pi/180.0
  dLat = (lat2-lat1)*rad
  dLon = (lon2-lon1)*rad
  a = math.sin(dLat/2) * math.sin(dLat/2) + \
      math.cos(lat1*rad) * math.sin(dLon/2) * \
      math.sin(dLon/2) * math.sin(dLon/2)
  c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
  d = R * c

  return d

def distanceC (lat1,lon1,lat2,lon2):
  import math

  R = 6371
  rad = math.pi/180.0
  dLat = (lat2-lat1)*rad
  dLon = (lon2-lon1)*rad
  c = math.acos(math.sin(lat1*rad)*math.sin(lat2*rad) + \
      math.cos(lat1*rad)*math.cos(lat2*rad) * \
      math.cos(dLon*rad))
  d = R * c

  return d



