import sys
import re
import io

with open('your filename or location', "rb") as fp: #Open and read the file in read_binary mode

    for line in fp: 
        if b"\r\n" in line: # In if statement "b" means that all data read from the file is returned as bytes objects, not str.
            print("CR+LF (Windows) format.")
        elif b"\n" in line:
            print("LF (UNIX) format.")
        elif b"\r" in line:
            print("CR (MAC) format.")
        else:
            print("NULL")


