// Play Trailer Button
function playTrailer() {
    window.open("https://www.youtube.com/watch?v=b9EkMc79ZSU", "_blank");
}

// More Info Button
function showInfo() {
    window.open("https://en.wikipedia.org/wiki/Stranger_Things", "_blank");
    // alert("Stranger Things: A group of kids uncover a mystery involving secret experiments and supernatural forces.");
}

// URLs for each image
const urls = {
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
};

// Titles for each image
const titles = {
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
};

// Image Click Handler
function openWebsite(imageId) {
    const url = urls[imageId];
    if (url) {
        window.open(url, "_blank");
    } else {
        console.error('URL not found for image ID:', imageId);
    }
}

// Function to get movie title
function getMovieTitle(imageId) {
    return titles[imageId] || 'Unknown Title';
}

// Smooth Scrolling for Navbar Links
document.querySelectorAll('nav ul li a').forEach(anchor => {
    anchor.addEventListener('click', function (event) {
        event.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
