from os import makedirs, listdir, path, getcwd
from os.path import isfile, join
import shutil
import sys
import time
import subprocess

dir_raw = path.realpath(__file__).split('/')
dir_raw.pop()
base_dir = "/".join(dir_raw)
print(base_dir)
if not path.exists(f'{base_dir}/folder_test'):
    makedirs(f'{base_dir}/folder_test')

folder_1 = sys.argv[1] if len(sys.argv) > 1 else f'{base_dir}/folder_full'
folder_2 = sys.argv[2] if len(sys.argv) > 1 else f'{base_dir}/folder_test'

def main():
    files = [f for f in sorted(listdir(folder_1)) if isfile(join(folder_1, f))]
    for f in files:
        print(f'Movendo o arquivo {folder_1}/{f} para a pasta a ser observada')
        shutil.copy(f'{folder_1}/{f}', f'{folder_2}/{f}')
        time.sleep(8)

def remove_files():
    shutil.rmtree(folder_2)
    makedirs(folder_2)
    