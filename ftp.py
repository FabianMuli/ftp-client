import ftplib
from ftplib import FTP
import os

# connecting to the server
try:
    ftp = FTP("ftp.fabdesignskenya.co.ke")

    ftp.login(user="fabdesig", passwd="d0ZoAm797a")
    print(ftp.getwelcome())  # welcome messages

    wdir = ftp.pwd()
    print(wdir)

    cwd = input("Enter the directory you want to work in -> ")
    ftp.cwd(cwd)
    files = []
    ftp.dir(files.append)
    for file in files:
        print(file)  # print the files in the working directory

    if_upload = input("Do you want to download a file? (y/N) : ")
    if if_upload == 'y':
        file_copy = input("Enter file to download -> ")

    def changeDir():
        os.chdir(cwd[12:])
        print("Changed directory to ", cwd[12:], " ...")
        ftp.retrbinary("RETR " + file_copy, open(file_copy, 'wb').write)

    def getFile(ftp, file_copy):
        try:
            if len(cwd) > 11:
                if not os.path.exists(cwd[12:]):
                    os.makedirs(cwd[12:])
                    print("Created directory ", cwd[12:], " ...")
                    changeDir()
                else:
                    print("Path already exists.")
                    changeDir()
        except ftplib.all_errors as e:
            print(e)

    getFile(ftp, file_copy)
except ftplib.all_errors as e:
    print('FTP error:', e)
