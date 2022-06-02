#1.Librerías necesarias:
%matplotlib inline
from plotly import graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from collections import Counter
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
from nltk.corpus import stopwords
from tqdm import tqdm
import os
import nltk
import spacy
import random
from spacy.util import compounding
from spacy.util import minibatch
import warnings
warnings.filterwarnings("ignore")
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import pandas as pd


#2.Lectura de datos

data_train= pd.read_csv("train.csv")
data_test=pd.read_csv("test.csv")
data_sample=pd.read_csv("sample_submission.csv")

def eliminar_nulos_train():
    data_train.dropna()
    return data_train


