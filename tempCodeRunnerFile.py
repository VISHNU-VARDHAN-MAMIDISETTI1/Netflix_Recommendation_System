import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import bs4 as bs
import urllib.request
import pickle
import requests

# Load saved models
clf = pickle.load(open(r'D:\vishnu\Recommendation_system\saved_models\nlp_model.pkl', 'rb'))
vectorizer = pickle.load(open(r'D:\vishnu\Recommendation_system\saved_models\tranform.pkl', 'rb'))

# Globals
data = None
similarity = None

def create_similarity():
    df = pd.read_csv('D:/vishnu/Recommendation_system/datasets/updated_data.csv')
    df['comb'] = df['comb'].fillna('').astype(str)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['comb'])
    sim = cosine_similarity(count_matrix)
    return df, sim

def rcmd(m):
    global data, similarity
    m = m.lower()

    if data is None or similarity is None:
        data, similarity = create_similarity()

    if m not in data['movie_title'].unique():
        return 'Sorry! Try another movie name.'
    else:
        i = data.loc[data['movie_title'] == m].index[0]
        lst = sorted(list(enumerate(similarity[i])), key=lambda x: x[1], reverse=True)[1:11]
        return [data['movie_title'][a] for a, _ in lst]

def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["', '')
    my_list[-1] = my_list[-1].replace('"]', '')
    return my_list

def get_suggestions():
    df = pd.read_csv('D:/vishnu/Recommendation_system/datasets/updated_data.csv')
    return list(df['movie_title'].str.capitalize())

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    suggestions = get_suggestions()
    return render_template('home.html', suggestions=suggestions)

@app.route("/similarity", methods=["POST"])
def similarity_route():
    movie = request.form['name']
    rc = rcmd(movie)
    return rc if isinstance(rc, str) else "---".join(rc)

@app.route("/recommend1", methods=["POST"])
def recommend():
    # Extract fields
    title = request.form['title']
    imdb_id = request.form['imdb_id']
    poster = request.form['poster']
    genres = request.form['genres']
    overview = request.form['overview']
    vote_average = request.form['rating']
    vote_count = request.form['vote_count']
    release_date = request.form['release_date']
    runtime = request.form['runtime']
    status = request.form['status']

    # Recommended movies
    rec_movies = convert_to_list(request.form['rec_movies'])
    rec_posters = convert_to_list(request.form['rec_posters'])
    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}

    # Cast data
    cast_names = convert_to_list(request.form['cast_names'])
    cast_chars = convert_to_list(request.form['cast_chars'])
    cast_profiles = convert_to_list(request.form['cast_profiles'])
    cast_ids = request.form['cast_ids'].replace('[', '').replace(']', '').split(',')
    casts = {cast_names[i]: [cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_names))}

    # IMDb review scraping
    reviews_list, reviews_status = [], []
    if imdb_id:
        url = f'https://www.imdb.com/title/{imdb_id}/reviews?ref_=tt_ov_rt'
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            page_content = response.content
        except:
            page_content = None

        if page_content:
            soup = bs.BeautifulSoup(page_content, 'lxml')
            review_blocks = soup.find_all("div", {"class": "text show-more__control"})
            seen = set()
            for review in review_blocks:
                text = review.get_text(strip=True)
                if text and len(text) > 20 and text not in seen:
                    seen.add(text)
                    reviews_list.append(text)
                    try:
                        movie_vector = vectorizer.transform(np.array([text]))
                        pred = clf.predict(movie_vector)
                        reviews_status.append('Good' if pred[0] == 1 else 'Bad')
                    except:
                        reviews_status.append('Good')

    movie_reviews = {reviews_list[i]: reviews_status[i] for i in range(len(reviews_list))}

    return render_template('recommend1.html',
                           title=title,
                           poster=poster,
                           overview=overview,
                           vote_average=vote_average,
                           vote_count=vote_count,
                           release_date=release_date,
                           runtime=runtime,
                           status=status,
                           genres=genres,
                           movie_cards=movie_cards,
                           reviews=movie_reviews,
                           casts=casts)

if __name__ == '__main__':
    app.run(debug=True)
