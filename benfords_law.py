import csv

def populate_data():
    ''' This creates a blank dictionary and parses the values
    of the csv file to it '''
    
    return_dict = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0
    }

    with open('flights.csv') as csvfile:
        line = csv.reader(csvfile)
        next(line)
        for each in line:
            try:
                digits = each[13]
                leading_digit = int(digits[0])
                return_dict[leading_digit] += 1
            except:
                continue

    return return_dict

def print_results(insert_dict):
    ''' This just prints the data results in a user friendly manner '''
    
    print("")
    total_numbers = sum(insert_dict.values())
    for each in insert_dict:
        stars_print = round((insert_dict[each]/total_numbers) * 100)
        print(str(each) + "  ", end='')
        for i in range(0, stars_print):
            print("*", end='')
        print("   " + str(stars_print)+ "%" )
    print("")


###################################
''' Program Below '''
##################################



benford_results = populate_data()

print_results(benford_results)
