#! /usr/bin/python3

import sys
import os

def main():
    # initialize new project
    try:
        if sys.argv[1] == "new":
            path = "projects/" + sys.argv[2] + "/"
            os.mkdir(path, 7777)
            open(path + "worklog", 'x')
    except FileExistsError:
        print("A project by this name already exists. Please pick a unique name")

if __name__ == "__main__":
    main()
