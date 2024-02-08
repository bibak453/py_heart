import pymedia.removable.cd as cd
import crossfiledialog

import sys



def get_os_info():
    """
    Get information about the operating system.
    """
    if sys.platform.startswith('linux'):
        return 'Linux'
    elif sys.platform.startswith('darwin'):
        return 'macOS'
    elif sys.platform.startswith('win'):
        return 'Windows'
    else:
        return 'Unknown'

if __name__ == "__main__":
    print("Python is running on:", get_os_info())


def get_path():
    file = crossfiledialog.choose_folder(title="Pick CDROM")
    
    return file
