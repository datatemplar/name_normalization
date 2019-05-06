## Created the 05/03/19
## By Data Templar
##
## The purpose of this script is to remove all space in all files
## and folders' name. So we can share the "server url" directly

try:

    from tqdm import tqdm

    tqdmimport = True

except ImportError as e:

    tqdmimport = False

    print("enable to import the progress bar value. Please install tqdm if you want a progress bar")

import argparse, sys, re, os, time

 

# Argument creation

parser = argparse.ArgumentParser()

parser.add_argument("--begin", help="The folder you want to make a modification by default its the current folder", default=os.getcwd())

args = parser.parse_args()

 

root_dir = args.begin

print(root_dir)

 

def removeescape(dir,file,log):

    filename = file

    filename = filename.replace(" -","-")

    filename = filename.replace("- ","-")

    filename = filename.replace(" _","_")

    filename = filename.replace("_ ","_")

    filename = filename.replace(" ","_")

    #print("Transformation of %s in %s" % (file,filename))

    try:

        os.rename(os.path.join(dir,file),os.path.join(dir,filename))

    except Exception as e:

        print("The file %s is open and can't be modified" % (file))

        print("The %s is open and can't be modified,%s,%s" % (file,os.path.join(dir,filename),e),file=log)

 

def scanRecurse(dir,log):

    for entry in os.scandir(dir):

        if entry.is_file():

            removeescape(dir,entry.name,log)

        else:

            scanRecurse(entry.path,log)

            removeescape(dir,entry.name,log)

with open(root_dir+"\log.csv",'w',encoding='utf-8') as target:

    scanRecurse(root_dir,target)
