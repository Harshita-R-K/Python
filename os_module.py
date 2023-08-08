import os

print(os.getcwd())   #to get current working directory

os.chdir('D:\casdev')   #to change directory
print(os.getcwd())

os.chdir('D:\Python_files')
print(os.listdir())      # to list the items in current directory

os.mkdir('samplefile')         #to create folder
os.makedirs('samplefile.txt')  #to create folders
print(os.listdir()) 

os.rmdir('samplefile')          #to delete folder
os.removedirs('samplefile.txt') #to delete folders

#os.rename('Untitled-1.py', 'unused.py')  #to rename file
#print(os.listdir()) 


for dirpath,dirname,dirfiles in os.walk('D:\casdev\BuildTools'):
    print('current path:',dirpath)
    print('directories:',dirname)
    print('file names:',dirfiles)
