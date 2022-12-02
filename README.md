<p align="center"> <b><i>Sarcasm/Fake News</i> Detector</b>
<p align="center">
☆.｡.:*　　.｡.:*☆ Introduction ☆.｡.:*　　.｡.:*☆

Sarcasm can often be difficult to detect even for humans, especially for those who may be neurodivergent. In today's day and age, misinformation makes it even harder to decipher the truth from fiction, especially with the rise of fake news on social media. Efficient and accurate sarcasm detection can help distinguish between true and false information, and can provide helpful insights into the sentiment of a statement.

The project uses natural language processing and machine learning techniques to build a model that can accurately identify if a given statement is sarcastic or not. The model utilizes a large dataset of news headlines that have been labeled as either sarcastic (fake), or non-sarcastic (real).

<p align="center">
∞༺♥༻✧ Data Collection ✧༺♥༻∞


The data used for this project was collected from two sources: [_@theonion_](https://twitter.com/TheOnion) and [_@cnnbrk_](https://twitter.com/cnnbrk). 

@theonion is a popular satirical news website and Twitter handle that often posts humorous and sarcastic articles. 

@cnnbrk is the official Twitter handle for CNN Breaking News, a website dedicated to providing the latest (serious) news and updates. 

The data was collected using the sntwitter library and was stored in two CSV files. Each file contains 5,000 tweets from each source. The tweets were then labeled as either “sarcastic” or “non-sarcastic”.
