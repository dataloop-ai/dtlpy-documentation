## Uploading Data Samples

If you followed up the onboarding tutorial so far, you should have created and selected a dataset already. This means you are now ready to add data samples to your dataset and then learn how to annotate them.

Data samples you upload to your dataset will be stored in something called an "item". Items are Dataloop objects belonging to the custom Dataloop "Item" class. They are represented as a Dataloop data model objects and are stored as a "json" file. Items contain the data sample you upload and the afferent metadata that you add to that data sample.

To do that, you must first create a local directory on your computer, where you will place your data samples. If you are on windows, for example, you can create a folder at "C:\UploadDemo". Now you need to place an image (any image you have laying around). Then, I recommend you rename it to "test1.jpg". Now you can upload that sample to the dataset we created in the last chapter, using the following command:

```python
dataset.items.upload(local_path=r'C:\UploadDemo\test1.jpg')
```





<br>If everything goes right, you should get something simmilar to the output below: <br>
<div class="gatsby-highlight" data-language="text"><pre class="language-text"><code class="language-text">Upload Items: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00&lt;00:00,  1.54it/s]
Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/'632c24ae3444a86f029acb47', created_at='2022-09-22T10:18:03.000Z', dataset_id='632c24ae3444a86f029acb47', filename='/test1.jpg', name='test.jpg', type='file', id='632dadf7b28a0c0da317dfc8', spec=None, creator='JohnDoe@gmail.com', _description=None, annotations_count=0)</code></pre></div>

In there you will also see an "id" line, which refers to the item's id code. Keep that in mind, since we will use it. Now  you can get the image you just uploaded, from the dataset, and then print the item's details, using the following lines of code:

<pre class="language-python">
<code class="language-python">item <span class="token operator">=</span> dataset<span class="token punctuation">.</span>items<span class="token punctuation">.</span>get<span class="token punctuation">(</span>item_id<span class="token operator">=</span><span class="token string">'my_item_id'</span><span class="token punctuation">)</span>
item<span class="token punctuation">.</span><span class="token keyword">print</span><span class="token punctuation">(</span><span class="token punctuation">)</span></code></pre>

Remember that you need to replace "my_item_id" with the item id you got after you uploaded your data sample. Or, you can just print that item's details using this simple line of code:
```python
print(item)
```
Now that the sample has been uploaded, you can also open it in web view, using the following code:
```python
item.open_in_web()
```
This will open a new tab, where you will see the sample you just uploaded. In the URL you will be able to see all of the ID for Project, dataset and item:

