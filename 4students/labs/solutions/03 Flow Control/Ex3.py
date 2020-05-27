import sys, glob, os

if sys.platform == 'win32':
    dir = os.environ['HOMEPATH']
else:
    dir = os.environ['HOME']

pattern = os.path.join(dir,'*')

for file in glob.iglob(pattern):
    size = os.path.getsize(file)
    if size > 0:
        print(os.path.basename(file),size)
