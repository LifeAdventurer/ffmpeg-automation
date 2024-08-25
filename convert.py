import subprocess


def convert_opus_to_mp3(input_filepath, output_filepath):
    command = [
        "ffmpeg",
        "-i",
        input_filepath,
        "-acodec",
        "libmp3lame",
        "-aq",
        "4",
        output_filepath,
    ]
    subprocess.run(command)
