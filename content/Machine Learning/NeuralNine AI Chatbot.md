---
tags:
  - NeuralNine
  - neural_networks
  - machine_learning
  - machine_learning
  - python
---
A chatbot is a robot that can understand the intent of a prompt and be able to react differently every time asked.

[https://www.youtube.com/watch?v=1lwddP0KUEg&list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-&index=8](https://www.youtube.com/watch?v=1lwddP0KUEg&list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-&index=8)

before we make the bot, we need to set up an intents.json file. We program the bot to be able to respond to certain events like the user greeting the bot, the user can ask about the creator of chatbot. Each event is built with a tag. The tag can be so called greeting tag and along with the tag we also specify patterns like “hello”. “good day”. A couple of examples of how the user can greet the chatbot. We will also have responses which are pre-made responses that the AI will choose depending on the user input. Now, the user input varies all the time, we will have the bot be able to recognize various inputs that the human gives regardless of if its been exposed to it or not by training the model. The responses are all pre-made. We are not going to have a generated response. Just static responses.

So we have our JSON like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_ee89a25f8b4dc9d4.png)

so in our intents.json we are making the tags. The tags will named appropriately, not used too much by the AI, but it helps organize patterns and responses of a specific nature. Patterns are the user inputs. Types of greetings possible. Responses will be static responses the robot can give. Keep setting up more tags.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_c4ea985eff19c3d7.png)

ok that is it.

Now for later on, we can also fire scripts if a certain tag is found. Like we don’t always need a flat response, we can webcrawl or search databases to get responses that are better.

Ok, so lets make 2 more files. One is training.py, another is chatbot.py

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_23ce3c0b9f89e43f.png)

its just cleaner to have 2 files.

  

### Training.py

So inside this script we want to import several libraries

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_12c2c3b23e086685.png)

random for the randomization of our response. Json for reading the json intents file. Pickle for serializtng, nltk for natural language processing, stem to stem words like working → work. Tensorflow sequential as neural network framework as well as the tensorflow layers and a SGD optimizer.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_440e955a08fb53d4.png)

then we have some lemmatizer constants

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_2e583ebd3eefeed7.png)

then let us make the word lists

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_1792861f1bfb577.png)

we use word tokenize to split the sentences into individual words and then add the wordlist into the 3 constants of words, documents and classess.

Then we just print documents.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_4bfc73ae92394acc.png)

then what we can do is, lemmatize the wordlist. Each word in the wordlist will be lematized.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_62368b4cc2925cb8.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_3f6985cdb0b6bcdb.png)

so we will nltk.download(‘wordnet’)

ok and then the words are lematized.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_51d148aad0d6a552.png)

now we serialize.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_b33e72b638f18e99.png)

so, in order to train the neural network, we need to represent these words as numerical values for the AI to understand. In order to do that we are going to be using bag of words we are going to make the individual word values either 0 or 1 if they are occuring or not in the current user inputted pattern and do the same thing for classes.

Bag of words is a machine learning model.

  

### Bag of words

[https://machinelearningmastery.com/gentle-introduction-bag-words-model/](https://machinelearningmastery.com/gentle-introduction-bag-words-model/)

LOOK GENTLE. BE GENTLE STAY CALM.

We have our wordlist. We want to assign each word a binary value. 0 or 1. We have a new list which correlates each word to an index like:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_b31078ab3535e208.png)

so assume in bagofwords[0], that is the value of the word “some”.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_1897215ebfe6fdac.png)

then, depending on the document, we update our baglist according to each wordindex. 1 is it occurs in the sentence, 0 if it doesn’t

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_ca2010e7c3d45feb.png)

and that is pretty much the model

now, since english language is a pain, and things are often phrase based. They have a version of bag-of-words called bigram, trigram, quadgram… so on so forth.

Bigram is when 2 words are paired together for an index. Like “it was” is just one index. “age of” is just one index. “the sludge” is just one index.

