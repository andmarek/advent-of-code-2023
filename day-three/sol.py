import re 
from typing import DefaultDict

symbols = {'@', '-', '=', '+', '&', '*', '$', '/', '%', '#'}

def part_one():
    with open("input.txt", "r") as f:
        data = f.read()
        lines = data.split("\n")

        symbol_coords = DefaultDict(list)        

        # get the symbol coordinates
        for i in range(len(lines)):
            line = lines[i]
            for j in range(len(line)):
                if line[j] in symbols:
                    symbol_coords[i].append(j)

        # get the coordinates of the number
        '''
        # key = index of number
        number_coords = {
            0: [{
                "value": "1234",
                "span": (0, 4),
                "is_part_no": False
            },
            {
                "value": "1234",
                "span": (0, 4),
                "is_part_no": False
            },
        ]}
        '''
        number_coords = DefaultDict(list)
        for i in range(len(lines)):
            line = lines[i]
            match_objects = re.finditer(r'\d+', line)
            if match_objects:
                for match_object in match_objects:
                    number_coords[i].append(
                        {"span": match_object.span(), "value": match_object.group(0), "is_part_no": False}
                    )

        # parse using the two sets of coords 
        for row, num_objs in number_coords.items():
            for num_obj in num_objs:
                cur_span = num_obj["span"]                

                below_row = row + 1
                above_row = row - 1

                if below_row in symbol_coords.keys():
                    indices = symbol_coords[below_row]

                    for index in indices:
                        if index in range(cur_span[0]-1, cur_span[-1]+1):
                            num_obj["is_part_no"] = True

                if above_row in symbol_coords.keys():
                    indices = symbol_coords[above_row]
                    for index in indices:
                        if index in range(cur_span[0]-1, cur_span[-1]+1):
                            num_obj["is_part_no"] = True

                if row in symbol_coords.keys():
                    indices = symbol_coords[row]
                    for index in indices:
                        if index in range(cur_span[0]-1, cur_span[-1]+1):
                            num_obj["is_part_no"] = True
                
        sum_of_parts = 0                    
        for index, num_objs in number_coords.items():
            for num_obj in num_objs:
                if num_obj["is_part_no"]:
                    sum_of_parts += int(num_obj["value"])
        '''                
        for current_row, number_coords in number_coords.items():
            above_row = current_row - 1
            below_row = current_row + 1

            if current_row in symbol_coords.keys():
                
                print(current_row)
                for symbol_coord in symbol_coords[current_row]:
                    for number_coord in number_coords:
                        print(number_coord, symbol_coord)
                        if number_coord[1] == symbol_coord or number_coord[0] - 1 == symbol_coord:
        '''                            


        # pretty print the symbol and number coords
        for index, coords in number_coords.items():
            print(index, coords)
        print("*********")
        for index, symbol_coord in symbol_coords.items():
            print(index, symbol_coord)
        # print(symbol_coords) 
        print(sum_of_parts)
    return ""

def part_two():
    pass 


part_one()
part_two()

'''
symbols = set() 
with open("input.txt", "r") as f:
    data = f.read()
    lines = data.split("\n")
    for l in lines:
        for x in l:
            if not x.isdigit() and x != '.':
                symbols.add(x)
print(symbols)
'''
                
# 508875 bad 