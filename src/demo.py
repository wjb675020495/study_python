import os
import re

if __name__ == '__main__':
    os.system("find ~/tes -name '*.xml' > dir.txt")
    xml_path = []
    with open("dir.txt", "r") as all_xml_path:
        for line in all_xml_path:
            xml_path.append(line)

    f = open("tes/2/1.xml", "r")
    lines = f.readlines()
    feature_list = []
    print(type(lines))
    for line in lines:
        new_line = line.splitlines() and line.strip()
        match_obj = re.findall('''<feature name="(.*?)"/>''', new_line)
        # print(match_obj)
        feature_list.append(match_obj)
    print(feature_list)