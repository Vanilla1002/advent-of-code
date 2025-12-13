def process_input(file_path):
    output = []
    with open (file_path) as file:
        for line in file.readlines():
            output.append([ch for ch in line.strip()])

    return output

def part1(list1 :list[list[str]]) -> int:
    result = 0
    rows = len(list1)
    cols = len(list1[0])
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    for r in range(rows):
        for c in range(cols):
            if list1[r][c] != '@':
                continue
            neighbors = 0
            for y, x in directions:
                nr, nc = r + y, c + x
                if 0 <= nr < rows and 0 <= nc < cols and list1[nr][nc] == '@':
                    neighbors += 1
            if neighbors < 4:
                result += 1
    return result

def part2(list2 :list[list[str]]):
    result = 0
    def part1_consepts(list1: list[list[str]]) -> int:
        result = 0
        rows = len(list1)
        cols = len(list1[0])
        points_to_change = []
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        for r in range(rows):
            for c in range(cols):
                if list1[r][c] != '@':
                    continue
                neighbors = 0
                for y, x in directions:
                    nr, nc = r + y, c + x
                    if 0 <= nr < rows and 0 <= nc < cols and list1[nr][nc] == '@':
                        
                        neighbors += 1
                if neighbors < 4:
                    points_to_change.append((r, c))
                    result += 1
        return result , points_to_change
    while True:
        added, points = part1_consepts(list2)
        if added == 0:
            break
        for r, c in points:
            list2[r][c] = '.'
        result += added
    return result

if __name__ == "__main__":
    path = './input.txt'
    input_lines = process_input(path)
    result = part1(input_lines)
    result2 = part2(input_lines)
    print(f'Result: {result}')
    print(f'Result 2: {result2}')
    