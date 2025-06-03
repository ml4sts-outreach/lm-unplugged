---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
import svg
import itertools as itt
from random import random, shuffle,sample
from numpy import linspace
from  matplotlib._color_data import XKCD_COLORS
from random import choice
import pandas as pd
from IPython.display import SVG as ipySVG
```

```{code-cell} ipython3
dist_init = pd.read_csv('init.csv',index_col=0)
dist_init
```

```{code-cell} ipython3
words = list(dist_init.columns)
non_stop = list(dist_init.index)
```

```{code-cell} ipython3
sample([ki for k,v in dist_init['pink'].to_dict().items() for ki in [k]*v],1)
```

```{code-cell} ipython3
def next_word(prev,dist =dist_init):
    if isinstance(prev,list):
        # print(type(prev))
        prev = tuple(prev)
    cur_dict = dist.loc[prev].to_dict().copy()
    # print(cur_dict)
    cur_dist = [ki for k,v in cur_dict.items() for ki in [k]*v]
    # print(cur_dist)
    return sample(cur_dist,1)[0]
```

```{code-cell} ipython3
next_word('blue')
```

```{code-cell} ipython3
def sample_doc(prompt,context_len=1,dist =dist_init):
    doc = prompt
    nxt_word = doc[-1]
    # print ("prompt: ",prompt)
    while not(nxt_word  == 'white'):
        prev = doc[-context_len:]
        # print(prev)
        nxt_word = next_word(prev,dist)
        # print(nxt_word)
        doc.append(nxt_word)
    return doc

```

```{code-cell} ipython3
sample_doc(['blue'])
```

```{code-cell} ipython3
def train(doc_list,context_len):
    # create df of 0s
    to_train = pd.DataFrame(columns = words,data=0,
                            index = pd.MultiIndex.from_product(tuple([non_stop]*context_len)))
    for doc in doc_list:
        # print(doc)
        row = tuple(doc[:context_len])
        for w in doc[context_len:]:
            to_train.loc[(row),w] +=1
            row = row[1:] + (w,)
    return to_train
```

```{code-cell} ipython3
doc_list = [sample_doc(sample(words[:-1],1)) for i in range(400)]
```

```{code-cell} ipython3
good_docs = [d for d in doc_list if len(d) >3 and len(d)<10]
len(good_docs)
```

```{code-cell} ipython3
learned_dist2 = train(good_docs,2)
```

```{code-cell} ipython3
learned_dist1 = train(doc_list,1)
```

```{code-cell} ipython3
learned_dist1.div(learned_dist1.sum(axis=1).values,axis=0)
```

```{code-cell} ipython3
dist_init.div(dist_init.sum(axis=1).values,axis=0)
```

```{code-cell} ipython3
learned_dist2
```

```{code-cell} ipython3
[sample_doc(sample(words[:-1],2),dist=learned_dist2,context_len=2) for i in range(4)]
```

```{code-cell} ipython3
words
number = {w:i for i,w in enumerate(non_stop)}
number
```

words can only go in order, unless a double word.
1 skip is okay. 
purple is valid after pink

-  plurple green is okay
- purlpe, green, blue is not
- green green blue is okay

doc can end at anytime

```{code-cell} ipython3
valid_words_next_double = {w:[w,non_stop[(i+1)%4],words[-1]] for i,w in enumerate(non_stop)}
valid_words_next2_double = {w:[w,non_stop[(i+1)%4],non_stop[(i+2)%4],words[-1]] for i,w in enumerate(non_stop)}
# ,non_stop[(i+2)%4]

# {w:non_top
# [[non_stop[(i+1)%4],non_stop[(i+2)%4]] for i in range(4)]
valid_words
```

```{code-cell} ipython3

def grammar_check(doc,valid_words=valid_words_next_double):
    past_word = doc[0]
    valid=True
    double_past=doc[0] ==doc[1]
    for word in doc[1:-1]:
        cur_valid = valid_words[past_word]
        # print(past_word,word,double_past,cur_valid)
        if not(word in cur_valid) and not double_past:
            valid=False
            break
        
        
        double_past = word ==past_word
        past_word = word
    # last must be white
    if not(doc[-1] =='white'):

        valid=False
    return valid
    
def gen_valid(valid_words=valid_words_next_double):
    doc = sample(non_stop,1)
    double_past = False
    while not(doc[-1] =='white'):
        if double_past:
            doc += sample(words,1)
        else:
            cur_valid = valid_words[doc[-1]]
            doc += sample(cur_valid+cur_valid[:-1],1)
        double_past = doc[-1] ==doc[-2]
    return doc

def gen_valid_prompt(n,valid_words=valid_words_next_double):
    doc = sample(non_stop,1)
    double_past = False
    for i in range (n-1):
        if double_past:
            doc += sample(words,1)
        else:
            cur_valid = valid_words[doc[-1]]
            doc += sample(cur_valid+cur_valid[:-1],1)
        double_past = doc[-1] ==doc[-2]
    return doc
```

```{code-cell} ipython3
grammar_check(['purple','green','white'])
```

```{code-cell} ipython3
grammar_check(['purple','green','blue','white'])
```

```{code-cell} ipython3
grammar_check(['green','green','blue','white'])
```

```{code-cell} ipython3
grammar_check(['blue','green','green','blue','white'])
```

```{code-cell} ipython3
grammar_check(['blue','green','pink','pink','green','purple','white'])
```

```{code-cell} ipython3
gen_valid()
```

```{code-cell} ipython3
valid_sample = [gen_valid() for i in range(400)]
len(doc_list)
```

```{code-cell} ipython3
good_docs = [d for d in valid_sample if grammar_check(d)]
len(good_docs)
```

```{code-cell} ipython3
good_train1 = train(good_docs,1)
good_train2 = train(good_docs,2)
good_train2
```

```{code-cell} ipython3
valid_words
```

```{code-cell} ipython3
grammar_check(['purple','green','blue','white'])
```

```{code-cell} ipython3
good_train1
```

```{code-cell} ipython3
re_train1 = [sample_doc(sample(non_stop,1),dist=good_train1,context_len=1) for i in range(100)]
re_train2 = [sample_doc(gen_valid_prompt(2),dist=good_train2,context_len=2) for i in range(100)]
```

```{code-cell} ipython3
re1_good = [d for d in re_train1 if grammar_check(d)]
re2_good = [d for d in re_train2 if grammar_check(d)]
len(re1_good),len(re2_good)
```

```{code-cell} ipython3
[(d,grammar_check(d)) for d in re_train2 ]
```

```{code-cell} ipython3
valid_words
```

```{code-cell} ipython3

```
