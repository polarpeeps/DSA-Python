# from turtle import Turtle,Screen
from prettytable import PrettyTable
x = PrettyTable()# t = Turtle()
# print(tt)
# tt.shape("turtle")
# tt.color("teal")
# tt.forward(100)
# my_s = Screen()
# print(my_s.canvheight)
# my_s.exitonclick()t
# pp =PrettyTable()
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])
# print(x)
x.field_names = ['Pokemon Name',"Type"]
x.add_row(["pikachu","electric"])
x.add_row(["squritle","water"])
x.add_row(["charmandar","fire"])
x.align = "l"
print(x)