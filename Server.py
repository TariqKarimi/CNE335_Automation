import server

def print_program_info():
    print("Server Automator v0.1 by Tariq")

#This is the entry point
if __name__ == ' __main__':
    print_program_info()

    server = Server.Server("35.155.213.121")

    print(server.print())
