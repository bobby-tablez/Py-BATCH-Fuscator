import os
import sys

if len(sys.argv) < 2:
    sys.exit('Please provide a batch file. IE: code_obfuscated.bat')
    
batchfile = sys.argv[1]
if not batchfile.lower().endswith(('.bat', '.cmd')):
    sys.exit('ERROR: Expected filetypes: ".bat" or ".cmd"')

outfile = f'{os.path.splitext(batchfile)[0]}___{os.path.splitext(batchfile)[1]}'
if os.path.exists(outfile):
    os.remove(outfile)

term_size = os.get_terminal_size()
print('=' * term_size.columns)

with open(batchfile, 'r', encoding='utf-8',  errors='ignore') as f:
    for line in f.readlines()[1:]:
        print(line, end='')
        with open(outfile, 'a', encoding='utf-8',  errors='ignore') as g:
            g.write(line)
print('\n')
print('=' * term_size.columns)           
input('\nPress Enter to continue...')
