import copy
q_map = []
direction = 0
result = 1
result2 = 0
part2_set = set()

with open ('./day6/input6.txt') as f:
    for line in f:
        line = line.strip()
        
        list_of_line = []
        for i in line:
            list_of_line.append(i)
        q_map.append(list_of_line)





def guard_position(map : list):
    for i in map:
        for j in i:
            if j == '^':
                return map.index(i),i.index(j) 

def direction_path(map,direc, y , x):
    direc = direc%4
    if direc == 0 and y - 1 >= 0:
        return {map[y -1][x]: [y -1, x]}
    
    if direc == 1 and x + 1 < len(map[0]):
        return {map[y][x + 1]: [y, x + 1]}
    
    if direc == 2 and y + 1 < len(map):
        return {map[y + 1][x]: [y + 1, x]}
    
    if direc == 3 and x - 1 >= 0:
        return {map[y][x - 1]: [y, x - 1]}
    return {}

def part2(part2_set_var, part2_copy, direction, y, x):

    while True:
        if (y, x, direction) in part2_set_var:
            return 1  

        part2_set_var.add((y, x, direction))
        currect_point = direction_path(part2_copy, direction, y, x)

        if not currect_point:  
            return 0

        if '.' in currect_point:  
            y, x = currect_point['.']
        elif 'X' in currect_point:  
            y, x = currect_point['X']
        elif '#' in currect_point:  
            direction = (direction + 1) % 4
            continue
        if part2_copy[y][x] == '.':
            part2_copy[y][x] = 'X'
        



y , x = guard_position(q_map)
q_map[y][x] = 'X'

while True:
    current_point = direction_path(q_map,direction,y,x)
    if not current_point:  
        break
    if '.' in current_point:
        #for part2
        part2_copy = copy.deepcopy(q_map)
        part2_set_copy = copy.deepcopy(part2_set)
        helper = direction_path(q_map,direction,y,x)
        y2, x2 =  next(iter(helper.values()))
        part2_copy[y2][x2] = '#'
        part2_set_copy.add((y2,x2,direction%4))
        part2_direction = direction
        result2 += part2(part2_set_copy,part2_copy,part2_direction+1,y,x)
        ##
        y, x = current_point['.']
    elif 'X' in current_point:
        y, x = current_point['X']
    elif '#' in current_point:
        part2_set.add((y,x,direction%4))
        direction +=1
        continue
    if q_map[y][x] == '.':
        q_map[y][x] = 'X'
        result+=1
        

print(result)
print(result2)





