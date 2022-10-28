from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
from newspaper import Article
import nltk
import pandas as pd
from PIL import Image
import requests
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def wordpic(Feeds,StopWords,InputImage,OutputImage):
    """Ingests RSS newsfeeds and outputs a shaped wordcloud

        Keyword arguments:
        Feeds -- List with xml RSS News feeds
        StopWords -- List of words to skip over
        InputImage -- name of PNG or JPG source image
        OutputImage -- name of PNG or JPG output image

        Usage example:
        wordpic(Feeds=['http://rss.cbc.ca/lineup/topstories.xml'],
        StopWords=["a", "eh", "sorry"],
        InputImage='CDN_Flag.png',
        OutputImage='words.png')
    """
    try:
        nltk.data.find('punkt')
    except:
        nltk.download('punkt')

    feeds = Feeds

    articles = []

    for feed in feeds:
        response = requests.get(feed)
        webpage = response.content
        soup = BeautifulSoup(webpage, features='xml')

        items = soup.find_all('item')

        for item in items:
            link = item.find('link').text
            articles.append(link)

    data = []

    for url in articles:
        info = Article(url)
        try:
            info.download()
            info.parse()
            info.nlp()
            keywords = info.keywords
            texts = info.text
            saved = [url, keywords, texts]
            data.append(saved)
        except:
            ## Packing this all in to a try statement to handle bad urls that are sometimes included
            continue

    label = ['URL', 'Keywords','Text']
    df = pd.DataFrame(data)
    df.columns = label

    stopwords = set(STOPWORDS)
    stopwords.update(StopWords)

    text = df.Text[1]

    frame = np.array(Image.open(InputImage))
    flag_wordcloud = WordCloud(stopwords=stopwords,collocations=False,background_color='white',mask=frame).generate(text)
    image_colors = ImageColorGenerator(frame)
    plt.figure(figsize=[40,40])
    plt.imshow(flag_wordcloud.recolor(color_func=image_colors))
    plt.axis('off')
    plt.axis('off')
    plt.show;
    plt.savefig(OutputImage)