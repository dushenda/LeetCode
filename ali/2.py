line1 = []
line2 = []
line3 = []
floor_time = list(map(int, line1.split()))
floor = dict()
floor[0] = list(map(map(int,line2.split())))
floor[1] = list(map(int,line3.split()))

sum=0
for a_time in range(floor_time[1]):
    selected = []
    for a_floor in range(floor_time[0]):

