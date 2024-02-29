import os
import time
import os.path
import subprocess
import _thread


#_thread.start_new_thread(os.system,(f'"{os.path.dirname(__file__)}\\test.bat"',))

t = 0
while True:
    time.sleep(5)
    print(t)
    t += 1