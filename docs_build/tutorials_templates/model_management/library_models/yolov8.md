# YOLOv8

description

## Quick Start

new_model = model.clone
service = new_model.deploy
execution = new_model.predict

## Model Configurations

model.configurations:

imgsz=640
model_weights=model.pt

## UI Toolbars and Pipeline
How to create button in Dataset,
How to add component to pipeline

## Training

new_model = model.clone(dataset='')
service = new_model.train()
service.logs()
new_model.metrics()

## GitHub Repo
README.md
License
Citation
