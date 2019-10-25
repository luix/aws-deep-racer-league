'''
    http://forums.cgsociety.org/t/divide-curve-equidistant-straight-line/1557425

    divide curve equidistant straight line
'''

import math
import maya.OpenMaya as om
import maya.cmds as mc
def eqDistanceCurveDivide(curvename,segmentcurveLength):
	uValeStart=0.0
 
	curveLength=mc.arclen(curvename)
	kk=(int(curveLength/segmentcurveLength))
 
	intCL=int(curveLength)
	accur=100*intCL
 
	uVale=1.0/accur
 
	for t in range(kk):
		for i in range(accur):
 
			pointA=mc.pointOnCurve(curvename,top=True, pr=uValeStart, p=True )
			vecA=om.MVector(pointA[0],pointA[1],pointA[2])
			pointB=mc.pointOnCurve(curvename,top=True, pr=uVale, p=True)
			vecB=om.MVector(pointB[0],pointB[1],pointB[2])
 
			vecC=om.MVector()
			vecC=(vecB-vecA)
			distance=vecC.length()
 
			if distance<segmentcurveLength:
				uVale+=1.0/accur
			else:
				uValeStart=uVale
				break
 
		mc.spaceLocator(p=(pointB[0],pointB[1],pointB[2]))
 
		if uValeStart>=0.99:
			break
eqDistanceCurveDivide('curve1',1.0)