from mast_stat import MastStat
from mast_data_reader import MastDataReader
from show_help import ShowHelp
import datetime
from datetime import timedelta

path_to_csv = "Mobile Phone Masts.csv"

def print_list(list_to_print):
    for item in list_to_print:
        print(item)

def print_dict(dict_to_print):
    print("*" * 87)
    print("| Tenant Name" + " " * 60 +"| Total Mast |")
    print("*" * 87)
    for k, v in dict_to_print.items():
        print("|{:55}                 |{:12}|".format(k,v))

def run_command(command):
    if command.startswith("--help"):
        showhelp = ShowHelp()
        showhelp.show()
    elif command.startswith("--list"):
        mastreader = MastDataReader(path_to_csv)
        top5 = mastreader.sorted_top(5)
        print_list(top5)
    elif command.startswith("--filter"):
        mastreader = MastDataReader(path_to_csv)
        lease25year = mastreader.list_filtered(lambda x: x[9] == "25")
        print_list(lease25year)
    elif command.startswith("--stat"):
        maststate = MastStat()
        stat = maststate.get_tenant_mast_count(MastDataReader(path_to_csv).get_all(), 6)
        print_dict(stat)
    elif command == "--exit":
        pass


command = input()
run_command(command)
