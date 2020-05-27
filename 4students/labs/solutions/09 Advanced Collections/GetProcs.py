import subprocess
tasks = []
def GetFirstProc():
    global tasks
    proc = subprocess.run('ps -e',shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    tasks = proc.stdout.decode().splitlines()
    print(tasks[1])
    pass
def GetNextProc():
    pass

GetFirstProc()