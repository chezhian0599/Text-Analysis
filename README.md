# Text-Analysis
## **Agenda:**

To do **"Text Analysis"** on data that we scrapped during our **[Web Scrapping](https://github.com/chezhian0599/Web-Scrapping)** project and to compute various Scores( see List of Variables) and store it in a csv file.
## We have .txt file of 

- **stopwords** 
- **positivewords** 
- **negativewords** 

## **Tools Used:**
- Programming Language - Python
- Text Editor - Visual Studio Code

## **List of Variables**

- 	POSITIVE SCORE
- 	NEGATIVE SCORE
- 	POLARITY SCORE
- 	SUBJECTIVITY SCORE
- 	AVG SENTENCE LENGTH
- 	PERCENTAGE OF COMPLEX WORDS
- 	FOG INDEX
- 	AVG NUMBER OF WORDS PER SENTENCE
- 	COMPLEX WORD COUNT
- 	WORD COUNT
- 	SYLLABLE COUNT PER WORD
- 	COUNT OF PERSONAL PRONOUN
- 	AVERAGE WORD LENGTH




## **Calculation Procedures**

**1.POSITIVE SCORE**
This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.

**2.NEGATIVE SCORE**
This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.

**3.	POLARITY SCORE**
This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula: 
Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
Range is from -1 to +1

**4.	SUBJECTIVITY SCORE**
This is the score that determines if a given text is objective or subjective. It is calculated by using the formula: 
Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
Range is from 0 to +1

**5.	AVG SENTENCE LENGTH**
Average Sentence Length = the number of words / the number of sentences.

**6.	PERCENTAGE OF COMPLEX WORDS**
Percentage of Complex words = the number of complex words / the number of words 

**7.	FOG INDEX**
Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)

**8.	AVG NUMBER OF WORDS PER SENTENCE**
Average Number of Words Per Sentence = the total number of words / the total number of sentences.

**9.	COMPLEX WORD COUNT**
Complex words are words in the text that contain more than two syllables.

**10.	WORD COUNT**
We count the total cleaned words present in the text by 
	removing the stop words (using stopwords class of nltk package).
	
**11    SYLLABLE COUNT PER WORD**
We count the number of Syllables in each word of the text by counting the vowels present in each word. We also handle some exceptions like words ending with "es","ed" by not counting them as a syllable.

**12 COUNT OF PERSONAL PRONOUN**
To calculate Personal Pronouns mentioned in the text, we use regex to find the counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country name US is not included in the list.

**13 AVAERAGE WORD LENGTH**
Average Word Length is calculated by the formula:
Sum of the total number of characters in each word/Total number of words



	
	
## **Execution:**
To Calculate the scores I have **defined function**, with the help of those functions I have calculated the Scores.

Finally I have Stored all the data in a csv file.
  
