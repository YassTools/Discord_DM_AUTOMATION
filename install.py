import os


depedencies = ['colorama','requests','time','json']
print('Preparing to install modules...')

for library in depedencies:
    print(f'Installing {library}...')
    os.system(f'pip install {library}')
