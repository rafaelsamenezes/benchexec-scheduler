from scheduler import create_app

if __name__ == "__main__":
    # TODO: Create a JSON for this config
    app = create_app({"TESTING": False})
    app.run()