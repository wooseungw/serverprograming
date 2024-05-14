import gradio as gr

#어떤 파일을 열 때 with 블록을 사용하면, 그 블록이 끝나면 파일이 자동으로 닫힌다.
#그래서 메모리 누수를 막을 수 있어 권장된다.
with gr.Blocks() as demo:
    html = """
        <h3>Hello, world!</h3>
        <a href="http://www.google.com">google</a>
        
    """
    gr.HTML("<h1>Hello, world!</h1>")
    gr.HTML("<h2>Hello, world!</h2>")
    gr.HTML(html)
    gr.Markdown("# Hello, world!")
    gr.Markdown("## Hello, world!")
    gr.Markdown("### Hello, world!")
    gr.Markdown("- Hello, world!")
    gr.Markdown("+ Hello, world!")
    gr.Markdown(" **Hello, world!**")
    
    
if __name__ == "__main__":   
    demo.launch()