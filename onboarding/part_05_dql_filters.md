## Querying and Filtering

**Metadata**

Each entity in our system has a JSON code that represents its data within our system.
There are different json structure between [item](https://dataloop.ai/docs/en/item-json-format?highlight=metadata) and 
[annotations](https://dataloop.ai/docs/annotation-json-format). 

You can learn more [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/80f1e828ef6b27fe28e8c12ea5f2f4c53573b426/tutorials/data_management/working_with_metadata/chapter.ipynb) how to use the metadata for SDK. 

**Pagination**

We use pages instead of a list when we have an object that contains a lot of information. While in UI you would simply go page by page or in batches of pages. 

You can learn more [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md) how to work with pages and use this concept with filters. 


**Filters**

[Filters](https://dataloop.ai/docs/sort-filter) are part of the Dataset and Task Browsers, enabling you to filter items based on every aspect of your files.

Filters are very powerful when using SDK and can help you build automatic flows based on different queries. 

You can learn basic queries [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/item_level/chapter.ipynb)

***Exercise:***

1. Get dataset 
2. Filter out only image that has annotation box 
3. Print how many images of this type you found


> What will you learn next? 

1. If you want to learn more complex filtering and queries continue to [this chapter](part_14_advanced_filtering.md)
2. If you want to learn how to create tasks and assignments continue to [this chapter](part_6_task%20&%20assignments.md)










