from pkgutil import get_data
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from column import detect_column_types  

def visualize(df, threshold=20):
   
    col_types = detect_column_types(df, threshold)

    for col, ctype in col_types.items():
        plt.figure(figsize=(8, 5))  
        if ctype == "numerical":
         
            plt.subplot(1, 3, 1) 
            sns.histplot(df[col].dropna(), kde=True)
            plt.title("Histogram of " + col)

            plt.subplot(1, 3, 2)
            sns.boxplot(y=df[col].dropna())
            plt.title("Boxplot of " + col)

            plt.subplot(1, 3, 3)
            plt.scatter(range(len(df)), df[col])
            plt.title("Scatter of " + col)

        elif ctype == "categorical":
            sns.countplot(x=df[col], order=df[col].value_counts().index)
            plt.title("Count Plot of " + col)
            plt.xticks(rotation=45)

        elif ctype == "text":
            wordcloud = WordCloud(width=800, height=400, background_color="white").generate(get_data)
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.title("Word Cloud of " + col)

        plt.tight_layout()
        plt.show()
