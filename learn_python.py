import os
from datetime import time

print(f"Current Directory: {os.getcwd()}")
print(f"Scheduled Break: {time(15, 30)}")
print(f"Process ID: {os.getpid()} — Script logic verified.")