from telnetlib import Telnet
import paramiko
import subprocess
from os import listdir
from os.path import isfile, join
import os


def telnet_to_the_server(host, port=22):
    with Telnet(host, port) as tn:
        tn.interact()

def ssh_to_server(host, username, password):
    ssh = paramiko.SSHClient()
    ssh.connect(host, username=username, password=password)

def check_disk_usage():
    threshold = 10
    child = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    output = child.communicate()[0].strip().split("\n")
    for x in output[1:]:
        if int(x.split()[-2][:-1]) >= threshold:
            print x

def list_from_dir(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(onlyfiles)

def copy_to_server(localpath, remotepath, server, username, password):
    ssh = paramiko.SSHClient() 
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(server, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath)
    sftp.close()
    ssh.close()

def restart_apache_when_high_load():
    for I in [0, 1, 2, 3, 4, 5]:
        check=$(uptime | tr -d ',.' | awk '{print $10}')
        if [ "$check" -gt 5 ]:
            subprocess.Popen('/usr/bin/systemctl restart httpd.service')        
        sleep(10)
