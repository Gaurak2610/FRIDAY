from ctypes import windll
import string
import os
import stat
import ast
import tempfile
temp_dir = tempfile.gettempdir()

file_system_dict = {}
def get_duplicate_key(key,keys):
    count= 0
    for k in keys:
        if key in k:
            count+=1
    return count 
#get_duplicate_key('Users\HP\Desktop\Gaurav', [''])

def is_hidden(path):
    return bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
def get_dirves():
    drives = []
    value = windll.kernel32.GetLogicalDrives()
    print (value)
    for char in string.ascii_uppercase:
        if value & 1:
            drives.append(char)
        value >>= 1
    return drives
def find():
    drives = get_dirves()
    for drive in drives:
        for root, dirs, files in os.walk(drive + ':\\Users\HP\Desktop\mining'):
            for f in files:
                if is_hidden(os.path.join(root, f))==False:
                    key = os.path.join(root, f).rsplit('\\')[-1]
                    print(key+'_{}'.format(get_duplicate_key(key,file_system_dict.keys())), os.path.join(root, f))
                    file_system_dict.update({key+'_{}'.format(get_duplicate_key(key,file_system_dict.keys())): os.path.join(root, f)})

            for dir in dirs:
                if is_hidden(os.path.join(root, dir))==False:
                    print(os.path.join(root, dir))
                    key = os.path.join(root, dir).rsplit('\\')[-1]
                    print(key+'_{}'.format(get_duplicate_key(key,file_system_dict.keys())), os.path.join(root, dir))
                    file_system_dict.update({key+'_{}'.format(get_duplicate_key(key,file_system_dict.keys())): os.path.join(root, dir)})

    return file_system_dict
file_name = 'dict3.txt'
if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        file_system_dict = ast.literal_eval(f.read())
        f.close()

else:
    with open(file_name, 'w') as f:
        print('File System dictionary not found. Wait, i am doing so for the search functionality.')
        f.write(str(find()))
        f.close()


