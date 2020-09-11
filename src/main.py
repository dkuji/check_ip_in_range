#!/usr/bin/env python


def check_ip_in_range(ip_list, ip_in_range_list):
    """
    ipアドレスがレンジの中にあればIPとそのレンジを、なければIPだけを返す
    Args:
      ip_list(list)
      ip_in_range_list(list)


    Returns:
      res(dict): {"status": bool, "error": ""}

    stdout:
      ip,start,end
      ip
    """

    res = {"status": True, "error": ""}

    try:
        for ip in ip_list:
            for ip_in_range in ip_in_range_list:
                if ip[0] in ip_in_range:
                    print("{},{},{}".format(ip[0],
                                            ip_in_range[0], ip_in_range[-1]))
                    break
            else:
                print(ip[0])
        return res
    except Exception as e:
        res["status"] = False
        res["error"] = e
        return res


def get_ip_in_range(range_list):
    """"
    IPレンジのリストからレンジ内のIPアドレスを返す

    Args:
      range_list(list)

    Returns:
      list [['192.168.0.1', '192.168.0.2', ......], ['192.168.1.1', '192.168.1.2', ......]]
    """
    import ipaddress

    result_ip_list = []
    for range in range_list:
        ip_in_range = []
        startip = ipaddress.IPv4Address(range[0])
        endip = ipaddress.IPv4Address(range[1])
        summary = ipaddress.summarize_address_range(startip, endip)
        for networks in summary:
            for network in networks:
                ip_in_range.append(str(network))
        result_ip_list.append(ip_in_range)
    return result_ip_list


def load_csv(file):
    """"
    csvを読み込んでリストで返す

    Args:
      file(str): CSVファイル

    Returns:
      list [['192.168.0.1', '192.168.0.254'], ['192.168.1.1', '192.168.1.254']]
    """
    import csv

    with open(file, 'r') as f:
        reader = csv.reader(f)
        result = []
        for i in reader:
            result.append(i)

    return result


def main():
    ip_list = load_csv("ipaddress.txt")
    range_list = load_csv("iprange.txt")
    ip_in_range_list = get_ip_in_range(range_list)
    check_ip_in_range(ip_list, ip_in_range_list)


if __name__ == "__main__":
    main()
