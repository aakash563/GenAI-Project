# pip install gradio
# pip install pdfplumber
# pip install pypdf
# pip install langchain
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
import gradio as gr
import pdfplumber

api_key = 'AIzaSyDYXGPlBg1NpgSWOEAXHDYdqjyIg1NDnwA' # get this free api key from https://makersuite.google.com/

llm = GooglePalm(google_api_key=api_key, temperature=0.1)

def extract_text(file_path):
    with open(file_path, 'rb') as f:
        pdf = pdfplumber.open(f)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        prompt_template = PromptTemplate.from_template("""

        **Q:** Make important notes and extract important information from the given below PDF text that is asked in any competitive exam.

        **PDF Text:**

        ```
        {PDF_text}
        ```

        **A:**

        ```
        [Notes and important information]
        ```"""
        )
        prompt = prompt_template.format(PDF_text=text)
        return llm(prompt)
demo = gr.Interface(
    fn=extract_text,
    inputs="file",
    outputs="text",
    description="Extract Important inforamtion from PDF file",
    )

demo.launch(debug=True)