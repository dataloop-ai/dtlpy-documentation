## FAAS

Dataloop Function-as-a-Service ([FAAS](https://dataloop.ai/docs/faas))  is a compute service that automatically runs your code based on time patterns or in response to trigger events.
You can use this tool for pre annotation processing (resize, video assembler/dissembler); post annotation processing (auto-parenting, augmentation); ML models (auto-detection), QA models (auto QA, consensus model, majority vote model)

**The main concepts in FAAS:**

- [Service](https://dataloop.ai/docs/service-runtime)
- [Docker image](https://dataloop.ai/docs/faas-docker-images)
- [Service analytics](https://dataloop.ai/docs/service-analytics)

**Advanced examples how to implement FAAS:**

1. Create and deploy [simple function](../tutorials/faas/single_function_rgb_to_gray/chapter.md)
2. Write a function that extracts image Exif information and uploads it [to the item's metadata](https://github.com/dataloop-ai/image-exif)
3. Add [classification](../functions/add_annotation_to_item/README.md)
4. Auto [pre annotating process](../tutorials/faas/auto_annotate/chapter.md#model-and-weights-files)

**Video tutorials how to create FAAS in UI**

1. FAAS with [module](https://app.guidde.co/share/playbooks/j7iGAKHJas4iZjP8umCgK4?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
2. FAAS [cron](https://app.guidde.co/share/playbooks/9pA98jkVBjScnYKbL1GcLK?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)

> What you will learn next? 

In the next chapter you will learn about pipelines which you can use to integrate with any FAAS you will create. 
To continue go to [chapter 9](part_09_pipelines.md)








