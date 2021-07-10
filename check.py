import typing as t

box_colour_:str = "white"
msg_colour_:str = "bright_yellow"
type_info_colour_:str = "bright_blue"
type_success_colour_:str = "bright_green"
type_error_colour_:str = "bright_red"
type_warning_colour_:str = "bright_magenta"

def setConfig(box_colour:t.Optional[str] = None,
        msg_colour:t.Optional[str] = None,
        type_info_colour:t.Optional[str] = None,
        type_success_colour:t.Optional[str] = None,
        type_error_colour:t.Optional[str] = None,
        type_warning_colour:t.Optional[str] = None):

        if box_colour is not None:
            global box_colour_
            box_colour_ = box_colour

setConfig(box_colour="green")
print (box_colour_)

# x = "global"

# def foo():
#     global x
#     x = x * 2
#     print(x)

# # foo()
# print ("a")