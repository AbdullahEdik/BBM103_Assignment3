import sys


def is_category_recorded(category_name):
    for name in categories.keys():
        if name == category_name:
            return categories[name]

    return None


def create_category(category_info):
    category_info = category_info.split(' ')

    if is_category_recorded(category_info[0]) is not None:
        print(f"Warning: Cannot create the category for the second time. The stadium has already {category_info[0]}.\n")
        w_file.write(f"Warning: Cannot create the category for the second time. The stadium has already "
                     f"{category_info[0]}.\n")

    else:
        num_of_rows, num_of_columns = category_info[1].split('x')
        num_of_rows, num_of_columns = int(num_of_rows), int(num_of_columns)
        category = [['X' for _ in range(num_of_columns)] for _ in range(num_of_rows)]
        categories[category_info[0]] = category

        print(f"The category ’{category_info[0]}’ having {num_of_rows * num_of_columns} seats has been created\n")
        w_file.write(f"The category ’{category_info[0]}’ having {num_of_rows * num_of_columns} "
                     f"seats has been created\n")

def sell_ticket(ticket_info):
    ticket_info = ticket_info.split(' ')

    


if __name__ == '__main__':
    file_name = sys.argv[1]
    r_file = open(file_name, 'r')
    w_file = open('output.txt', 'w')
    lines = r_file.read()
    lines = lines.split("\n")

    categories = {}

    for line in lines:
        line_list = line.split(' ', 1)

        if line_list[0] == "CREATECATEGORY":
            create_category(line_list[1])

        elif line_list[0] == "SELLTICKET":
            sell_ticket(line_list[1])
