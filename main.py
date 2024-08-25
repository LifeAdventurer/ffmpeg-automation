import os

from combine import combine_audio_and_video
from convert import convert_opus_to_mp3

AUDIO_FOLDER = "./audio-folder/"
VIDEO_FOLDER = "./video-folder/"
OUTPUT_FOLDER = "./output-folder/"
DUMP_FOLDER = "./dump-folder/"


def main():
    for filename in os.listdir(AUDIO_FOLDER):
        if filename.endswith(".opus"):
            output_filename = f"{os.path.splitext(filename)[0]}.mp3"
            convert_opus_to_mp3(
                os.path.join(AUDIO_FOLDER, filename),
                os.path.join(AUDIO_FOLDER, output_filename),
            )
            os.rename(
                os.path.join(AUDIO_FOLDER, filename),
                os.path.join(DUMP_FOLDER, filename),
            )

    for audio_filename in os.listdir(AUDIO_FOLDER):
        for video_filename in os.listdir(VIDEO_FOLDER):
            if video_filename.endswith(".mp4"):
                audio_filename_number = os.path.splitext(audio_filename)[
                    0
                ].split("-")[-1]
                video_filename_number = os.path.splitext(video_filename)[
                    0
                ].split("-")[-1]
                if audio_filename_number == video_filename_number:
                    combine_audio_and_video(
                        os.path.join(AUDIO_FOLDER, audio_filename),
                        os.path.join(VIDEO_FOLDER, video_filename),
                        os.path.join(OUTPUT_FOLDER, video_filename),
                    )
                    os.rename(
                        os.path.join(AUDIO_FOLDER, audio_filename),
                        os.path.join(DUMP_FOLDER, audio_filename),
                    )
                    os.rename(
                        os.path.join(VIDEO_FOLDER, video_filename),
                        os.path.join(DUMP_FOLDER, video_filename),
                    )
                    break


if __name__ == "__main__":
    main()
