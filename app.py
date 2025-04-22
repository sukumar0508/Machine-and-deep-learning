from flask import Flask, request, send_file
import os
from generate_image import generate_image

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <body>
                <h2>Upload an Image for Anime Style Generation</h2>
                <form action="/generate" method="post" enctype="multipart/form-data">
                    <input type="file" name="image" />
                    <input type="submit" value="Generate Image" />
                </form>
            </body>
        </html>
    '''

@app.route('/generate', methods=['POST'])
def generate():
    if 'image' not in request.files:
        return 'No file part', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    # Save the uploaded file temporarily
    input_path = os.path.join('uploads', file.filename)
    file.save(input_path)

    # Define the output path for the generated image
    output_path = os.path.join('generated_images', 'output.png')

    # Generate the anime-style image
    style = 'Hayao'  # You can specify the style here
    generate_image(input_path, output_path, style)

    # Send the generated image back to the user
    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    # Create necessary directories if they don't exist
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('generated_images', exist_ok=True)
    
    app.run(debug=True)
