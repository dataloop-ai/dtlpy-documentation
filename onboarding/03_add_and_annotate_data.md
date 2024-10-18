# Chapter 3 - Add and Annotate data

### Uploading Data Samples

If you followed the onboarding tutorial so far, you should have created a Project and Dataset and selected that Dataset to work with. This means you are now ready to add data samples to your Dataset and then learn how to annotate them.

Data samples you upload to your dataset will be stored as something called an Item. Items are Dataloop objects belonging to the Dataloop Item class. They are represented as a Dataloop data model object and are stored as a binary object along with a JSON file that contains metadata about the Item. Item JSON files also contain metadata from annotations, for example, that you add to further describe or classify the data sample. Each Item has a `stream` method to get the data sample along with other attributes, such as the metadata, from the accompanying JSON file.

To get going, create a local directory on your computer where you will place your data sample files. If you are on Windows, for example, you can create a folder `C:\UploadDemo`. Now place an image file in that folder (any `.jpg` image you have laying around will do). Rename the file `test1.jpg` so the rest of the following steps will work as written. Now you can upload that sample to the Dataset we created in the last chapter, using the following command:

```python
dataset.items.upload(local_path=r'C:\UploadDemo\test1.jpg')
```

\
If everything goes right, you should get something similar to the output below:

```
Upload Items: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.54it/s]
Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/'632c24ae3444a86f029acb47', created_at='2022-09-22T10:18:03.000Z', dataset_id='632c24ae3444a86f029acb47', filename='/test1.jpg', name='test.jpg', type='file', id='632dadf7b28a0c0da317dfc8', spec=None, creator='JohnDoe@gmail.com', _description=None, annotations_count=0)
```

When you examine the string that shows you the attributes about the Item, you will see an `id` entry.  This refers to the Item's ID code. Copy this Item ID and paste it into a text file or similar since we will use it later. Now you can `get` and `print` the details about the image, now an Item, you just uploaded into the Dataset using the following lines of code:

```python
item = dataset.items.get(item_id=<my_item_id>)
item.print()
```

Remember to replace `my_item_id` in the `get` request with the Item ID you got after you uploaded your data sample. 

For which you should get the following output:

```python
+----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------+
|    | annotated   | filename   | name      | type   | id                       | hidden   | dir   |   annotationsCount | dataset                                                           | createdAt                | datasetId                | creator             |
|----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------|
|  0 | True        | /test1.jpg | test1.jpg | file   | 63da62df7592bf239854adc0 | False    | /     |                  3 | https://gate.dataloop.ai/api/v1/datasets/63da62d973b62f22086f1d8f | 2023-02-01T13:02:23.000Z | 63da62d973b62f22086f1d8f | email@gmail.com |
+----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------+
```

Or, you can just print that Item's details using the print function:

```python
print(item)
```

After executing the `print` code, you will get this output:

```python
Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/63da62d973b62f22086f1d8f', created_at='2023-02-01T13:02:23.000Z', dataset_id='63da62d973b62f22086f1d8f', filename='/test1.jpg', name='test1.jpg', type='file', id='63da62df7592bf239854adc0', spec=None, creator='email@gmail.com', _description=None, annotations_count=3)
```

Now that the sample has been uploaded, you can also open it in web UI, using the following code:

```python
item.open_in_web()
```

This will open a new browser tab where you will see the sample you just uploaded. In the URL you will be able to see all of the IDs for Project, Dataset and Item:

