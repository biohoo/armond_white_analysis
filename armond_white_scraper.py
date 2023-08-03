import pandas as pd
import requests 

url_list = ['https://www.rottentomatoes.com/napi/critics/armond-white/movies?',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MQ%3D%3D&pagecount=50', 
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=Mg%3D%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=Mw%3D%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=NA%3D%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=NQ%3D%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=Ng%3D%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=Nw%3D%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=OA%3D%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=OQ%3D%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTA%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTE%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTI%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTM%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTQ%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTU%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTY%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTc%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTg%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MTk%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MjA%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MjE%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MjI%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MjM%3D&pagecount=50',
        'https://www.rottentomatoes.com/napi/critics/armond-white/movies?after=MjQ%3D&pagecount=50']



armond_white_reviews = []

# Loop through each URL and make a request to get JSON data
for url in url_list:
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"Error reading JSON from {url}: {e}")
        continue

    # Process the JSON data and extract reviews
    for review in data["reviews"]:
        compare_value = review["compareValue"]
        tomatometer_state = review["tomatometerState"]
        media_tomatometer_state = review["mediaTomatometerState"]
        media_tomatometer_score = review["mediaTomatometerScore"]
        quote = review["quote"]
        publication_name = review["publicationName"]
        date = review["date"]
        try:
            media_title = review["mediaTitle"]
        except:
            media_title = 'UNKNOWN'

        armond_white_reviews.append({
            "Armond Review": tomatometer_state,
            "Tomatometer Review": media_tomatometer_state,
            "Tomatometer Score": media_tomatometer_score,
            "Quote": quote,
            "Publication Name": publication_name,
            "Movie": media_title,
            "Date": date
        })
        print(media_title)


# Create DataFrames from the lists
armond_white_df = pd.DataFrame(armond_white_reviews)

armond_white_df.to_csv('armond_white-revision.csv')