import os, ftplib
###############################################################
filepath = '//xxx//share//Scans//Delivery_Forms//'
FTPserver = '10.103.17.10'
User = ''
Pass = ''
################################################################
ftp = ftplib.FTP(FTPserver)
ftp.login(User, Pass)
ftp.cwd('//malam//')
dirs = []
for filename in ftp.nlst():
    try:
        ftp.size(filename)
        new_name = None
        new_name = filename.split('_')[1] + '_LC' + '.' + filename.split('.')[-1]
        ftp.retrbinary('RETR '+ filename, open(os.path.join(filepath, new_name), 'wb').write)
        ftp.delete(filename)
    except:
        pass
ftp.quit()
