import os

def where():
    f = os.path.split(__file__)[0]
    return os.path.join(f, 'cacert.pem')

if __name__ == '__main__':
    print where()