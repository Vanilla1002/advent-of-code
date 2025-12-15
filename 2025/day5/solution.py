def process_input(file_path):
    output = []
    with open (file_path) as file:
        for line in file.readlines():
            output.append(line.strip())
    return output


def input_praser(lines):
    ranges = []
    numbers = []
    for line in lines:
        if '-' in line:
            a,b = line.split('-')
            ranges.append( (int(a), int(b)) )
        elif not line:
            continue
        else:
            
            numbers.append(int(line))
    return ranges, numbers

def _merge_ranges(ranges: list[tuple[int,int]]) -> list[tuple[int,int]]:
    if not ranges:
        return []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]
    for current in sorted_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

def part1(ranges: list[tuple[int,int]], numbers: list[int]) -> int:
    merged_ranges = _merge_ranges(ranges)
    result = 0
    for i in numbers:
        for r in merged_ranges:
            if r[0] <= i <= r[1]:
                result += 1
                break
    return result

def part2 (ranges: list[tuple[int,int]]) -> int:
    merged_ranges = _merge_ranges(ranges)
    result = 0
    for i in merged_ranges:
        result += (i[1] - i[0] + 1)
    return result

if __name__ == "__main__":
    path = './input.txt'
    input_lines = process_input(path)
    ranges, numbers = input_praser(input_lines)
    result = part1(ranges, numbers)
    print(f'Result: {result}') 
    result2 = part2(ranges)
    print(f'Result part 2: {result2}')