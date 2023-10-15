from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='68cef2651d654e11838e8d4f8ae7484a')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en')

# /v2/everything


dt=top_headlines['articles']

for x,y in enumerate(dt):
    print(f'{x} {y["description"]}')