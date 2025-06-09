---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Low code Example


We have also developed a Python module that allows for a low-code version
that will visualize the unplugged activity in a website or jupyter notebook.

```{warning}
The package is currently not broadly installable (not packaged), here we locally import it
```

```{code-cell} python
from lmunplugged import Bin,Table, Ball, Sticky, Doc, TrainDemo
```

We can load a preset from a file, just to display it:
```{code-cell} python
Table.from_csv('init.csv')
```

or save it  to a variable for future use
```{code-cell} python
preset = Table.from_csv('init.csv')
preset
```

:::{note}
notice the balls are placed randomly each time it is loaded!
:::

We can sample whole documents: 
```{code-cell} python
preset.sample_doc('blue')
```

```{code-cell} python
preset.sample_doc('purple')
```

```{code-cell} python
preset.sample_doc('green')
```


## Visualizing the training process 

We can prepare to demo the training process from a fixed document: 

```{code-cell} python
train_doc = Doc.from_list(['green','blue','purple','blue','pink','blue','white'],
                    max_width_words = 5)
to_train = Table.from_list(['purple','blue','green','pink'])

my_demo = TrainDemo(to_train, train_doc)
my_demo
```

and train:


```{code-cell} python
my_demo.train_step(1)
```




```{code-cell} python
my_demo.train_step(2)
```

```{code-cell} python
my_demo.train_step(3)
```


```{code-cell} python
my_demo.train_step(4)
```

```{code-cell} python
my_demo.train_step(5)
```

```{code-cell} python
my_demo.train_step(6)
```


```{code-cell} python
print(my_demo.table.bins['green'].contents[0])
```

## Built up from components


```{code-cell} python
pinkbin = Bin('magenta')
purplebin = Bin('purple',contents =[Ball('purple'),Ball('white')])
greenbin = Bin('lime')
bluebin = Bin('blue', contents =[Ball('purple'),Ball('blue'),
                Ball('lime'),Ball('magenta'),Ball('white')])

greenbin.add_ball(Ball('purple'))
greenbin.add_ball(Ball('lime'))
pinkbin.add_ball(Ball('white'))
pinkbin.add_ball(Ball('lime'))
pinkbin.add_ball(Ball('blue'))

tab = Table([bluebin,pinkbin,greenbin,purplebin])
tab
```

```{code-cell} python
bluebin.add_ball(Ball('lime'))
bluebin.add_ball(Ball('magenta'))
tab
```

let's start a doc by prompting it to be blue 
```{code-cell} python
prompt = [Sticky('blue')]
doc = Doc(prompt)
doc
```

Next, we sample from the blue bin and add that to our document

```{code-cell} python
sampled_word = bluebin.sample()
```



```{code-cell} python
:tags: ["remove-cell"]
is_white = sampled_word=='white'
continue_lang = {True:'since it is white we are done, but the cell below shows how we would continue',
                False:'since it is not white, we continue'}
```
we got {eval}`sampled_word`, lets add it to the doc:

```{code-cell} python
doc.add_word(sampled_word)
```

{eval}`continue_lang[is_white]`

```{code-cell} python
while not(sampled_word=='white'):
    sampled_word = tab.sample_bin(sampled_word)
    print(sampled_word)
    doc.add_word(sampled_word)

doc
```

