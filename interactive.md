---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Interactive use

Use the button to the right to make this page interactive! 

```{code-cell} python
:tags: ["remove-cell"]
from lmunplugged import Bin,Table, Ball, Sticky, Doc, TrainDemo
import ipywidgets as widgets
from IPython.display import display, Markdown, HTML
```


When you click the button it iwll update the document

```{code-cell} python
:tags: ["hide-cell"]
doc_text_area_btn = widgets.Textarea(
    value='purple blue pink blue white',
    placeholder='Type something',
    description='Document:',
    disabled=False
)

button = widgets.Button(
    description="render doc",
    button_style='info', 
    layout=widgets.Layout(width='100px', height='30px')
)


doc = Doc.from_string(doc_text_area_btn.value)

html_output = widgets.Output()

def update_doc_button(b):
    print('clickd')
    my_doc = Doc.from_string(doc_text_area_btn.value)
    with html_output:
        html_output.clear_output(wait=True)
        display(my_doc)

button.on_click(update_doc_button)
ctrl = widgets.HBox([doc_text_area_btn, button])
layout = widgets.VBox([ctrl,html_output])
```



The code is hidden, but will work! 
```{code-cell} python
display(layout)
```

## Using Colors

```{code-cell} python
:tags: ["remove-cell"]

# TODO: fix this demo to use Doc.is_valid and to disable buttons at end fo doc instead of resetting
initital_doc = ['green','blue','purple','blue','pink','blue','white']
bin_colors = ['purple','blue','green','pink']
allowed_colors = bin_colors + ['white']
color_tags = widgets.ColorsInput(
    value=initital_doc,
    allowed_tags=allowed_colors,
    # allow_duplicates=False
)

my_doc = Doc.from_list(color_tags.value,max_width_words=5)
to_train = Table.from_list(bin_colors)

my_demo = TrainDemo(to_train, my_doc)

html_output_demo= widgets.Output()
with html_output_demo:
    display(my_demo)

def set_demo_button(b):
    my_demo.doc.reset_words(color_tags.value)
    my_demo.reset_training()
    with html_output_demo:
        html_output_demo.clear_output(wait=True)
        display(my_demo)


def train_step(b):    
    with html_output_demo:
        html_output_demo.clear_output(wait=True)
        display(my_demo.train_next())



demo_button = widgets.Button(
    description="load doc",
    button_style='info', 
    layout=widgets.Layout(width='100px', height='30px')
)

step_button = widgets.Button(
    description="step",
    button_style='success', 
    layout=widgets.Layout(width='100px', height='30px')
)

demo_button.on_click(set_demo_button)
step_button.on_click(train_step)
demo_ctrl = widgets.HBox([ demo_button,step_button])
layout = widgets.VBox([color_tags,demo_ctrl,html_output_demo])
```

```{code-cell} python
display(layout)
```

## free update no button (has errors)

The code is hidden, but will work! 
```{code-cell} python
doc_text_area = widgets.Textarea(
    value='purple blue green pink blue white',
    placeholder='Type something',
    description='String:',
    disabled=False
)
def update_doc(text_area):
    my_doc = Doc.from_string(text_area)
    display(my_doc)
# doc_text_area.observe(update_doc, names='value')
widgets.interact(update_doc,text_area = doc_text_area)

```