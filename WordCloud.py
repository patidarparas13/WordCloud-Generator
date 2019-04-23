from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import urllib
import requests
import matplotlib.pyplot as plt

words = 'access guest guest apartment area area bathroom bed bed bed bed bed bedroom block coffee coffee coffee coffee entrance \
         entry francisco free garden guest home house kettle kettle kitchen kitchen kitchen kitchen kitchen kitchen \
         living located microwave neighborhood new park parking place privacy private queen room san separate separate shared space space space street suite time welcome'

mask = np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png',stream=True).raw))

def generate_wordcloud(words, mask):

    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS, mask=mask).generate(words)

    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')

    plt.imshow(word_cloud)

    plt.axis('off')

    plt.tight_layout(pad=0)

    plt.show()

    

#Run the following to generate your wordcloud

generate_wordcloud(words, mask)

