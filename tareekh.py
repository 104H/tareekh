#! /usr/bin/python3

import sys
import os
import json

def main():
    # initialize new project
    if sys.argv[1] == "new":
        path = "projects/" + sys.argv[2] + "/"

        if os.path.exists(path):
            print("A project by this name already exists. Please pick a unique name")
            return

        os.mkdir(path)
        open(path + "worklog", 'x')

    if sys.argv[1] == "record":
        project = sys.argv[2]
        start = sys.argv[3]
        end = sys.argv[4]
        date = sys.argv[5]
        description = sys.argv[6]

        with open("projects/" + project + "/worklog", "a") as worklog:
            #log = json.load(worklog)
            log = {
                    "date" : date,
                    "starttime" : start,
                    "endtime" : end,
                    "description" : description
                }

            json.dump(log, worklog)

    if sys.argv[1] == "view":
        project = sys.argv[2]

        with open("projects/" + project + "/worklog", "r") as worklog:
            log = json.load(worklog)["log"]

            if sys.argv[3] == "total":
                totaltime = 0
                for l in log:
                    totaltime += int(l["endtime"]) - int(l["starttime"])
                print(f"Total Number of Hours Spent {totaltime / 100}")

if __name__ == "__main__":
    main()
