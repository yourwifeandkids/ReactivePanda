# # To change this license header, choose License Headers in Project Properties.
# # To change this template file, choose Tools | Templates
# # and open the template in the editor.
#
# import unittest
# import sched, time
# import piface.pfio as piface
# import Globals
# from PiObjects import *
# from Signal import *
# from Functions import *
#
# piface.init()
#
# def heartBeat(ct, events):
#     #print "objects " + str(len(Globals.worldObjects))
#     Globals.dt = ct - Globals.currentTime
#     Globals.currentTime = ct
#     Globals.events = events
#     Globals.thunks = []
#     for worldObject in Globals.worldObjects:
#         #print("Updating object: " + repr(worldObject))
#         #print repr(worldObject)
#         Globals.thunks.extend(worldObject._update())
#     for f in Globals.thunks:
#         f()
#     for obj in Globals.newObjects:
#         #print("Adding object: " + repr(obj))
#         Globals.worldObjects.append(obj)
#     Globals.newObjects = []
#     for obj in Globals.worldObjects:
#         #print("Initializing object: " + repr(obj))
#         obj._initialize()
# #will need to check the proxy module to find the right name for this initialize method
# #make an initialize method that clears out all the variables and resets the clock
# def initialize(ct):
#     Globals.thunks = []
#     Globals.currentTime = 0 #Not sure if this should be 0 or CT
#     Globals.newModels = []
#     Globals.worldObjects = {}
#     Globals.events = []
#
# def engine(ct):
#     #Initialize all signals (signalF.start)
#     #set the time to 0
#     #get events and clear thunks
#     Globals.currentTime = ct
#     while True:
#         ctime = time.time()
#         #print "heartbeat: " + str(ctime-ct)
#         heartBeat(ctime, Globals.newEvents)
#         time.sleep(.05)
