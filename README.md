# CNE335_Automation
# This is the template code for the CNA337 Final Project

#FNU Tariq, ftariq@student.rtc.edu
#CNA 335

import server


def print(param):
    pass


def print_program_info():
    
    print("Server Automator v0.1 by Tariq")

#This is the entry point
class Server:
    pass


if __name__ == ' __main__':
    print_program_info()

    server = Server.Server("35.155.213.121")

    print(server.print())

    server.ssh_and_update()
