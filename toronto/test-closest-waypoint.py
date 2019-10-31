
closest_waypoints = [0, 1]

for i in range(0, 202):
    closest_waypoints[0] = i
    closest_waypoints[1] = i + 1    

    # Calculate closest waypoints indices in racing line
    if closest_waypoints[0] > closest_waypoints[1]:
        top = closest_waypoints[0]
    else: 
        top = closest_waypoints[1]

    if top % 2 == 1:
        top += 1

    d = top // 2
    a = d - 3
    b = d - 2
    c = d - 1
    e = d + 1

    if a < 0:
        a = 101 + a
    if b < 0:
        b = 101 + b
    if c < 0:
        c = 101 + c

    if a > 100:
        a -= 100
    if b > 100:
        b -= 100
    if c > 100:
        c -= 100
    if d > 100:
        d -= 100
    if e > 100:
        e -= 100

    # Possible closest waypoints tuples
    closest_points = [a, b, c, d, e]

    print('closest[0]:',closest_waypoints[0],',closest[1]:',closest_waypoints[1],',',a,',',b,',',c,',',d,',',e)