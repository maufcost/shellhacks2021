fin = open("formatted.txt", "r")
line_c = 0
le_dict = {}
done = []

# Normalize Volume str
def convert_volume(strnum):
    if "M" in strnum:
        return float(strnum[:-1]) * 1_000_000
    if "K" in strnum:
        return float(strnum[:-1]) * 1_000

all_lines = []
for line in fin:
    if line_c != 0:
        all_lines.append(line.rstrip())
    line_c += 1

formatted_data = {}
for i in range(len(all_lines)-5):
    nested_dict = {}
    c = 1
    for x in range(i, i+5):
        le_string = "prevp{}".format(c)
        le_string2 = "prevo{}".format(c)
        le_string3 = "prevh{}".format(c)
        le_string4 = "prevl{}".format(c)
        le_string5 = "prevv{}".format(c)

        current_arr = all_lines[x].split(",")
        print(current_arr)
        nested_dict[le_string] = float(current_arr[1]) #price
        nested_dict[le_string2] = float(current_arr[2]) #price
        nested_dict[le_string3] = float(current_arr[3]) #price
        nested_dict[le_string4] = float(current_arr[4]) #price
        nested_dict[le_string5] = convert_volume(current_arr[5]) #price

        c += 1
    formatted_data[all_lines[i].split(",")[0]] = nested_dict

csv_export = "Date,"
for i in range(1,6):
    csv_export += "prevp{},".format(i)
    csv_export += "prevo{},".format(i)
    csv_export += "prevh{},".format(i)
    csv_export += "prevl{},".format(i)
    csv_export += "prevv{},".format(i)
csv_export += "\n"
for each_key in formatted_data:
    csv_export += each_key + ","
    for i in range(1,6):
        csv_export += str(formatted_data[each_key]["prevp{}".format(i)]) + ","
        csv_export += str(formatted_data[each_key]["prevo{}".format(i)]) + ","
        csv_export += str(formatted_data[each_key]["prevh{}".format(i)]) + ","
        csv_export += str(formatted_data[each_key]["prevl{}".format(i)]) + ","
        csv_export += str(formatted_data[each_key]["prevv{}".format(i)]) + ","
    csv_export += "\n"

print(csv_export)
fout = open("test.csv","w")
fout.write(csv_export)
fout.close()
fin.close()
