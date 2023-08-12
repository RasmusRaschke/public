#RasmusRaschke, 13/08/23, zur freien Verwendung
import os

path = "init"
print("Welcome to my sweep-separator!")

while True:
    sweepfile = input("Please enter the complete path to the sweep file (i.e. ~/foo/bar/sweep.asc):")
    try:
        with open(sweepfile, 'r') as f:
            sweeps = f.read().split("\n\n")
            break
    except:
        print("The input is not valid, please try again.")

while True:
    path = input(
        "Please enter the complete path and name of the directory you want to create for the sweep files to be "
        "stored in (i.e. ~/foo/bar/sweeps):")
    if not os.path.exists(path):
        os.makedirs(path)
        break
    else:
        print("This directory already exists, please try again.")

for i in range(len(sweeps)):
    f = open(path + "/sweep_{}.txt".format(i+1), 'x')
    f.write(sweeps[i])
    f.close()
print("Finished!")
