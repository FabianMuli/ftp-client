import ftplib
from ftplib import FTP

# connecting to the server
try:
    ftp = FTP("ftp.fabdesignskenya.co.ke")

    ftp.login(user="fabdesig", passwd="d0ZoAm797a")
    print(ftp.getwelcome())  # welcome messages

    wdir = ftp.pwd()
    print(wdir)

    ftp.cwd("public_html")
    files = []
    ftp.dir(files.append)
    for file in files:
        print(file)  # print the files in the working directory

    if_upload = input("Do you want to download a file? (y/N) : ")
    if if_upload == 'y':
        file_copy = input("Enter file to download -> ")

        def getFile(ftp, file_copy):
            try:
                ftp.retrbinary("RETR " + file_copy, open(file_copy, 'wb').write)
            except ftplib.all_errors as e:
                print(e)

        getFile(ftp, file_copy)
except ftplib.all_errors as e:
    print('FTP error:', e)
