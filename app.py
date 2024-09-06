from tkinter import simpledialog
from tkinter import messagebox
from base64 import b64encode
from base64 import b64decode

def encodefunc():
    encode = simpledialog.askstring("Encode", "Please insert data to encode")
    if (type(None)):
        raise(SystemExit)
    messagebox.showinfo("Encoded data (CTRL+C to copy)", b64encode(str.encode(encode)))
def decodefunc():
    decode = simpledialog.askstring("Decode", "Please insert data to decode")
    if (type(None)):
        raise(SystemExit)
    messagebox.showinfo("Decoded data (CTRL+C to copy)", b64decode(decode))

ask = messagebox.askyesno("Base64 encode/decode", "Select an action")
if (ask == True):
    encodefunc()
if (ask == False):
    decodefunc()