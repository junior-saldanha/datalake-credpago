from urllib.request import urlretrieve
import py7zr
import os

basepath = "./opt/ml/processing/output"
dlpath = f"{basepath}/credpago"

names = [
    
]
urls = [
    

def obter_dados(url, name):
    filename = dlpath + '/' + name
    urlretrieve(url, filename=filename)
    #print(filename)
    #archive = py7zr.SevenZipFile(filename)
    #archive.extractall(path=dlpath)
    #archive.close()
    #os.remove(filename)
    return True
    
if __name__ == "__main__":
    os.makedirs(dlpath, exist_ok=True)

    for i in range(len(urls)):
        print(f"Extracting from {urls[i]}")
        res = obter_dados(urls[i], names[i])
        print(res)
    
    print("Done!")
