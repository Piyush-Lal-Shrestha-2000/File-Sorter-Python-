from tkinter import *
from tkinter import messagebox 
import tkinter.font as font
from file_sorter_functions import feed_path

def execute_sort():
    path = entry_directory_path.get()
    if(feed_path(str(path))):
        messagebox.showinfo("Success", "Successfully sorted files of the provided path.")     
    else:
        messagebox.showinfo("Error", "Error, the provided path is not valid.") 
        
root = Tk()
root.title('File Sorter')
root.geometry("500x180")
root.resizable(False, False)

label_title = Label(root, text = 'FILE SORTER')
label_title['font'] = font.Font(family = 'Helvetica', weight = 'bold', size = 20, underline = 1)
label_title.place(x = 10, y = 10)

label_directory_path = Label(root, text = 'Directory Path: ')
label_directory_path['font'] = font.Font(size = 10)
label_directory_path.place(x = 10, y = 80)

entry_directory_path = Entry(root, borderwidth = 4, justify = CENTER)
entry_directory_path['font'] = font.Font(size = 10)
entry_directory_path.place(x = 110, y = 75, width = 375, height = 30)

button_sort = Button(root, text = 'SORT FILES', bg = '#0052cc', fg = '#ffffff', cursor = "exchange", command = execute_sort)
button_sort['font'] = font.Font(family = 'Cambria', weight = 'bold', size = 12)
button_sort.place(x = 10, y = 120)

root.mainloop() 