import hashlib
import os
import platform
import requests
import json
import html2text
import urllib.request


checkpoint_list = []
vae_list = []
embedding_list = []
hypernetwork_list = []
lora_list = []

checkpoint_needing_hash = []
vae_needing_hash = []
embedding_needing_hash = []
hypernetwork_needing_hash = []
lora_needing_hash = []

base_dir = 'C:\\Users\\zetap\\stable-diffusion-webui\\'


if platform.system() == 'Windows':
    print('Operating system is Windows')
else:
    print('Operating system is not Windows')
    base_dir = '/home/zetaphor/stable-diffusion-webui/'


def loadAssets():
    if os.path.exists(base_dir + 'models/Stable-diffusion'):
        extension_list = ['.safetensors', '.ckpt']
        for root, dirs, files in os.walk(base_dir + 'models/Stable-diffusion'):
            for file in files:
                file_path = os.path.join(root, file)

                file_name, file_ext = os.path.splitext(file)
                if os.path.isfile(os.path.join(root, file_name + '.md')):
                    file_name + '.md'

                found_file = False
                info_path = ""
                if file_ext not in extension_list:
                    continue

                if os.path.isfile(os.path.join(root, file_name + '.txt')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.txt')
                elif os.path.isfile(os.path.join(root, file_name + '.md')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.md')

                formatted_name = ""
                if platform.system() == 'Windows':
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion\\', '')
                else:
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion/', '')

                if not found_file:
                    checkpoint_needing_hash.append({
                        'name': formatted_name,
                        'filename': os.path.join(root, file),
                        'filenameNoExt': file_name,
                        'rootDir': root
                    })
                else:
                    checkpoint_list.append({
                        'name': formatted_name,
                        'filename': info_path,
                    })

    if os.path.exists(base_dir + 'models/hypernetworks'):
        extension_list = ['.pt']
        for root, dirs, files in os.walk(base_dir + 'models/hypernetworks'):
            for file in files:
                file_path = os.path.join(root, file)

                file_name, file_ext = os.path.splitext(file)
                if os.path.isfile(os.path.join(root, file_name + '.md')):
                    file_name + '.md'

                found_file = False
                info_path = ""
                if file_ext not in extension_list:
                    continue

                if os.path.isfile(os.path.join(root, file_name + '.txt')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.txt')
                elif os.path.isfile(os.path.join(root, file_name + '.md')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.md')

                formatted_name = ""
                if platform.system() == 'Windows':
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion\\', '')
                else:
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion/', '')

                if not found_file:
                    hypernetwork_needing_hash.append({
                        'name': formatted_name,
                        'filename': os.path.join(root, file),
                        'filenameNoExt': file_name,
                        'rootDir': root
                    })
                else:
                    hypernetwork_list.append({
                        'name': formatted_name,
                        'filename': info_path,
                    })

    if os.path.exists(base_dir + 'models/Lora'):
        extension_list = ['.safetensors', '.pt']
        for root, dirs, files in os.walk(base_dir + 'models/Lora'):
            for file in files:
                file_path = os.path.join(root, file)

                file_name, file_ext = os.path.splitext(file)
                if os.path.isfile(os.path.join(root, file_name + '.md')):
                    file_name + '.md'

                found_file = False
                info_path = ""
                if file_ext not in extension_list:
                    continue

                if os.path.isfile(os.path.join(root, file_name + '.txt')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.txt')
                elif os.path.isfile(os.path.join(root, file_name + '.md')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.md')

                formatted_name = ""
                if platform.system() == 'Windows':
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion\\', '')
                else:
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion/', '')

                if not found_file:
                    lora_needing_hash.append({
                        'name': formatted_name,
                        'filename': os.path.join(root, file),
                        'filenameNoExt': file_name,
                        'rootDir': root
                    })
                else:
                    lora_list.append({
                        'name': formatted_name,
                        'filename': info_path,
                    })

    if os.path.exists(base_dir + 'embeddings'):
        extension_list = ['.bin', '.pt']
        for root, dirs, files in os.walk(base_dir + 'embeddings'):
            for file in files:
                file_path = os.path.join(root, file)

                file_name, file_ext = os.path.splitext(file)
                if os.path.isfile(os.path.join(root, file_name + '.md')):
                    file_name + '.md'

                found_file = False
                info_path = ""
                if file_ext not in extension_list:
                    continue

                if os.path.isfile(os.path.join(root, file_name + '.txt')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.txt')
                elif os.path.isfile(os.path.join(root, file_name + '.md')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.md')

                formatted_name = ""
                if platform.system() == 'Windows':
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion\\', '')
                else:
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion/', '')

                if not found_file:
                    embedding_needing_hash.append({
                        'name': formatted_name,
                        'filename': os.path.join(root, file),
                        'filenameNoExt': file_name,
                        'rootDir': root
                    })
                else:
                    embedding_list.append({
                        'name': formatted_name,
                        'filename': info_path,
                    })

    if os.path.exists(base_dir + 'models/VAE'):
        extension_list = ['.bin', '.pt']
        for root, dirs, files in os.walk(base_dir + 'models/VAE'):
            for file in files:
                file_path = os.path.join(root, file)

                file_name, file_ext = os.path.splitext(file)
                if os.path.isfile(os.path.join(root, file_name + '.md')):
                    file_name + '.md'

                found_file = False
                info_path = ""
                if file_ext not in extension_list:
                    continue

                if os.path.isfile(os.path.join(root, file_name + '.txt')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.txt')
                elif os.path.isfile(os.path.join(root, file_name + '.md')):
                    found_file = True
                    info_path = os.path.join(root, file_name + '.md')

                formatted_name = ""
                if platform.system() == 'Windows':
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion\\', '')
                else:
                    formatted_name = file_path.replace(
                        base_dir + 'models/Stable-diffusion/', '')

                if not found_file:
                    vae_needing_hash.append({
                        'name': formatted_name,
                        'filename': os.path.join(root, file),
                        'filenameNoExt': file_name,
                        'rootDir': root
                    })
                else:
                    vae_list.append({
                        'name': formatted_name,
                        'filename': info_path,
                    })


loadAssets()
# print(checkpoint_needing_hash)


def getJson(hash):
    url = 'https://civitai.com/api/v1/model-versions/by-hash/' + hash
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        print(
            f"Model request for {hash} failed with status code {response.status_code}")
        return None


def iterate_missing_list(target_list, asset_path):
    for asset in target_list:
        print('Hashing', asset['filename'])
        with open(os.path.join(asset_path, asset['filename']), 'rb') as f:
            file_contents = f.read()
            hash = hashlib.sha256(file_contents).hexdigest()
            data = getJson(hash)
            # data = getJson('9aba26abdfcd46073e0a1d42027a3a3bcc969f562d58a03637bf0a0ded6586c9')
            if data is None:
                print('Failed to get info for ' + asset['filename'], '\n')
                continue

            info_output = f"# [{data['model']['name']}](https://civitai.com/models/{data['modelId']}) ({data['model']['type']})\n\n"

            if data['baseModel'] is not None:
                info_output += f"## Base Model: **{data['baseModel']}**\n\n"

            if data['trainedWords'] is not None and len(data['trainedWords']):
                info_output += '## Trigger Words\n\n'
                for word in data['trainedWords']:
                    info_output += f"* {word}\n"
                info_output += '\n'

            if data['description'] is not None:
                info_output += f"## Description\n\n{html2text.html2text(data['description'])}\n\n"

            if data['images'] is not None and len(data['images']):
                print('Saving image',
                      f"{asset['rootDir']}/{asset['filenameNoExt']}.preview.png")
                imgresponse = requests.get(data['images'][0]['url'])
                if imgresponse.status_code:
                    fp = open(
                        f"{asset['rootDir']}/{asset['filenameNoExt']}.preview.png", 'wb')
                    fp.write(imgresponse.content)
                    fp.close()

                for index, image in enumerate(data['images']):
                    example_prompt = ""
                    if image['meta'] is None:
                        continue
                    if 'prompt' not in image['meta']:
                        continue
                    if index == 0:
                        info_output += '## Example Prompts\n\n'
                    example_prompt += f"\n\n### [Prompt #{index + 1}]({image['url']})\n\n"
                    example_prompt += f"> {image['meta']['prompt']}\n>\n"
                    if 'negativePrompt' in image['meta'] and image['meta']['negativePrompt'] is not None:
                        example_prompt += f"> Negative prompt: {image['meta']['negativePrompt']}\n>\n"
                    if 'seed' in image['meta'] and image['meta']['seed'] is not None:
                        example_prompt += f"> Seed: {image['meta']['seed']}, CFG Scale: {image['meta']['cfgScale']}, Steps: {image['meta']['steps']}, Sampler{image['meta']['steps']}"
                    if 'Clip skip' in image['meta']:
                        example_prompt += f", Clip Skip: {image['meta']['Clip skip']}"
                    example_model_data = None
                    if 'Model hash' in image['meta']:
                        example_model_data = getJson(
                            image['meta']['Model hash'])
                    if (example_model_data is not None):
                        example_prompt += f">\n>\n> Model: [{example_model_data['model']['name']}/{example_model_data['name']}](https://civitai.com/models/{example_model_data['modelId']}) \n\n"
                    info_output += example_prompt

            info_output = info_output.rstrip("\n")

            print('Writing', f"{asset['rootDir']}/{asset['filenameNoExt']}.md")
            with open(f"{asset['rootDir']}/{asset['filenameNoExt']}.md", "w") as file:
                file.write(info_output)
            print('\n')


print('Checking checkpoints...')
iterate_missing_list(checkpoint_needing_hash, os.path.join(
    base_dir + '/models/Stable-diffusion'))

print('\nChecking embeddings...')
iterate_missing_list(embedding_needing_hash,
                      os.path.join(base_dir + 'embeddings'))

print('\nChecking hypernetworks...')
iterate_missing_list(hypernetwork_needing_hash,
                      os.path.join(base_dir + 'models/hypernetworks'))

print('\nChecking loras...')
iterate_missing_list(lora_needing_hash, os.path.join(base_dir + 'models/Lora'))

print('\nChecking vaes...')
iterate_missing_list(vae_needing_hash, os.path.join(base_dir + 'models/VAE'))
