
# Description

A script to replace system rm, moves dirs or files to ~/.Trash instead of deleting them directly.

e.g. rm2mv xx.v            delete a file  
     rm2mv -rf rtl         delete a directory  
     rm2mv --force simv*   delete file or dir not going to ~/.Trash  
     rm2mv --clean         clean files 1 week before from ~/.Trash  


# Usage

```
mkdir ~/bin
cd ~/bin
git clone https://github.com/chenfengrugao/rm2mv
ln -s rm2mv/rm2mv.py rm
setenv ~/bin:$PATH
```



