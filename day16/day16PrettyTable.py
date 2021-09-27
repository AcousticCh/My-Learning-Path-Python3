#!usr/bin/env python
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Element Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

table2 = PrettyTable()
table2.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table2.add_column("Element Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)
print(table2)
