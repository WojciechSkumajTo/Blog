from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        'author': 'Wojciech Dolowy',
        'title': 'Blog post 1',
        'content': 'First content',
        'date_posted': 'April, 20, 2023',
    },

    {
        'author': 'Marcin Musk',
        'title': 'Blog post 2',
        'content': 'SpaceX',
        'date_posted': 'May, 1, 2023',
    },

    {   'author': 'Mentzen',
        'title': 'Tips',
        'content': 'Easy solve problem',
        'date_posted': 'June, 22, 2022',
    }
]



@app.route('/')
def hello():
    return render_template('home.html', posts=posts)



@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)



