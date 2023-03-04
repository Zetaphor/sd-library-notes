import os
import platform


base_dir = '/mnt/c/Users/zetap/stable-diffusion-webui/'


if os.path.exists(base_dir + 'models/Stable-diffusion'):
    extension_list = ['.safetensors', '.ckpt']
    for root, dirs, files in os.walk(base_dir + 'models/Stable-diffusion'):
        print(root)


base_dir = '/mnt/c/Users/zetap/stable-diffusion-webui/'


if os.path.exists(base_dir + 'models/Stable-diffusion'):
    extension_list = ['.safetensors', '.ckpt']
    for root, dirs, files in os.walk(base_dir + 'models/Stable-diffusion'):
        print(root)
