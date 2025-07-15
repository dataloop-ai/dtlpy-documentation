# Update Model Configurations

You can update a deployed model’s configuration either via the Dataloop UI or programmatically using the SDK.

## 🖥️ Update via the UI

Refer to the [Dataloop Documentation](https://docs.dataloop.ai/docs/model-versions#update-model-configurations).

## Update via the SDK

You can also modify model configurations programmatically using the Dataloop SDK:

```python

import dtlpy as dl

# Get the model by ID
model = dl.models.get(model_id='<your-model-id>')

# Update the configuration
model.configuration['new'] = 'value'

# Save and reload associated services
model.update(reload_services=True)

```

**Parameters**:

- `model_id` – The unique identifier of your model.
- `reload_services`:
    – Set to `True` if you want all related services to be updated with the new configuration.
    - When you use `model.update(reload_services=False)`, the model's configuration is updated, but the changes are not applied to any deployed services that use this model.
