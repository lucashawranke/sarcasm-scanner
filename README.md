<p align="center"> <b><i>Satire/Fake News</i> Detector</b>
  
![chart](https://i.ibb.co/tYHpMd2/Screenshot-2022-12-04-at-8-20-29-PM.png)
<p align="center">. 　　 ·　 ˚ ✧ Introduction ✧ ˚ 　· 　　 .

Sarcasm can often be difficult to detect even for humans, especially for those who may be neurodivergent, or younger/older in age. In today's day and age, misinformation makes it even harder to decipher the truth from fiction, especially with the rise of fake news on social media. Efficient and accurate satire detection can help distinguish between true and false information, and can provide helpful insights into the sentiment of a statement.

The project uses natural language processing and machine learning techniques to build a model that can accurately identify if a given statement is sarcastic or not. The model utilizes a large dataset of news headlines that have been labeled as either satire (fake), or authentic (real).

<p align="center">. 　　 ·　 ˚ ✧ Data Collection ✧ ˚ 　· 　　 .

The data used for this project was collected from four sources: [_@theonion_](https://twitter.com/TheOnion) and [_@ClickHole_](https://twitter.com/ClickHole), both satire accounts on Twitter, as well as [_@cnnbrk_](https://twitter.com/TheOnion) and [_@PopCrave_](https://twitter.com/PopCrave), accounts that post authentic news. 

@theonion and @ClickHole are both popular satirical news websites and Twitter handles that often posts humorous and sarcastic articles, whereas @cnnbrk is the official Twitter handle for CNN Breaking News, a website dedicated to providing the latest (serious) news and updates, and @PopCrave is an account which posts celebrity news updates.

The data was collected using the sntwitter library and was stored in two CSV files. Each file contains 5,000 tweets from each source. The tweets were then labeled as either “sarcastic” or “non-sarcastic”.

<p align="center">. 　　 ·　 ˚ ✧ ML Models ✧ ˚ 　· 　　 .

Throughout this project, I have focused on developing two models for deployment, and three others for testing; one Multinomial Naive Bayes model and one LinearSVC model are saved in the repository, as well as a Logistic Regression model, Random Forest Classifier model, Decision Tree Classifier model, and K Neighbors Classifier model saved at the end of the main notebook with their precision scores as well as matrices.

<p align="center">. 　　 ·　 ˚ ✧ Deployment ✧ ˚ 　· 　　 .

The model is deployed using Flask. The user can input a statement into the text box and the model will predict whether the statement is sarcastic or not.
  
<p align="center">. 　　 ·　 ˚ ✧ Results ✧ ˚ 　· 　　 .

The Multinomial Naive Bayes model achieved an accuracy score of ~0.91, and the LinearSVC model achieved an accuracy score of ~0.95! Other models mentioned in 

<p align="center">. 　　 ·　 ˚ ✧ Future Work ✧ ˚ 　· 　　 .

In the future, I would like to expand the dataset to include more sources of varying types of accounts, news or satire parodies of such or not, and also play around with certain parameters of the models to see if I can achieve a higher accuracy score. I would also like to deploy the model using a different framework, such as Heroku, and create a beautiful web application that can be used by anyone.
  
In an earlier project I worked on, I commented on how having a model that can detect sarcasm would be perfect for separating YouTube comments into their own clusters, so implementing this in projects where I need serious, raw data can make my process much easier.

<p align="center">. 　　 ·　 ˚ ✧ Acknowledgements ✧ ˚ 　· 　　 .

I would love to thank my mentors, [Mohammed Salma[(https://github.com/dataubc) and [Mohammad Sultan](https://github.com/mohammad9522), for their guidance and support throughout this project. I would also like to thank StackOverflow for being there for me when things got hard.

<p align="center">. 　　 ·　 ˚ ✧ Contact ✧ ˚ 　· 　　 .

If you have any questions, comments, or concerns, please feel free to reach out to me at [my email](mailto:lucashawranke@gmail.com), or [my LinkedIn](https://www.linkedin.com/in/lucas-hawranke-98a317125/).
