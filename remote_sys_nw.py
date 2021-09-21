import paramiko
import time
from rich.console import Console
from rich.text import Text
console = Console()

def connect(hostname,port,username,password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("connecting........")
    ssh_client.connect(hostname=hostname,port=port,username=username,password=password)
    # ssh_client.connect(hostname="127.0.0.1",port=22,username="greeshma",password="1234")

def get_mem(ssh_client):
    stdin,stdout,stderr = ssh_client.exec_command("free -m\n")
    console.print(Text("free memory :",style="bold red"))
    console.print(Text(stdout.read().decode(),style="bold blue"))

def get_load_avg(ssh_client):
    stdin,stdout,stderr = ssh_client.exec_command("uptime  | grep -o 'load.*'\n")
    console.print(Text("load average :",style="bold red"))
    console.print(Text(stdout.read().decode(),style="bold blue"))

def get_route_list(ssh_client):
    stdin,stdout,stderr = ssh_client.exec_command("ip route list\n")
    console.print(Text("routing table:",style="bold red"))
    console.print(Text(stdout.read().decode(),style="bold blue"))

def get_uptime(ssh_client):
    stdin,stdout,stderr = ssh_client.exec_command("uptime -s\n")
    console.print(Text("uptime:",style="bold red"))
    console.print(Text(stdout.read().decode(),style="bold blue"))

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
	    print("Disconnecting.........")
	    ssh_client.close()

def menu():
    console.print("1. Free Memory\n2. Load Average\n3. Route List\n4. Uptime\n5. Exit",style="bold blue")


if __name__ == "__main__":
    hostname = input("Enter the Hostname : ")
    port = input("Enter the Port : ")        
    username = input("Enter the Username : ")    
    password = input("Enter the Password : ")

    client = connect(hostname,port,username,password)

    while True:
        menu()
        c = int(input("Enter the choice : "))
        if c==1:
            get_mem(client)
        elif c==2:
            get_load_avg(client)
        elif c==3:
            get_route_list(client)
        elif c==4:
            get_uptime(client)
        elif c==5:
            close(client)
            break
        else:
            console.print("Invalid choice",style="bold blue")
