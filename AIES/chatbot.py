"""
================================================================================
NLP-BASED QUESTION ANSWERING CHATBOT (TOPIC: INFLUENZA)
================================================================================

PREREQUISITES:
1. Python 3.x installed.
2. Active Internet Connection:
   - Needed on first run to download NLTK corpora (punkt, stopwords).
   - Needed at startup to fetch the Wikipedia article on Influenza.
3. Required Third-Party Libraries:
   - nltk: Natural Language Toolkit for tokenization & stopword removal.
   - newspaper3k: Web scraping library to extract clean text from articles.
   - lxml_html_clean: Required dependency for newspaper3k with modern lxml.

HOW TO INSTALL DEPENDENCIES:
  Run the following command in your terminal / command prompt:
      pip install nltk newspaper3k lxml_html_clean

  Or using the python module flag:
      python -m pip install nltk newspaper3k lxml_html_clean

HOW TO RUN:
  Open terminal in this directory and execute:
      python chatbot.py

HOW IT WORKS:
  1. Scrapes the Wikipedia article on "Influenza".
  2. Splits the article into candidate sentences.
  3. When a user asks a question, it removes stopwords and matches keywords
     against all sentences using set intersection.
  4. Returns the sentence with the highest keyword overlap.
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORTS
# ==============================================================================
import nltk                                          # Natural Language Toolkit
from newspaper import Article                         # For scraping & parsing web articles
from nltk.tokenize import sent_tokenize, word_tokenize # For sentence & word splitting
from nltk.corpus import stopwords                    # For filtering common filler words


# ==============================================================================
# SECTION 2: NLTK RESOURCE DOWNLOADS
# ==============================================================================
# Download required pre-trained tokenizers and corpora (cached locally after first run)
nltk.download('punkt', quiet=True)       # Standard Punkt tokenizer models
nltk.download('punkt_tab', quiet=True)   # Punkt tokenizer tables (required in newer NLTK)
nltk.download('stopwords', quiet=True)   # English stopwords list (e.g., 'the', 'is', 'at')


# ==============================================================================
# SECTION 3: WEB SCRAPING & KNOWLEDGE BASE PREPARATION
# ==============================================================================
# Define the source URL to build the chatbot's knowledge base
ARTICLE_URL = 'https://en.wikipedia.org/wiki/Influenza'

# Initialize the Article object with the target URL
article = Article(ARTICLE_URL)

# Download the HTML content from Wikipedia
article.download()

# Parse the raw HTML to extract only clean article body text
article.parse()

# Tokenize the entire article text into individual sentences (our search corpus)
sentences = sent_tokenize(article.text)

# Load English stopwords into a set for fast O(1) membership lookups
stop_words = set(stopwords.words('english'))


# ==============================================================================
# SECTION 4: ANSWER RETRIEVAL ENGINE (KEYWORD OVERLAP)
# ==============================================================================
def get_answer(question):
    """
    Finds the most relevant sentence from the article for a given question.
    
    Approach:
      1. Tokenizes the user's question into individual words.
      2. Converts to lowercase and eliminates punctuation & stopwords.
      3. Compares the question words with words in each article sentence.
      4. Measures relevance using set intersection count (keyword overlap).
      5. Returns the sentence with the highest overlap score.
    
    Parameters:
      question (str): The user input query.
      
    Returns:
      str: The sentence with the highest keyword match, or empty string if none.
    """
    # Tokenize question, lowercase it, and remove stopwords
    q_tokens = word_tokenize(question.lower())
    q = set(q_tokens) - stop_words

    best = ""
    score = 0

    # Iterate through all candidate sentences in the article
    for s in sentences:
        # Tokenize candidate sentence, lowercase, and remove stopwords
        s_tokens = word_tokenize(s.lower())
        words = set(s_tokens) - stop_words

        # Compute keyword overlap count using set intersection
        count = len(q & words)

        # Update best match if current sentence has more matching keywords
        if count > score:
            best = s
            score = count

    return best


# ==============================================================================
# SECTION 5: INTERACTIVE CHAT INTERFACE
# ==============================================================================
def main():
    print("=" * 60)
    print("Chatbot ready! Ask me anything about Influenza.")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("=" * 60)

    while True:
        # Prompt user for input
        user = input("You: ").strip()

        # Handle empty inputs gracefully
        if not user:
            continue

        user_lower = user.lower()

        # Exit condition
        if user_lower in ['bye', 'exit', 'quit']:
            print("Bot: Goodbye! Stay healthy!")
            break

        # Greeting condition
        elif user_lower in ['hi', 'hello', 'hey', 'greetings']:
            print("Bot: Hello! Ask me anything about influenza (symptoms, causes, prevention).")

        # Query response via NLP retrieval
        else:
            answer = get_answer(user)
            if answer:
                print(f"Bot: {answer}")
            else:
                print("Bot: I'm sorry, I couldn't find an answer to that in my article.")


if __name__ == "__main__":
    main()
