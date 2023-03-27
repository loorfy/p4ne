from ipaddress import IPv4Interface
import glob
import re

def filtering(x):
    m = re.match("^ ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})$", x)
    if m:
        return {IPv4Interface(str(m.group(1)) + "/" + str(m.group(2)))}
    else:
        return ("None")

set_of_ip = []

for current_file in glob.glob(r"E:/Learning/seafiles/store/Seafile/My library/p4ne_training/config_files/*.log"):
    with open(current_file) as f:
        for line in f:
            string = filtering(line)
            if string != "None":
                set_of_ip.append(string)

print(set_of_ip)