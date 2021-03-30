import os

def menushka():
    print("""Choose option:
    Press 1 to work with files;
    Press 2 to work with directories;
    Press 0 to exit""")

def fileMenushka():
    print("""Choose option:
    1. Delete file
    2. Rename file
    3. Add content""")


def dirsMenushka():
    print("""Choose option:
    1. Rename file
    2. Print number of files""")

print("             Welcome to file manager!")



while True:
    menushka()
    curPath = os.getcwd()
    location = int(input())
    
    if location == 1:
        # files
        fileMenushka()
        n = int(input()) 

        if n == 1:
            #delete file
            fileName = input("Enter the name of the file you want to delete: ")
            if os.path.exists(fileName + '.txt'):
                os.remove(curPath + '/' + fileName + '.txt')
                print("File removed!")
            else:
                print("Error!")
        #os.chdir("..")
        elif n == 2:
            #rename
            fileName = input("Enter the name of the file you want to rename: ")
            if os.path.exists(fileName + '.txt'):
                print("Enter new name of the file: ")
                newName = input()
                os.rename(fileName + '.txt', newName + '.txt')
                print("File renamed!")
            else:
                print("Error!")
        elif n == 3:
            #add content
            fileName = input("Enter the name of the file you want to add content: ")
            if os.path.exists(fileName + '.txt'):
                print("Enter new content: ")
                newContent = input()
                curFile = open(fileName + '.txt', 'a')
                curFile.write(newContent)
                curFile.close()
                print("Content added!")
            else:
                print("Error!")

    elif location == 2:
        #dir-s
        dirsMenushka()
        curDir = os.getcwd()
        print(curDir)
        n = int(input())
        if n == 1:
            #rename
            dirRename = input("Enter the name of the directory you want to rename: ")
            if os.path.exists(dirRename):
                newName = input("Enter the new name:")
                os.rename(dirRename, newName)
                print("Renamed!")
            else:
                print("Error!")
        elif n == 2:
            #print number of files
            dirCount = input("Enter the name of directory to print the number of files: ")
            if os.path.exists(dirCount):
                dirList = os.listdir(dirCount)
                numOfFiles = len([1 for i in list(os.scandir(dirCount)) if i.is_file])
                print("In this directory " + str(numOfFiles) + " files.")
            else:
                print("Error!")
    elif location == 0:
        #exit
        print("Ok. Bye!")
        exit()