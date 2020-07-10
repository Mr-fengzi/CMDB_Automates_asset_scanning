import paramiko

# 实例化SSH客户端对象
# with paramiko.SSHClient() as client:
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(hostname='39.106.145.114',
#                    port=22,
#                    username='root',
#                    password='ygf1995918.')
#
#     stdin, stdout, stderr = client.exec_command('hostname')
#     print(stdout.read().decode('utf-8'))

def login_ssh_passwd(host, port, user, password, command):
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host,
                       port=port,
                       username=user,
                       password=password)

        stdin, stdout, stderr = client.exec_command(command)
        # print(stdout.read().decode('utf-8'))
        return stdout.read().decode('utf-8')

def login_ssh_key(host, port, user, password, command):
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host,
                       port=port,
                       username=user,
                       password=password)

        stdin, stdout, stderr = client.exec_command(command)
        # print(stdout.read().decode('utf-8'))
        return stdout.read().decode('utf-8')

if __name__ == '__main__':
    result = login_ssh_passwd('39.106.145.114', 22, 'root', 'ygf1995918.', 'hostnamectl')
    print(result)