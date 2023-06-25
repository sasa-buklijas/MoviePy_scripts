from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips
import sys
from pathlib import Path


def main():
    # combine 1.png and 1.mp3 in video clip
    # loop from 1 to n files
    # write all to 1.mp4

    if len(sys.argv) == 2:
        input_dir = Path(sys.argv[1])
    else:
        exit()

    # just png images, from 1 to n
    png_files = sorted([str(file) for file in input_dir.iterdir() 
                        if file.suffix == '.png'])
    print(png_files)

    video_clips = []
    for png_file in png_files:
        audio = AudioFileClip(png_file.replace('.png', '.mp3'))
        clip = ImageClip(png_file).set_audio(audio).set_duration(audio.duration)

        video_clips.append(clip)

    # Concatenate the video clips into a single video
    final_video = concatenate_videoclips(video_clips)
    final_video.write_videofile(f'{input_dir}.mp4', fps=24, codec='libx264',
                                audio_codec='aac') 
    # use aac, quick time does not understand mp3 inside mp4 aac and mp4 have same size


if __name__ == '__main__':
	main()