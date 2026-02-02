---
title: LMs, Unplugged
site:
  hide_outline: true
  hide_toc: true
  hide_title_block: true
---

<!-- https://mystmd.org/guide/website-landing-pages -->


+++ {"kind": "justified"}

# What is AI


What is AI and where does it come from?

There are lots of different types, but the most common current and most popular that has changed thigns is an LLM.

An LLM is a large language model,

what does this mean? let's break it down.

we'll start with a model

a model is a simplificaiton of something that conveys important ideas. We use them in science a lot and we might see different ones all mosedl are wrong, but some are useful, or at least useful in some contexts. some familiar models might be a the model of an atom, the model of a volcano, a model train. they convey somme important things, but there are also errors in them. to implement a model in a computer, t's always a mathematical mdoel, in most machien learning, it's specifically a statistical model.

we can model thing sisn different ways.

in this case it is a model of language, what does it mean that it is language, we can define it. language consistes of wrokds and a grammar and somethign sood.

languages have lot of workd sin or der o work with them we can do didfferent hting sand this ib sthe best way forwad

it is alarge model, a large languag emodel it means it is a lot of parameters. the parameters are the function we write. aparameter and the function tht this can be that this can be what it is.

to get the idea of parameter and how comples they are, let's look at a familiar equation, the one for a line. we can fit one liek this a. line can be describd with two parameters. one for the slope and one for the intercept. if we want to make the equation a bit more compex, we can add more parameters, a parabola, can have x parameters, we can make a model more and more complex with different functions.

a neural network uses more and more parameters.

we can have one neuon that look liek this

we can add more things

we can addmore pparameter and more neurons and each one works liek this

we can mkae this work,. we can make them all . the big lls have billions of parameters, hundreds of billions of parameters.

this means these models are really complex,

...

how do we model language. over time, we ahve modeled lanaguge in different ways for differnt purposes, but for generative AI, they have modeled lanague as a distribution of what word comes after the current sequence of words.

SO for example, if we have "hello how are" different words are diffren tprobabilites some are more likely than others, then when we generate we sample fromt he one. in some cases, the right word willmmosty come out

in others it can do weird thigns.

in a language like english, we neeed to do a bunch of otehr thigns to the langauge to get it into numerical representations, we're going to set those aside for now.

WIf we make a simpler language, we can ahve a simpler model.

so here is a langague athat conists of four words, with one end of document symbol.

Here is a model based on this language, we can represent it with just 20 parameters for each word, we have a probabliy for each of the next possible words.

we can represent this as a percent chance of each word coming up. as we have here or we can reprsent it with ping pong balls in prportion in the a bucket. we will make sure that each one will be there in proportion. so with 10 5 chance we gget this and that we cant erh net, and so on.

we can make one for each possible previous word, so we ahve 4 total bins.

Now, we can simulate how an LLM generates. we need a prompt

then we draw, and keep drawing until we draw the white ball to end the document.

Now we can draw another one. and and another. we can get diffeetn types of docuemtns and different lengths and different lagnthes. and differen words that start out differnt ways.

we can prompt a few but one thin si that if we prompt longer it does not chagne that much

...

where does a model come from though?

a model comes from traingin.

inn an llm they get the data from the internet and they use a variet of sources.

in each different lenght we get the way set up. and that this can be

in our case, we are going to author some documents, and then we'll train amodel. we are going to pass out the stickies and when we get them document authroed, you can come up to. I am going to go through waht the trainign looks liek one example ehre

so we will train by looking at the firtst wrod then adding the next token and then thennext

and then we get to draw samples out. we draw diffrent numbers.

first is blue then we look at the lbueone thene xt workd is green so we bput a green ball in the blue bucket, next we look at the green bucket and the next workd bis purple, so we put a purple ball in the green bin. next green bin, but the next word is pink, then teh pink ball to the green bin. and so on. we get a lot of to the end. then we pput the last wone in.

next we think about how things.

so author your documents and then come up and train.

No, we can draw documents. we have differnet docuemtns.

If. you are on the left, ou train here ad then we train t the other side.

Now we can train things on each side.

we have two models and two sets of samples generated.

Next we can make this. we will compre, we can see if anythign worked out.

So what is different than when you use a bigger langauge model? One difference is that things are shorter, we need to have longer understanding, we need to have thin

we can make sure that things are better

