from src.main import get_os_and_sys_version

def test_system():
    python_ver, sys_ver = get_os_and_sys_version()

    os_list =  ['Windows', 'Linux']
    python_ver_list = ['3.7', '3.8', '3.9', '3.11', '3.12']
    
    assert python_ver in python_ver_list
    assert (sys_ver in os_list) if sys_ver else True

if __name__ == "__main__":
    test_system()