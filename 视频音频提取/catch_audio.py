import sys
import os
from moviepy.editor import VideoFileClip

# 获取命令行参数
video_file = sys.argv[1]

# 获取视频文件名（不包括后缀）
video_name = os.path.splitext(os.path.basename(video_file))[0]

video = VideoFileClip(video_file)
audio = video.audio

# 保存音频文件，文件名与视频文件名一致（除了后缀）
wav_file = f"{video_name}.wav"
mp3_file = f"{video_name}.mp3"

audio.write_audiofile(wav_file)
audio.write_audiofile(mp3_file, codec="libmp3lame")