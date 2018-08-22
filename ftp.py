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

    files = []
    ftp.dir(files.append)
    for file in files:
        print(file)  # print the files in the working directory

    file_copy = "robots"
    file_orig = "/public_html/"
    with open(file_copy, 'w') as fp:

            res = ftp.retrlines('RETR ' + file_orig, fp.write)

            if not res.startswith('226 Transfer complete'):
                print('Download failed')
                if os.path.isfile(file_copy):
                    os.remove(file_copy)
except ftplib.all_errors as e:
    print('FTP error:', e)

    if os.path.isfile(file_copy):
            os.remove(file_copy)
