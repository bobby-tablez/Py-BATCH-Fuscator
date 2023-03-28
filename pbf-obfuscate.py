import os
import sys
import base64

if len(sys.argv) < 2:
    sys.exit('Please provide a batch file. IE: obfuscateme.bat')

infile = sys.argv[1]
if not infile.lower().endswith(('.bat', '.cmd')):
    sys.exit('ERROR: Expected filetypes: ".bat" or ".cmd"')

b64_encoded = '//4mY2xzDQo='.strip().encode('utf-8')
decoded_content = base64.b64decode(b64_encoded)

outfile = f'{os.path.splitext(infile)[0]}_obfuscated{os.path.splitext(infile)[1]}'
with open(outfile, 'wb') as f:
    f.write(decoded_content)

with open(outfile, 'ab') as f:
    with open(infile, 'rb') as g:
        f.write(g.read())

print(f"Done! Saved as:", outfile)
