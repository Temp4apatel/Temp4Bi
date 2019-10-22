from show_help import ShowHelp

def run_command(command):
    if command.startswith("--help"):
        showhelp = ShowHelp()
        showhelp.show()
    elif command.startswith("--list"):
        pass
    elif command == "--exit":
        pass

command = input()
run_command(command)
