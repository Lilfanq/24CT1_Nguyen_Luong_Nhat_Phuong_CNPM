import gradio as gr

# Hàm xử lý giao diện
def chao_mung():
    return "Chào bạn khóa 24CT đến với học phần CNPM- DAU"

# Tạo giao diện Web
with gr.Blocks(title="Yêu cầu nhận thức 1 - CNPM DAU") as demo:
    gr.Markdown("# YÊU CẦU NHẬN THỨC 1")
    gr.Markdown("### Hướng phát triển: Phát triển ứng dụng AI")
    gr.Markdown("---")
    
    # Nội dung
    output_text = gr.Textbox(
        label="Thông báo hệ thống", 
        value="Chào bạn khóa 24CT đến với học phần CNPM- DAU",
        interactive=False
    )
demo.launch(server_name="127.0.0.1", server_port=7860)
# Chạy ứng dụng 
#pip install torch gradio
#pip freeze > requirements.txt
#python main.py