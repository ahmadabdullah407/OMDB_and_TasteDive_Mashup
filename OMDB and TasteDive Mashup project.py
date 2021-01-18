import requests
import json
def get_movies_from_tastedive(name):
    baseurl = "https://tastedive.com/api/similar"
    params = {}
    params['q'] = name
    params['type'] = 'movies'
    params['limit'] = 5
    res = requests.get(baseurl, params = params)
    return res.json()
def extract_movie_titles(dict1):
    movielist = []
    for movie in dict1['Similar']['Results']:
        movielist.append(movie['Name'])
    return movielist
def get_related_titles(mlist):
    finalmovielist = []
    for m in mlist:
        movielist = extract_movie_titles(get_movies_from_tastedive(m))
        for movie in movielist:
            if movie not in finalmovielist:
                finalmovielist.append(movie)
    return finalmovielist
def get_movie_data(moviename):
    baseurl = "http://www.omdbapi.com/"
    params = {}
    params['t'] = moviename
    params['r'] = 'json'
    res = requests.get(baseurl, params = params)
    return res.json()
def get_movie_rating(movie):
    try:
        return int(movie['Ratings'][1]['Value'][:-1])
    except:
        return 0
def get_sorted_recommendations(movielist):
    related_movies_list = get_related_titles(movielist)
    sorted_rml = sorted(related_movies_list, key = lambda m:(get_movie_rating(get_movie_data(m)),m), reverse = True)
    return sorted_rml
# print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])) 
