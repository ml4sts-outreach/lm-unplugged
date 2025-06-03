---
title: Welcome to My Landing Page
site:
  hide_outline: true
  hide_toc: true
  hide_title_block: true
---

<!-- https://mystmd.org/guide/website-landing-pages -->


+++ {"kind": "justified"}

# What is AI

Modern AI, the biggest models are chatbot-powering LLMs, large language models. In this activity, we will discover what those are and start to build up intuition for how they work, where they come from and how they can fail.

An important thing to udnerstnad when you encounter a new technology is what it is good for, what it does not do well, how is it effective and not. What are the risks and the limitations. There are challenges in many different ways.

In this, we are going to take the idea that a lot of the complexity in an LLM is because the language(s) that they are modeling are also large and complex. English has an inderminitely sized vocabulary, it is totally valid for us to create new words when we want them. So, for this activity, we are going to model a small language. It will have only four words to start, then we will build up what we need to have a model, nd see how the generation works.

Next we'll see one way to train and how training data can impact what the the model learns.

We have a tools that will allow you to work online lightly and make your won tinty tiny language, author documents with it, train a tiny model with a few hyper parameters tha tyou can control. hyper parameters are the settings we use in the training proces and the structure of the model that change how it works.

We can then add more complexity in a few different ways and you can test out your ideas and author them digitally. For the a few, we can also impelemtn them with physical objects and compare and extend them.


+++ {"kind":"centered","class":"slide"}


## LLM



+++ {"kind":"centered","class":"slide"}

## Large Language Model

Let's break this down:
- model:
- language
- large


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
