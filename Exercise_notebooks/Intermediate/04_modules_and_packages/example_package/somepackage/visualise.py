# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:04:03 2021

@author: onno_
"""


from wordcloud import WordCloud
import matplotlib.pyplot as plt

def make_wordcloud(text):
    """ generates and plots a wordcloud.
    
    Parameters
    ----------
    text : str
        text for the wordcloud
        
    Returns
    ------
    matplotlib.image.AxesImage
    
    """
    
    wordcloud = WordCloud().generate(text)
    ax = plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    
    return ax