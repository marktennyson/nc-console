from nc_console import Console

Console.setLogConfig(msg_colour="bright_cyan")
# Console.setInputConfig(msg_colour="bright_cyan")

Console.log.Info("started info message")

Console.log.Error("started Error message", log_type_options={"fg":"red", "reverse":True})

a = Console.input.Integer("enter integer type value: ")
b = Console.input.String("Enter your name: ")
c = Console.input.Boolean("Do you really love me")
p = Console.input.Password("enter the password here: ")
# a=9
Console.log.Success("the value of p: "+str(p))

# import click as c

# st = c.style("enter your name: ", fg="red")
# input(st)