import sys
import re
import io


path = '/user/name/Yourfile.exy' # Enter your file path


with open(path, "rb") as fp1:

    for data in fp1:

        if b"\r\n" in data:
            with open(path, "rb") as fp2:
                for data1 in fp2:

                    if b"\r\n" in data1:
                        continue
                    else:
                        print(data1)
                        print("mixed Format")
                        exit()

        elif b"\n" in data:
            with open(path, "rb") as fp2:
                for data1 in fp2:
                    if b"\n" in data1:
                        continue
                    else:
                        print(data1)
                        print("mixed Format")
                        exit()

        elif b"\r" in data:
            with open(path, "rb") as fp2:
                for data1 in fp2:
                    if b"\r" in data1:
                        continue
                    else:
                        print(data1)
                        print("mixed Format")
                        exit()

        else:
            print("NULL")
    print("No Foramt Changes")
