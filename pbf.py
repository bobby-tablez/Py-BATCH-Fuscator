import os
import sys
import base64

param = sys.argv[1]

if param == '-h' or param == '--help':
    sys.exit(f'Usage:\nTo Obfuscate: python pbf.py [-e/--encode] file.bat\nTo Deobfuscate: python pbf.py [-d/--decode] file_obfuscated.bat')

filename = sys.argv[2]

if not os.path.isfile(filename):
    sys.exit(f'Error: {filename} not found')

if not filename.lower().endswith(('.bat', '.cmd')):
    sys.exit(f'Error: {filename} is not a batch file. Expected filetypes: ".bat" or ".cmd"')

def obfuscate(filename):
    infile = filename

    b64_encoded = '//4mY2xzDQo='.strip().encode('utf-8')
    decoded_content = base64.b64decode(b64_encoded)

    outfile = f'{os.path.splitext(infile)[0]}_obfuscated{os.path.splitext(infile)[1]}'
    with open(outfile, 'wb') as f:
        f.write(decoded_content)

    with open(outfile, 'ab') as f:
        with open(infile, 'rb') as g:
            f.write(g.read())

    print(f"Done! Saved as:", outfile)

def deobfuscate(filename):
    batchfile = filename

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

if param == '-e' or param == '--encode':
    obfuscate(filename)

elif param == '-d' or param == '--decode':
    deobfuscate(filename)
