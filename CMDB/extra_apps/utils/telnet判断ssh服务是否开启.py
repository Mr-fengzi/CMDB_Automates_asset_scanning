import telnetlib
import re
# 实例化对象
# tn = telnetlib.Telnet(host='172.25.254.80', port=22, timeout=5)
# # read_until读取直到遇到了换行符或超时秒数。默认返回bytes类型,通过decode方法解码为字符串。
# tn_result = tn.read_until(b"\n", timeout=5).decode('utf-8')
#
# searchObj = re.search('ssh', tn_result, flags=re.I)
# if searchObj:
#     print("ssh服务是开启的，且是linux操作系统。")
# else:
#     print("ssh服务未开启或者不是linux系统。")

def is_ssh_up(host='127.0.0.1', port=22, timeout=5):
    tn = telnetlib.Telnet(host=host, port=port)
    # read_until读取直到遇到了换行符或超时秒数。默认返回bytes类型,通过decode方法解码为字符串。
    tn_result = tn.read_until(b"\n", timeout=timeout).decode('utf-8')

    searchObj = re.search('ssh', tn_result, flags=re.I)
    if searchObj:
        return True
    else:
        return False

if __name__ == '__main__':
    result = is_ssh_up()
    print(result)
