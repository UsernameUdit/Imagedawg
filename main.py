import subprocess as sb
from pathlib import Path
from rich import print

print("Welcome to [italic red]Imagedawg[/italic red] your offline CLI image converter\n")

def get_input_path():
    c = input("Enter full path of the image\n")
    file_path = Path(c)

    if file_path.exists():
        print(f"The path '{file_path}' exists.")
    else:
        print(f"The path '{file_path}' does not exist.")
        exit()

    return c

def detect_format(path):
    inp_format = [".png",".jpg",".webp"]
    if path.endswith(".png"):
        print("Input format .png detected")
        return inp_format[0]
    elif path.endswith(".jpg"):
        print("Input format .jpg detected")
        return inp_format[1]
    elif path.endswith(".webp"):
        print("Input format .webp detected")
        return inp_format[2]
    else:
        print("The given format is invalid")
        exit()

def get_output_format():
    out_format = [".png",".jpg",".webp"]
    a = input("type .jpg/.webp/.png to convert into the given format\n")
    if a==".jpg":
            return out_format[1]
    elif a==".png":
        return out_format[0]
    elif a==".webp":
            return out_format[2]
    else:
        print("Invalid choice")
        exit()


def convert(path,gof):
    print("Violating your state secrets beeeep boooop beeeeep................")
    command = ["ffmpeg", "-i",path, "img123"+gof]
    sb.run(command,shell = False)
    print("File cooked dawg")


path = get_input_path()
inp_format = detect_format(path)
out_format = get_output_format()
convert(path, out_format)


