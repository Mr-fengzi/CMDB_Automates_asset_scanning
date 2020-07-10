import pexpect

# (command_output, exitstatus) = pexpect.run('hostname', withexitstatus=1)
# command_output = command_output.decode('utf-8')
# if exitstatus == 0:
#     print("命令执行成功： ", command_output)
# else:
#     print("命令执行失败： ", command_output)

# command = 'ssh -p22 root@39.106.145.114'
# child = pexpect.spawn(command, timeout=2)
# status_code = child.expect(['continue connecting (yes/no)?', 'password:'])
# if status_code == 0:
#     child.sendline('yes')
#     child.expect(['password:'])
#     child.sendline('ygf1995918.')
# elif status_code == 1:
#     child.sendline('ygf1995918.')
#
# match_index = child.expect(['#', '$', pexpect.EOF, pexpect.TIMEOUT])
# if match_index == 0:
#     print('登录超级用户成功')
# elif match_index == 1:
#     print("普通用户登录失败")
# elif match_index == 2:
#     print("登录失败：logout")
# elif match_index == 3:
#     print("登录失败：超时")

def login_ssh_password(user, host, password, port=22):
    command = 'ssh -p%s %s@%s' %(port, user, host)
    child = pexpect.spawn(command, timeout=2)
    status_code = child.expect(['continue connecting (yes/no)?', 'password:'])
    if status_code == 0:
        child.sendline('yes')
        child.expect(['password:'])
        child.sendline(password)
    elif status_code == 1:
        child.sendline(password)

    match_index = child.expect(['#', '$', pexpect.EOF, pexpect.TIMEOUT])
    if match_index == 0:
        print('登录超级用户成功')
    elif match_index == 1:
        print("普通用户登录失败")
    elif match_index == 2:
        print("登录失败：logout")
    elif match_index == 3:
        print("登录失败：超时")