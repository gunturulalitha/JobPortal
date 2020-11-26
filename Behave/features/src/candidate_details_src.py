import csv


def do_login():
    user_data = csv.DictReader(open("C://employee_file.csv"))
    for row in user_data:
        print(row['First Name'], row['Last Name'], row['Phone Num'], row['Email'], row['Skills'], row['Education'],
              row['Emp Auth'])


do_login()


