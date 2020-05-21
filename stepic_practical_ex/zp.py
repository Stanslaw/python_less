import zipfile

with zipfile.ZipFile("rogaikopyta.zip", 'r') as zip_ref:
    zip_ref.extractall("./unzipped/")

