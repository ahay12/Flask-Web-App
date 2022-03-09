from website import create_app

app = create_app()

if __name__ == "__main__":
    app.secret_key = "secret"
    
    app.run(debug=True)