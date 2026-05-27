import gradio as gr
from config import openai
from ai import ask_ai
from analytics import get_summary, provider_usage_chart, response_time_chart, get_dataframe

provider_models = {
    "OpenAI": [
        "gpt-5-mini",
        "gpt-4o-mini",
        "gpt-4o"
    ],
    "Google": [
        "gemini-2.5-flash",
        "gemini-2.5-pro"
    ],
    "Claude": [
        "claude-sonnet-4-5",
        "claude-haiku-4-5"
    ]
}


def update_model_dropdown(selected_provider):
    models = provider_models[selected_provider]

    return gr.update(
        choices=models,
        value=models[0]
    )

def put_message_in_chatbot(message, history):
    return "", history + [{'role': 'user', 'content': message}]

def transcribe_audio(audio_path):
    if audio_path is None:
        return ""
    
    with open(audio_path, 'rb') as audio_file:
        transcript = openai.audio.transcriptions.create(
            model= 'whisper-1',
            file= audio_file
        )

    if not transcript.text.strip():  # In case whisper returned nothing
        return "Could not transcribe audio. Please try again."

    return transcript.text


with gr.Blocks() as demo:

    gr.Markdown('# QueryForge')

    with gr.Tabs():
        
        with gr.Tab('Technical Q&A'):
            
            with gr.Row():

                chatbot = gr.Chatbot(height=500)
                
            with gr.Row():
                provider = gr.Dropdown(
                    choices=list(provider_models.keys()),
                    value="OpenAI",
                    label="Select the Provider",
                    interactive=True
                )

                model = gr.Dropdown(
                    choices=provider_models["OpenAI"],
                    value=provider_models["OpenAI"][0],
                    label="Select the Model",
                    interactive=True
                )

                provider.change(
                    fn=update_model_dropdown,
                    inputs=provider,
                    outputs=model
                )

            with gr.Row():
                audio_input= gr.Audio(
                    sources= ['microphone', 'upload'],
                    type= "filepath",
                    label='Speak or upload audio'
                )

            with gr.Row():
                transcribe_button = gr.Button('Transcribe', variant='secondary', scale=4)

            with gr.Row():

                message = gr.Textbox(label='Enter message', info='Ask your question', scale=5)

                transcribe_button.click(
                    fn=transcribe_audio,
                    inputs=audio_input,
                    outputs=message
                
                ).then(
                    fn=put_message_in_chatbot,
                    inputs=[message, chatbot],
                    outputs=[message, chatbot]
                ).then(
                    fn=ask_ai,
                    inputs=[provider, model, chatbot],
                    outputs=[chatbot]
                )

                message.submit(put_message_in_chatbot, inputs=[message, chatbot], outputs=[message, chatbot]).then(
                    fn=ask_ai, inputs=[provider, model, chatbot], outputs=[chatbot]
                )

    

        with gr.Tab('Analytics'):
            refresh_button = gr.Button('Refresh Analytics')

            summary_output = gr.Markdown()
            provider_plot = gr.Plot(label='Provider Usage')
            response_time_plot = gr.Plot(label='Response Time over Interactions')
            analytics_table = gr.DataFrame(label='Interaction History')

            refresh_button.click(
                fn=lambda: (
                    get_summary(),
                    provider_usage_chart(),
                    response_time_chart(),
                    get_dataframe()
                ),
                inputs=None,
                outputs=[
                    summary_output,
                    provider_plot,
                    response_time_plot,
                    analytics_table
                ]


            )

demo.launch(inbrowser=True)