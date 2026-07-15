from prettytable import PrettyTable

table=PrettyTable()
table.add_column("pokemon",["pikachu","charizard","meotod","straxus","caracuxs"])
table.add_column("type",["electric","fire","physcic","rock","fire"])
print(table)
table.align="l"
print(table)