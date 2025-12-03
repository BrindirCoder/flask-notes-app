from app import create_note_app
app = create_note_app()

if __name__ == "__main__":
    app.run(host="localhost", port=5555, debug=True)
