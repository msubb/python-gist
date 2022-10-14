import github.InputFileContent
from github import Github
import threading  # used to delay actions

pain = 0  # this can be any variable


def printit():  # defines the function
    threading.Timer(5, printit).start()  # the 5 represents 5 seconds 
    global pain
    pain = pain + 1  # this adds 1 to the global variable pain each loop

    g = Github("insert access token here")

    gist = g.get_gist("insert gist link here")
    gist.edit(
        "",
        {"gistfile1.txt": github.InputFileContent(str(pain))},
    )

    print(pain)  # prints pain to the terminal


printit()  # runs the functions
