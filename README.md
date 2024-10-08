# Audio-Video Merging with FFmpeg

This project allows you to convert `.opus` audio files to `.mp3` format and then combine them with `.mp4` video files. The input files should be organized under specified folders, and the output will be stored in a designated directory. The process is automated using a Python script that utilizes [FFmpeg](https://ffmpeg.org/).

## Prerequisites

- Python 3.11+
- FFmpeg: Ensure FFmpeg is installed on your system. You can download it from the [official FFmpeg website](https://www.ffmpeg.org/)

## Project Structure

- `audio-folder/`: Contains the input audio files in `.opus` format. Files should follow the naming convention `name-{number}.opus` (e.g., `audio-1.opus` ).
- `video-folder/`: Contains the input video files in `.mp4` format. The video files should correspond to the audio files based on the `{number}`.
- `output-folder/`: The folder where the final comnined video files will be saved.

## Usage:

1. Place your `.opus` audio files in the `audio-folder/`.
2. Place your corresponding `.mp4` video files in the `video-folder`.
3. Run the Python script to process the files:

    ```sh
    python main.py
    ```

4. Check the combined video files in the `output-folder/`.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- [FFmpeg](https://www.ffmpeg.org/) for providing a powerful multimedia framework.
