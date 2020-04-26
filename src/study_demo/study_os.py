import os


def get_all_files():
    """get a files from a path
    :return: files list
    """
    cur_path = os.getcwd()
    paths_dir = os.listdir(cur_path)
    path_list = []
    for path in paths_dir:
        file_path = os.path.join(cur_path, path)
        path_list.append(file_path)
    return path_list


def read_file(path):
    """read file content from a path
    :param path:
    :return:file content
    """
    with open(path, 'r') as all_file:
        print(all_file.read())
        files_content = all_file.read()
        if files_content.find('add') != -1:
            print(files_content)


if __name__ == '__main__':
    files_all = get_all_files()
    for file in files_all:
        read_file(file)
