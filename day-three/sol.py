import re 
from typing import DefaultDict

symbols = set() 

input_file_name = "input.txt"
with open(input_file_name, "r") as f:
    data = f.read()
    lines = data.split("\n")
    for l in lines:
        for x in l:
            if not x.isdigit() and x != '.':
                symbols.add(x)

def part_one(symbols):
    with open(input_file_name, "r") as f:
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
                row_types = {below_row, above_row, row}
                for row_type in row_types: 
                    if row_type in symbol_coords.keys():
                        indices = symbol_coords[below_row]

                        for index in indices:
                            if index in range(cur_span[0]-1, cur_span[-1]+1):
                                num_obj["is_part_no"] = True

        sum_of_parts = 0                    
        for index, num_objs in number_coords.items():
            for num_obj in num_objs:
                if num_obj["is_part_no"]:
                    sum_of_parts += int(num_obj["value"])
    return sum_of_parts 


def part_two(symbols):
    with open("input.txt", "r") as f:
        data = f.read()
        lines = data.split("\n")

        # TODO: change to symbol_objs
        symbol_objs = DefaultDict(list)        

        # get the symbol coordinates
        for i in range(len(lines)):
            line = lines[i]
            for j in range(len(line)):
                if line[j] in symbols:
                    symbol_objs[i].append({"adj_list": [], "index": j, "value": line[j]})

        # get the coordinates of the number
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

                below_row = row + 1
                above_row = row - 1
                cur_span = num_obj["span"]                

                for row_type in {below_row, above_row, row}:
                    symbols = symbol_objs[row_type]
                
                    for symbol in symbols:
                        index = symbol["index"]
                        if index in range(cur_span[0]-1, cur_span[-1]+1):
                            num_obj["is_part_no"] = True
                            if symbol["value"] == "*":
                                symbol["adj_list"].append(int(num_obj["value"]))
                
        sum_of_parts = 0                    
        for index, num_objs in number_coords.items():
            for num_obj in num_objs:
                if num_obj["is_part_no"]:
                    sum_of_parts += int(num_obj["value"])

        product_ratio_sum = 0
        for index, symbol_objs in symbol_objs.items():
            for symbol_obj in symbol_objs:
                cur_product_ratio = 1
                if len(symbol_obj["adj_list"]) == 2:
                    for neighbor in symbol_obj["adj_list"]:
                        cur_product_ratio *= neighbor 
                else: continue
                product_ratio_sum += cur_product_ratio
    return product_ratio_sum


symbols = set() 

input_file_name = "input.txt"
with open(input_file_name, "r") as f:
    data = f.read()
    lines = data.split("\n")
    for l in lines:
        for x in l:
            if not x.isdigit() and x != '.':
                symbols.add(x)

print(f"Part 1: {part_one(symbols)}")
print(f"Part 2: {part_two(symbols)}")

