from mast_stat import MastStat
from mast_data_reader import MastDataReader
from show_help import ShowHelp
from datetime import datetime

path_to_csv = "Mobile Phone Masts.csv"

# Printing the given list to console
def print_list(list_to_print):
    for item in list_to_print:
        print(item)

# Printing the given dictionary to console
def print_dict(dict_to_print):
    print("*" * 87)
    print("| Tenant Name" + " " * 60 +"| Total Mast |")
    print("*" * 87)
    total = 0
    for k, v in dict_to_print.items():
        print("|{:55}                 |{:12}|".format(k,v))
        total += v
    print("*" * 87)
    print("Total: ", total)

#Run the user commands
def run_command(command):
    if command.startswith("--help"):
        showhelp = ShowHelp()
        showhelp.show()
    elif command.startswith("--list"):
        mastreader = MastDataReader(path_to_csv)
        top5 = mastreader.sorted_top(5)
        print_list(top5)
    elif command.startswith("--lease25"):
        mastreader = MastDataReader(path_to_csv)
        lease25year = mastreader.list_filtered(lambda x: x[9] == "25")
        print_list(lease25year)

        maststate = MastStat()
        rent_col_index = 10
        total_rent = maststate.aggregate(lease25year, rent_col_index)
        print("*" * 87)
        print("total rent: ", total_rent)       

    elif command.startswith("--stat"):
        mastreader = MastDataReader(path_to_csv)
        all_records = mastreader.get_all()
        
        maststate = MastStat()
        tenant_name_col_index = 6
        stat = maststate.get_tenant_mast_count(all_records, tenant_name_col_index)

        print_dict(stat)
    elif command.startswith("--between"):
        fmt = "%d %b %Y"
        start_date = datetime(1999, 6, 1)
        end_date = datetime(2007, 8, 31)
        
        mastreader = MastDataReader(path_to_csv)
        betweenList = mastreader.list_filtered(lambda x: start_date < datetime.strptime(x[7], fmt) < end_date)
        
        for item in betweenList:
            item[7] = datetime.strptime(item[7], fmt).strftime("%d/%m/%Y")
            item[8] = datetime.strptime(item[8], fmt).strftime("%d/%m/%Y")
        print_list(betweenList)

# Take user inputs and invoke run command
command = input()
run_command(command)
