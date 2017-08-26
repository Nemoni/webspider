import urllib.request

def getFile(url):
    file_name = 'book.pdf'
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print("Sucessful to download"," " ,file_name)

url = 'http://merger.ishare.down.sina.com.cn/8003406.pdf?ssig=eLLSBgsIzs&Expires=1508830535&KID=sina,ishare&ip=&fn=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E4%B8%AD%E6%96%87%E7%89%88.pdf'
getFile(url)