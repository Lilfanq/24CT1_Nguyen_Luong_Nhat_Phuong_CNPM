import gradio as gr

def build_ui():
    with gr.Blocks(title="Yêu cầu nhận thức 1 - CNPM DAU") as demo:
        gr.Markdown("# YÊU CẦU NHẬN THỨC 1")
        gr.Markdown("### Hướng phát triển: Phát triển ứng dụng AI")
        gr.Markdown("---")
        
        # Nội dung gốc
        output_text = gr.Textbox(
            label="Thông báo hệ thống", 
            value="Chào bạn khóa 24CT đến với học phần CNPM- DAU",
            interactive=False
        )
    return demo