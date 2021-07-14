from nc_console import Console

Console.setLogConfig(box_colour="bright_cyan")
Console.setInputConfig(box_colour="bright_cyan")

Console.log.Info("started info message")
Console.log.Error("started Error message")

Console.log.Error("started Error message with options", log_type_options={"fg":"red", "reverse":True})

# a = Console.input.Integer("enter integer type value: ")
# b = Console.input.String("Enter your name: ")
# c = Console.input.Boolean("Do you really love me")
# p = Console.input.Password("enter the password here: ")
Console.log.Success("the value of p: "+str(4))