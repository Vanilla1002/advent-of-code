with open ('./day3/input3.txt') as f:
    text = f.read()
    



result = 0
starting_point = 5
enable = True

for i, letter in enumerate(text):
    if letter == 'd' and text[i:i+4] == 'do()':
        enable = True
    if letter == 'd' and text[i:i+7] == "don't()":
        enable = False
        
    if enable and letter == 'm' and text[i:i+4] == 'mul(':
        first_number = 0
        second_number = 0
        is_valid = True

        idx = i + 4
        while idx < len(text) and text[idx].isnumeric():
            first_number = first_number * 10 + int(text[idx])
            idx += 1

        if idx < len(text) and text[idx] == ',':
            idx += 1
        else:
            is_valid = False

        while is_valid and idx < len(text) and text[idx].isnumeric():
            second_number = second_number * 10 + int(text[idx])
            idx += 1

        if not (is_valid and idx < len(text) and text[idx] == ')'):
            continue

        result += first_number * second_number

print(result)



                        

                


                    

                
            
