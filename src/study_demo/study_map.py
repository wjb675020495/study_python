import os
import re


def has_java(java_path):
    if re.match(re.compile(".*?.java$"), java_path):
        return True
    else:
        return False


def get_all_package_name(path):
    packages = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            packages.append(os.path.join(subdir, file))
    save_list = []
    for package in packages:
        package_path = str(package)
        save_list.append(package_path)
    return save_list


if __name__ == '__main__':
    path_old = r"E:\Project\java\getMethod\test"
    java_list = get_all_package_name(path_old)
    obj = map(has_java, java_list)
    with open("result.txt", "w") as file:
        file.write(str(list(obj)))
