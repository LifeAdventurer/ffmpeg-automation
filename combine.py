import subprocess

def combine_audio_and_video(audio_filepath, video_filepath, combined_output_filepath):
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            video_filepath,
            "-i",
            audio_filepath,
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-strict",
            "experimental",
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            combined_output_filepath,
        ]
    )
