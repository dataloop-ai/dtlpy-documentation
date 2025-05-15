# 📝 Text Annotations - Making Words Come Alive!

Welcome to the world of text annotations! Just like highlighting important passages in a book, text annotations help us mark and categorize important pieces of text. Let's dive in! 

## 🎯 Basic Text Annotation

Think of text annotations like digital highlighters - they help you mark specific words, phrases, or characters in your text. Here's how to create one:

```python
# Get your document ready
item = dataset.items.get(filepath='/your-text-file.txt')
builder = item.annotations.builder()

# Create your digital highlight
builder.add(annotation_definition=dl.Text(text_type='block',
                                          start=11,
                                          end=19,
                                          label='Person'))

# Save your work
item.annotations.upload(builder)
```


# 💡 Pro Tips for Text Annotations

- Always verify your character coordinates match the text exactly
- Use meaningful labels that describe the type of text you're marking
- Consider using attributes to add extra context to your annotations
- Keep your annotation scheme consistent across all documents

# 🎓 Best Practices

## Working with Large Documents
When dealing with large text files:
- Break down the annotation task into manageable sections
- Use clear label hierarchies to organize different types of annotations
- Consider using overlapping annotations when concepts intersect

## Annotation Guidelines
For consistent text annotations:
- Define clear rules for what should be included in each span
- Document edge cases and how to handle them
- Use attributes to capture uncertainty or ambiguity

Need help? Check out our other tutorials or reach out to our support team. Happy text annotating! 📚✨

