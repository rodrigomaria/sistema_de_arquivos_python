#importações de módulos
import os

#retorna %HOMEPATH%/data
home = os.curdir
if 'HOME' in os.environ:
    home = os.environ['HOME']
elif os.name == 'posix':
    home = os.path.expanduser("~/")
elif os.name == 'nt':
    if 'HOMEPATH' in os.environ and 'HOMEDRIVE' in os.environ:
        home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
else:
    home = os.environ['HOMEPATH']
data = os.path.join(home, "data")

#retorna in e out
in_folder = os.path.join(data, "in")
out_folder = os.path.join(data, "out")