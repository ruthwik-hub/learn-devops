import os
import platform

def check_ping(hostname):
    # Determine the operating system to use the correct ping flag
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    print(f"Checking connection to {hostname}...")
    response = os.system(f"ping {param} 1 {hostname} > nul 2>&1")

    if response == 0:
        return f"SUCCESS: {hostname} is reachable."
    else:
        return f"FAILURE: {hostname} is down or unreachable."

if __name__ == "__main__":
    # Test with a common DNS server
    target = "8.8.8.8" 
    result = check_ping(target)
    print(result)
    
    print("\nScript execution finished.")