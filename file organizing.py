import os,shutil
def organize_files(folder_path):
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path,file)):
            ext=file.split('.')[-1]
            os.makedirs(os.path.join(folder_path,ext),exist_ok=True)
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path,ext,file))
        
organize_files(r"C:\\Users\\hirwa\\OneDrive\\Documents\\Afra")
import os
print(os.path)


os.chdir("C:\\Users\\hirwa\\OneDrive\\Documents\\Afra")

fobj = open("sample.txt", "w")

os.makedirs("sample_folder")

os.listdir("C:\\Users\\hirwa\\OneDrive\\Documents\\Afra\\filehandling")
