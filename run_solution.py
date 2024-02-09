import sys
import subprocess
p = subprocess.getoutput("{} ./adventure.py < gameover".format(sys.executable))
print(p)
