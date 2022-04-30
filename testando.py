import zipfile

with zipfile.ZipFile(r'C:/Users/Lucas/Pictures/fotos para pdf/procurado.zip', 'r') as zip_ref:
    zip_ref.extractall(r'C:/Users/Lucas/Pictures/fotos para pdf')