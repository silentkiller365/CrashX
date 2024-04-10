import os
from termcolor import colored
import time

def check_credentials():
    username = input("Username: ");
    
    password = input("Password: ")

    if username == "Admin" and password == "@H3X4R":
        print(colored("Authentication successful!", "green"))
        time.sleep(3)  # Wait for 3 seconds
        os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal
        return True
    else:
        print(colored("Invalid credentials. Access denied.", "red"))
        return False

def print_banner():
    print(colored("----------------------------------------", "cyan"))
    print(colored("Welcome to the CrashX Control Panel!", "yellow"))
    print(colored("----------------------------------------", "cyan"))

def get_crashx_parameters():
    url = input(colored("Enter Target URL: ", "magenta"))
    threads = input(colored("Enter Number of Threads: ", "magenta"))
    method = input(colored("Enter Method (GET/POST): ", "magenta"))
    
    if method.lower() not in ["get", "post"]:
        print(colored("Invalid method. Please enter GET or POST.", "red"))
        return None, None, None, None
    
    duration = input(colored("Enter Duration (seconds): ", "magenta"))
    return url, threads, method, duration

def run_crashx(url, threads, method, duration):
    command = f"./CrashX {url} {threads} {method} {duration} header.txt"
    os.system(command)

if __name__ == "__main__":
    if check_credentials():
        print_banner()
        url, threads, method, duration = get_crashx_parameters()
        if url and threads and method and duration:
            run_crashx(url, threads, method, duration)
