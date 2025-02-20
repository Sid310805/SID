from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials (for testing)
USER_CREDENTIALS = {"admin": "password123"}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            return redirect(url_for("home"))  # Redirect to home page if login is successful
        else:
            return render_template("login.html", error="Invalid username or password")
    
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
