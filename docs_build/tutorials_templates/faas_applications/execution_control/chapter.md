# 🎮 Execution Control - Managing Your FaaS Functions

Welcome to the execution control guide! Learn how to manage, monitor, and control your FaaS function executions like a pro. Let's explore how to handle long-running tasks, implement graceful termination, and monitor execution status.

## 🛑 Execution Termination

### Graceful Termination with Checkpoints
Need to safely stop a long-running execution? Use checkpoints to implement graceful termination:

```python
class ServiceRunner(dl.BaseServiceRunner):
    def train_model(self, item: dl.Item, progress: dl.Progress):
        # Initialize training
        model = list()
        
        for epoch in range(100):
            # Check for termination request before each epoch
            self.kill_event()
            
            # Train for one epoch
            train_loss = model.append(epoch)
            
            # Save checkpoint
            print(model)
            
            # Check again after expensive operation
            self.kill_event()
            
            # Update progress
            progress.update(progress=epoch, message=f'Epoch {epoch}: loss={train_loss}')
```

### Triggering Termination
Terminate an execution from another process:

```python
# Get the execution
execution = dl.executions.get(execution_id='execution-id')

# Request termination
execution.terminate()

# Wait for termination to complete
execution = execution.wait()
print(f"Execution status: {execution.latest_status['status']}")
```

## ⏲️ Execution Timeout Management

### Setting Timeout Duration
Control how long your function can run:

```python
# Get your service
service = dl.services.get(service_name='my-service')

# Set timeout in seconds
service.execution_timeout = 3600  # 1 hour
service.update()

# For longer tasks
service.execution_timeout = 86400  # 24 hours
service.update()
```

### Configuring Timeout Behavior
Choose what happens when timeout occurs:

```python
# Option 1: Mark as failed (default)
service.on_reset = 'failed'
service.update()

# Option 2: Automatically retry
service.on_reset = 'rerun'
service.update()
```

## 📊 Execution Monitoring

### Basic Status Monitoring
Monitor a single execution:

```python
# Get execution by ID
execution = dl.executions.get(execution_id='execution-id')

# Wait for completion
execution = execution.wait()
print(f"Status: {execution.latest_status['status']}")
print(f"Duration: {execution.duration:.2f} seconds")
```

### Execution Logs
Access execution logs for debugging:

```python
# Get execution logs
execution = dl.executions.get(execution_id='execution-id')
logs = execution.logs()
print(logs)

# Stream logs in real-time
for log in execution.logs(follow=True):
    print(f"{log['timestamp']}: {log['message']}")
```

## 🔄 Execution Retry Management

### Manual Retry
Retry failed executions:

```python
# Get failed execution
execution = dl.executions.get(execution_id='failed-execution-id')

# Retry with same parameters
new_execution = execution.rerun()

# Wait for completion
new_execution = new_execution.wait()
print(f"Retry status: {new_execution.latest_status['status']}")
```

## 💡 Pro Tips & Best Practices

### Resource Management
- Implement regular checkpoints in long-running tasks
- Save intermediate results when possible
- Clean up temporary resources in case of termination

### Error Handling
- Use try/finally blocks for cleanup
- Implement proper logging for debugging
- Handle different types of termination gracefully

### Performance Optimization
- Monitor execution duration trends
- Adjust timeouts based on actual needs
- Use appropriate instance types for your workload

### Monitoring Guidelines
- Set up alerts for failed executions
- Monitor resource usage patterns
- Keep track of execution duration statistics

Need help? Check out our other tutorials or reach out to our support team. Happy coding! ⚡️
