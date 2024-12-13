import Rachael as R
from Rachael import *
import webbrowser
import tkinter as tk
from tkinter import filedialog

class MyGUI:
    def __init__(self, master):
        #give the window a title and set size and keep track of the paths
        self.master = master
        self.path = ""
        self.folder_path = None
        master.title("Recipe Organizer")
        master.geometry("400x400")

        #create and display labels explaining what the buttons do
        self.label = tk.Label(master, text="Click the 'Organize' button to organize a folder full of recipes.")
        self.label.pack()

        self.label = tk.Label(master, text="Click the 'Open' button to open the folder or file.")
        self.label.pack()

        self.label = tk.Label(master, text="Click the 'Return' button to return to the list of folders.")
        self.label.pack()

        self.label = tk.Label(master, text="Click the 'Random' button to open a random recipe.")
        self.label.pack()

        #create a list box that will hold the folders/recipes
        self.listBox = tk.Listbox(width=50)
        self.listBox.pack()

        #create and display a button that organizes the recipes in the folder
        self.button = tk.Button(master, text="Organize", command=self.Organize_Recipes)
        self.button.pack()

        #create and display a button that opens a folder and/or opens a recipe listed in the listbox
        self.button = tk.Button(master, text="Open", command=self.openRecipe)
        self.button.pack()

        #create and display a button that returns to the list of folders in the listbox
        self.button = tk.Button(master, text="Return", command=self.Return)
        self.button.pack()

        #create and display a button that chooses a random recipe and opens it
        self.button = tk.Button(master, text="Random", command=self.Random_Recipe)
        self.button.pack()

    def Organize_Recipes(self):
        #clear any items previously in the listbox
        self.listBox.delete(0, tk.END)

        try:
            #use filedialog from tkinter to alow user to select desired folder using a widget
            root = tk.Tk()
            root.withdraw()

            #get path from selected folder
            self.path = filedialog.askdirectory()

            #check if the user cancled/didn't select a folder
            if(not(self.path == "")):
                #function to organize the recipes in the selected folder
                R.organizeRecipeFiles(self.path)

                #make a list of the folders
                folders = []
                for (root,dirs,files) in os.walk(self.path,topdown=True):
                    folders.extend(dirs)
                
                #add the folders to the listbox
                for folder in folders:
                    self.listBox.insert(tk.END, folder)

        except:
            pass

    def openRecipe(self):
        try:
            #get what the user selected from the listbox
            selection = self.listBox.selection_get()
            
            #check to see if it has a ".", which means it is a file
            if(selection.find(".") > 0):
                #create the path for the file and open it
                file_path = self.folder_path + "\\" + selection
                webbrowser.open_new_tab(file_path)

            #if it doesn't have a ".", it is a folder
            else:
                #clear the list box, create the folder path, 
                #and get a list of the recipes in the selected sub folder
                self.listBox.delete(0, tk.END)
                self.folder_path = self.path + "\\" + selection
                contents = os.listdir(self.folder_path)

                #display the recipes in the list box
                for content in contents:
                    self.listBox.insert(tk.END, content)
        except:
            pass

    def Return(self):
        try:
            #check if the user did not previously select a folder to organize
            if(not(self.path == "")):
                #clear the list box
                self.listBox.delete(0, tk.END)

                #get a list of the folders in the path
                folders = os.listdir(self.path)

                #display the folders in the list box
                for folder in folders:
                    self.listBox.insert(tk.END, folder)
        except:
            pass

    def Random_Recipe(self):
        try:
            if(not(self.path == "")):
                #choose a random recipe and open it
                file_path = R.chooseRandomRecipe(self.path)
                webbrowser.open_new_tab(file_path)

        except:
            pass

#create the window
root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()