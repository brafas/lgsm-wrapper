import re

def find_setting(setting, setting_file):

    result = re.findall(r"^\w+", setting_file)
    print(result)

def kf_setting(file, setting, value):
    #file can be serverfiles/
