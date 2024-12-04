from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Charisard","Squirtel",])
table.add_column("Type",["Electric","Fire","Water"])
table.left_padding_width=6
print(table)