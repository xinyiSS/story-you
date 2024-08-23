from pydub import AudioSegment
import torch
import numpy as np

class ConcatAudio4:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio_file_1": ("AUDIO",),  # 第一个音频文件（来自CosyVoiceNode的输出）
                "audio_file_2": ("AUDIO",),  # 第二个音频文件（来自CosyVoiceNode的输出）
                "audio_file_3": ("AUDIO",),  # 第三个音频文件（来自CosyVoiceNode的输出）
                "audio_file_4": ("AUDIO",),  # 第四个音频文件（来自CosyVoiceNode的输出）
                "export_format": (["wav", "mp3", "flac"], {"default": "wav"}),  # 输出文件格式，支持WAV、MP3和FLAC
            }
        }

    RETURN_TYPES = ("AUDIO",)  # 返回合并后的音频数据
    FUNCTION = "merge_audio_files"
    CATEGORY = "Audio Processing"

    def merge_audio_files(self, audio_file_1, audio_file_2, audio_file_3, audio_file_4, export_format):
        audio_files = [audio_file_1, audio_file_2, audio_file_3, audio_file_4]
        combined = None
        for audio in audio_files:
            waveform = audio['waveform'].squeeze(0).numpy() * 32768  # 转换为numpy并放大
            waveform = waveform.astype(np.int16)
            sample_rate = audio['sample_rate']

            # 使用AudioSegment从numpy数组创建音频
            segment = AudioSegment(
                data=waveform.tobytes(),
                sample_width=2,  # 16-bit audio
                frame_rate=sample_rate,
                channels=1
            )
            combined = segment if combined is None else combined + segment
        
        # 导出为所需格式的音频
        output_path = f"combined_output.{export_format}"
        combined.export(output_path, format=export_format)

        # 读取导出的音频并返回
        final_audio = AudioSegment.from_file(output_path, format=export_format)
        waveform_output = torch.Tensor(np.array(final_audio.get_array_of_samples())).unsqueeze(0) / 32768
        
        # 确保返回的是一个2D Tensor，并添加一个额外的维度
        if waveform_output.ndim == 1:
            waveform_output = waveform_output.unsqueeze(0)
        elif waveform_output.ndim == 2 and waveform_output.shape[0] == 1:
            waveform_output = waveform_output.unsqueeze(0)

        audio_output = {"waveform": waveform_output, "sample_rate": final_audio.frame_rate}

        return (audio_output,)

NODE_CLASS_MAPPINGS = {
    "ConcatAudio4": ConcatAudio4
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ConcatAudio4": "Concat Audio 4"
}
