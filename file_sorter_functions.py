import os
import shutil

def create_folder(folder_name, absolute_path):
    try:
        os.mkdir(absolute_path)
        print("CREATED FOLDER: "+folder_name+" & PATH: "+absolute_path)
    except OSError as error:
        print(error)    

def move_file_to_folder(source, destination):
    try:
        shutil.move(source, destination)
        print("MOVED: "+source+", TO: "+destination)
    except:
        print("ERROR MOVING")
    
def feed_path(main_path):
    if(os.path.exists(main_path)):
        print("VALID PATH")
        extensions_list = []
        for content in os.listdir(main_path):
            content_absolute_path = main_path + '\\' + content
            if(os.path.isfile(content_absolute_path)):
                file_extension = os.path.splitext(content)[1].replace('.', '')  #OR FOLDER NAME
                extension_folder_absolute_path = main_path + '\\' + file_extension
                if file_extension not in extensions_list:
                    extensions_list.append(file_extension)
                    create_folder(file_extension, extension_folder_absolute_path)
                move_file_to_folder(content_absolute_path, extension_folder_absolute_path + "\\")
        return True
    print("INVALID PATH")
    return False