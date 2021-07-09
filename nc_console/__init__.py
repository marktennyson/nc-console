from .colours import colours
from getpass import getpass
import click as c
import typing as t

__version__ = "0.0.1"

__author__ = "Aniket Sarkar"

class _logger:

    @classmethod
    def _open_box(cls, **options:t.Any) ->str:
        return c.style("[ ", fg="white", bold=True)

    @classmethod
    def _close_box(cls, **options:t.Any) -> str:
        options.setdefault("fg", "white")
        options.setdefault("bold", True)
        return c.style(" ] ", **options)

    @classmethod
    def _create_log_base_msg(cls, type:str, **options:t.Any):

        colour:str = "blue" 

        if options.get("colour", None) is None:

            if type.lower() == "info":
                colour = "bright_blue"
            
            elif type.lower() == "warning":
                colour = "magenta"
            
            elif type.lower() == "success":
                colour = "green"

            elif type.lower() == "error":
                colour = "red"

        else:
            colour = options.get("colour")

        options.setdefault("fg", colour)
        options.setdefault("bold", True)
        return c.style(type.upper(), **options)

    @classmethod
    def _message(cls, msg:str, **options:t.Any):
        options.setdefault("fg", "bright_yellow")
        return c.style(msg, **options)

class Console:

    class log:

        _logger_class = _logger

        @classmethod
        def _clogger(cls, type:str, message_:str, **options) -> None:
                c.echo(cls._logger_class._open_box(**options)+\
                        cls._logger_class._create_log_base_msg(type, **options)+\
                            cls._logger_class._close_box(**options)+\
                                cls._logger_class._message(message_, **options))

        @classmethod
        def Success(cls, message:str=None, **options:t.Any) -> t.NoReturn:
            """
            Log the success message at terminal.

           :param message:
                the default message to be logged in the terminal.

            :param options:
                the kwargs based param. This is useful if you want
                to customize the logger colour and other options.
                By this you can set the arguments value for click.style().

            example::

                Console.log.Success("image added successfully.")
            """
            if "\n" in message:
                message_line_list:list = message.split("\n")
                for _message in message_line_list: cls._clogger("success", _message)
            else: cls._clogger("success", message)
        
        @classmethod
        def Error(cls, message:str=None) -> str:
            """
            Log the error message at terminal.

           :param message:
                the default message to be logged in the terminal.

            :param options:
                the kwargs based param. This is useful if you want
                to customize the logger colour and other options.
                By this you can set the arguments value for click.style().

            example::

                Console.log.Error("Failed to add image.")
            """
            if "\n" in message:
                message_line_list:list = message.split("\n")
                for _message in message_line_list: cls._clogger("error", _message)
            else: cls._clogger("error", message)
        
        @classmethod
        def Info(cls, message:str=None) -> str:
            """
            Log the info message at terminal.

           :param message:
                the default message to be logged in the terminal.

            :param options:
                the kwargs based param. This is useful if you want
                to customize the logger colour and other options.
                By this you can set the arguments value for click.style().

            example::

                Console.log.Info("Image upload process started.")
            """
            if "\n" in message:
                message_line_list:list = message.split("\n")
                for _message in message_line_list: cls._clogger("info", _message)
            else: cls._clogger("info", message)
        
        @classmethod
        def Warning(cls, message:str=None) -> str:
            """
            Log the warning message at terminal.

           :param message:
                the default message to be logged in the terminal.

            :param options:
                the kwargs based param. This is useful if you want
                to customize the logger colour and other options.
                By this you can set the arguments value for click.style().

            example::

                Console.log.Warning("Uploading image process is asking for S3 credentials.")
            """
            if "\n" in message:
                message_line_list:list = message.split("\n")
                for _message in message_line_list: cls._clogger("warning", _message)
            else: cls._clogger("warning", message)

    class input:

        @classmethod
        def String(cls, message:t.Optional[str]=None) -> t.Optional[str]:
            """
            take the string type input from the terminal.

            :param message:
                the default message you want to log 
                while taking the string input from terminal.

            example::

                Console.input.String("Please enter your name: ")
            """
            
            _message = colours.white+\
                    "[ "+colours.cyan+"INPUT"+colours.white+" ] "\
                        +colours.yellow+message+colours.reset

            string = input(_message)
            try: 
                return str(string)

            except: 
                Console.log.Error("Inputed data is not string type.")
                raise TypeError(f"string type data required. got : {type(string).__name__}")
                
        def Password(message:t.Optional[str]=None) -> str:
            """
            take the password input from the terminal.

            :param message:
                the default message you want to log 
                while taking the password input from terminal.

            example::

                Console.input.Password("Please enter your password: ")
            """
            _message = colours.white+\
                    "[ "+colours.cyan+"INPUT"+colours.white+" ] "+\
                        colours.yellow+message+colours.reset

            password = getpass(prompt=_message)
            return password
                    

        def Integer(message:t.Optional[str]=None) -> t.Optional[int]:
            """
            take the integer input from the terminal.

            :param message:
                the default message you want to log 
                while taking the integer input from terminal.

            example::

                Console.input.Integer("Please enter your age: ")
            """
            _message = colours.white+\
                    "[ "+colours.cyan+"INPUT"+colours.white+" ] "+\
                        colours.yellow+message+colours.reset

            integer = input(_message)
            try: 
                return int(integer)
            except:
                Console.log.Error("Input data is not Integer type")
                raise TypeError(f"int type data required. got: {type(integer).__name__}")

        def Float(message:t.Optional[str]=None) -> t.Optional[float]:
            """
            take the float input from the terminal.

            :param message:
                the default message you want to log 
                while taking the float input from terminal.

            example::

                Console.input.Float("Please enter any float value: ")
            """
            _message = colours.white+\
                    "[ "+colours.cyan+"INPUT"+colours.white+" ] "+\
                        colours.yellow+message+colours.reset
            
            _float = input(message)
            try: 
                return float(_float)
            except:
                Console.log.Error("input data is not float type.")
                raise TypeError(f"float type data required. got: {type(_float).__name__}")

        def Boolean(message:t.Optional[str]=None) -> bool:
            """
            take the float input from the terminal.

            :param message:
                the default message you want to log 
                while taking the float input from terminal.
                It will add (Y/n): after the message automatically.

            example::

                Console.input.Boolean("Do you want to continue")
            """
            _message = colours.white+\
                    "[ "+colours.cyan+"INPUT"+colours.white+" ] "+\
                        colours.yellow+message+"(Y/n): "+colours.reset
            while True:
                boolean = input(_message)
                if not boolean: continue
                if str(boolean).lower() == "y" or str(boolean).lower() == "yes": return True
                if str(boolean).lower() == "n" or str(boolean).lower() == "no": return False
                else: 
                    Console.log.Error("Invalid input type. Proper ans format is : y for yes and n for no") 
                    continue       