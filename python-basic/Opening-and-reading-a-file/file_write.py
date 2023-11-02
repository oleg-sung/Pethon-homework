def file_sorting(files):
    file_dict = {}
    for file in files:
        with open(file, 'r', encoding="UTF-8") as f:
            file_dict[file] = len(f.readlines())
    file_list = sorted(file_dict, key=file_dict.get)
    return file_list, file_dict


def rewrite_file(file):
    with open('files_txt/file_info.txt', 'w', encoding="UTF-8") as f:
        file_list, file_dict = file_sorting(file)
        for file_name in file_list:
            f.write(f'{file_name[10:]}\n')
            f.write(f'{file_dict[file_name]}\n')
            with open(file_name, 'r', encoding="UTF-8") as file:
                for line in file.readlines():
                    f.write(f'{line.rstrip()}\n')


rewrite_file(['files_txt/1.txt', 'files_txt/2.txt', 'files_txt/3.txt'])
