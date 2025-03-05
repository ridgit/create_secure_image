from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def serialize(self):
       return {
           'id': self.id,
           'title': self.title,
           'content': self.content
       }

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = Blog(title=data['title'], content=data['content'])
    db.session.add(post)
    db.session.commit()
    return jsonify(post.serialize()), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Blog.query.all()
    return jsonify([post.serialize() for post in posts]), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
