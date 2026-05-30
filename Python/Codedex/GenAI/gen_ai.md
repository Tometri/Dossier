# Generative AI

## How does AI work?

Generative AI (GenAI) is a system that creates new content (text,image,video,etc.) based on prompts and large-language-models (LLMs).

LLMs are trained using natural language processing (NLP) techniques and can generate content through it. NLP is a branch of machine learning that teaches computers to understand, interpret, and generate human language.

Popular LLMs include:

- OpenAI GPT-4
- Anthropic Claude
- Google Gemini

```Python3
print("Claude is cool")
```

## Language Models

Language models are a key part of AI that helps computers understand and generate human language.

### Sequences

Language models help computers predict the likelihood of a sequence of words. Similar to how a human may guess the next words in an unfinished common phrase.

### NLTK

Python comes with many libraries that make work with language models easier. One of the most used libraries for AI is the NLTK library. The Natural Language Toolkit (NLTK) specializes in NLP tasks such as text generation, spell check, and translation.

## Tokenization

### Tokens

Tokens are small units of data used to train gen-ai models and help them to understand and generate language. This data may come in the form of whole words, subwords, and other content.

Tokens are essential for language models because they are the smallest units of meaning. By analyzing tokens, models can understand the structure and semantics of text. The process of making raw data like text trainable for language models is known as tokenization.

```Python3
import nltk

sample_text = 'I am learning Generative AI'
tokens = nltk.word_tokenize(sample_text.lower())

print('Tokens:', tokens)
```

nltk.word_tokenize() method converts the sample_text into lowercase and splits it into a list of tokens. The sentence "I am learning generative AI" becomes ['i', 'am', 'learning', 'generative', 'ai'].

Using tokenized data, language models can learn patterns and relationships between small units of data in the context of large amounts of data. This helps the model predict and generate new content based on what it learned.

## N-Grams

N-grams are sequences of 'n' tokens from a given sample of text.

By analyzing these sequences, we can understand how words are commonly used together. This is essential for tasks like predicting the next word in a sentence or understanding the meaning of text.

There are three popular models of n-grams:

- Unigram: for a single character/word. ("I")
- Bigram: for two consecutive characters/words. ("I am")
- Trigram: for three consecutive characters/words. ("I am learning")

### Using N-grams

Below is an example of how to generate bigrams from a sentence:

```Python3
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am learning AI"
tokens = word_tokenize(sentence)
bigrams = list(ngrams(tokens, 2)) # Bigram

print(bigrams)
```

This would return a list of bigrams from the sentence: [('I', 'am'), ('am', 'learning'), ('learning', 'AI')]

## Text Classification

Text classification involves categorizing texts into different groups. These types of models use python to classify text into predefined categories using a Naive Bayes classifier. A Naive Bayes classifier is a simple and powerful tool in ML. It's based on a basic probability rule called Bayes' Theorem and assumes that all features (like words in a text) are independent of each other.

Naive Bayes works well for tasks like identifying spam emails, analyzing sentiment, and classifying documents. If you want to sort emails into 'spam' or 'not spam', Naive Bayes can learn from examples and predict the category of a new email based on word patterns.

We use the scikit-learn library to implement the Naive Bayes classifier. This library provides tools for text vectorization, model training, and evaluation.

### Classes and Functions

There are classes and functions that are crucial for text classification:

- CountVectorizer: This class converts text data in a numerical format that the ML model can understand. It counts how many times each word appears in the text, turning words into a matrix of counts.
- MultinomialNB: This is a Naive Bayes classifier, which is used to train our model on the numerical text data.
- train_test_split: This function helps split our dataset into training and testing sets. It is commonly used in predictive ML. The training set is used to train the model, while the testing set is used to evaluate its performance.
- accuracy_score: This function provides a way to measure the accuracy of our model by comparing the predicted labels with the actual labels in the test set. A higher accuracy score indicates a better performance, a score of 1.0 = great predictions.

These classes and functions are essential for building a text classification model.

## Machine Translation

Machine Translation automatically converts text from one language to another using computer algorithms.

IT generally works by 1. Training with data: Machine translation systems are trained on vast amounts of text in multiple languages. They learn patterns and relationships between words in these languages. 2. Once trained, the system can translate a sentence from one language to another. Modern systems can effectively understand the context of the words during translation.

One of the libraries that can help with machine translation is the 'translate' python library. It allows you to translate simple phrases by interacting with machine translation APIs like Google Translate.

## Spell Check

Spell checkers automatically find and correct spelling mistakes in text. They are helpful and ensure that your writing is clear and error-free.

They generally work by 1. Dictionary comparison: The spell checker compares each word against a dictionary of correctly spelled words. If a word isn't found, it's flagged as a potential mistake. 2. Suggesting corrections: it suggests possible corrections based on common mispellings or similar words.

### TextBlob

The TextBlob library is a key tool in natural language processing and text analysis. It simplifies text processing, making it easy to work with text data.

TextBlob is:

- Easy to Use: It is straight forward and allows you to perform tasks like sentiment analysis, part-of-speech tagging, and text translation with just a few lines of code.
- Spell Checking and Correction: It includes built in spell checking and correction features.
- Text Analysis: You can analyze text to extract useful information like determining its sentiment (positive, negative, or neutral) and summarizes text data.
