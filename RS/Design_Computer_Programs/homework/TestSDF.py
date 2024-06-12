import numpy as np
import math
from Design_Computer_Programs.tools.Memoization import *
# Center
@trace
def GetCenter(a, b, curvature):
    if abs(curvature) > 1e-6:
        m = 0.5 * (1. / curvature - curvature)
        x = ((a[0] + b[0]) - m * (b[1] - a[1])) * 0.5
        y = ((a[1] + b[1]) + m * (b[0] - a[0])) * 0.5
        return np.array([x, y])
    return (a + b) * 0.5

# 计算弧线半径
@trace
def GetRadius(a, b, curvature):
    if abs(curvature) > 1e-6:
        return np.linalg.norm(a - GetCenter(a, b, curvature))
    return 0.

@trace
def sdArc(p, trans, scb, ra, rb):
    p1 = np.dot(trans, np.array([p[0], p[1], 1]))
    scb1 = np.dot(trans, np.array([scb[0], scb[1], 0]))
    p = p1[:2]
    p[0] = abs(p[0])
    scb = scb1[:2]
    k = np.dot(scb, p) if scb[1]*p[0] > scb[0]*p[1] else np.linalg.norm(p)
    return np.sqrt(np.dot(p, p) + ra*ra - 2.0*ra*k) - rb

# 获取圆心点到拱顶点方向的法线
@trace
def GetSca(a, b, center, inCurvature):
    midpoint = 0.5 * (a + b)
    if np.linalg.norm(midpoint - center) < 1e-6:
        temp = np.linalg.norm(b - a)
        if inCurvature > 0.:
            sca = np.array([-temp[1], temp[0]])
        else:
            sca = np.array([temp[1], -temp[0]])
    else:
        if abs(inCurvature) < 1.:
            # 计算(midpoint - center)单位向量midpoint - center
            sca = (midpoint - center) / np.linalg.norm(midpoint - center)
        else:
            sca = (center - midpoint) / np.linalg.norm(midpoint - center)
    return sca

@trace
def sdfArcSegment(p, a, b, curvature):
    r = GetRadius(a, b, curvature)
    center = GetCenter(a, b, curvature)
    sca = GetSca(a, b, center, curvature)
    crossVal = b[0]*sca[1] - b[1]*sca[0]
    scb = (b - center) / np.linalg.norm(b - center) if crossVal > 0. else (a - center)/np.linalg.norm(a - center)
    print("scb", scb)
    t = (math.atan2(sca[1],sca[0]) - np.pi * 0.5)
    print("arctan", t)
    Trans = np.linalg.inv(np.array([[np.cos(t), -np.sin(t), center[0]], [np.sin(t), np.cos(t), center[1]], [0, 0, 1]]))
    return sdArc(p, Trans, scb, r, 0.)

start = np.array([1., 0.])
end = np.array([1., 1.])
curvature = 0.5
point = np.array([1., 0.5])
#期望结果为0.25
print(sdfArcSegment(point, start, end, curvature))

point = np.array([1., 0.])
#期望结果为0.
print(sdfArcSegment(point, start, end, curvature))

point = np.array([0.625, 0.5])
#期望结果为0.625
print(sdfArcSegment(point, start, end, curvature))

point = np.array([0.625, -0.125])
#期望结果不为0.
print(sdfArcSegment(point, start, end, curvature))

point = np.array([0.625, -0.125 + 0.625 * 2])
#期望结果不为0.
print(sdfArcSegment(point, start, end, curvature))

curvature = -0.5
point = np.array([1.375, -0.125])
#期望结果不为0.
print(sdfArcSegment(point, start, end, curvature))

curvature = -1.5
point = np.array([1.375, -0.125])
#期望结果不为0.
print(sdfArcSegment(point, start, end, curvature))