from mast_data_reader import MastDataReader
from show_help import ShowHelp
import datetime
from datetime import timedelta

def print_list(list_to_print):
    for item in list_to_print:
        print(item)

def run_command(command):
    if command.startswith("--help"):
        showhelp = ShowHelp()
        showhelp.show()
    elif command.startswith("--list"):
        mastreader = MastDataReader("Mobile Phone Masts.csv")
        top5 = mastreader.sorted_top(5)
        print_list(top5)
    elif command == "--exit":
        pass

command = input()
run_command(command)
