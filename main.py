import subprocess as sb
from pyfiglet import figlet_format
import questionary as q
from pathlib import Path
from rich.console import Console
from rich.text import Text

supported = [
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".avif"
]

console = Console()
art = figlet_format("Imagedawg", font="slant")

text = Text(art)
text.stylize("bold rgb(220,0,0) on rgb(0,0,0)")
console.print(text)
console.print("Welcome to [italic red]Imagedawg[/italic red] your offline CLI image converter\n")
console.print(f"Image format supported [sea_green2]'{supported}'[/sea_green2]")

def get_input_path():
    c = q.text("Enter full path of the image").ask()
    file_path = Path(c)

    if file_path.exists():
        print(f"The path '{file_path}' exists.")
    else:
        print(f"The path '{file_path}' does not exist.")
        exit()

    return file_path

def detect_format(path):
    if path.suffix.lower() in supported:
        print("The given format exists throwing the file for the next step")
    else:
        print("The given format is invalid")
        exit()

def get_output_format():
    a = input("type .jpg/.webp/.png or any other image format to convert into the given format\n")
    if a in supported:
        return a
    else:
        print("Invalid choice")
        exit()


def convert(path,gof):
    print("Violating your state secrets beeeep boooop beeeeep................")
    command = ["ffmpeg", "-i",path, "img123"+gof]
    sb.run(command,shell = False)


path = get_input_path()
inp_format = detect_format(path)
out_format = get_output_format()
convert(path, out_format)


