
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Flask CI/CD Application</title>
    </head>
    <body style="text-align:center; background-color:lightblue; padding:100px;">
        <h1>Welcome to Flask CI/CD Pipeline!</h1>
        <h2>GitHub Actions and Docker</h2>
        <p>Application deployed successfully.</p>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
