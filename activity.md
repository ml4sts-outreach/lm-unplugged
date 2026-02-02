---
kernelspec:
  name: python3
  display_name: 'Python 3'
---


# Activity

:::{note} 
:class: dropdown
:open: true

:::


## LLM

- AI has been the goal of CS for a long time
- Many strategies, most recently machine learning, finding patterns in data instead of writing code explicitly
- Current shift is LLMs or more broadly generative models
- LLM = Large Language Models

### Models

- simplification in order to communicated an idea
- ex: a volcano demo
- ex: diarama
- ex: globe
- ex: atom model with rings
- for computing, always a mathematical model
- in ML, typically a statistical model
- familiar mathematical model: line
- describes assumptions about the world

### Language

- consists of words and grammar
- in NLP we discuss tokens (approx words, but sometimes smaller) and documents (units of text to analyze)
- communicates ideas


### Large

- broadly: "bigger" is more complex
- refers to the number of parameters
- a line has two parameters: slope & intercept
- GPT 3 had 175 Billion parameters

## A Generative Trick

Over time, ML has done many different models, but the one that happens to have hit is a *generative* language model. 

It starts with a simple assumption:

> We can generate sequences of words by sampling from a distribution of what word comes next given a sequence of past words. 


Specifically, to generate word number $j$ given $n$ previous words:

$$P (w_j| w_{j-1}, w_{j-2},\ldots, w_{j-n})$$

Then we make computer code that implements this distribution and operations on it (like sampling).

:::{admonition} detail

this is what the neural network describes

:::


## A Tiny Language for a Small model

We need Large models to describe and mimic complex things like natural spoken languages (eg English, ...) and the many programming languages. To make it something small enough we can really get a good idea of, we will use a small langauge. 


```{code-cell} python
:tags: [remove-input]
from lmunplugged import Bin,Table, Ball, Sticky, Doc, TrainDemo
```

Our language will have just four words and one symbol for end of document.  We will "write" in the language using sticky notes in five different colors. 

```{code-cell} python
:tags: [remove-input]
vocab_list = [Sticky('purple'), Sticky('blue'),Sticky('green'),  Sticky('pink'),  Sticky('white')]
vocab = Doc(vocab_list)
vocab
```

### A pretrained model

We will use only the 1 past word to predict the next word.  Since our language only has 4 words and one end of document symbols the previous word can be any of the four words and the next word can be any of the four words or end of document.  This means that we can represent the distribution for our model with a 4x5 table: 


```{code-cell} python
:tags: [remove-input]
preset = Table.from_csv('init.csv')
preset.get_df()
```

We will represent this physically with four bins (for each possible previous word) and five different colored balls (for each possible next word): 

```{code-cell} python
:tags: [remove-input]
preset
```

### Generating Documents

```{code-cell} python
:tags: [remove-input]
prompt = Sticky("blue")
doc = Doc([prompt],max_width_words=6)
```



We will prompt with {eval}`prompt.name` so at first the document looks like: 

```{code-cell} python
:tags: [remove-input]
doc
```

Then we will sample draw a ball from the {eval}`prompt.name` bin. 


```{code-cell} python
:tags: [remove-input]
sampled_word = preset.sample_bin(prompt.name)
is_white = sampled_word =='white'
continue_lang = {True:'since it is white we are done',
                False:'since it is not white, we continue sampling until we get a white'}
```
we got {eval}`sampled_word`, lets add it to the doc:

```{code-cell} python
doc.add_word(sampled_word)
```

{eval}`continue_lang[is_white]`

```{code-cell} python
:tags: [remove-input]
while not(sampled_word=='white'):
    sampled_word = preset.sample_bin(sampled_word)
    doc.add_word(sampled_word)

doc
```

Let's  propmt with a few more times and draw additional documents. 

```{code-cell} python
:tags: [remove-input]
preset.sample_doc('blue')
```

```{code-cell} python
:tags: [remove-input]
preset.sample_doc('purple')
```

```{code-cell} python
:tags: [remove-input]
preset.sample_doc('green')
```

### Training



We can prepare to demo the training process from a fixed document: 

```{code-cell} python
:tags: [remove-input]
train_doc = Doc.from_list(['green','blue','purple','blue','pink','blue','white'],
                    max_width_words = 5)
to_train = Table.from_list(['purple','blue','green','pink'])

my_demo = TrainDemo(to_train, train_doc)
my_demo
```

and train by looking at the first two stickies to start: 


```{code-cell} python
:tags: [remove-input]
my_demo.train_step(1)
```

and then go to the next two: 

```{code-cell} python
:tags: [remove-input]
my_demo.train_step(2)
```

```{code-cell} python
:tags: [remove-input]
my_demo.train_step(3)
```


```{code-cell} python
:tags: [remove-input]
my_demo.train_step(4)
```

```{code-cell} python
:tags: [remove-input]
my_demo.train_step(5)
```

```{code-cell} python
:tags: [remove-input]
my_demo.train_step(6)
```


## Variations


### Context Two

We have so far used a model with a context length of one, but real models have longer context windows. 

We will have context windows of length two and then we can keep the words and we can make longer and longer to then start to conta better words and more choerent ideas

in LLMs there are often a context length of 1000-4000+ tokens. Tokens are a bit shorter than words, 1000 words is usually bout 750 words. 

We can do context length of two by putting two labels on each bin. 

```{code-cell} python
:tags: [remove-input]
ctx2 = Table.from_csv('context_two.csv')
ctx2
```

```{code-cell} python
:tags: [remove-input]
purpur = Bin(['purple','purple'])
purpur
```



### Impact of Training

Split the group into two groups and give each group a different rule, then train the two models. 

Discuss the differences. 