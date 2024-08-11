import zipfile


def extract(zfile, password):
    try:
        zf = zipfile.ZipFile(zfile)
        files = zf.infolist()
        zf.read(files[0], pwd=password.encode("utf-8"))  # password encoding
        zf.close()
        return True
    except KeyboardInterrupt:
        exit(0)

    return False
