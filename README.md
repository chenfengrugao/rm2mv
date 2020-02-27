
# Description

A script to replace system rm, moves dirs or files to ~/.Trash instead of deleting them directly.

e.g.

```shell
rm2mv xx.v            delete a file
rm2mv -rf rtl         delete a directory
rm2mv --force simv*   delete file or dir not going to ~/.Trash
rm2mv --clean         clean files 1 week before from ~/.Trash
rm2mv --status        check the size of ~/.Trash
```

# Installation

First, make sure you have installed python3, and then check you have the follow modules:

``` python
import os
import sys
import shutil
import getpass
import re
import time
import datetime
```

Second, install rm2mv:

```shell
#cshell
mkdir ~/bin
cd ~/bin
git clone https://github.com/chenfengrugao/rm2mv
ln -s rm2mv/rm2mv.py rm
chmod +x rm
setenv ~/bin:$PATH
```




