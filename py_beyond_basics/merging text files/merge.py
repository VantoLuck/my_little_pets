from datetime import datetime as dt
import glob2

filenames = glob2.glob("*.txt")
with open(dt.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", "w") as file:
    for f in filenames:
        with open(f, "r") as fl:
            file.write(fl.read() + "\n")
"""
with open("file1.txt", "r") as f1:
    f1_content = f1.read()
with open("file2.txt", "r") as f2:
    f2_content = f2.read()
with open("file3.txt", "r") as f3:
    f3_content = f3.read()
f_out_name =   f_out_name.strftime("%Y-%m-%d-%H-%M-%S-%f")
with open("%s.txt" %f_out_name, "w") as f_out:
    f_out.write(f1_content, "\n", f2_content, "\n", f3_content)
"""
