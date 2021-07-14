# nc-console

 ```bash

███╗   ██╗ ██████╗ ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗ ██╗     ███████╗
████╗  ██║██╔════╝██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██║     ██╔════╝
██╔██╗ ██║██║     ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     █████╗  
██║╚██╗██║██║     ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██╔══╝  
██║ ╚████║╚██████╗╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝
                                                                              

                                             
```
 The programmatic consoler.  
 Checkout the official documentation at [nc-console.netlify.app](nc-console.netlify.app)

##### Now it's quite easy to log the status and take inputs from the terminal using nc-colsole.

### Introduction

nc-console provides you a clean, understandable and programmatic overview to log your data on the terminal or take inputs from the terminal. 

It's internally using the [click](https://click.palletsprojects.com/en/8.0.x/) module from [palletsprojects](https://palletsprojects.com/) to deliver such services.

### Requirements

To use this module you must need to use Python version 3.6 or grater than it.

This module requires the following modules:
* click==8.0.1

### Installation

You can install the package from the official PYPI:
```bash
pip install nc-console
```
You can install it directly from the source code:
```bash
git clone https://github.com/marktennyson/nc-console.git && cd nc-colsole
python setup.py install
```

### Usage

#### Implementation of logging system.
##### It gives you a very logical way to print your logging output.

For a basic example:
```python
from nc_console import Console
Console.log.Info("This is the first info message.")
```
And the output will be:
```bash
[ INFO ] This is the first info message. 
```
Available options/methods to print the different log:
```python
Console.log.Info()
Console.log.Warning()
Console.log.Success()
Console.log.Error()
```
* The default colour for type `info` is `bright_blue`.
* The default colour for type `success` is `bright_green`.
* The default colour for type `warning` is `bright_magenta`.
* The default colour for type `Error` is `bright_red`.
* The default colour for `message` is `yellow`.

It's very easy to change the default colours. To do this please go with the below mentioned steps:
```python
from nc_console import Console

Console.setLogConfig(
        box_colour="cyan"
        type_info_colour="red"
        ...
)
```
So using the `setLogConfig` method you can adjust the default colours.
Available parameters for the `setLogConfig` method are:
* box_colour : to change the box([]) colour.
* msg_colour : to change the colour of message.
* type_info_colour : to change the base colour for the type info.
* type_success_colour : to change the base colour for the type success.
* type_warning_colour : to change the base colour for the type warning.
* type_error_colour : to change the base colour for the type error.

All of the colours accept the default available colour for `click.style`.

#### Implementation of input system.
##### Beside the logging system this module is able to take inputs from the terminal too. This system will give you the feelings like Java.

For a basic example:
```python
from nc_console import Console

#To take a string based input from the terminal
name = Console.input.String("Enter your name: ")

#To take a Integer based input from the terminal
age = Console.input.Integer("Enter your age: ")
```
The output will be:
```bash
[INPUT STRING] Enter your name: 
[INPUT INTEGER] Enter your age:
```

Available options/methods to take different types of input from the terminal:
```python
Console.input.String()
Console.input.Password()
Console.input.Integer()
Console.input.Float()
Console.input.Boolean()
```

* The default colour for `type` is `bright_blue`.
* The default colour for `message` is `yellow`.

It's very easy to change the default colours for the input system too. To do this please go with the below mentioned steps:
```python
from nc_console import Console

Console.setInputConfig(
        box_colour="cyan"
        msg_colour="red"
        ...
)
```

So using the `setInputConfig` method you can adjust the default colours.
Available parameters for the `setLogConfig` method are:
* box_colour : to change the box([]) colour.
* msg_colour : to change the colour of message.
* base_colour : to change the base colour for the input text.
* type_colour : to change the input type colour.

All of the colours accept the default available colour for `click.style`.

### Maintainers
Current Maintainers:
1. Aniket sarkar aka [marktennyson](https://github.com/marktennyson)

### Contributors
Current Contributors:  

<a href="https://github.com/marktennyson/nc-console/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=marktennyson/nc-console" />
</a>

### Contribution

If you want to become a contributor of this project then please contact me at => `aniketsarkar@yahoo.com` or follow the below mentioned steps.

1. Fork and clone this repository.
2. Make some changes as required.
3. Write unit test to showcase its functionality.
4. Submit a pull request under `development` branch.