Semantics of the words are lost using bag-of-words since you are just matching a word’s structural buildup rather than its meaning. Theres also often a lot of bloat in the words we say. I’d argue 50% of things we say are just filler text, of which the AI has no real reason to know. I like how search algorithm works by using keywords, however not always we require keyword specific cases.

Ok lets make the bag of words in python

  

  

before we compare the bag of words for the literal words, We will just have a output_empty for the values of how likely each class the user’s input falls under.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_d3d886d2b480c6b9.png)

then, we will have the bag of words

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_6445b1cfa314e94b.png)

super long algorithm. But all you need to know is that It goes through our documents list which includes tuples of wordlists and tags for a specific tag. Then it will check the wordlists, lemmatize it so then we can create the bag of words. Once the bag of words is done, we will also create a ‘bag-of-classes?”. Its like a bag of words, just that its for the tags instead of the wordlist. So after that is done, we append those 2 into the training dataset. The bagowords and the classrating2 bags.

Rant time: I wish more coding channels actually ran through to see if their code works. Just periodically running the program, not just running when you think its done. I know they have a seperate monitor where they see their finished code, but a human will make mistakes based off context completion assumptions.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_8a23f042ccec08ec.png)

this is the correct code. It peeves me off when they leave all their corrections in post recording, I don’t know If I have OCD but I have a supreme annoyance for loose ends. Leave something unfinished, it will be harder to diagnose in the future.

Ok next thing we wanted to do before I got sidetracked was to now create the neural network. You know how this goes. Make a sequential() fill it with layers, fit it, give it an optimizer and save it.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_5fa0e3400773951b.png)

so we make the neural network and we also make a SGD stocastic gradient descent object.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_b4654b930fd3a421.png)

compile the model.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_255ea4e169ce5824.png)

fit it in with 200 DAMN EPOCHS HOOLY. And also give it verbose. Verbose is optional though.

  

So again, more tinkering cause the code break. This part always gave me the heeby jeebies:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_6e6976938d9161c4.png)

I don’t know what this does, and what I don’t know hurt me so I changed it to somebody else’s version.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_7c5e3259c55bdc6b.png)

again, I don’t know what this does. But this works so we are using it.

  

### Chatbot.py

We are going to use the model that we just exported using a different file.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_4bf7a0efe0fb9c52.png)

in our chatbot.py file, you will want to import the following libraries.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_e5c30514ac8b4ea9.png)

next up, bring back a few essentials. Grab the lemmatizer, intent json and also grab our exported data from training.py

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_211c964490a5bd82.png)

know that we can use it now, but we want to use it the right way. Know we feed it numerical numpy arrays and it in return gives us a numerical numpy array.

In order to effectively use it, you will want to make 4 functions.

1. Cleaning sentences
    
2. grab the bag-of-words
    
3. predict the class
    
4. getting the response
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_e2a05623e91107f2.png)

so this is how we clean the sentence.

Now that we have the sentence, we want to convert the sentence into a bag-of-words so we can feed it into the model.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_9052d34a0f36cc36.png)

simple bag of words function. We will make a bag of words based on the wordlist. Then we will check the user’s given sentence and then match every word in our bag-of-words to the words in the user’s given sentence. Return a numpy array of bag.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_bd935b4592c8e531.png) this is the hard one. Il try to transcribe best I can. We will grab the results form a model.predict. Then we will have our error threshold to remove those prediction results that are really irrelevant, very far off. We only keep the predicion class results that are above 25% in softmax share. Then we will sort the results in reverse order so its highest probability first for the list. And lastly, we return the returnlist in a nice list[set] format. Its not just one possible tag, its several(if that happens)

we next have the code to ge the response

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_a28d051f539a6bb6.png)

this will get the response from the json file.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivxn_tmp_9f6ac78e29bbd30d.png)

and this is the AI loop. Not too difficult here.

The AI works. I mean it works. Got a lot of personality and it performs well.