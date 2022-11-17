from pTest_scheduler import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8088"), debug=True)
