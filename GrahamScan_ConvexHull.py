#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random
import matplotlib.pyplot as plt 
import time

graham_s_time = time.time()

total_points = 50
max_coordinate_val = 50
hull = []
points = []
non_hull_points = []

# generate random points
for i in range(total_points):
    points.append((random.randint(0,max_coordinate_val),random.randint(0,max_coordinate_val)))

# get slope of point x wrt to lowest_point
def get_slope_with_lowest_point(x, lowest_point):
    try:
        return -(x[0] - lowest_point[0]) / (x[1] - lowest_point[1])
    except:
        if((x[0] - lowest_point[0]) < 0):
            return 10000
        else:
            return -10000 + x[0] - lowest_point[0]
    
# sort points according to y axis
points.sort(key=lambda x : x[1])
lowest_point = points.pop(0)

# sort points according to slope with lowest_point
points.sort(key=lambda x : get_slope_with_lowest_point(x, lowest_point), reverse = True)

# initialize hull
p1 = points.pop()
p2 = points.pop()
hull.extend([lowest_point, p1, p2])

# get orientation of 3 points
def orient(p1, p2, p3):
    val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    # val = 0 -> colinear
    # val = 1 -> clock wise
    # val = 2 -> counterclock wise
    if (val == 0) :
        return 0 
    if (val > 0):
        return 1
    else:
        return 2

while(points):
    current_point = points.pop()
    current_point_orientation = orient(hull[-1], current_point, hull[-2])
    
    if(current_point_orientation > 1): # if counterclock wise add to hull
        hull.append(current_point)        
    else:
        non_hull_points.append(hull.pop()) # pop points till orientation is clockwise
        while(True):
            try:
                current_point_orientation = orient(hull[-1], current_point, hull[-2])
                if(current_point_orientation < 2):
                    non_hull_points.append(hull.pop())
                else:
                    break
            except:
                break
        hull.append(current_point)

# plot points
fig, ax = plt.subplots(figsize=(8,8))
ax.scatter([x[0] for x in non_hull_points], [x[1] for x in non_hull_points], c='red',marker='+') # non_hull_points
ax.scatter([x[0] for x in hull], [x[1] for x in hull], c='blue') # hull

# join hull points
i = 0
while i < len(hull):
    x, y = zip(hull[i-1], hull[i])
    ax.plot(x, y, c='blue')
    i+=1

plt.show()
print("graham scan time:",graham_s_time)


# In[ ]:




