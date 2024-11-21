import os
import os.path
import urllib.request
import zipfile
print(__file__)
if os.name == "nt":
    os.system(f"start '{os.path.join(os.path.split(__file__)[0],"python-3.13.0-amd64.exe")}'")
else:
    os.system("sudo apt-get install python3.6")
chemin = input("qu'elle est le chemin de téléchargement de l'application ? ")
if not chemin:
    chemin = os.path.split(__file__)[0]
try:
    url = "https://github.com/lugamecooper/sms-partage-de-co/archive/refs/tags/V1.0.zip"
    urllib.request.urlretrieve(url, filename=f"{os.path.join(chemin,"v1.0.zip")}")
    zipfile.ZipFile(os.path.join(chemin,"v1.0.zip")).extractall()
    os.remove(os.path.join(chemin,"v1.0.zip"))
except Exception as er:
    print(er)
    input()
os.system("pip install colorama")