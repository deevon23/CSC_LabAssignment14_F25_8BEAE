"""
Please open the file "lab2_file.txt" to see its structure.
It has the following structure:
    Pink,85
    Red,44
    Maroon,80

File "lab2_file.txt" records the number of paint bottles bought within a year,
every line has two fields: the color of the paint, and the number of bottles,
and they are separated by a comma (,)

This program is used to count the number of bottles for each color,
and write the final result into a new file.
"""


def count_paint_bottles(input_file, output_file):
    # TODO: create an empty dictionary called `totals` to count all bottles
    total = {}

    # TODO: open the file (argument `input_file`) with mode "r"
    file_obj = open(input_file, "r")

    for line in file_obj:
        line = line.strip()
        if not line:
            continue

        fields = [f.strip() for f in line.split(",")]
        color = fields[0]
        num = int(fields[1])

        if color not in totals:
            total[color] = num
            # TODO: if the dictionary doesn't record the color yet, add one new entry (the key is the color, the value is the num)
        else:
            totals[color] += num
            # TODO: if the dictionary has the color already, we add the num into the existing value

    # TODO: close the file object
    file_obj.close()

    # TODO: open the output file (argument `output_file`) with mode "w", name the file object as `file_obj2`
    file_obj2 = open(output_file, "w")

    for color in totals.keys():
        num_str = str(totals[color])
        string_to_write = color + ":" + num_str # comebine the string

        file_obj2.write(string_to_write + "\n")

    file_obj2.close()


if __name__ == "__main__":
    count_paint_bottles("lab2_file.txt", "lab2_result.txt")
