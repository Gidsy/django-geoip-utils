import os

def where():
    f = os.path.split(__file__)[0]
    return os.path.abspath(os.path.join(f, 'data'))

if __name__ == '__main__':
    print where()
