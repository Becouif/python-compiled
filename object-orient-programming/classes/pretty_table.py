from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Person Name","Age", "Country", "City"]

table.add_rows(
  [
    ["John", 25, "USA", "New York"],
    ["Mary", 30, "UK", "London"],
    ["Peter", 35, "Canada", "Toronto"],
    ["Sarah", 40, "Germany", "Berlin"],
    ["Michael", 45, "Japan", "Tokyo"],
    ["Emily", 50, "Australia", "Sydney"],
  ]
)
table.align = "l"


print(table)