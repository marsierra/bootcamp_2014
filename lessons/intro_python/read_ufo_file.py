import sys
def read_file(filename):
    ofile = open(filename, 'r')
    all_lines = ofile.readlines()
    return all_lines

def parse_line(iline):
    split_line = iline.split()
    split_line[1] = float(split_line[1])
    return split_line[0], split_line[1]

if __name__ == "__main__":
    filename = sys.argv[1]
    all_lines = read_file(filename)
    date_list = []
    ufo_num = []
    for iline in all_lines:
        date, number_of_ufos = parse_line(iline)
        date_list.append(date)
        ufo_num.append(number_of_ufos)
    print date_list
    print ufo_num