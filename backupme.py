import shutil
import distutils.file_util
import os

#pathSrc ="/home/qainfotech/Downloads"
#pathDest ="/home/qainfotech/DownloadsBackup"

pathSrc ="/home/qainfotech/Desktop"
pathDest ="/home/qainfotech/DesktopBackUp"

#pathSrc ="/home/qainfotech/Downloads/amazon apk"
#pathDest ="/home/qainfotech/Downloads/amazon_apk_backup"

# function to remove entire dir tree.
# Once all data is backed up, lets delete the source dir

#warning=input ("This action will back up content of "+ pathSrc)+ " to "+pathDest 
print ()

def remove(path):
 
    print ('inside remove method')
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else :
        raise ValueError("Some error occured")
    return;

try:
    global someFileNotCopied
    someFileNotCopied=0
    shutil.copytree(pathSrc,pathDest, ignore=shutil.ignore_patterns('*.exe'))

    # distutils.file_util.move_file('/home/qainfotech/p1/ic_launcher.png', '/home/qainfotech/p2'
    # Directories are the same

except shutil.Error as e:
	print('Directory not copied. Error: %s' % e)
	someFileNotCopied=1

# Any error saying that the directory doesn't exist
except OSError as e:
	print('Directory not copied. Error: %s' % e)
	someFileNotCopied=1

if someFileNotCopied==0:
    remove(pathSrc)

#remove method removes the entire dir and dir tree
#so we will need to re create source dir once bacvk up and removal work is done
if not os.path.exists(pathSrc):
    os.makedirs(pathSrc)



