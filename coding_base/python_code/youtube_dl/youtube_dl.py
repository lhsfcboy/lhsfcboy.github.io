
import os, os.path
import subprocess



for playlist in [
        "PLRCe1CegVgvjb7h9ii3DlRimro3j3IH65",
        "PLRCe1CegVgvhsyauKR2gzA42nw_ONzkan",
        "PLRCe1CegVgvibFxQuHUpD3BoKTweVvXs0",
        "PLRCe1CegVgvjH9Qsygn8y4CIY7BOnxqHv",
        ]:

    command = [
        r"youtube-dl",
        r"--format", r"best",  
        # r"--get-filename",  
        r"--output", r'"%(playlist)s-%(title)s.%(ext)s"',
        playlist,
    ]
    
    command = " ".join(command)

    print(f"----------------\n{command}\n------------------")
    with subprocess.Popen(command) as process:
        print(r"youtube-dl return code :", process.returncode)