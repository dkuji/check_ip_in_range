from unittest.mock import MagicMock
from src import main


def test_get_ip_in_range():
    range_list = [
        ['192.168.0.1', '192.168.0.254'],
        ['192.168.10.1', '192.168.11.254'],
        ['192.168.100.1', '192.168.100.1'],
    ]
    result = main.get_ip_in_range(range_list)
    assert len(result) == 3
    assert len(result[0]) == 254
    assert result[0][0] == "192.168.0.1"
    assert result[0][-1] == "192.168.0.254"
    assert len(result[1]) == 510
    assert result[1][0] == "192.168.10.1"
    assert result[1][-1] == "192.168.11.254"
    assert len(result[2]) == 1
    assert result[2][0] == "192.168.100.1"
    assert result[2][-1] == "192.168.100.1"


def test_check_ip_in_range(capfd):
    """正常系のテスト"""
    ip_list = [['192.168.0.1'], ['192.168.100.1'], ['172.16.0.1']]
    ip_in_range_list = [
        ['192.168.0.1', '192.168.0.254'],
        ['192.168.10.1', '192.168.11.254'],
        ['192.168.20.1', '192.168.21.254'],
        ['172.16.0.1', '172.16.10.254'],
    ]

    result = main.check_ip_in_range(ip_list, ip_in_range_list)
    out, err = capfd.readouterr()
    expect_stdout = """192.168.0.1,192.168.0.1,192.168.0.254
192.168.100.1
172.16.0.1,172.16.0.1,172.16.10.254
"""
    assert result["status"] is True
    assert result["error"] == ""
    assert out == expect_stdout


def test_check_ip_in_range_same_ip(capfd):
    """レンジの開始と終了が同じパターンのテスト"""
    ip_list = [['192.168.0.1']]
    ip_in_range_list = [
        ['192.168.0.1', '192.168.0.1'],
    ]

    result = main.check_ip_in_range(ip_list, ip_in_range_list)
    out, err = capfd.readouterr()
    expect_stdout = """192.168.0.1,192.168.0.1,192.168.0.1
"""
    assert result["status"] is True
    assert result["error"] == ""
    assert out == expect_stdout
