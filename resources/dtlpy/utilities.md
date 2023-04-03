# Utilities

## converter


### _class_ Converter(concurrency=6, return_error_filepath=False)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Annotation Converter


#### attach_agent_progress(progress: Progress, progress_update_frequency: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None)
Attach agent progress.


* **Parameters**

    
    * **progress** (*Progress*) – the progress object that follows the work


    * **progress_update_frequency** ([*int*](https://docs.python.org/3/library/functions.html#int)) – progress update frequency in percentages



#### convert(annotations, from_format: [str](https://docs.python.org/3/library/stdtypes.html#str), to_format: [str](https://docs.python.org/3/library/stdtypes.html#str), conversion_func=None, item=None)
Convert annotation list or single annotation.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **item** ([*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – item entity


    * **annotations** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)* or *[*AnnotationCollection*](entities.md#dtlpy.entities.annotation_collection.AnnotationCollection)) – annotations list to convert


    * **from_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – AnnotationFormat to convert to – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP


    * **to_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – AnnotationFormat to convert to – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP


    * **conversion_func** (*Callable*) – Custom conversion service



* **Returns**

    the annotations



#### convert_dataset(dataset, to_format: [str](https://docs.python.org/3/library/stdtypes.html#str), local_path: [str](https://docs.python.org/3/library/stdtypes.html#str), conversion_func=None, filters=None, annotation_filter=None)
Convert entire dataset.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **dataset** (*dtlpy.entities.dataet.Dataset*) – dataset entity


    * **to_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – AnnotationFormat to convert to – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to save the result to


    * **conversion_func** (*Callable*) – Custom conversion service


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filter parameters


    * **annotation_filter** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filter entity



* **Returns**

    the error log file path if there are errors and the coco json if the format is coco



#### convert_directory(local_path: [str](https://docs.python.org/3/library/stdtypes.html#str), to_format: AnnotationFormat, from_format: AnnotationFormat, dataset, conversion_func=None)
Convert annotation files in entire directory.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to the directory


    * **to_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – AnnotationFormat to convert to – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP


    * **from_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – AnnotationFormat to convert from – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset entity


    * **conversion_func** (*Callable*) – Custom conversion service



* **Returns**

    the error log file path if there are errors



#### convert_file(to_format: [str](https://docs.python.org/3/library/stdtypes.html#str), from_format: [str](https://docs.python.org/3/library/stdtypes.html#str), file_path: [str](https://docs.python.org/3/library/stdtypes.html#str), save_locally: [bool](https://docs.python.org/3/library/functions.html#bool) = False, save_to: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, conversion_func=None, item=None, pbar=None, upload: [bool](https://docs.python.org/3/library/functions.html#bool) = False, \*\*_)
Convert file containing annotations.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **to_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – AnnotationFormat to convert to – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP


    * **from_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – AnnotationFormat to convert from – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP


    * **file_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path of the file to convert


    * **pbar** (*tqdm*) – tqdm object that follows the work (progress bar)


    * **upload** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if True upload


    * **save_locally** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – If True, save locally


    * **save_to** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to save the result to


    * **conversion_func** (*Callable*) – Custom conversion service


    * **item** ([*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – item entity



* **Returns**

    annotation list, errors



#### _static_ custom_format(annotation, conversion_func, i_annotation=None, annotations=None, from_format=None, item=None, \*\*_)
Custom convert function.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **annotation** ([*dtlpy.entities.annotation.Annotation*](entities.md#dtlpy.entities.annotation.Annotation)* or *[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – annotations to convert


    * **conversion_func** (*Callable*) – Custom conversion service


    * **i_annotation** ([*int*](https://docs.python.org/3/library/functions.html#int)) – annotation index


    * **annotations** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of annotations


param str from_format: AnnotationFormat to convert to – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP
:param dtlpy.entities.item.Item item: item entity
:return: converted Annotation


#### from_coco(annotation, \*\*kwargs)
Convert from COCO format to DATALOOP format. Use this as conversion_func param for functions that ask for this param.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **annotation** – annotations to convert


    * **kwargs** – additional params



* **Returns**

    converted Annotation entity



* **Return type**

    [dtlpy.entities.annotation.Annotation](entities.md#dtlpy.entities.annotation.Annotation)



#### _static_ from_voc(annotation, \*\*_)
Convert from VOC format to DATALOOP format. Use this as conversion_func for functions that ask for this param.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    **annotation** – annotations to convert



* **Returns**

    converted Annotation entity



* **Return type**

    [dtlpy.entities.annotation.Annotation](entities.md#dtlpy.entities.annotation.Annotation)



#### from_yolo(annotation, item=None, \*\*kwargs)
Convert from YOLO format to DATALOOP format. Use this as conversion_func param for functions that ask for this param.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **annotation** – annotations to convert


    * **item** ([*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – item entity


    * **kwargs** – additional params



* **Returns**

    converted Annotation entity



* **Return type**

    [dtlpy.entities.annotation.Annotation](entities.md#dtlpy.entities.annotation.Annotation)



#### save_to_file(save_to, to_format, annotations, item=None)
Save annotations to a file.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **save_to** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to save the result to


    * **to_format** – AnnotationFormat to convert to – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP


    * **annotations** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – annotation list to convert


    * **item** ([*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – item entity



#### _static_ to_coco(annotation, item=None, \*\*_)
Convert from DATALOOP format to COCO format. Use this as conversion_func param for functions that ask for this param.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **annotation** ([*dtlpy.entities.annotation.Annotation*](entities.md#dtlpy.entities.annotation.Annotation)* or *[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – annotations to convert


    * **item** ([*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – item entity


    * **\*\*_** – additional params




* **Returns**

    converted Annotation



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### _static_ to_voc(annotation, item=None, \*\*_)
Convert from DATALOOP format to VOC format. Use this as conversion_func param for functions that ask for this param.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **annotation** ([*dtlpy.entities.annotation.Annotation*](entities.md#dtlpy.entities.annotation.Annotation)* or *[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – annotations to convert


    * **item** ([*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – item entity


    * **\*\*_** – additional params




* **Returns**

    converted Annotation



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### to_yolo(annotation, item=None, \*\*_)
Convert from DATALOOP format to YOLO format. Use this as conversion_func param for functions that ask for this param.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **annotation** ([*dtlpy.entities.annotation.Annotation*](entities.md#dtlpy.entities.annotation.Annotation)* or *[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – annotations to convert


    * **item** ([*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – item entity


    * **\*\*_** – additional params




* **Returns**

    converted Annotation



* **Return type**

    [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)



#### upload_local_dataset(from_format: AnnotationFormat, dataset, local_items_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, local_labels_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, local_annotations_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, only_bbox: [bool](https://docs.python.org/3/library/functions.html#bool) = False, filters=None, remote_items=None)
Convert and upload local dataset to dataloop platform.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **from_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – AnnotationFormat to convert to – AnnotationFormat.COCO, AnnotationFormat.YOLO, AnnotationFormat.VOC, AnnotationFormat.DATALOOP


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset entity


    * **local_items_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to items to upload


    * **local_annotations_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to annotations to upload


    * **local_labels_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to labels to upload


    * **only_bbox** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – only for coco datasets, if True upload only bbox


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filter parameters


    * **remote_items** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of the items to upload



* **Returns**

    the error log file path if there are errors
