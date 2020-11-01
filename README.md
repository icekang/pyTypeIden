# pyTypeIden

![Sample Prediction](https://github.com/icekang/pyTypeIden/blob/main/images/sample.jpg?raw=true)
Identifies person by her/his typing behavior

# Getting started

## Harvesting training and testing data

run `program.py`
<br>
The program will prompt you to enter your name and the number of data.
<br>
For example, `namkang-1` if "namkang" enter the data for the first time. It will count down and ask you to type the word according to what it prompts.
<br><br>
![In program.py](https://github.com/icekang/pyTypeIden/blob/main/images/program.jpg?raw=true)
<br>

## Prediction

I used a simple KNN algorithm to identify the typing and yeah I am so lazy that I don't even normalize the data! 😎
<br>
![In program.py](https://github.com/icekang/pyTypeIden/blob/main/images/knn.jpg?raw=true)
<br>
Use `utils`'s `fileToDict` to read data you've entered
<br>
Use class `Knn`'s`train` to train all the data.
<br>
Use `Knn`'s`predict` to predict the data.
<br>
<strong>Vola! The result is as follows!</strong>
<br>
![Sample Prediction](https://github.com/icekang/pyTypeIden/blob/main/images/sample.jpg?raw=true)
