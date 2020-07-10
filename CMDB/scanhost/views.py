import re
import telnetlib

import nmap
import paramiko
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from CMDB.settings import base
from scanhost.models import Server


def get_active_hosts(hosts='39.106.145.114', ports='22,80'):
    nm = nmap.PortScanner()
    result = nm.scan(hosts=hosts, ports=ports, arguments='-n')

    return nm.all_hosts()

def is_ssh_up(host='39.106.145.114', port=22, timeout=5):
    tn = telnetlib.Telnet(host=host, port=port)
    # read_until读取直到遇到了换行符或超时秒数。默认返回bytes类型,通过decode方法解码为字符串。
    tn_result = tn.read_until(b"\n", timeout=timeout).decode('utf-8')

    searchObj = re.search('ssh', tn_result, flags=re.I)
    if searchObj:
        return True
    else:
        return False

def login_ssh_key(host, port, user, keyfile, command):
    with paramiko.SSHClient() as client:
        private = paramiko.RSAKey.from_private_key_file(keyfile)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host,
                       port=port,
                       username=user,
                       pkey=private
                       )

        stdin, stdout, stderr = client.exec_command(command)
        # print(stdout.read().decode('utf-8'))
        return stdout.read().decode('utf-8')

def scanhost(request):
   # 访问所有要扫描的网段/IP
   for host in base.scanhosts:
       print("正在扫描%s......" %(host))
       # 获取所有可以ping通的主机IP
       active_hosts = get_active_hosts(hosts=host)
       # 依次遍历判断ssh服务是否开启
       for active_host in active_hosts:
           if is_ssh_up(active_host):
               server = Server()
               # 设置IP地址
               server.IP = active_host
               # 执行指令
               for attr, command in base.commands.items():
                   # attr ='hostname' , command = 'hostname'
                   # 存储主机名、操作系统.....指令执行的结果
                   result = login_ssh_key(active_host, 22, 'root','/mnt/id_rsa', command)
                   setattr(server, attr, result)
               server.save()
       return  HttpResponse('扫描成功')