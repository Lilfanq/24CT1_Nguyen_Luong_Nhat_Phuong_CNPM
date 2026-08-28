from ui.app import build_ui

if __name__ == "__main__":
    app = build_ui()
    # Khởi chạy server
    app.launch(server_name="127.0.0.1")