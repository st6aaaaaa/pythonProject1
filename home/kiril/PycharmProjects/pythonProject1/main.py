from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intro = db.Column(db.String(300), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(300), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/')
@app.route('/home')
def index():
    return render_template("in.html")

@app.route('/elixir.html')
def about():
    return render_template("elixir.html")


@app.route('/my.html')
def myf():
  return render_template("my.html")

@app.route('/elixir.html')
def elixir():
    return render_template("elixir.html")

@app.route('/lounge.html')
def melix():
    return render_template("lounge.html")

@app.route('/directions.html')
def dr():
    return render_template("directions.html")


@app.route('/posts')
def posts():
    articles= Article.query.order_by(Article.date.desc()).all()
    return render_template("posts.html",articles=articles)

@app.route('/posts/<int:id>')
def posts_detail(id):
    article= Article.query.get(id)
    return render_template("post_detail.html",article=article)

@app.route('/create-article',methods=['POST','GET'])
def create_article():
    if request.method =="POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro =intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "при добавлении статьи произошла ошибка"
    else:
        return render_template("create-article.html")


if __name__=="__main__":
    app.run(debug=True)