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

**Note**: You need to call `model.update()` here since this is a model entity, not a model adapter. No auto-update will happen (see next section).

**Parameters**:

- `model_id` – The unique identifier of your model.
- `reload_services`:
    – Set to `True` if you want all related services to be updated with the new configuration.
    - When you use `model.update(reload_services=False)`, the model's configuration is updated, but the changes are not applied to any deployed services that use this model.

## 🔄 Auto-Update Model Configurations and Adapter Defaults

In the implementation of a model adapter (that inherits from the base model adapter), if any changes are done to the configuration or adapter defaults, these changes will automatically update the deployed model entity. This provides seamless configuration management without requiring manual updates.

### How It Works

The base model adapter automatically syncs configuration changes through its `ModelConfigurations` and `AdapterDefaults` classes. When you modify any configuration value or adapter default, the system automatically:

1. Updates the backing configuration dictionary
2. Triggers an automatic update to the model entity
3. Propagates changes to deployed services

**Important**: The `configuration.get()` method and `adapter_defaults.resolve()` method automatically add new configuration keys to the deployed model configuration, even when using default values. For example, if you call `configuration.get('non_existing_key', 'brand_new_value')` or `adapter_defaults.resolve('non_existing_key', 'brand_new_value')`, this will add the new key `'non_existing_key'` with the value `'brand_new_value'` to the deployed model's configuration. This ensures that users are always aware of all configuration keys being used, even if they're just default values.

### Example Usage

```python
model_adapter = SimpleModelAdapter(model)

# Update adapter defaults
model_adapter.adapter_defaults.upload_annotations = False
model_adapter.adapter_defaults.resolve('upload_features', False)

# Update model configuration
model_adapter.configuration['new_config_key'] = 'new_value'
model_adapter.configuration.update({'key1': 'value1', 'key2': 'value2'})
model_adapter.configuration.get('existing_key', 'default_value')

# Add new configuration key with default value (auto-updates deployed model)
model_adapter.configuration.get('non_existing_key', 'brand_new_value')
```

**Note**: No manual update is needed here since this is a model adapter.

### Benefits

- **Automatic Synchronization**: Configuration changes are immediately reflected across the system
- **Reduced Manual Steps**: No need to manually call update methods after configuration changes
- **Consistent State**: Ensures model configuration and deployed services stay in sync
- **Real-time Updates**: Changes take effect immediately without service restarts
