import os
content = (".DS_Store\n.ipynb_checkpoints\n.idea")
for i in range(1,27):
    folder_name = f'Python-IT-Academy-Grodno-2022-Lesson-{i}'
    if i < 10:
        folder_name = f'Python-IT-Academy-Grodno-2022-Lesson-0{i}'
    path_name = f'./{folder_name}/.gitignore'
    print("Creating Lesson",i,"Folder")
    os.mkdir(f'./{folder_name}/')
    print("Creating gitignore for lesson", i)
    file = open(path_name,"w")
    print(file, "created")
    file.write(content)
    print("written")
    file.close()
    print(file, "closed")
print("Finish")
