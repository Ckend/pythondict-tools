import subprocess


def decode_result(system, result):
    """
    解码密码

    Arguments:
        system {str} -- [系统类型]
        result {str} -- [输出]

    Returns:
        [str] -- [解码后的密码]

    Author: Python 实用宝典
    """

    if system == "windows":
        # cmd命令得到的结果是bytes型，需要decode
        result = result.decode("gb2312")
    result = result.strip('\r|\n')
    if result != "":
        result = result.replace(" ", "")
        result = result[result.find(":") + 1:]
    result = result[result.find("=") + 1:]
    return result


def fetch_result(system, command):
    """
    用于执行命令获取结果

    Arguments:
        system {str} -- 系统类型
        command {str} -- 命令

    Returns:
        str -- 解码后的密码

    Author: Python 实用宝典
    """
    result, _ = subprocess.Popen(
        command, stdout=subprocess.PIPE, shell=True
    ).communicate()
    return decode_result(system, result)


def fetch_password(system, wifi_name):
    """
    用于获取命令

    Arguments:
        system {str} -- 系统类型
        wifi_name {str} -- wifi名

    Returns:
        str -- 密码

    Author: Python 实用宝典
    """

    if system == "linux":
        command = f"sudo cat /etc/NetworkManager/" \
                  f"system-connections/{wifi_name}| grep psk="
    elif system == "macos":
        command = f"sudo security find-generic-password" \
                  f" -l{wifi_name} -D 'AirPort network password' -w"
    elif system == "windows":
        command = f"netsh wlan show profile name={wifi_name} " \
                  f"key=clear | findstr 关键内容"
    result = fetch_result(system, command)
    return result


print(fetch_password('windows', 'Ckend'))