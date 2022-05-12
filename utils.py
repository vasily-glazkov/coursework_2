import json

COMMENTS = "data/comments.json"
POSTS_DATA = "data/data.json"

def load_data(PATH):
    
    """Returns data form json file

    Returns:
        list: list of dictionaries
    """
    
    with open(PATH, encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_posts_by_user(user_name, data):
    """Returns posts by user name

    Args:
        user_name (str)
        data (list)
        Takes an username and returns all posts associated with that user from the data
    """
    return [post for post in data if user_name in post["poster_name"].lower() ]


def get_comments_by_post_id(post_id, data):
    
    """Returns comments by post id

    Returns:
        list: list of dict
    """ 
    
    comments = []
    
    for comment in data:
        if post_id == comment["post_id"]:
            comments.append(comment)
    
    return comments


def search_for_posts(query, data):
    """Searches for a keyword in posts and returns relevant post(s) """
    results = []
    for post in data:
        if query.lower() in post['content'].lower() or query in post['content']:
            results.append(post)
    if len(results) > 0:
        return results
    else:
        return None


def get_post_by_pk(pk, data):
    """Searches for the post with unique id (pk)"""
    results = [post for post in data if str(pk) in str(post["pk"]) ]
    if len(results) > 0:
        return results
    else:
        return None


