
#imports
from ftplib import FTP
from genericpath import exists
from shutil import copyfile
import os
from datetime import datetime
#from sys import path

def log(msg: str):
    log = open('ftp.log', 'a')
    log.write('{} - {}\n'.format(datetime.now().strftime('%Y.%m.%d. %H:%M:%S'), msg))
    log.close()



def upload():
    try:
        ftp = FTP(host='ftp.peter68.hu')
        ftp.login(user='kristof@peter68.hu', passwd='Kisfiam')
    except:
        # log.write('{} - {}'.format(datetime.now().strftime('%Y.%m.%d. %H:%M:%S'), 'Failed to connect FTP server!\n'))
        log('Failed to connect FTP server! (upload)')
    try:
        path = 'recept/mentes'
        ftp.cwd(path)
        # print(ftp.pwd())
    except:
        # print('Error at ftp.cwd!')
        log('Error at ftp.cwd! (upload)')
    try:
        if not os.path.exists('tmp'):
            os.mkdir('tmp')
        copyfile('receptek.db', 'tmp/receptek_up.db')
    except:
        # print('Error at making "tmp" directory or copy file')
        log('Error at making "tmp" directory or copy file (upload)')
    try:
        ftp.storbinary('STOR receptek.db', open('tmp/receptek_up.db', 'rb'))
    except:
        # print('Error at copy file to FTP')
        log('Error at copy file to FTP (upload)')

    ftp.quit()

def download():
    try:
        ftp = FTP(host='ftp.peter68.hu')
        ftp.login(user='kristof@peter68.hu', passwd='Kisfiam')
    except:
        log('Error while connecting to FTP server! (download)')
    try:
        path = 'recept/mentes'
        ftp.cwd(path)
    except:
        log('Error while changing dir (download)')
    try:
        if not os.path.exists('tmp'):
            os.mkdir('tmp')
    except:
        log('Error while creating "tmp" dir (download)')
    try:
        # localfile = open('tmp/receptek_down.db', 'wb')
        ftp.retrbinary('RETR receptek.db', open('tmp/receptek_down.db', 'wb').write)
    except:
        log('Error while downloading db (download)')
    try:
        copyfile('tmp/receptek_down.db', 'receptek_uj.db')
    except:
        log('Error whilne copying file')

# upload()
# download()