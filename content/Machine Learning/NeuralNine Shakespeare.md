---
tags:
  - machine_learning
  - machine_learning
  - machine_learning
  - machine_learning
  - python
---

We will make a python AI that generates shakespere like poetry.

These are the functions we will use:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_1a9b49bcafd84ec8.png)

ln 4: sequential is the barebones neural network template. We add layers to it to make it the complete neural network.

Ln 5: the different types of layers there are. Biggest difference is that they are made for different types of neural networks. Recurrent is LSTM, dense is core, activation is also core.

Ln 6: RMSprop to optimize compilation of the model. Before we used adam, this time we use RMSprop. Deepmind loves RMSprop.

  

### keras.utils.get_file()

We will get the data from here:

[https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt](https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt)

we could download it, we could also just use tensorflow to get the data straight.

Use tf.keras.utils.get_file()

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_babe11c766766f6a.png)

fname is the filename we give it so you can give it any name. I just name it ‘shakespeare.txt’. Origin is the https website it can use a webcrawler and just download it. It will be downloaded on ur pc anyways.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_2acc503767dec8a8.png)

and yes, it downloads it to your computer so, when you run the program again it is saved in your cache so it doesn’t download again.

[https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file)

this is where it stores it:

C:\Users\Digit\.keras\datasets

know that the filepath variable only stores the file path. To get the binary data, we need to open the filepath and read binary.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_ee6615384b0f7394.png)

so we open it in read binary mode, we read it to get the binaries, decode it in utf-8 which is common for these files and lowercase it. The reason why we lowercase it is because we want to model to predict the next character, and it will be so much of a hassle to train it with capitalization so we just make it lowercase for now to make it easier.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_4732f444d0512e22.png)

Ok reading the text gives this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_fafc6f125143aa2e.png)

lots and lots of shakespeare texts.

The text is a little too much and will take too long for the neural network to process.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_caef73f297e3d295.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_51f2da24e13098c1.png) a fuckin million words.

Lets shorten it down to like half a million then.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_c1e2828790118a1e.png)

  

### Ascii to number lookup tables

Ok but the problem is that the neural network cannot read ascii text directly, it must read a numerical value.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_22817256fdb1e785.png)

so we grab all the characters that the text uses. Remember that there are a couple hundred ascii characters and a lot of them we probably wont even use.

So we only get the character we will use and put them all in a set. Characters don’t repeat in a set so we have only 1 copy of each character.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_a1afd50bf4b3aceb.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_f36a02eb67830d47.png)

suprisingly, the only number used is 3.

  

to map it, my first idea was to use ord() and chr() to convert ascii to decimal and decimal to ascii. However, I learned later that these will be mapped to coordinates and it doesn’t make sense for coordinate indices to jump from like 10 to 194. so instead, neuralnine has this solution of making 2 dictionaries. One for converting decimal from char, another to convert decimal to char

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_92f6eabb6cb36479.png)

enumerate assigns each character a number. He made a dictionary using 1 line of code.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_5f1a57e40edc37f8.png)

im gonna do it in 3 lines of code. I don’t like that hypercompactness, makes it difficult to understand yknow.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_da0c551137285abf.png)

did the same for the other lookup table

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_66635ed2fd5e51e.png)

these are what the 2 look like. Chartoindex is the first dictionary, indextochar is the second.

  

### Predict next character

We want to model to be able to predict the next character. So we need a list of sentences and a list of characters. Sentences will be the target, characters will be the future data we use for testing.

We feed the AI like 40 characters from the sentences and we want it to give us the 41st character from looking at each character neuron we give it. How many input neurons we give is always a flat value. So if we give a sentence with 40 chars, there are 40 neurons. I think 40 is a good number, neuralnine thinks 40 is a good number too. make a variable that stores 40.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_b37a572aea3f836e.png)

aswell, we will have a variable called stepsize. The stepsize tells us for the next part of the sentence, how much do we move?

  

We move 3 steps so if we had a sentence with SEQLENGTH 5 like: nigge

a stepsize 3 would shift the starting character 3 right and then its like: elina

notice 3 steps from n is e in the sentence.

  

So this is how we implement the algorithm:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_bc3f2376130459ac.png)

it will stepsize 3, grab the current sentence from the point it is at, and save the next character right after the sentence.

  

The next step is to make the x and y data in numbers.

this next part is difficult for me to understand. 70% understood, transcribed meaning from video.

Lets make our x and y data now.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_adf9f10f2226c3d8.png)

x is a 3d numpy array. We have a dimension for all possible sentences we can have, we have a dimension for all the individual positions inside the sentence and we have a dimension for all possible characters we can have(from the lookup table).

