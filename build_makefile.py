#!/usr/bin/env python3


import os
import sys
import subprocess


def main():
    scripts_dir = sys.stdin.readline().splitlines()[0]
    scripts_local = f"{os.environ['PWD']}/{scripts_dir}"
    
    try:
        scripts_dir_ls = os.listdir(scripts_local)
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        return 1

    entries = list()
    entry = ""
    for script in scripts_dir_ls:
        script_name = script.split(".")[0]
        entry = f".PHONY: {script_name}\n\{script_name}:\n\t{scripts_dir}/{script}\n\n"
        entries.append(entry)
    
    h = open("./makefile", 'w')
    for entry in entries:
        h.write(entry)
    h.close()

    return 0


if __name__ == '__main__':
    sys.exit(main())
