from threading import Thread
import lookup_file_system_events
from ctypes import windll
import string

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives


def read_dir():

    drives = get_drives()
    for drive in drives:
        t = Thread(target=lookup_file_system_events.lookup(drive+':\\'))
        # t.daemon = True
        t.start()