Whenever in a specific sentence a, at a specific position, a specific character occurs, we want that cell to be true, and all other cells to be false. So for example I have sentence # 5, at position #7 and I want to check if the character has enum #8(from the lookup tables). If it is, then that specific cell is True and all others is false.

Y is a 2d numpy array. This is for the future values. It says at sentence # 5, the future value is character with enum #8.

then we fill up the x and y data

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_d921aa660fdad9e2.png)

For x:

so for every sentence, you have a 2d list of positions characters the 2d list spans the SEQLENGTH, so 40 and the number of possible characters is around 39? i think? for my case its around 39.

so its 40*39 2 list.

every row in the 2d list is a 39 length row. it is the character enums row. so there is only always 1 TRUE value for every row.

again, this is just turning the strings into numbers, very complicated way but it is organized i guess.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_f94eabf2a3f929cb.png)

above is an example of one of those character enum rows.

For y:

just grabs the position and the character enum. Pretty similar to the x list just that its missing one dimension(which is sentence #) and it also predicts future values.

I don’t understand this completely, but I will see later in the future.

  

### Building the network

We will build the neural network now.

We get the barebones framework,

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_2533230e37bebe7c.png)

then we decorate it. First layer is the LSTM input layer. This is what allows our model to be recurrent. LSTM(long short term memory) it is the memory of our network. It will remember the past input characters. If we didn’t have this, then our model would only look at the input layer it has now, and forget the ones that came before.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_bb1c84205a85c661.png)

I believe the 128 is the neurons for the hidden layer after it. SEQLENGTH is 40, the length of characters is 39(for me) so 40*39 = 1560, that would be the input layer neurons?

We give a dense layer as a hidden layer for more sophistication.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_395953cd399cc7bb.png)

and finally the activation output layer.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_93b5ed5625c064b1.png)

we softmax it so it is distributed percentage of all neurons

at last we compile the model.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_2186435bb8da17bd.png)

loss function is categorical cross entropy, and the optimizer we use is RMSprop with a learning rate of 0.01

  

finally feed it the training data with .fit()

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_239574653feee65f.png)

fit the x and y data and the batch size is 256 so we show it 256 examples at the same time, epochs is how much times it will read the same data over and over.

  

We now want to save the model. Model.save() style

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_27a8a8ca810ece54.png)

run the program and wait….

The loss is:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_2ad0465d5d2305ed.png)

2. not too bad

now instead of building the model over and over again, we can just reference that model is the shakespeare model file.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivnc_tmp_2ac94c6ce17f2c6e.png)

### Generation

What our model does is it takes a sequence then predicts the next character. We need to make it somehow generate text. To do that, we need a helper function:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_62f943540bc1a880.png)

we create a helper function to grab the most likely outcome from a probability array.

Remember that the output of our network is softmax of the likely characters that will be used.

The helper function takes one of them depending on the temperature, it will pick either very conservative(highest activation value) or somewhat experimental(2nd or 3rd highest activation values)

again, it only picks 1 character.

Higher temperature will pick a character thats a little more risky to pick, lower temperature sticks more closely to the generated results

  

the last function we need is the function to generate text.

Sample requires a prediciton. Text gen will give it that prediction

it has 2 arguments.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_4aa022607d2cfd76.png)

the length of the text we want to generate and the temperature that we directly pass to the sample function.

What we want to do in this function is start with a starting text. The starting text is the input for our neural network. The neural network will predict the first next character. We can make this input the first 40 characters of shakespeare’s text. Everything that follows after that 40 characters is generated by our neural network. If you want a text completely generated by the neural network, you will need to cut off the first 40 characters, its impossible for it to generate on its own without input.

  

So we will give it the starting text now. Lets first slice the text to get that starting 40 characters.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_3e55caa71936ea1d.png)

  

we grab it directly from the text. Start index is a random character in the text, it can be anywhere except in the final 40 characters because we want to get the 40 characters after it to. Then we slice text from the starting index to starting index + 40 to get our sentence.

  

Then lets generate the text.

We have a generated string which will hold the final generated sentences.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_aca08edb31a11333.png)

add the sentence from the original text so we can generate from it.

Now lts generate. Inside a for loop for the length of length. We generate length ammount of characters.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_46dd2a7e5033fbfb.png)

inside this loop, we are going to turn our sentence text into a numpy array

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_2c5b1f9bcbfffe24.png)

now lets feed that into our model.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_4f1ba2f56cdbb44a.png)

predictions we feed it the x value. Then we get the next index which is the number representation of our character, we convert that to the character

we do a few touches to make the loop work for the next iteration.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_bbdeef18719429d8.png)

save the next character in our generated text, then shift the sentence left a bit to include the next character and finally return the generated characters

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_aee675476f6128d7.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivo8_tmp_99d3ee27a4b146ca.png)