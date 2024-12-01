from gpt4all import GPT4All
import gradio as gr
from assisting_functions import *
with gr.Blocks() as app:

    gr.Markdown("## Welcome to the EU AI Act Assistant!")
    gr.Markdown("This is currently only applicable to Chapter III of the EU AI Act on High-Risk AI Systems. Created for the LAW4032 course at SMU.")

    with gr.Row():

        with gr.Column():
            gr.Markdown("## .pdf Conversion")
            my_file = gr.File(
                label="Upload your .pdf file here!",
                file_types=[".pdf"],
                type="filepath",
                scale=2
            )

        compliance_query = gr.TextArea(
            label="Your document will appear here!",
            scale=2
        )
        with gr.Column():
            gr.Markdown("## .docx Conversion")
            docx_file = gr.File(
                label="Upload your .docx file here!",
                file_types=[".docx"],
                type="filepath",
                scale=2
            )
        my_file.upload(fn=process_file, inputs=my_file, outputs=compliance_query)
        docx_file.upload(fn=get_docx_text, inputs=docx_file, outputs=compliance_query)

    with gr.Row():

        check_button = gr.Button("Submit")
        final_output = gr.TextArea(
            label="Your results will appear here!",
            scale=2
        )

        check_button.click(fn=test_models, inputs=[compliance_query], outputs=final_output)


app.launch(debug=True)