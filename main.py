import os 
import glob
import requests, zipfile, io

zip_file_url = 'https://pythonhow.com/media/django-summernote/2024-03-18/56329707-c901-4a2b-954a-6f647c433f20.zip'
r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))

outdir = 'files'

if not os.path.exists(outdir):
  os.makedirs(outdir)
  
z.extractall(outdir)

files = glob.glob(f'{outdir}/*txt')

files.sort()
merged_file = f'{outdir}/merged.txt'
with open(merged_file, 'w') as merged:
  for file in files:
    with open(file, 'r') as f:
      merged.write(f.read())
      merged.write('\n')  
print(f'Merged file saved to {merged_file}')
  