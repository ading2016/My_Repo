#!/usr/bin/env python
import paramiko
hostname='192.168.133.129'
username='root'
password='ading'
port=36251

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,port=port,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('ls /')
print stdout.read()
ssh.close()
