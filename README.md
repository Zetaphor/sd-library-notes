# sd-library-notes

## Note: This is broken with the latest release of Automatic1111 on March 25'th. This update broke a LOT of extensions. I'm working on a fix. [See this reddit post for more details](https://www.reddit.com/r/StableDiffusion/comments/121kqkd/psa_hold_up_with_updating_automatic1111_for_now/).

Extension for Automatic1111 Stable Diffusion WebUI to display information from text or markdown files for all of your custom assets. It also supports general notes so you can easily reference your stable diffusion documentation.

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

### General Notes

The extension also includes a general notes section, which can be accessed by selecting "General Notes" from the asset type dropdown menu. The extension will search for markdown or text files in the `notes` folder in your Automatic1111 installation directory, and any files found will appear in the dropdown menu below the asset type selection.

## Installation

1. From the extensions tab in web ui click install from url
2. Paste `https://github.com/Zetaphor/sd-library-notes` into the url box.
3. Click Install
4. from the Installed tab click apply and restart.

![image](https://user-images.githubusercontent.com/3112763/222820664-edaebedd-09a4-4290-8354-f3141c701a13.png)

TODO:

- [ ] Refresh button
- [ ] Image previews
- [ ] Move to right side of UI, make an optional setting?
- [ ] In-UI editing/saving/creation
