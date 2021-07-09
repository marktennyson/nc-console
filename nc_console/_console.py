from ._logger import _logger
from ._colours import colours
from getpass import getpass
import typing as t
import click as c

default_input = input

class log:

    _logger_class = _logger

    @classmethod
    def _clogger(cls, 
            type:str, 
            message_:str,
            open_box_options:t.Optional[t.Dict[str, t.Any]]=None,
            create_log_base_options:t.Optional[t.Dict[str, t.Any]]=None,
            close_box_options:t.Optional[t.Dict[str, t.Any]]=None,
            message_options:t.Optional[t.Dict[str, t.Any]]=None 
            ) -> None:
            
            if open_box_options is not None:
                ob_msg_ins = cls._logger_class._open_box(**open_box_options)
            else:
                ob_msg_ins = cls._logger_class._open_box()

            if create_log_base_options is not None:
                clbm_msg_ins = cls._logger_class._create_log_base_msg(type, **create_log_base_options)
            else:
                clbm_msg_ins = cls._logger_class._create_log_base_msg(type)

            if close_box_options is not None:
                cb_msg_ins = cls._logger_class._close_box(**close_box_options)
            else:
                cb_msg_ins = cls._logger_class._close_box()

            if message_options is not None:
                m_msg_ins = cls._logger_class._message(message_, **message_options)
            else:
                m_msg_ins = cls._logger_class._message(message_)

            c.echo(ob_msg_ins+clbm_msg_ins+cb_msg_ins+m_msg_ins)

    @classmethod
    def Success(cls, 
                message:str=None, 
                open_box_options:t.Optional[t.Dict[str, t.Any]]=None,
                create_log_base_options:t.Optional[t.Dict[str, t.Any]]=None,
                close_box_options:t.Optional[t.Dict[str, t.Any]]=None,
                message_options:t.Optional[t.Dict[str, t.Any]]=None
                ) -> t.NoReturn:
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
            
            for _message in message_line_list: 
                 cls._clogger("success", _message,
                        open_box_options,
                        create_log_base_options,
                        close_box_options,
                        message_options)
        
        else: cls._clogger("success", message,
                open_box_options,
                create_log_base_options,
                close_box_options,
                message_options)
    
    @classmethod
    def Error(cls, message:str=None,
                open_box_options:t.Optional[t.Dict[str, t.Any]]=None,
                create_log_base_options:t.Optional[t.Dict[str, t.Any]]=None,
                close_box_options:t.Optional[t.Dict[str, t.Any]]=None,
                message_options:t.Optional[t.Dict[str, t.Any]]=None
                ) -> t.NoReturn:
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
            
            for _message in message_line_list: 
                 cls._clogger("error", _message,
                        open_box_options,
                        create_log_base_options,
                        close_box_options,
                        message_options)
        
        else: cls._clogger("error", message,
                open_box_options,
                create_log_base_options,
                close_box_options,
                message_options)
    
    @classmethod
    def Info(cls, message:str=None, 
                open_box_options:t.Optional[t.Dict[str, t.Any]]=None,
                create_log_base_options:t.Optional[t.Dict[str, t.Any]]=None,
                close_box_options:t.Optional[t.Dict[str, t.Any]]=None,
                message_options:t.Optional[t.Dict[str, t.Any]]=None
                ) -> t.NoReturn:
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
            
            for _message in message_line_list: 
                 cls._clogger("info", _message,
                        open_box_options,
                        create_log_base_options,
                        close_box_options,
                        message_options)
        
        else: cls._clogger("info", message,
                open_box_options,
                create_log_base_options,
                close_box_options,
                message_options)
    
    @classmethod
    def Warning(cls, message:str=None, 
                open_box_options:t.Optional[t.Dict[str, t.Any]]=None,
                create_log_base_options:t.Optional[t.Dict[str, t.Any]]=None,
                close_box_options:t.Optional[t.Dict[str, t.Any]]=None,
                message_options:t.Optional[t.Dict[str, t.Any]]=None
                ) -> t.NoReturn:
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
            
            for _message in message_line_list: 
                 cls._clogger("warning", _message,
                        open_box_options,
                        create_log_base_options,
                        close_box_options,
                        message_options)
        
        else: 
            cls._clogger("warning", message,
                open_box_options,
                create_log_base_options,
                close_box_options,
                message_options)

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

        string = default_input(_message)
        try: 
            return str(string)

        except: 
            log.Error("Inputed data is not string type.")
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

        integer = default_input(_message)
        try: 
            return int(integer)
        except:
            log.Error("Input data is not Integer type")
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
        
        _float = default_input(message)
        try: 
            return float(_float)
        except:
            log.Error("input data is not float type.")
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
            boolean = default_input(_message)
            if not boolean: continue
            if str(boolean).lower() == "y" or str(boolean).lower() == "yes": return True
            if str(boolean).lower() == "n" or str(boolean).lower() == "no": return False
            else: 
                log.Error("Invalid input type. Proper ans format is : y for yes and n for no") 
                continue