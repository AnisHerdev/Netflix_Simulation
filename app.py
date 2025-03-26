"""
This module implements the backend for the Netflix-inspired frontend project.
It includes routes for playing trailers, showing movie info, and retrieving movie details.
"""

from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='.', static_url_path='', template_folder='.')

# URLs for each image
urls = {
    'T1': 'https://example.com/trending1',
    'T2': 'https://example.com/trending2',
    'T3': 'https://example.com/trending3',
    'T4': 'https://example.com/trending4',
    'T5': 'https://example.com/trending5',
    'A1': 'https://example.com/action1',
    'A2': 'https://www.youtube.com/watch?v=NOhDyUmT9z0',
    'A3': 'https://example.com/action3',
    'A4': 'https://www.youtube.com/watch?v=j7jPnwVGdZ8',
    'A5': 'https://example.com/action5',
    'D1': 'https://example.com/drama1',
    'D2': 'https://www.youtube.com/watch?v=dlnmQbPGuls&pp=ygUQdGhlIHRydSBtYW4gc2hvdw%3D%3D',
    'D3': 'https://example.com/drama3',
    'D4': 'https://example.com/drama4',
    'D5': 'https://example.com/drama5',
    'C1': 'https://example.com/comedy1',
    'C2': 'https://example.com/comedy2',
    'C3': 'https://example.com/comedy3',
    'C4': 'https://example.com/comedy4',
    'C5': 'https://example.com/comedy5'
}

# Titles for each image
titles = {
    'T1': 'Pushpa 2',
    'T2': 'Trending Movie 2',
    'T3': 'Trending Movie 3',
    'T4': 'Captain America',
    'T5': 'Jailer 2',
    'A1': 'Action Movie 1',
    'A2': 'Action Movie 2',
    'A3': 'Action Movie 3',
    'A4': 'Fall Guy',
    'A5': 'John Wick',
    'D1': 'Drama Movie 1',
    'D2': 'Drama Movie 2',
    'D3': 'Interstellar',
    'D4': 'GodFather',
    'D5': 'Shawshank Redemption',
    'C1': 'Comedy Movie 1',
    'C2': 'Comedy Movie 2',
    'C3': 'Comedy Movie 3',
    'C4': 'Comedy Movie 4',
    'C5': 'Comedy Movie 5'
}

@app.route('/')
def index():
    """Render the homepage."""
    return "Welcome to Inflix!"

@app.route('/play-trailer', methods=['GET'])
def play_trailer():
    """Play the trailer for the featured movie."""
    return jsonify({'url': 'https://www.youtube.com/watch?v=b9EkMc79ZSU'})

@app.route('/show-info', methods=['GET'])
def show_info():
    """Show additional information about the featured movie."""
    return jsonify({'url': 'https://en.wikipedia.org/wiki/Stranger_Things'})

@app.route('/get-url/<image_id>', methods=['GET'])
def get_url(image_id):
    """
    Retrieve the URL for a specific movie.

    Args:
        image_id (str): The ID of the movie.

    Returns:
        str: The URL of the movie or a 404 error if not found.
    """
    url = urls.get(image_id)
    if url:
        return jsonify({'url': url})
    return jsonify({'error': 'URL not found'}), 404

@app.route('/get-title/<image_id>', methods=['GET'])
def get_title(image_id):
    """
    Retrieve the title for a specific movie.

    Args:
        image_id (str): The ID of the movie.

    Returns:
        str: The title of the movie or a 404 error if not found.
    """
    title = titles.get(image_id)
    if title:
        return jsonify({'title': title})
    return jsonify({'error': 'Title not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
