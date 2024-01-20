# Licensed under GNU General Public License
# Copyright (C) 2024  Dhruv-Tara


import subprocess
import re


def encode_file(directory : str) -> str :

    input_file = directory
    pattern = re.compile(r'^\.\/downloads\/(.*?)\.mkv$')
    match = pattern.match(directory)

    output_file = f"{match.group(1)}.mp4"

    bitrate = "700k"  

    subprocess.run(["ffmpeg", "-i", input_file, "-c:s", "srt", "subtitles.srt"])

    command = [
        "ffmpeg",
        "-i", input_file,
        "-i", "subtitles.srt",
        "-c:v", "libx264",
        "-b:v", bitrate,
        "-c:a", "aac",
        "-c:s", "mov_text",  
        output_file
    ]

    subprocess.run(command)

    subprocess.run(["rm", "subtitles.srt"])

    return output_file

