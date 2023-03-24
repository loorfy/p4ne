import glob

set_of_ip = []

for current_file in glob.glob(r"E:/Learning/seafiles/store/Seafile/My library/p4ne_training/config_files/*.log"):
    with open(current_file) as f:
        for line in f:
            if "ip address" in line:
                if "no ip address" not in line:
                    set_of_ip.append(line.replace("ip address", "").strip())

for i in set_of_ip:
    print(i)

