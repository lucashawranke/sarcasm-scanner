<p align="center"> <b><i>Satire/Fake News</i> Detector</b>
<p align="center">. 　　 ·　 ˚ ✧ Introduction ✧ ˚ 　· 　　 .

Sarcasm can often be difficult to detect even for humans, especially for those who may be neurodivergent, or younger/older in age. In today's day and age, misinformation makes it even harder to decipher the truth from fiction, especially with the rise of fake news on social media. Efficient and accurate satire detection can help distinguish between true and false information, and can provide helpful insights into the sentiment of a statement.

The project uses natural language processing and machine learning techniques to build a model that can accurately identify if a given statement is sarcastic or not. The model utilizes a large dataset of news headlines that have been labeled as either satire (fake), or authentic (real).

<p align="center">. 　　 ·　 ˚ ✧ Data Collection ✧ ˚ 　· 　　 .

The data used for this project was collected from four sources: [_@theonion_](https://twitter.com/TheOnion) and [_@ClickHole_](https://twitter.com/ClickHole), both satire accounts on Twitter, as well as [_@cnnbrk_](https://twitter.com/TheOnion) and [_@PopCrave_](https://twitter.com/PopCrave), accounts that post authentic news. 

@theonion and @ClickHole are both popular satirical news websites and Twitter handles that often posts humorous and sarcastic articles, whereas @cnnbrk is the official Twitter handle for CNN Breaking News, a website dedicated to providing the latest (serious) news and updates, and @PopCrave is an account which posts celebrity news updates.

The data was collected using the sntwitter library and was stored in two CSV files. Each file contains 5,000 tweets from each source. The tweets were then labeled as either “sarcastic” or “non-sarcastic”.

<p align="center">. 　　 ·　 ˚ ✧ ML Models ✧ ˚ 　· 　　 .

Throughout this project, I have focused on developing two models for deployment; one Multinomial Naive Bayes model and one LinearSVC model.

The Multinomial Naive Bayes model is a simple model that uses the Naive Bayes algorithm to classify text. The LinearSVC model is a more complex model that uses the Linear Support Vector Classification algorithm to classify text. Both models were both given the same data.

<p align="center">. 　　 ·　 ˚ ✧ Results ✧ ˚ 　· 　　 .

The Multinomial Naive Bayes model achieved an accuracy score of 0.❓, a precision score of 0.❓, a recall score of 0.❓, and an f1 score of 0.❓.
***
The LinearSVC model achieved an accuracy score of 0.❓, a precision score of 0.❓, a recall score of 0.❓, and an f1 score of 0.❓.

