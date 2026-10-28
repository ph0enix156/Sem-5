
# Code 7: NLP Chatbot using Python and NLTK

# Install these libraries in the VS Code terminal:
# python -m pip install nltk
# python -m pip install newspaper3k
# python -m pip install lxml_html_clean

# Import libraries
import nltk
from newspaper import Article
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Download required NLTK datasets
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Get article
article = Article('https://en.wikipedia.org/wiki/Influenza')
article.download()
article.parse()

sentences = sent_tokenize(article.text)
stop_words = set(stopwords.words('english'))

# Find answer
def get_answer(question):
    q = set(word_tokenize(question.lower())) - stop_words
    best, score = "", 0

    for s in sentences:
        words = set(word_tokenize(s.lower())) - stop_words
        count = len(q & words)

        if count > score:
            best, score = s, count

    return best

# Chatbot
print("Chatbot ready! Type bye to exit.")

while True:
    user = input("You: ").lower()

    if user in ['bye', 'exit', 'quit']:
        print("Bot: Goodbye!")
        break

    elif user in ['hi', 'hello', 'hey']:
        print("Bot: Hello! Ask me about influenza.")

    else:
        answer = get_answer(user)
        print("Bot:", answer if answer else "No answer found.")