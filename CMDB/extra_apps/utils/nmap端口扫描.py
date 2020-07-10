import nmap

# nm = nmap.PortScanner()
# result = nm.scan(hosts='172.25.254.0/24', arguments='-n -sP')
#
# print("扫描结果: ", result)
#
# # 返回的扫描具体的nmap命令行
# print("nmap命令行: ", nm.command_line())
#
# # 返回nmap扫描的主机清单,格式为列表类型
# print("主机清单: ", nm.all_hosts())

def get_active_hosts(hosts='127.0.0.1', ports='22,80'):
    nm = nmap.PortScanner()
    result = nm.scan(hosts=hosts, ports=ports, arguments='-n')

    return nm.all_hosts()
    # print("扫描结果: ", result)

    # # 返回的扫描具体的nmap命令行
    # print("nmap命令行: ", nm.command_line())
    #
    # # 返回nmap扫描的主机清单,格式为列表类型
    # print("主机清单: ", nm.all_hosts())
if __name__ == '__main__':
    active_hosts = get_active_hosts()
    print("所有存活的主机： ", active_hosts)