we need a longer context window. We can make a longer context window by training and looking at the longer two window lenght. we can do this next, so we'll take next the same documents you have already have and we'll train again. (and another brak). As you were training the first time, the helpers made note of your things, so that we can now fill in a longer context windoow lenght. we hvae now two things.

we can make thigns

we can add different documents that wer longer.

we are doing two wrods, now. Can we do two window length, we will next and take how they are the longer we have to have these thigns set up.

we hav to have set of rules to make the documents differnt so that e can think about how they are. maybe the docs look more like and have similar thigns and windows and we can make sure that

we will have context window lenght o two and then we can see th tse are bidferetn.


+++ {"kind":"centered","class":"slide"} 


```{figure} /img/clean-train.svg
:alt: second step in training
:align: center

the chaotic figure with all of the arrows that can be used to generate others
```

+++ {"kind":"centered","class":"slide"}


## LLM



+++ {"kind":"centered","class":"slide"}

## Large Language Model

Let's break this down:
- model:
- language
- large

+++ {"kind":"centered","class":"slide"}
## P(next word| past words)

```{list-table}
* - .
  - ```{image} img/sticky-purple.svg
    :width: 100px
    ```
  - ```{image} img/sticky-blue.svg
    :width: 100px
    ```
  - ```{image} img/sticky-green.svg
    :width: 100px
    ```
  - ```{image} img/sticky-pink.svg
    :width: 100px
    ```
  - ```{image} img/sticky-white.svg
    :width: 100px
    ```
* - ```{image} img/sticky-purple.svg
    :width: 100px
    ```
  - 10%
  - 30%
  - 10%
  - 30%
  - 20%
* - ```{image} img/sticky-blue.svg
    :width: 100px
    ```
  - 10%
  - 10%
  - 40%
  - 20%
  - 20%
* - ```{image} img/sticky-green.svg
    :width: 100px
    ```
  - 10%
  - 20%
  - 20%
  - 30%
  - 20%
* - ```{image} img/sticky-pink.svg
    :width: 100px
    ```
  - 40%
  - 10%
  - 10%
  - 10%
  - 30%
```

+++{"kind":"centered","class":"slide"}

## A pretrained model, as represented with balls in bins
```{figure} /img/trained-model.svg
:label: trained
:alt: second step in training
:align: center

a trained model represented with balls in bins
```




+++{"kind":"centered","class":"slide"}

```{figure} /img/training-demo00.svg
:label: training0
:alt: first step in training
:align: center

First, we look at the first word, and go to the corresponding bin. We focus on the green bin. 
```

<!-- 
+++ {"kind":"centered","class":"slide"} 
-->


```{figure} /img/training-demo01.svg
:label: training1
:alt: second step in training
:align: center

next, we add a ball in the next color in that bin. So, we add a blue ball to the green bin
```

<!-- 
+++ {"kind":"split-image","class":"slide"}
 -->

```{figure} /img/training-demo02.svg
:label: training2
:alt: second step in training
:align: center

now we lok at the blue bin
```
<!-- 
+++ {"kind":"centered","class":"slide"}
 -->

```{figure} /img/training-demo03.svg
:label: training3
:alt: second step in training
:align: center

and add the next color
```


+++ {"kind":"centered","class":"slide"}

```{figure} /img/training-demo04.svg
:label: training4
:alt: second step in training
:align: center
```

+++ {"kind":"centered","class":"slide"}

```{figure} /img/training-demo05.svg
:label: training5
:alt: second step in training
:align: center
```



+++ {"kind":"centered","class":"slide"}

```{figure} /img/training-demo06.svg
:label: training6
:alt: second step in training
:align: center
```


+++ {"kind":"centered","class":"slide"}

```{figure} /img/training-demo07.svg
:label: training7
:alt: second step in training
:align: center
```


+++ {"kind":"centered","class":"slide"}
```{figure} /img/training-demo08.svg
:label: training8
:alt: second step in training
:align: center
```
+++ {"kind":"centered","class":"slide"}

```{figure} /img/training-demo09.svg
:label: training9
:alt: second step in training
:align: center
```


+++{"kind":"centered","class":"slide"}


## What is different?

we will have context windows of length two and then we can keep the words and we can make longer and longer to then start to conta better words and more choerent ideas

in LLMs there are oftern a context length of 1000-4000+ tokens. tokesn are a bit shorter than words, 1000 words is usually bout 750 words. we can ha little bie tosre
