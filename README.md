# sd-library-notes

Extension for Automatic1111 Stable Diffusion WebUI to display information from text or markdown files for all of your custom assets.

## About

This extension is designed to help you keep track of prompts, trigger words, and general information for all of your Stable Diffusion assets.
Create a text or markdown file (.txt or .md) in the folder with your asset and give the file the exact same name as the asset.

For example to create a document for"example.safetensors\" would mean you create another file named "example.txt" or "example.md"
This file will then be recognized by the extension and shown to you in the dropdown matching that asset type.

The following asset types are supported:

| Asset Type         | Folder                  | Extension(s)        |
| ------------------ | ----------------------- | ------------------- |
| Checkpoint         | models/Stable-diffusion | .safetensors, .ckpt |
| Lora               | models/Lora             | .safetensors, .pt   |
| Textual Inversions | embeddings              | .bin, .pt           |
| Hypernetworks      | models/hypernetworks    | .pt                 |
| VAE                | models/VAE              | .safetensors, .pt   |

Any content loaded from the notes file will be rendered with full markdown.
This means you can use rich text formatting in your asset documentation!

## Installation

1. From the extensions tab in web ui click install from url
2. Paste `https://github.com/Zetaphor/sd-library-notes` into the url box.
3. Click Install
4. from the Installed tab click apply and restart.

This screenshot was from development and so it doesn't show the markdown functionality:
![image](https://user-images.githubusercontent.com/3112763/221681151-0104a366-27cc-41a0-a044-91e012d60902.png)



TODO:

- [ ] Refresh button
- [ ] Image previews
- [ ] Move to right side of UI, how is Preset Manager doing this?
- [ ] Code cleanup
- [ ] In-UI editing/saving/creation

