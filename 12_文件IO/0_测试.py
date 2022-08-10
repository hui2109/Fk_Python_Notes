import pathlib
# print(pathlib.PurePath.__subclasses__())
def getSubClasses(cls):
    for subcls in cls.__subclasses__():
        print(subcls)
        if len(cls.__subclasses__()) > 0:
            getSubClasses(subcls)
    
getSubClasses(pathlib.PurePath)
pathlib.PosixPath