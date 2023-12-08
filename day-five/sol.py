from typing import DefaultDict

file_name = "input.txt"
with open(file_name, 'r') as f:
    data = f.read()

def translate_a_to_b(map, val_to_translate: int):
    translated_val = val_to_translate

    translations = map.strip().split("\n")

    for translation in translations:
        vals = translation.split(" ")

        dest = int(vals[0])
        source = int(vals[1])
        translation_range = int(vals[2])

        if val_to_translate in range(source, source + translation_range + 1):
            diff_from_source = val_to_translate - source 
            translated_val = diff_from_source + dest
            break

    return translated_val


def part_one():
    # random attempt here 
    splitted_data = data.split("\n\n")
    seeds, rest = splitted_data[0], splitted_data[1:]
    maps = []
    for x in rest:
        maps.append(x.split(":\n")[1])

    cur_seed_val = 0
    loc_vals = []
    for seed in seeds.split(": ")[1].split(" "):
        cur_seed_val = int(seed)
        for map in maps:
            cur_seed_val = translate_a_to_b(map, cur_seed_val)
        loc_vals.append(cur_seed_val)
    print(min(loc_vals))

part_one()