import os,sys
os.system("git pull")
try:
    __import__("FILE").main_menu()
except Exception as e:
    exit(str(e))
