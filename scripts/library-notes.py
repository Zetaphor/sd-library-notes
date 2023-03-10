import contextlib
from pathlib import Path
import platform
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
    general_note_list = []

    checkpoint_path = 'models/Stable-diffusion'
    vae_path = 'models/VAE'
    embedding_path = 'embeddings'
    hypernetwork_path = 'models/hypernetworks'
    lora_path = 'models/Lora'
    notes_path = 'notes'

    def title(self):
        return "Library Notes"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def get_general_notes(self, dir_path):
        note_list = []

        if os.path.exists(dir_path):
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_name, file_ext = os.path.splitext(file)
                    if os.path.isfile(os.path.join(root, file_name + '.md')):
                        file_name + '.md'

                    found_file = False
                    info_path = ""

                    if os.path.isfile(os.path.join(root, file_name + '.txt')):
                        found_file = True
                        info_path = os.path.join(root, file_name + '.txt')
                    elif os.path.isfile(os.path.join(root, file_name + '.md')):
                        found_file = True
                        info_path = os.path.join(root, file_name + '.md')

                    if found_file:
                        # formatted_name = Path(file_path).relative_to(dir_path)
                        formatted_name = ""
                        if platform.system() == 'Windows':
                            print(dir_path, file_path)
                            formatted_name = file_path.replace(
                                dir_path + '\\', '')
                        else:
                            formatted_name = file_path.replace(
                                dir_path + '/', '')

                        note_list.append({
                            'name': formatted_name,
                            'filename': info_path
                        })
        note_list = sorted(note_list, key=lambda x: x['name'])
        return note_list

    def pull_note_list(self, dir_path, *extension_list):
        note_list = []
        extension_list = extension_list[0]

        if os.path.exists(dir_path):
            for root, dirs, files in os.walk(dir_path):
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
                        # formatted_name = Path(file_path).relative_to(dir_path)
                        formatted_name = ""
                        if platform.system() == 'Windows':
                            print(dir_path, file_path)
                            formatted_name = file_path.replace(
                                dir_path + '\\', '')
                        else:
                            formatted_name = file_path.replace(
                                dir_path + '/', '')

                        note_list.append({
                            'name': formatted_name,
                            'filename': info_path
                        })
        note_list = sorted(note_list, key=lambda x: x['name'])
        return note_list

    def loadLibraryNotes(self, *args, **kwargs):
        LibraryNotes.checkpoint_list = self.pull_note_list(
            LibraryNotes.checkpoint_path, ['.safetensors', '.ckpt'])
        LibraryNotes.hypernetwork_list = self.pull_note_list(
            LibraryNotes.hypernetwork_path, ['.pt'])
        LibraryNotes.lora_list = self.pull_note_list(
            LibraryNotes.lora_path, ['.safetensors', '.pt'])
        LibraryNotes.embedding_list = self.pull_note_list(
            LibraryNotes.embedding_path, ['.bin', '.pt'])
        LibraryNotes.vae_list = self.pull_note_list(
            LibraryNotes.vae_path, ['.bin', '.pt', '.ckpt', '.safetensors'])
        LibraryNotes.general_note_list = self.get_general_notes(
            LibraryNotes.notes_path)

        # print('VAE', self.vae_list, '\n\n')
        # print('TIs', self.embedding_list, '\n\n')
        # print('checkpoints', self.checkpoint_list, '\n\n')
        # print('hypernetworks', self.hypernetwork_list, '\n\n')
        # print('loras', self.lora_list, '\n\n')
        # print('notes', self.general_note_list, '\n\n')

    def dropdown(self, dictList, *args, **kwargs):
        options = []
        for item in dictList:
            options.append(item["name"])
        return options

    def ui(self, is_img2img):
        self.loadLibraryNotes()
        self.add_ui_components()

    def add_ui_components(self, *args, **kwargs):
        with gr.Accordion(label="Library Notes", open=False, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_accordion"):
            with gr.Tab(label="General Notes"):
                with gr.Row():
                    list_notes = gr.Dropdown(label="Select Note", choices=self.dropdown(
                        LibraryNotes.general_note_list), interactive=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_note_selection")
                with gr.Row():
                    with gr.Accordion(label="Notes", open=True, elem_id=f"{'txt2img' if self.is_txt2img else 'img2img'}_library_notes_note_info_accordion"):
                        info_output = gr.Markdown(
                            "Notes will display here")
                list_notes.change(
                    fn=self.show_note_info, inputs=[list_notes], outputs=[info_output])

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

    def after_component(self, component, **kwargs):
        ele = kwargs.get("elem_id")
        # if ele == "txt2img_generation_info_button" or ele == "img2img_generation_info_button":
        # self.add_ui_components(self)

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

    def show_note_info(self, filename):
        output_text = ""
        for item in LibraryNotes.general_note_list:
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
