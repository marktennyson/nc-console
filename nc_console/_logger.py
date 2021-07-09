import click as c
import typing as t

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