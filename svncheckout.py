import os
import sys
import subprocess

# the directories that we want to scan
repo = sys.argv[1]
repo_url = sys.argv[2]

if not repo or not repo_url:
    print ("Enter repository and url to checkout.")
    
print (os.curdir + '/' + repo)
projects_list = open(os.curdir + '/' + repo, 'r')
for project in projects_list:
    print(repo_url + '/' + project)
    subprocess.call('svn checkout %s' % repo_url + '/' + project.strip())
