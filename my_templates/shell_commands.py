
# Best way since subprocess doesn't even use 
# the shell and has less overhead as a result.
import subprocess

subprocess.call(['ls', '-l'])
output = subprocess.Popen('ls -l', 
                          shell=True, 
                          stdout=subprocess.PIPE
                          ).stdout.read()
print output

# Probably the worst way for several reasons. (Manually escaping spaces etc..)
# However, this makes piping very easy.
import os
os.system('ls -l')

