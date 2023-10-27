from flask import Flask, render_template, request
from bardapi import Bard
import os

app = Flask(__name__)

# Set your Bard API key
os.environ['_BARD_API_KEY'] = "cQglfdYUp7aw3ZlGaBJe2s7n77VkF2rGuZ-P_Xra6oQqOH_oIYmZbIbOv04WdKwZjCehog."

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    username = request.form['username']
    specimen_name = request.form['specimen_name']
    relation = request.form['relation']
    qualities = request.form['qualities']
    content_type = request.form['content_type']

    input_text = f"Dear {relation}, I would like to express my heartfelt {content_type} for {specimen_name}. {qualities}. Sincerely, {username}"

    generated_content = Bard().get_answer(input_text)['content']

    return render_template('result.html', generated_content=generated_content)

if __name__ == '__main__':
    app.run(debug=True)
