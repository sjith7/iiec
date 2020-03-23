import os
from datetime import datetime

SCREEN_WIDTH = os.get_terminal_size().columns
HALF_SCREEN_WIDTH = int(SCREEN_WIDTH/2)

def printDash(character):
   charList = [character for num in range(SCREEN_WIDTH)]
   print(*charList,sep="",end="\n\n")

"""   
 Original syntax :  [variable/function for x in range(num)]
 working         :  in charList list, "X" number of characters are stored, where "X" = num
"""


#----------------------Screen 1----------------------------

os.system('reset')
os.system('tput setaf 3')
printDash("_")

os.system('tput setaf 9')
print("Indian Innovation & Entrepreneurship Community RISE".center(SCREEN_WIDTH))

os.system('tput setaf 3')
printDash("_")
print("Thanks to Vimal sir and Preeti ma'am".center(HALF_SCREEN_WIDTH),end="")
print("#MakingIndiaFutureReady".center(HALF_SCREEN_WIDTH))
printDash("-")

print("Welcome user please provide your name".center(HALF_SCREEN_WIDTH),end="")
print(str(datetime.now()).center(HALF_SCREEN_WIDTH))

printDash("-")
name = input("Please Enter your name : ".rjust(HALF_SCREEN_WIDTH))
os.system('reset')

#--------------------------------------------------------


#------------------Screen 2------------------------------

os.system('tput setaf 2')
printDash("_")
os.system('tput setaf 9')
print("Indian Innovation & Entrepreneurship Community RISE".center(SCREEN_WIDTH))
os.system('tput setaf 2')
printDash("_")

print(("Welcome "+name).center(HALF_SCREEN_WIDTH), end="")
print(str(datetime.now()).center(HALF_SCREEN_WIDTH))
printDash("_")

os.system('tput setaf 11')
print('Just one click and all your configuration will be done automatic'.center(SCREEN_WIDTH))
os.system('tput setaf 3')
printDash("-")
print('\n\t\t\t\t1. Yum configuration \n\n\t\t\t\t2. httpd configuration')
choice = int(input("\t\t\tEnter your choice please : "))

#------------------------------------------------------


if choice == 1 :
    os.system('reset')
    os.system('tput setaf 2')
    print("\t____________________________________________________________________________________________________\n")
    print("\n\tcurrent working directory : " ,end="")
    print(os.getcwd()) # It will print current directory
    print("\n\tChanging to : " , end ="")
    os.chdir('/etc/yum.repos.d') #It will change the directory
    print( os.getcwd()+"\n")
    for filenames,dirpath,dirnames in os.walk('.') :
        print("\tAll the Directoris : ", dirpath)
        print("\t----------------------------------------------------- ^")
        print("\n")
        print("\tAll files : ", dirnames)
        print("\t----------------------------------------------------- ^")
        print("\n")
        print("\tcurrent file Path : ", filenames)
        print("\t----------------------------------------------------- ^")
    os.system('tput setaf 9')
    print("________________________________________________________________________________________________\n")
    os.system('tput setaf 7')
    filename = input("\tGive your repo name but don't include '.repo' extension(e.g. docker or myyum) : ")
    properFilename = filename+".repo"
    os.system('tput setaf 12')
    print("\t" + properFilename +"\n\tLet me check if file already exist")

    if os.path.isfile(properFilename) :
        print("\tfile is already created")
        fileOpen = open(properFilename)
        readContent = fileOpen.read()
        print(readContent)
        fileOpen.close()
        print()
        print("\tfirst remove that file and try again")
        removeRepo = input("\tDo you want to remove the repo Y|N : ")

        if(removeRepo == 'Y') :
            os.remove(properFilename)
            print("\tfile removed successfully. Relauch the program")
        else :
            os.system('dnf update')
    else :
        fileOpenuser = open(properFilename,"+w")
        fileOpenuser.write('[repo1]\n baseurl = https://cdn.redhat.com/content/dist/rhel8/$releasever/x86_64/baseos/os\n gpgcheck = 0 \n\n [repo2]\n baseurl = https://cdn.redhat.com/content/dist/rhel8/$releasever/x86_64/appstream/os\n gpgcheck = 0')
        fileOpenuser.close()
        os.system('dnf update')
        print('\tsuccessfully configured')
        os.system('reset')







if choice == 2 :
    print("\tCurrent directory is",os.getcwd())
    os.chdir("/etc/httpd/conf.d")
    if (os.path.isdir("/etc/httpd/conf.d")== True) :
        httpdFilename = input("\tIn which name you want to make httpd config file : ")
        httpdFilenameProper = httpdFilename + ".conf"
        print(httpdFilenameProper)
        print("\tWhat you want to add in that file")
        print("\t1. Adding another port")
        print("\t2. Adding someother document root")
        choice2 = int(input("Enter you choice here : "))
        if(choice2 == 1) :
            print("By default we had choose good port for you 8080")
            httpdFileopen = open(httpdFilenameProper, "+w")
            httpdFileopen.write("Listen 8080")
            httpdFileopen.close()
            os.system('systemctl restart httpd')
        if(choice2 == 2) :
            print("give proper path for document root")
            httpdPath = input()
            httpdPathProper = "DocumentRoot ",httpdPath
            httpdFileopen = open(httpdFilenameProper, "+w")
            httpdFileopen.write(str(httpdPathProper))
            httpdFileopen.close()
            os.system('ls /etc/httpd/conf.d')
    else :
        print("Directory is not found which means httpd service is not installed")
        os.system('dnf install httpd')
        print("service install successfully")