![image](https://user-images.githubusercontent.com/58508793/216602773-016eee27-a914-4922-8a5e-938c3d0eecd7.png)


You can also loop through all of the items in the dataset, and print their details, using the following code:

<pre class="language-python"><code class="language-python">pages <span class="token operator">=</span> dataset<span class="token punctuation">.</span>items<span class="token punctuation">.</span><span class="token builtin">list</span><span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token keyword">for</span> item <span class="token keyword">in</span> pages<span class="token punctuation">.</span><span class="token builtin">all</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    item<span class="token punctuation">.</span><span class="token keyword">print</span><span class="token punctuation">(</span><span class="token punctuation">)</span></code></pre>

For the best results, I suggest you upload multiple items before using the command above.

## Annotating items
Dataset items are annotated using Labels. A Label is composed of various Label Settings and Instructions that are defined by a dataset’s [Recipe](https://dataloop.ai/blog/data-recipes/). For example, an item can contain 1 label defined as a Classification, to categorize the entire data sample. It can also contain multiple labels covering only parts of your data sample, to identify specific sections of that item.

### Classification
Classification is used to categorize an entire data sample. For example, a Classification label can be used to classify product images under categories, subcategories, and characteristics, such as men’s clothes, polo shirts, hand cremes, etc.

The Python SDK can add Classification labels to an item using 2 steps:

1. Firstly, you need to add a label to be part of the dataset (create label);
2. Add that label to the item you wish (to classify it).

To complete the first step, you can run the following command to add a Label (Person) to the "My-First-Dataset" dataset's list of labels:

<pre class="language-python"><code class="language-python">dataset<span class="token punctuation">.</span>add_label<span class="token punctuation">(</span>label_name<span class="token operator">=</span><span class="token string">'Person'</span><span class="token punctuation">)</span></code></pre>

After executin that code, you should get something similar to this result:
<div class="gatsby-highlight" data-language="text"><pre class="language-text"><code class="language-text">[Label(tag='Person', display_data={}, color='#0214a7', display_label='Person', attributes=[], children=[])]</code></pre></div>

The second step is to annotate the image you just uploaded:

<pre class="language-python"><code class="language-python">builder <span class="token operator">=</span> item<span class="token punctuation">.</span>annotations<span class="token punctuation">.</span>builder<span class="token punctuation">(</span><span class="token punctuation">)</span>
builder<span class="token punctuation">.</span>add<span class="token punctuation">(</span>annotation_definition<span class="token operator">=</span>dl<span class="token punctuation">.</span>Classification<span class="token punctuation">(</span>label<span class="token operator">=</span><span class="token string">'Person'</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
item<span class="token punctuation">.</span>annotations<span class="token punctuation">.</span>upload<span class="token punctuation">(</span>builder<span class="token punctuation">)</span></code></pre>

Now the item you added a bit earlier is successfully annotated and classified with the label "Person".

### Example: Annotating images using Point Markers
A Point Marker is used to identify specific regions in your data samples. For example, it can identify regions where objects are present, in an image or video item, like an image of a person's face that contains multiple Point Marker labels specifying where the person’s eyes, mouth, ears, etc. are.

Point Marker commands accept 2 sets of coordinates (x, y) as input parameters, which specify the location which you want to label.
Just as in the case of Classification, we need to first create the label and add it to the dataset, before we can use it. Let's just add a new label to our current dataset:

<pre class="language-python"><code class="language-python">dataset<span class="token punctuation">.</span>add_label<span class="token punctuation">(</span>label_name<span class="token operator">=</span><span class="token string">'Ear'</span><span class="token punctuation">)</span></code></pre>

Easy, right? Now you can add the "Ear" label we just created to a specific region of your image:

<pre class="language-python"><code class="language-python">builder <span class="token operator">=</span> item_1<span class="token punctuation">.</span>annotations<span class="token punctuation">.</span>builder<span class="token punctuation">(</span><span class="token punctuation">)</span>
builder<span class="token punctuation">.</span>add<span class="token punctuation">(</span>annotation_definition<span class="token operator">=</span>dl<span class="token punctuation">.</span>Point<span class="token punctuation">(</span>x<span class="token operator">=</span><span class="token number">80</span><span class="token punctuation">,</span> y<span class="token operator">=</span><span class="token number">80</span><span class="token punctuation">,</span> label<span class="token operator">=</span><span class="token string">'Ear'</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
builder<span class="token punctuation">.</span>add<span class="token punctuation">(</span>annotation_definition<span class="token operator">=</span>dl<span class="token punctuation">.</span>Point<span class="token punctuation">(</span>x<span class="token operator">=</span><span class="token number">120</span><span class="token punctuation">,</span> y<span class="token operator">=</span><span class="token number">120</span><span class="token punctuation">,</span> label<span class="token operator">=</span><span class="token string">'Ear'</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
item_1<span class="token punctuation">.</span>annotations<span class="token punctuation">.</span>upload<span class="token punctuation">(</span>builder<span class="token punctuation">)</span></code></pre>

After this, you can open the sample in web view, to see the new labels you have added, using the following command:
```python
item.open_in_web()
```

Congratulations, you just learned how to create and select a dataset, add data samples to it and then anotate those items.

In the next chapter, you will learn the basics of filtering the data items from your dataset, which is extremely helpful when you have a high number of data samples.

