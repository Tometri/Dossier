import csv

sales = []
with open('bestsellers.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # skip the header row
    for column in csv_reader:
        # columns: Title, Author, Language, Year, Sales_in_millions, Genre
        try:
            sales_val = float(column[4])
        except (ValueError, IndexError):
            continue
        sales.append(sales_val)

if sales:
    print(max(sales))