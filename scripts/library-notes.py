import contextlib
from pathlib import Path
import gradio as gr
import modules.scripts as scripts
import os

base_dir = scripts.basedir()
refresh_symbol = '\U0001f504'  # 🔄


class LibraryNotes(scripts.Script):

    checkpoint_list = []
    vae_list = []
    embedding_list = []
    hypernetwork_list = []
    lora_list = []

    def title(self):
        return "Library Notes"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def loadLibraryNotes(self, *args, **kwargs):
        if os.path.exists('models/Stable-diffusion'):
            extension_list = ['.safetensors', '.ckpt']
            for root, dirs, files in os.walk('models/Stable-diffusion'):
                for file in files:
                    file_path = os.path.join(root, file)

                    file_name, file_ext = os.path.splitext(file)
                    if os.path.isfile(os.path.join(root, file_name + '.md')):
                        file_name + '.md'

                    found_file = False
                    info_path = ""
                    if file_ext in extension_list:
                        if os.path.isfile(os.path.join(root, file_name + '.txt')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.txt')
                        elif os.path.isfile(os.path.join(root, file_name + '.md')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.md')

                    if found_file:
                        display_name = file_path.replace(
                            'models/Stable-diffusion\\', '')
                        formatted_name = display_name.replace("\\\\", "\\")

                        LibraryNotes.checkpoint_list.append({
                            'name': formatted_name,
                            'filename': info_path
                        })

        if os.path.exists('models/hypernetworks'):
            extension_list = ['.pt']
            for root, dirs, files in os.walk('models/hypernetworks'):
                for file in files:
                    file_path = os.path.join(root, file)

                    file_name, file_ext = os.path.splitext(file)
                    if os.path.isfile(os.path.join(root, file_name + '.md')):
                        file_name + '.md'

                    found_file = False
                    info_path = ""
                    if file_ext in extension_list:
                        if os.path.isfile(os.path.join(root, file_name + '.txt')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.txt')
                        elif os.path.isfile(os.path.join(root, file_name + '.md')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.md')

                    if found_file:
                        display_name = file_path.replace(
                            'models/hypernetworks\\', '')
                        formatted_name = display_name.replace("\\\\", "\\")

                        LibraryNotes.hypernetwork_list.append({
                            'name': formatted_name,
                            'filename': info_path
                        })

        if os.path.exists('models/Lora'):
            extension_list = ['.safetensors', '.pt']
            for root, dirs, files in os.walk('models/Lora'):
                for file in files:
                    file_path = os.path.join(root, file)

                    file_name, file_ext = os.path.splitext(file)
                    if os.path.isfile(os.path.join(root, file_name + '.md')):
                        file_name + '.md'

                    found_file = False
                    info_path = ""
                    if file_ext in extension_list:
                        if os.path.isfile(os.path.join(root, file_name + '.txt')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.txt')
                        elif os.path.isfile(os.path.join(root, file_name + '.md')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.md')

                    if found_file:
                        display_name = file_path.replace(
                            'models/Lora\\', '')
                        formatted_name = display_name.replace("\\\\", "\\")

                        LibraryNotes.lora_list.append({
                            'name': formatted_name,
                            'filename': info_path
                        })

        if os.path.exists('embeddings'):
            extension_list = ['.bin', '.pt']
            for root, dirs, files in os.walk('embeddings'):
                for file in files:
                    file_path = os.path.join(root, file)

                    file_name, file_ext = os.path.splitext(file)
                    if os.path.isfile(os.path.join(root, file_name + '.md')):
                        file_name + '.md'

                    found_file = False
                    info_path = ""
                    if file_ext in extension_list:
                        if os.path.isfile(os.path.join(root, file_name + '.txt')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.txt')
                        elif os.path.isfile(os.path.join(root, file_name + '.md')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.md')

                    if found_file:
                        display_name = file_path.replace(
                            'embeddings\\', '')
                        formatted_name = display_name.replace("\\\\", "\\")

                        LibraryNotes.embedding_list.append({
                            'name': formatted_name,
                            'filename': info_path
                        })

        if os.path.exists('models/VAE'):
            extension_list = ['.bin', '.pt']
            for root, dirs, files in os.walk('models/VAE'):
                for file in files:
                    file_path = os.path.join(root, file)

                    file_name, file_ext = os.path.splitext(file)
                    if os.path.isfile(os.path.join(root, file_name + '.md')):
                        file_name + '.md'

                    found_file = False
                    info_path = ""
                    if file_ext in extension_list:
                        if os.path.isfile(os.path.join(root, file_name + '.txt')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.txt')
                        elif os.path.isfile(os.path.join(root, file_name + '.md')):
                            found_file = True
                            info_path = os.path.join(root, file_name + '.md')

                    if found_file:
                        display_name = file_path.replace(
                            'models/VAE\\', '')
                        formatted_name = display_name.replace("\\\\", "\\")

                        LibraryNotes.vae_list.append({
                            'name': formatted_name,
                            'filename': info_path
                        })

        # print('VAE', self.vae_list, '\n\n')
        # print('TIs', self.embedding_list, '\n\n')
        # print('checkpoints', self.checkpoint_list, '\n\n')
        # print('hypernetworks', self.hypernetwork_list, '\n\n')
        # print('loras', self.lora_list, '\n\n')

    def dropdown(self, dictList, *args, **kwargs):
        options = []
        for item in dictList:
            options.append(item["name"])
        return options

    def ui(self, is_img2img):
        self.loadLibraryNotes()
        with gr.Accordion(label="Library Notes", open=False, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_accordion"):
            with gr.Tab(label="Textual Inversions"):
                with gr.Row():
                    list_embeddings = gr.Dropdown(label="Select Embedding", choices=self.dropdown(
                        LibraryNotes.embedding_list), interactive=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_embedding_selection")
                with gr.Row():
                    with gr.Accordion(label="Embedding Notes", open=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_embedding_info_accordion"):
                        info_output = gr.Markdown(
                            "Embedding notes will display here")
                list_embeddings.change(
                    fn=self.show_embedding_info, inputs=[list_embeddings], outputs=[info_output])

            with gr.Tab(label="Hypernetworks"):
                with gr.Row():
                    list_hypernetworks = gr.Dropdown(label="Select Hypernetwork", choices=self.dropdown(
                        LibraryNotes.hypernetwork_list), interactive=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_hyper_selection")
                with gr.Row():
                    with gr.Accordion(label="Hypernetwork Notes", open=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_hyper_info_accordion"):
                        info_output = gr.Markdown(
                            "Hypernetwork notes will display here")
                list_hypernetworks.change(
                    fn=self.show_hypernetwork_info, inputs=[list_hypernetworks], outputs=[info_output])

            with gr.Tab(label="Checkpoints"):
                with gr.Row():
                    list_checkpoints = gr.Dropdown(label="Select Checkpoint", choices=self.dropdown(
                        LibraryNotes.checkpoint_list), interactive=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_checkpoint_selection")
                with gr.Row():
                    with gr.Accordion(label="Checkpoint Notes", open=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_checkpoint_info_accordion"):
                        info_output = gr.Markdown(
                            "Checkpoint notes will display here")
                list_checkpoints.change(
                    fn=self.show_checkpoint_info, inputs=[list_checkpoints], outputs=[info_output])

            with gr.Tab(label="Lora"):
                with gr.Row():
                    list_loras = gr.Dropdown(label="Select Lora", choices=self.dropdown(
                        LibraryNotes.lora_list), interactive=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_lora_selection")
                with gr.Row():
                    with gr.Accordion(label="Lora Notes", open=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_lora_info_accordion"):
                        info_output = gr.Markdown(
                            "Lora notes will display here")
                list_loras.change(
                    fn=self.show_lora_info, inputs=[list_loras], outputs=[info_output])

            with gr.Tab(label="VAE"):
                with gr.Row():
                    list_vaes = gr.Dropdown(label="Select VAE", choices=self.dropdown(
                        LibraryNotes.vae_list), interactive=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_vae_selection")
                with gr.Row():
                    with gr.Accordion(label="VAE Notes", open=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_vae_info_accordion"):
                        info_output = gr.Markdown(
                            "VAE notes will display here")
                list_vaes.change(
                    fn=self.show_vae_info, inputs=[list_vaes], outputs=[info_output])
            with gr.Tab(label="About"):
                gr.Markdown("## <center>Library Info</center> \
                  \nThis extension is designed to help you keep track of prompts, trigger words, and general information for all of your Stable Diffusion assets. \
                  Create a text or markdown file (.txt or .md) in the folder with your asset and give the file the exact same name as the asset. \
                  \n\nFor example to create a document for \"example.safetensors\" would mean you create another file named \"example.txt\" or \"example.md\" \
                  This file will then be recognized by the extension and shown to you in the dropdown matching that asset type. \
                  \n\nThe following asset types are supported: \
                  \n| Asset Type         | Folder                  | Extension(s)        | \
                  \n|--------------------|-------------------------|---------------------| \
                  \n| Checkpoint         | models/Stable-diffusion | .safetensors, .ckpt | \
                  \n| Lora               | models/Lora             | .safetensors, .pt   | \
                  \n| Textual Inversions | embeddings              | .bin, .pt           | \
                  \n| Hypernetworks      | models/hypernetworks    | .pt                 | \
                  \n| VAE                | models/VAE              | .safetensors, .pt   | \
                  \n\n Any content loaded from the notes file will be rendered with full markdown. \
                  \nThis means you can use rich text formatting in your asset documentation!\
                ")

    def show_embedding_info(self, filename):
        output_text = ""
        for item in LibraryNotes.embedding_list:
            if item['name'] == filename:
                output_text = self.get_note_data(item['filename'])
                break
        txt_update = gr.Markdown.update(value=output_text)
        return txt_update

    def show_checkpoint_info(self, filename):
        output_text = ""
        for item in LibraryNotes.checkpoint_list:
            if item['name'] == filename:
                output_text = self.get_note_data(item['filename'])
                break
        txt_update = gr.Markdown.update(value=output_text)
        return txt_update

    def show_vae_info(self, filename):
        output_text = ""
        for item in LibraryNotes.vae_list:
            if item['name'] == filename:
                output_text = self.get_note_data(item['filename'])
                break
        txt_update = gr.Markdown.update(value=output_text)
        return txt_update

    def show_lora_info(self, filename):
        output_text = ""
        for item in LibraryNotes.lora_list:
            if item['name'] == filename:
                output_text = self.get_note_data(item['filename'])
                break
        txt_update = gr.Markdown.update(value=output_text)
        return txt_update

    def show_hypernetwork_info(self, filename):
        output_text = ""
        for item in LibraryNotes.hypernetwork_list:
            if item['name'] == filename:
                output_text = self.get_note_data(item['filename'])
                break
        txt_update = gr.Markdown.update(value=output_text)
        return txt_update

    def get_note_data(self, filename):
        file_contents = ""
        with open(filename, 'r') as file:
            for line in file:
                file_contents = f'{file_contents}{line.strip()}\n'
        return file_contents
