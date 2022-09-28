from pathlib import Path
import arrow,os,ftplib
###############################################################
filepath = '\\\\xx\\xx\\Services'
FTPserver = '192.168.42.10'
FTPDir = 'PrimeLease'
User = ''
Pass = ''
daystocut = -1
################################################################

filetime = arrow.now().shift(days= daystocut)

def filetocopy(filepath, daystocut, FTPserver, User, Pass, FTPDir):
    filetime = arrow.now().shift(days=daystocut)
    for _ in Path(filepath).glob('*'):
        if _.is_file():
            if arrow.get(_.stat().st_atime) > filetime:
                upload(_, FTPserver, User, Pass, FTPDir)

def upload(file,FTPserver,User,Pass,FTPDir):
    class FTP_TLS_IgnoreHost(ftplib.FTP_TLS):
        def makepasv(self):
            _, port = super().makepasv()
            return self.host, port

    ftp = FTP_TLS_IgnoreHost(FTPserver,User,Pass)
    #ftp.set_debuglevel(1)
    ftp.cwd(FTPDir)
    with open(str(file), 'rb') as f:
        ftp.storbinary('STOR ' + file.name , f)
    ftp.quit()

filetocopy(filepath,daystocut,FTPserver,User,Pass,FTPDir)
