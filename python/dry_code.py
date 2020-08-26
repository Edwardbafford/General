from pathlib import Path

dir_name = 'data'
file_names = ['file-1.txt', 'file-2.txt', 'file-3.txt']

print(', '.join([Path('{0}/{1}'.format(dir_name, f)).read_text() for f in file_names]))