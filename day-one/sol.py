def part_one(): 
    with open("input.txt", "r") as f:
        data = f.read()
        lines = data.split("\n")
        
        numbers_on_lines = []

        for line in lines:
            first_digit = ""
            last_digit = ""

            for i in range(len(line)):
                if line[i] in "0123456789":
                    if not first_digit:
                        first_digit = line[i]
                    last_digit = line[i]

            calibration_number = first_digit + last_digit            
            if first_digit and last_digit:
                numbers_on_lines.append(int(calibration_number))

        return sum(numbers_on_lines)

def part_two(): 
    str_to_num = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    with open("input.txt", "r") as f:
        data = f.read()
        lines = data.split("\n")

        nums_on_lines = []
        for line in lines:
            nums_on_line = []
            for i in range(len(line)):
                if line[i] in "123456789":
                    nums_on_line.append(line[i])
                    pass
                else:
                    if line[i] in "onetwothreefourfivesixseveneightnine":
                        potential_num = ""
                        for j in range(i, len(line)):
                            potential_num += line[j]
                            if potential_num in str_to_num.keys():
                                nums_on_line.append(str_to_num[potential_num])
                                break
                            else:
                                continue
            nums_on_lines.append(nums_on_line)
        total = 0
        for line in nums_on_lines:
            total += int(line[0] + line[-1])
        return total

print("Part One")
print(part_one())

print("Part Two")
print(part_two())

