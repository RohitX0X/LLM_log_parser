import gradio as gr
from langchain.llms import Ollama

ollama = Ollama(base_url='http://localhost:11434',
model="mistral")

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as text_file:
            content = text_file.read()
            return content
    except Exception as e:
        print(f"Error: {e}")
        return None


def log_parser(inp,file_path):
    # Example usage:
    if(file_path is None):
        file_path = ['./logs/log_3.txt']
        
    print(file_path)
    text_content = read_text_file(file_path[0])
    if text_content is not None:
        fprompt = "you are a log parser , you need to answer questions based on the file content..." + '\n' + "here is the file content:" + '\n' + text_content + '\n' + inp
    r = ollama(fprompt)
    print(r)
    return r 

demo = gr.Interface(fn=log_parser, inputs=["text","files"], outputs="text")
demo.launch(share = True)