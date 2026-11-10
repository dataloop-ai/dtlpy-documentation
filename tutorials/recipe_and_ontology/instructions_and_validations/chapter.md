# Recipe Instructions and Validations

Welcome to the guide on recipe instructions and validations in Dell Data Orchestration Engine (DDOE)! Let's explore how to set up instructions and validation rules for your annotation tasks.

## PDF Instructions

DDOE allows you to provide clear guidance to your annotation team through PDF instructions:

```python
import dtlpy as dl

# Get your recipe
recipe = dataset.recipes.get(recipe_id='your-recipe-id')

# Upload annotation instructions
recipe.add_instruction(annotation_instruction_file='/path/to/instructions.pdf')

```

When creating tasks, you can specify which pages from these PDFs should be shown to annotators.

[Learn more about PDF Instructions](https://docs.dataloop.ai/docs/instructions?highlight=pdf%20instr#pdf-instructions)

## Annotation Validation with JavaScript

Add validation rules to ensure annotation quality using JavaScript. Here's a simple example:

```javascript
function validateAnnotations(annotationsArr) {
    let result = {
        ok: true,
        errorMessage: "",
        errors: {}
    }
    
    // Example: Ensure at least one annotation exists
    if (annotationsArr.length === 0) {
        result.ok = false;
        result.errorMessage = "Item must have at least one annotation";
    }
    
    return result;
}
```

Adding a JS validation script to a recipe:

```python
recipe.upload_annotations_verification_file(local_path='/path/to/validation_script.js')
```

### Common Validation Use Cases:

1. **Label Coexistence**
   ```javascript
   // Example: Only one person per image
   if (annotations.filter(a => a.label === 'person').length > 1) {
       result.ok = false;
       result.errorMessage = "Only one person allowed per image";
   }
   ```

2. **Geometry Rules**
   ```javascript
   // Example: Ensure polygon has minimum points
   if (a.type === 'segment' && a._def[0].length < 4) {
       result.ok = false;
       result.errors[a.clientId] = "Polygon must have at least 4 points";
   }
   ```

### Key Points:

- Validation runs when annotators click the "Complete" button
- Scripts must follow the required format with `validateAnnotations` function
- Can validate label combinations, geometry, attributes, and more
- Supports detailed error messages per annotation

[Learn more about Annotation Validation](https://docs.dataloop.ai/docs/annotations-validation)

## Best Practices

1. Keep instructions clear and concise
2. Include visual examples in PDF instructions
3. Test validation rules thoroughly
4. Keep validation logic simple and efficient
5. Use console.log for debugging validation scripts

## Need More Help?

- [Complete Instructions Guide](https://docs.dataloop.ai/docs/instructions)
- [Validation Documentation](https://docs.dataloop.ai/docs/annotations-validation)
- [Recipe Management Guide](https://docs.dataloop.ai/docs/ontology-overview#recipe)

Happy validating!
