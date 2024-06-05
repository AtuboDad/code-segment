import ChatTTS
from IPython.display import Audio
import torchaudio
import torch

chat = ChatTTS.Chat()
chat.load_models() # 设置为True以获得更快速度

texts = ["你好啊，你是谁哈，我来自中国台湾，很高兴认识你！",]

wavs = chat.infer(texts, use_decoder=True)

torchaudio.save("output1.wav", torch.from_numpy(wavs[0]), 24000)