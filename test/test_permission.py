import ctypes, os
import sys


def is_admin_win():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin


def test_permission():
    print(sys.platform)
    if sys.platform == "win32":
        priv = is_admin_win()
        print(priv)
        assert priv == True


if __name__ == "__main__":
    test_permission()
