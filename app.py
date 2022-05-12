from flask import Flask, render_template, request, jsonify, json
from utils import *

app = Flask(__name__)

data = load_data(POSTS_DATA)
comments = load_data(COMMENTS)


@app.route('/')
def index():
    posts = load_data(POSTS_DATA)
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:uid>")
def post_page(uid):
    comments_ = get_comments_by_post_id(uid, comments)
    post = get_post_by_pk(uid, data)
    return render_template('post.html', comments=comments_, post=post)


@app.route("/users/<username>/")
def user_feed_page(username):
    user_feed = get_posts_by_user(username, data)

    return render_template('user-feed.html', posts=user_feed, username=username)


@app.route('/search/', methods=['GET', 'POST'])
def search_page():
    query = request.args.get('s')
    query_not_found = "Ничего не нашлось"
    if query:
        query_result = search_for_posts(query, data)
        if type(query_result) == list:
            if len(query_result) > 10:
                query_result = query_result[0:10]
                return render_template('search.html', s=query, query_result=query_result)
            return render_template('search.html', s=query, query_result=query_result)
    return render_template("search.html", query_not_found=query_not_found)


@app.route("/api/posts")
def index_test():
    return json.dumps(data, ensure_ascii=False)


@app.route("/api/posts/<int:uid>")
def post_page_test(uid):
    post = get_post_by_pk(uid, data)
    return json.dumps(post, ensure_ascii=False)
