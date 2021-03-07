## What is the difference between prediction and inference?

The terms inference and prediction are frequently used in the context of statistics. Understanding the difference between them can be difficult even for people working long in the field. They are often confused because they are not mutually inclusive. Both of them are related to gain information from the data. They appear similar but the difference should be well-drawn out. In this post, I will try to distinguish them based on definition, problem statement and application. In the meantime, I will explain the difference by considering examples from both inference and prediction perspectives.

#### Definition
Let‘s start with the famous Titanic example. Assuming we are provided with information on the age, passenger class, gender and survival rate of Titanic passengers, inference is to find out what are the effect of age, passenger class and gender on survival rate for each passenger, while prediction is to compute the survival rate as correct as possible given some information on a Titanic passenger. We can see that inference and prediction are actually answering  different questions. In this example, age, passenger class and gender are input predictor variables, and survival rate is the output outcome variable. Inference is to understand the relationships between the input variables and the outcome variable given the data, and then infer how the output variable is generated as a function of the input variables generally in the world. Prediction is to use the given data to build a function which can make the best guess on the outcome variable given some specific values on the input variables. In a word, inference is about what happened while prediction is about what will happen.

#### Problem statement
Now, we have some basic understanding about what is inference and what is prediction. Let’s dig in to see what is the difference between an inference problem and a prediction problem more specifically. Continuing with the Titanic example, we may seek to relate the output survival rate to the inputs such as age and  passenger class. In this case, we might have interest in how the individual input variables affect the survival rate, for example,  how much extra will the survival rate be if the passenger has a first-class ticket instead of an economic-class ticket? This is an inference problem. Alternatively, we may have interest in predicting the value of the survival rate given the age is 20 and the passenger class is first-class, that is,  what is the survival rate given these characteristics? This is a prediction problem. From this example, we can see that the emphasis is quite different in an inference problem and a prediction problem. For an inference problem, we are focusing on gaining an understanding about the effect of the inputs on output in the data set and utilize this information to infer what is the effect in all individuals units of the population. Instead, for a prediction problem, we are focusing on having better predictions on the output based on some data or features.

#### Application
Last but not least, I will talk about how an inference application and a prediction application differs. In an inferential application, we are aiming to find a right model explaining the data and make sure the model generalizes well in all the individuals in the whole population. For the purpose of this, we should collect the sample carefully and make the assumptions seriously.  Additionally, we should pay close attention to the interpretability of the results because an inferential application has a strong interest in the underlying mechanics causing the outcome. In terms of a predictive application, we have more emphasis on achieving high accuracy. In this case, we do not care about the relationships between inputs and the output and we just focus on developing a best model to predict the output with lowest error.

#### Conclusion
In conclusion, the point is that given some data if you want to know how the output changes as the input changes then it is inference, if you want to estimate the output based on some values of the inputs then it is prediction. Inference is more about interpretability while prediction is more about accuracy.

![title](infer_vs_predict.png)