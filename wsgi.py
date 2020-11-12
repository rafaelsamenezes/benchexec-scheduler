from scheduler import create_app

# TODO: Create a JSON for this config
config = {}
config["TESTING": False]
config["DATABASE": "/tmp/database.file"]
config["APPLICATION_ROOT": "/benchexec"]

app = create_app(config)

if __name__ == "__main__":
    app.run()