![image](https://user-images.githubusercontent.com/58508793/216602773-016eee27-a914-4922-8a5e-938c3d0eecd7.png)

You can also loop through all of the Items in the Dataset, and print their details, using the following code:

```python
pages = dataset.items.list()
for item in pages.all():
    item.print()
```

And you should get an output similar to this:

```python
Iterate Entity: 100%|████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.44it/s]
+----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------+
|    | annotated   | filename   | name      | type   | id                       | hidden   | dir   |   annotationsCount | dataset                                                           | createdAt                | datasetId                | creator             |
|----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------|
|  0 | True        | /test1.jpg | test1.jpg | file   | 63da62df7592bf239854adc0 | False    | /     |                  3 | https://gate.dataloop.ai/api/v1/datasets/63da62d973b62f22086f1d8f | 2023-02-01T13:02:23.000Z | 63da62d973b62f22086f1d8f | email@gmail.com |
+----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------+
Iterate Entity: 100%|████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.29it/s]
```

For the best results, I suggest you upload multiple items before using the command above.

### Annotating Items

Dataset Items are annotated using Labels. A Label is composed of various Label Settings and Instructions that are defined by a Dataset’s [Recipe](https://dataloop.ai/blog/data-recipes/). For example, an Item can contain 1 Label defined as a Classification, to categorize the entire data sample. It can also contain multiple annotation labels covering only parts of your data sample to identify specific sections of that Item.  For example, if the Item contains cats and dogs, you might find a label for Cat and a label for Dog in the Recipe.

#### Classification

Classification is used to categorize an entire data sample. For example, a Classification label can be used to classify product images under categories, subcategories, and characteristics, such as men’s clothes, polo shirts, hand cremes, etc.

The Python SDK can add Classification Labels to an item using 2 steps:

1. Firstly, you need to add a Classification Label to be part of the Dataset's Recipe (create Label);
2. Add that Label to the Item you wish to classify.

To complete the first step, you can run the following command to add a Label (Person) to the "My-First-Dataset" Dataset's list of Labels:

```python
dataset.add_label(label_name='Person')
```

After executing the code, you should get something similar to this result:

```
[Label(tag='Person', display_data={}, color='#0214a7', display_label='Person', attributes=[], children=[])]
```

The second step is to annotate the image you just uploaded:

```python
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='Person'))
item.annotations.upload(builder)
```

And should get this output:

```python
AnnotationCollection(item=Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/63da62d973b62f22086f1d8f', created_at='2023-02-01T13:02:23.000Z', dataset_id='63da62d973b62f22086f1d8f', filename='/test1.jpg', name='test1.jpg', type='file', id='63da62df7592bf239854adc0', spec=None, creator='email@gmail.com', _description=None, annotations_count=3), annotations=[Annotation(id='63db94346b35f547a1539602', item_id='63da62df7592bf239854adc0', creator='email@gmail.com', created_at='2023-02-02T10:45:08.711Z', type='class', item_height=738, item_width=564, label_suggestions=None, _start_frame=0, _start_time=0)])
```

Now the Item you added a bit earlier is successfully annotated and classified with the label "Person".

#### Example: Annotating images using Point Markers

Be sure to complete this Example as we will refer to it in the coming sections.

A Point Marker is used to identify specific regions in your data sample files. For example, it can identify regions where objects are present, in an image or video Item, like an image of a person's face that contains multiple Point Marker Labels specifying where the person’s eyes, mouth, ears, etc. are.

Point Marker commands accept 2 sets of coordinates (x, y) as input parameters, which specify the location which you want to label. Just as in the case of Classification, we need to first create the Label and add it to the Dataset Recipe before we can use it. Let's just add a new Label to our current Dataset:

```python
dataset.add_label(label_name='Ear')
```

Easy, right? Now you can add the "Ear" label we just created to a specific region of your image:

```python
builder = item_1.annotations.builder()
builder.add(annotation_definition=dl.Point(x=80, y=80, label='Ear'))
builder.add(annotation_definition=dl.Point(x=120, y=120, label='Ear'))
item_1.annotations.upload(builder)
```

With this output:

```python
AnnotationCollection(item=Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/63da62d973b62f22086f1d8f', created_at='2023-02-01T13:02:23.000Z', dataset_id='63da62d973b62f22086f1d8f', filename='/test1.jpg', name='test1.jpg', type='file', id='63da62df7592bf239854adc0', spec=None, creator='email@gmail.com', _description=None, annotations_count=3), annotations=[Annotation(id='63da632797d0cfccbab6ae88', item_id='63da62df7592bf239854adc0', creator='email@gmail.com', created_at='2023-02-01T13:03:35.121Z', type='point', item_height=738, item_width=564, label_suggestions=None, _start_frame=0, _start_time=0), Annotation(id='63da632797d0cf0f7cb6ae87', item_id='63da62df7592bf239854adc0', creator='email@gmail.com', created_at='2023-02-01T13:03:35.119Z', type='point', item_height=738, item_width=564, label_suggestions=None, _start_frame=0, _start_time=0)])
```

After this, you can open the sample in web view, to see the new labels you have added, using the following command:

```python
item.open_in_web()
```

Congratulations, you just learned how to create and select a dataset, add data samples to it and then annotate those items.

In the next chapter, you will learn the basics of filtering the data Items within your Dataset, which is extremely helpful when you have a high number of data sample files.
