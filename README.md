# SWE-Project
This project aims to analyze user reviews of ChatGPT to extract actionable insights. It uses Natural Language Processing (NLP) techniques such as topic modeling and sentiment analysis to understand user sentiment and identify key areas for product improvement.

## Getting Started

These instructions will guide you through setting up and running the project on your local machine for development and testing purposes.

### Prerequisites

You'll need Python 3.6 or later and the following packages:
pandas
numpy
scikit-learn
gensim
textblob
matplotlib

### Installation

Follow these steps to set up your environment:

1. Clone this repository:
2. Navigate to the project's directory: cd SWE-Project
3. Install the required dependencies:
4.     pip install -r requirements.txt
5. Download the necessary NLTK data:
6.       import nltk 
         nltk.download('all')
   
### Results
The script will output:

    Topics discovered from the ChatGPT reviews with the top words in each topic.
    A summary of sentiment analysis showing the sentiment distribution for each topic.
