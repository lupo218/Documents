import paramiko
from stat import S_ISDIR, S_ISREG

sftpURL = 'xxx.xxx.co.il'
sftpUser = 'xxx@xxx.com'
sftpPass = 'xxx'
Dir = '/From AIG/'
Dst = '\\\\smlt-fs\\IT\\SapDocs\\QLIK\\AIG\\'
Dstbackup = '/From AIG/Archive/OLD/'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # add cer
ssh.connect(sftpURL, username = sftpUser, password = sftpPass)
ftp = ssh.open_sftp()

for entry in ftp.listdir_attr(Dir): # check file/dir
    mode = entry.st_mode
    if S_ISDIR(mode):
       print(entry.filename + " is folder")
    elif S_ISREG(mode): # check is a file
        print(entry.filename)
        ftp.get(Dir + entry.filename, Dst + str(entry.filename)) # copy file
        ftp.remove(Dir + entry.filename) # del file

ftp.close()
ssh.close()