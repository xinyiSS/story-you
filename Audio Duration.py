from pydub import AudioSegment
import torch
import numpy as np

class AudioDuration:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio_file": ("AUDIO",),  # 单个音频文件
            }
        }

    RETURN_TYPES = ("FLOAT",)  # 返回音频的时长，单位为秒，浮点数格式
    FUNCTION = "calculate_duration"
    CATEGORY = "Audio Processing"

    def calculate_duration(self, audio_file):
        waveform = audio_file['waveform'].squeeze(0).numpy() * 32768  # 转换为numpy并放大
        waveform = waveform.astype(np.int16)
        sample_rate = audio_file['sample_rate']

        # 使用AudioSegment从numpy数组创建音频
        segment = AudioSegment(
            data=waveform.tobytes(),
            sample_width=2,  # 16-bit audio
            frame_rate=sample_rate,
            channels=1
        )

        # 计算音频的时长，以秒为单位，直接返回浮点数格式
        duration_seconds = len(segment) / 1000.0

        return (duration_seconds,)

NODE_CLASS_MAPPINGS = {
    "AudioDuration": AudioDuration
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AudioDuration": "Audio Duration"
}
