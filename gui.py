import os.path
import tkinter as tk
from tkinter import ttk, filedialog

import text
import util


# this function opens a file chooser dialog
def browseFiles():
    # using the tkinter file dialog
    chosenFile = filedialog.askopenfilename(initialdir="/",
                                            title="Select a File",
                                            filetypes=(("Text files",
                                                        "*.txt*"),
                                                       ))
    # resetting the file path input field
    filePath.delete(0, "end")
    # setting the file path in the input field to the selected file
    filePath.insert(0, chosenFile)


# function to set the cryptic keys
def setKey():
    # checking if the key was set or is changed
    if setKeyInput != "Enter new Custom key or let it generate" and len(setKeyInput.get()) == 26:
        # resetting the current keys
        text.cryptKeyU, text.cryptKeyL = [], []
        # looping through all letters in the input field
        for letter in setKeyInput.get():
            # adding the current letter to the upper case key
            text.cryptKeyU.append(letter)
            # making the current key lower case and adding it to the lower key
            text.cryptKeyL.append(letter.lower())
        # updating the labels of the GUI
        upperKeyLabel.config(text='UPPER KEY: ' + str(text.cryptKeyU))
        lowerKeyLabel.config(text='LOWER KEY: ' + str(text.cryptKeyL))


# function for generating random keys
def genRndKey():
    # generating the key with the function from 'utils'
    rndKey = util.generateKey()
    finalKey = ""
    # looping through every letter in the key
    for letter in rndKey:
        # adding the letter to the key as a string
        finalKey = finalKey + letter
    # resetting the key input field
    setKeyInput.delete(0, "end")
    # inserting the key into the key input field
    setKeyInput.insert(0, finalKey)


# function to generate cryptik keys with an offset
def genKeyOffset():
    # checking if the input offset is a number
    if generateKeyOffsetInput.get().isnumeric():
        # getting the offset
        offset = int(generateKeyOffsetInput.get())
        # generating the keys
        tmpKeyU, tmpKeyL = util.genKeyOffset(offset)
        key = ""
        # looping over every letter in the key
        for letter in tmpKeyU:
            # adding the letter to the final key as a string
            key = key + letter
        # resetting the key input field
        setKeyInput.delete(0, "end")
        # inserting the key into the key input field
        setKeyInput.insert(0, key)


# function to load the text from a .txt file into the text input field
def loadFile():
    # getting file path
    file = filePath.get()
    # checking if path is a file
    if os.path.isfile(file):
        # opening the file to read
        file = open(file, "r")
        # reading the files content
        fileContent = file.read()
        # resetting the text input field
        textInput.delete('1.0', tk.END)
        # inserting the loaded text into the text input field
        textInput.insert(tk.END, fileContent)


# function to encrypt a given text
def encrypt():
    # checking if the cryptik keys are set
    if text.cryptKeyL != [] and text.cryptKeyU != []:
        # getting the text that should get encrypted from the text input field
        textToGetEncrypted = textInput.get('1.0', tk.END)
        # encrypting the text with the function from 'text'
        encryptedText = text.encrypt(textToGetEncrypted)
        # generating the Output file with the encrypted text
        util.genOutputFile(encryptedText, True)
        # resetting the text output field
        textOutput.delete('1.0', tk.END)
        # inserting the encrypted text into the text output field
        textOutput.insert(tk.END, encryptedText)


# function to decrypt a given text
def decrypt():
    # checking if the cryptik keys are set
    if text.cryptKeyL != [] and text.cryptKeyU != []:
        # getting the text that should get decrypted from the text input field
        textToGetDecrypted = textInput.get('1.0', tk.END)
        # decrypting the text with the function from 'text'
        decryptedText = text.decrypt(textToGetDecrypted)
        # generating the Output file with the decrypted text
        util.genOutputFile(decryptedText, False)
        # resetting the text output field
        textOutput.delete('1.0', tk.END)
        # inserting the decrypted text into the text output field
        textOutput.insert(tk.END, decryptedText)


# this mess is for creating all the necessary tkinter objects so that they are accessible for the functions
# getting a root instance
root = tk.Tk()
# setting the window dimensions
root.geometry('700x800')
# disabling resizing of the window
root.resizable(False, False)
# setting the window title
root.title('Text Crypting')
# loading the window icon form the project files
icon = tk.PhotoImage(file='icon.png')
# setting the loaded icon as the window icon
root.iconphoto(False, icon)
# creating the main container (frame)
frm = tk.Frame(root, padx=10, pady=10)
# enabling the positioning grid for this frame
frm.grid()

# creating a container for the cryptik key label stuff
keyContainer = tk.Frame(frm, padx=10, pady=10)
# creating a small informational label
keyLabel = tk.Label(keyContainer, text='Current key:')
# creating the labels that contain the information about the cryptik keys
upperKeyLabel = tk.Label(keyContainer, text='UPPER KEY: ' + str(text.cryptKeyU))
lowerKeyLabel = tk.Label(keyContainer, text='LOWER KEY: ' + str(text.cryptKeyL))

# creating a container for the cryptik key action stuff
keyActionsContainer = tk.Frame(frm, padx=10, pady=10)
# adding a button to set the cryptik key with the matching function
setKeyBtn = tk.Button(keyActionsContainer, text='Set new Key', command=setKey)
# adding an input field for inputting custom keys
setKeyInput = tk.Entry(keyActionsContainer, width=50)
# adding a button to generate a random key with the matching function
generateKeyRnd = tk.Button(keyActionsContainer, text='Random', command=genRndKey)
# adding a button to generate a cryptik key with an offset with the matching function
generateKeyOffset = tk.Button(keyActionsContainer, text='Offset', command=genKeyOffset)
# adding an input field for entering the offset
generateKeyOffsetInput = tk.Entry(keyActionsContainer, width=5)

