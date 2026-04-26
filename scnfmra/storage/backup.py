import shutil

def backup_file(src, dest):
    shutil.copy(src, dest)