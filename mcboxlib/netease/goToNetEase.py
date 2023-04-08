import random
import uuid

def get_random_filename() -> str:
    fristName = uuid.uuid4()
    secondName = str(random.randint(10000, 99999))
    name = fristName + secondName
    return name

def newFile(filename: str,neteaseMinecraft: str) -> int:
    newFileName = get_random_filename()
    with open(filename, 'r') as f:
        fileText = f.read()
    fileText += uuid.uuid4().hex()
    with open(newFileName, 'w') as f:
        f.write(fileText)
    del fileText
    del newFileName
    return 0

def importNetease(modfile:str,minecraftName: str) -> None:
    newFile(modfile,minecraftName)
