# Tacotron2 for Korean (taKotron2)

- Code borrow from [NVIDIA/tacotron2](https://github.com/NVIDIA/tacotron2)
- Modify for Korean TTS System (see [text/\_\_init\_\_.py](https://github.com/sooftware/nvidia-tacotron2/blob/master/text/__init__.py))
  - Normalize with NFKD
  - [g2pK](https://github.com/Kyubyong/g2pK)
- Add learning rate scheduler (transformer style)
- Add [Wandb](https://wandb.ai/) monitoring
- Add generate mel-spectrogram and alignment monitoring. 
  
<img src="https://user-images.githubusercontent.com/42150335/137355410-f4df3b72-d3fa-43e0-9bfb-194e01e9b35a.png" width=800>
