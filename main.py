def run_command(command):
    if command.startswith("--help"):
        pass
    elif command.startswith("--list"):
        pass
    elif command == "--exit":
        pass

command = input()
run_command(command)
