# terminalutilities
A set of utilities for use in a terminal.



## Progress Bar
A progress bar used to track the progress of a value from 0 to some maximum value, printing in-place (overwriting) this progress.

### Usage
Initialise the bar by creating a `ProgressBar` object, passing at least a title and a maximum value, then call `Update` with the new value. Once the value has reached its maximum, call `Complete` to finalise the bar and continue with the program.

### Example
```python
n = 999999
pb = terminalutilities.ProgressBar("Doing", n)
x = 0
while x < n:
    x += 1
    pb.Update(x)
pb.Complete()
```



## Selection Menu
A selection menu used to allow the user to execute one of a set of prebuilt commands.

### Usage
Set up a list of 'options', which are dictionaries with keys
* `name`: The name of the option
* `aliases`: A list of all the words that will trigger this option
* `desc`: A description of the option
* `func`: The function to be executed upon selecting this option; such a function must take in a single argument `args` which is a list of all words given after the trigger word (e.g. inputting 'test arg1 arg2' makes `args == ['arg1', 'arg2']`; inputting 'test' makes `args == []`).

Two options are included by default: 
"Help", which displays a list of all the options available to this menu; and
"Quit", which quits the menu.

The menu will continue prompting the user until one of the functions it calls returns something not `None` (the function for "Quit" returns `-1`)

### Example
```python
def TestOption(args):
    print("test option's function is working")
options = [ {"name": "testoption",
             "desc": "this is a test option",
             "aliases": ["testoption", "test", "t", "testop"],
             "func": TestOption} ]
SelectionMenu(options)
```
