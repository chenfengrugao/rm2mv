#!/usr/bin/env python3

#
# Revision :
#   1.0 Initial
#   1.1 fix bugs
#   1.2 fix bugs
#   1.3 21/5/2013 add help options
#   1.4 23/5/2013 move the deleted files to ~/.Trash/datatime folder 
#                   to avoid the files with the same name
#   1.5 29/5/2013 do not move when $MyFileList is empty
#   1.6 2/9/2013  change 'unix rm' to 'linux rm', and add a bug notes
#   1.7 16/9/2013 change default to silence mode
#                 move to trash only when the files exist.
#   1.8 9/8/2019  implement with python

import os
import sys
import shutil
import getpass
import re
import time
import datetime

Ver = "1.8"
LastUpd = "Aug. 9, 2019"
Author = "BillC"

MyFileList = []
MyIgnoreList = []
NotGotoTrash = 0 #whether moved to Trash
HelpFlag = 0

# get current login user name
user = getpass.getuser()

date_time_dir = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
#print(date_time_dir)

# handle options
for arg in sys.argv[1:]:
    if arg == '-h' or arg == '-help' or arg == '--help':
        print("rm2mv v" + Ver)
        print("a script to replace system rm, moves dirs or files to ~/.Trash instead of deleting them directly.")
        print("e.g. rm2mv xx.v            delete a file")
        print("     rm2mv -rf rtl         delete a directory")
        print("     rm2mv --force simv*   delete file or dir not going to ~/.Trash")
        print("     rm2mv --clean         clean files 1 week before from ~/.Trash")
        sys.exit()
    elif arg == '--version':
        print('rm2mv v' + Ver)
        sys.exit()
        
    # delete with --force
    elif arg == '--force':
        print('/bin/rm -rf ' + ' '.join(sys.argv[1:]))

    # delete files in .Trash
    elif re.search(r'/\.Trash/', arg):
        print('/bin/rm -rf ' + ' '.join(sys.argv[1:]))

    # clean .Trash
    elif arg == '--clean':
        dirs = os.listdir('/home/{}/.Trash'.format(user))
        for dt in dirs:
            if((datetime.datetime.now() - datetime.datetime(int(dt[0:4]), int(dt[4:6]), int(dt[6:8]))).days > 7):
                shutil.rmtree(dt)
        sys.exit()

    # save filelist to list
    elif not arg.startswith('-'):
        # protect /xxx and /home/xxx
        if arg == '/' or \
           arg == '~' or \
           re.match(r'/home/\w+/?$', arg) or \
           re.match(r'/\w+/?$', arg):
            print("[Warning] deleting dangerous files: " + arg)
            sys.exit()
        else:
            if os.path.exists(arg):
                MyFileList.append(arg)
            else:
                MyIgnoreList.append(arg)
    else:
        MyIgnoreList.append(arg)

if len(MyFileList) != 0:
    target = '/home/{}/.Trash/{}'.format(user, date_time_dir)
    if not os.path.exists(target):
        os.makedirs(target)
    os.system('mv {} {}/'.format(' '.join(MyFileList), target))
