from nc_console import Console

Console.log.Info("started info message")

Console.log.Error("started Error message")

a = Console.input.Integer("enter integer typr value: ")
Console.log.Success("the value of a is: "+str(a))