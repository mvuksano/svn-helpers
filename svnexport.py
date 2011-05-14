import os
import sys
import subprocess

# the directories that we want to scan
dirs = sys.argv[1]
export_dir = sys.argv[2]
if not dirs:
    cur_dir = os.path.abspath(os.curdir)
    print ("Using the current directory (%s) since none have been specified." % cur_dir)
    dirs = [cur_dir]
# we will walk each dir structure looking for working copies
to_up = []
ta = to_up.append
print(dirs)
print(export_dir)
for directory in dirs:
    directory = os.path.expanduser(directory)
    # TODO os.walk doesn't follow symlinks...
    for current_dir, directories, files in os.walk(directory):
        if '.svn' in directories:
            ta(current_dir)
            # delete the subdirs to stop recursion
            del directories[:]
number_of_updates = len(to_up)
print ("Exporting %s projects...\n" % number_of_updates)
scall = subprocess.call
# loop through all the paths and svn export them
for upper in to_up:
    print ("\n%s" % upper)
    scall(('svn export %s %s' % (upper, export_dir + upper)).split())
# what just happened? oh...
print ("""
*******
summary
*******

The following %s items have been exported:

""" % number_of_updates)
for upper in to_up:
    print (upper)
print