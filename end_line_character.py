import sys
import re
import io

with open('your filename or location', "rb") as fp: #Open and read the fil in read_binary mode

    for line in fp: 
        if b"\r\n" in line:
            print("CR+LF (Windows) format.")
        elif b"\n" in line:
            print("LF (UNIX) format.")
        elif b"\r" in line:
            print("CR (MAC) format.")
        else:
            print("NULL")


