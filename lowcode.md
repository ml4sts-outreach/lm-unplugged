---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

```{code-cell} python
from lmunplugged import Bin,Table, Ball,Sticky,Doc
from random import choice
from IPython.display import SVG

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
SVG(tab.render())
# redbin.render().as_str()
```

```{code-cell} python
bluebin.add_ball(Ball('lime'))
bluebin.add_ball(Ball('magenta'))
SVG(tab.render())
```

let's start a doc by prompting it to be blue 
```{code-cell} python
prompt = [Sticky('blue')]
doc = Doc(prompt)
SVG(doc.render())
# Sticky('purple').get_elements()
```

Next, we sample from the blue bin and add that to our document

```{code-cell} python
sampled_word = bluebin.sample()
is_white = sampled_word=='white'
continue_lang = {True:'since it is white we are done',
                False:'since it is not white, we continue'}
```
we got {eval}`sampled_word`, lets add it to the doc:

```{code-cell} python
doc.add_word(sampled_word)
SVG(doc.render())

```

{eval}`continue_lang[is_white]`

```{code-cell} python
while not(sampled_word=='white'):
    sampled_word = tab.sample_bin(sampled_word)
    print(sampled_word)
    doc.add_word(sampled_word)

SVG(doc.render())
```