from flask import Flask, render_template, request

app = Flask(__name__)

def binary_to_text(binary_str):
    # Split binary string into 8-bit chunks
    chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

    # Convert each 8-bit chunk to decimal and then to character
    text = ''.join([chr(int(chunk, 2)) for chunk in chunks])

    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        binary_input = request.form['binary_input'].replace(" ", "")
        text_output = binary_to_text(binary_input)
        return render_template('index.html', text_output=text_output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