# creating a container for the text stuff
textContainer = tk.Frame(frm, padx=10, pady=10)
# adding a label for the input text field
textInputLabel = tk.Label(textContainer, text='Text Input:')
# adding an input text field
textInput = tk.Text(textContainer, width=75, height=10)
# adding a label for the output text field
textOutputLabel = tk.Label(textContainer, text='Text Output:')
# adding an output text field
textOutput = tk.Text(textContainer, width=75, height=10)

# creating a container for all the file related stuff
fileContainer = tk.Frame(frm, padx=10, pady=10)
# adding a label for the file path input field
filePathLabel = tk.Label(fileContainer, text='File Path:')
# adding the file path input field
filePath = tk.Entry(fileContainer, width=50)
# adding a button for choosing a file directly with the matching function
fileChooserBtn = tk.Button(fileContainer, text='Browse File', command=browseFiles)
# adding a button to load the text from the file with the matching function
fileLoadBtn = tk.Button(fileContainer, text='Load file', command=loadFile)

# creating a container for the decrypt and encrypt buttons
actionContainer = tk.Frame(frm, padx=10, pady=10)
# adding the encrypt Button with the matching function
encryptBtn = tk.Button(actionContainer, text='Encrypt', command=encrypt)
# adding the decrypt Button with the matching function
decryptBtn = tk.Button(actionContainer, text='Decrypt', command=decrypt)

# adding an informational label
infoLabel = tk.Label(frm, text='The BruteForceDecrypt and autoDecrypt functions are only available in the CLI version '
                               'as they are currently Experimental!',
                     foreground="red")
# adding a button to exit the application
exitBtn = tk.Button(frm, text="Exit", command=root.destroy)


# function for loading and showing the GUI
def GUI():
    # positioning the first container
    keyContainer.grid(row=0, column=0, sticky=tk.W)
    # positioning the first informational label
    keyLabel.grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)
    # positioning the key labels
    upperKeyLabel.grid(row=1, column=0, padx=0, pady=0, sticky=tk.W)
    lowerKeyLabel.grid(row=2, column=0, padx=0, pady=0, sticky=tk.W)

    # positioning the second container
    keyActionsContainer.grid(row=1, column=0, sticky=tk.W)
    # positioning the setKey button
    setKeyBtn.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    # positioning the input field for inputting a key
    setKeyInput.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
    # adding some informational text to the input field
    setKeyInput.insert(0, "Enter new Custom key or let it generate")
    # adding event listeners to the input field for adding/removing the informational text
    setKeyInput.bind("<FocusIn>", lambda event: setKeyInputPlaceholder(event))
    setKeyInput.bind("<FocusOut>", lambda event: setKeyInputPlaceholder(event))

    # positioning the button for generating a random key
    generateKeyRnd.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)
    # positioning the button for generating an offset key
    generateKeyOffset.grid(row=3, column=3, padx=5, pady=5, sticky=tk.W)
    # positioning the input field for inputting an offset
    generateKeyOffsetInput.grid(row=3, column=4, padx=0, pady=0, sticky=tk.W)

    # positioning the container for the text stuff
    textContainer.grid(row=2, column=0, sticky=tk.W)
    # positioning the text input field label
    textInputLabel.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    # positioning the text input field
    textInput.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    # positioning the text output field label
    textOutputLabel.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    # positioning the text output field
    textOutput.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    # positioning the container for the file stuff
    fileContainer.grid(row=3, column=0, sticky=tk.W)
    # positioning the label of the path input field
    filePathLabel.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    # positioning the file path input field
    filePath.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
    # adding some informational text to the path input field
    filePath.insert(0, "Enter file path to file to be encrypted or decrypted")
    # adding event listeners to the input field for adding/removing the informational text
    filePath.bind("<FocusIn>", lambda event: filePathPlaceholder(event))
    filePath.bind("<FocusOut>", lambda event: filePathPlaceholder(event))
    # positioning the button which opens the file chooser
    fileChooserBtn.grid(row=6, column=2)
    # positioning the button for loading the file
    fileLoadBtn.grid(row=6, column=3, padx=5, pady=5, sticky=tk.W)

    # positioning the container with the encrypt/decrypt buttons
    actionContainer.grid(row=4, column=0, sticky=tk.W)
    # positioning the encrypt Button
    encryptBtn.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    # positioning the decrypt Button
    decryptBtn.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    # positioning the informational label at the bottom
    infoLabel.grid(padx=10, pady=10, sticky=tk.W)
    # positioning the exit button
    exitBtn.grid(padx=10, pady=10, sticky=tk.SE)

    # running the infinite loop which also opens the window
    root.mainloop()


# function for handling clicking events of the set key input field
def setKeyInputPlaceholder(event):
    # checking if the input field is empty
    if setKeyInput.get() == "":
        # adding the informational text
        setKeyInput.insert(0, "Enter new Custom key or let it generate")
    # checking if the informational text is the displayed text in the input field
    elif setKeyInput.get() == "Enter new Custom key or let it generate":
        # emptying the input field so that the user can enter a text
        setKeyInput.delete(0, "end")


# function for handling clicking events of the path input field
def filePathPlaceholder(event):
    # checking if the input field is empty
    if filePath.get() == "":
        # adding the informational text
        filePath.insert(0, "Enter file path to file to be encrypted or decrypted")
    # checking if the informational text is the displayed text in the input field
    elif filePath.get() == "Enter file path to file to be encrypted or decrypted":
        # emptying the input field so that the user can enter a text
        filePath.delete(0, "end")


# main function of the project if it gets run as GUI
if __name__ == "__main__":
    # running 'GUI()' function for opening the window
    GUI()
    # this line is just there to get 300 lines of code in this file with the empty line at the end
