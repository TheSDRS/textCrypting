import os.path
import tkinter as tk
from tkinter import ttk, filedialog

import text
import util

chosenFile = ""


def browseFiles():
    global chosenFile
    chosenFile = filedialog.askopenfilename(initialdir="/",
                                            title="Select a File",
                                            filetypes=(("Text files",
                                                        "*.txt*"),
                                                       ))
    filePath.delete(0, "end")
    filePath.insert(0, chosenFile)


def setKey():
    if setKeyInput != "Enter new Custom key or let it generate" and len(setKeyInput.get()) == 26:
        text.cryptKeyU, text.cryptKeyL = [], []
        for letter in setKeyInput.get():
            text.cryptKeyU.append(letter)
            text.cryptKeyL.append(letter.lower())
        upperKeyLabel.config(text='UPPER KEY: ' + str(text.cryptKeyU))
        lowerKeyLabel.config(text='LOWER KEY: ' + str(text.cryptKeyL))


def genRndKey():
    rndKey = util.generateKey()
    finalKey = ""
    for letter in rndKey:
        finalKey = finalKey + letter
    setKeyInput.delete(0, "end")
    setKeyInput.insert(0, finalKey)


def genKeyOffset():
    if generateKeyOffsetInput.get().isnumeric():
        offset = int(generateKeyOffsetInput.get())
        tmpKeyU, tmpKeyL = util.genKeyOffset(offset)
        key = ""
        for letter in tmpKeyU:
            key = key + letter
        setKeyInput.delete(0, "end")
        setKeyInput.insert(0, key)


def loadFile():
    file = filePath.get()
    if os.path.isfile(file):
        file = open(file, "r")
        fileContent = file.read()
        textInput.delete('1.0', tk.END)
        textInput.insert(tk.END, fileContent)


def encrypt():
    if text.cryptKeyL != [] and text.cryptKeyU != []:
        textToGetEncrypted = textInput.get('1.0', tk.END)
        encryptedText = text.encrypt(textToGetEncrypted)
        util.genOutputFile(encryptedText, True)
        textOutput.delete('1.0', tk.END)
        textOutput.insert(tk.END, encryptedText)


def decrypt():
    if text.cryptKeyL != [] and text.cryptKeyU != []:
        textToGetDecrypted = textInput.get('1.0', tk.END)
        decryptedText = text.decrypt(textToGetDecrypted)
        util.genOutputFile(decryptedText, False)
        textOutput.delete('1.0', tk.END)
        textOutput.insert(tk.END, decryptedText)


root = tk.Tk()
root.geometry('700x800')
root.resizable(False, False)
root.title('Text Crypting')
icon = tk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)
frm = tk.Frame(root, padx=10, pady=10)
frm.grid()

keyContainer = tk.Frame(frm, padx=10, pady=10)
keyLabel = tk.Label(keyContainer, text='Current key:')
upperKeyLabel = tk.Label(keyContainer, text='UPPER KEY: ' + str(text.cryptKeyU))
lowerKeyLabel = tk.Label(keyContainer, text='LOWER KEY: ' + str(text.cryptKeyL))

keyActionsContainer = tk.Frame(frm, padx=10, pady=10)
setKeyBtn = tk.Button(keyActionsContainer, text='Set new Key', command=setKey)
setKeyInput = tk.Entry(keyActionsContainer, width=50)
generateKeyRnd = tk.Button(keyActionsContainer, text='Random', command=genRndKey)
generateKeyOffset = tk.Button(keyActionsContainer, text='Offset', command=genKeyOffset)
generateKeyOffsetInput = tk.Entry(keyActionsContainer, width=5)

textContainer = tk.Frame(frm, padx=10, pady=10)
textInputLabel = tk.Label(textContainer, text='Text Input:')
textInput = tk.Text(textContainer, width=75, height=10)
textOutputLabel = tk.Label(textContainer, text='Text Output:')
textOutput = tk.Text(textContainer, width=75, height=10)

fileContainer = tk.Frame(frm, padx=10, pady=10)
filePathLabel = tk.Label(fileContainer, text='File Path:')
filePath = tk.Entry(fileContainer, width=50)
fileChooserBtn = tk.Button(fileContainer, text='Browse File', command=browseFiles)
fileLoadBtn = tk.Button(fileContainer, text='Load file', command=loadFile)

actionContainer = tk.Frame(frm, padx=10, pady=10)
encryptBtn = tk.Button(actionContainer, text='Encrypt', command=encrypt)
decryptBtn = tk.Button(actionContainer, text='Decrypt', command=decrypt)

infoLabel = tk.Label(frm, text='The BruteForceDecrypt and autoDecrypt functions are only available in the CLI version '
                               'as they are currently Experimental!')
exitBtn = tk.Button(frm, text="Exit", command=root.destroy)


def GUI():
    keyContainer.grid(row=0, column=0, sticky=tk.W)
    keyLabel.grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)
    upperKeyLabel.grid(row=1, column=0, padx=0, pady=0, sticky=tk.W)
    lowerKeyLabel.grid(row=2, column=0, padx=0, pady=0, sticky=tk.W)

    keyActionsContainer.grid(row=1, column=0, sticky=tk.W)
    setKeyBtn.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    setKeyInput.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
    setKeyInput.insert(0, "Enter new Custom key or let it generate")
    setKeyInput.bind("<FocusIn>", lambda event: setKeyInputPlaceholder(event))
    setKeyInput.bind("<FocusOut>", lambda event: setKeyInputPlaceholder(event))

    generateKeyRnd.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)
    generateKeyOffset.grid(row=3, column=3, padx=5, pady=5, sticky=tk.W)
    generateKeyOffsetInput.grid(row=3, column=4, padx=0, pady=0, sticky=tk.W)

    textContainer.grid(row=2, column=0, sticky=tk.W)
    textInputLabel.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    textInput.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    textOutputLabel.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    textOutput.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    fileContainer.grid(row=3, column=0, sticky=tk.W)
    filePathLabel.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    filePath.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
    filePath.insert(0, "Enter file path to file to be encrypted or decrypted")
    filePath.bind("<FocusIn>", lambda event: filePathPlaceholder(event))
    filePath.bind("<FocusOut>", lambda event: filePathPlaceholder(event))
    fileChooserBtn.grid(row=6, column=2)
    fileLoadBtn.grid(row=6, column=3, padx=5, pady=5, sticky=tk.W)

    actionContainer.grid(row=4, column=0, sticky=tk.W)
    encryptBtn.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    decryptBtn.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    infoLabel.grid(padx=10, pady=10, sticky=tk.W)
    exitBtn.grid(padx=10, pady=10, sticky=tk.SE)

    root.mainloop()


def setKeyInputPlaceholder(event):
    if setKeyInput.get() == "":
        setKeyInput.insert(0, "Enter new Custom key or let it generate")
    elif setKeyInput.get() == "Enter new Custom key or let it generate":
        setKeyInput.delete(0, "end")


def filePathPlaceholder(event):
    if filePath.get() == "":
        filePath.insert(0, "Enter file path to file to be encrypted or decrypted")
    elif filePath.get() == "Enter file path to file to be encrypted or decrypted":
        filePath.delete(0, "end")


if __name__ == "__main__":
    GUI()
