#!/usr/bin/bash

echo "initilzing virtual environment..."
python -m venv venv
source venv/Scripts/activate

echo "preparing files and directories..."
echo 'from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)' > main.py

mkdir templates
cd templates || exit
echo '<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="static/css/styles.css" />
    <title>Flask App</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>' > index.html

cd ..

mkdir static
cd static || exit

mkdir css
cd css || exit
echo 'body {
    background-color: #232323;
    color: #fff;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
    font-family: sans-serif;
}' > styles.css

cd ..
mkdir assets
cd ..

echo "installing packages..."
echo ""
pip install Flask
export FLASK_APP=main.py

echo "opening pycharm"
# add pycharm to .zshrc
pycharm .
