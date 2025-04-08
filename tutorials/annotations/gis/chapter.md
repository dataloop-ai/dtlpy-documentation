# GIS Annotations

## Overview

The **GIS Annotation SDK** enables users to efficiently annotate geospatial data within Dataloop's platform. With this SDK, you can create, manage, and share geospatial annotations such as bounding boxes, polygons, polylines, and points directly on maps. The SDK supports various GIS file formats and provides full control over annotation workflows. Read the [GIS user documentation](https://docs.dataloop.ai/docs/gis-studio) for information.


## Supported GIS Annotation Types

### **GIS Classification**

Classification annotations follow the standard classification structure.

```python
class GisClassification(label, attributes=None, description=None)
```

### **GIS Bounding Box**

A bounding box is defined using latitude and longitude coordinates.

```python
class GisBox(geo, label=None, attributes=None, description=None, angle=None)
```
- `geo`: List of lat-long coordinates defining the bounding box.
- `angle`: Optional, used for rotated boxes.
- **Box is created using two points (top-left and bottom-right).**

### **GIS Polygon**

A polygon is defined using a list of latitude and longitude coordinates. The first and last coordinates must be identical to close the shape.

```python
class GisPolygon(geo, label, attributes=None, description=None)
```

### **GIS Polyline**

A polyline consists of a list of latitude and longitude points.

```python
class GisPolyline(geo, label, attributes=None, description=None)
```

### **GIS Point**

A point annotation is defined by a single latitude and longitude coordinate.

```python
class GisPoint(lat, long, label, attributes=None, description=None)
```


## Create GIS Box Annotation

Defines a rectangular bounding box using latitude and longitude coordinates to annotate an object. The example below creates a bounding box labeled "car."

```python
import dtlpy as dl

box = dl.Gis(
    annotation_type=dl.GisType.BOX,
    geo=[
        [
            [-118.33545, 33.82643],
            [-118.33544, 33.82643],
            [-118.33544, 33.82642],
            [-118.33545, 33.82642],
            [-118.33545, 33.82643]
        ]
    ], label='car')

```

## Create GIS Polyline Annotation

A polyline annotation is used to define linear features such as roads, rivers, or paths. The example below creates a polyline labeled "road."

```python
import dtlpy as dl

polyline = dl.Gis(
    annotation_type=dl.GisType.POLYLINE,
    geo=[
        [-118.33542, 33.82643],
        [-118.33540, 33.82643],
        [-118.33540, 33.82642]
    ], label='road')
```

## Create GIS Point Annotation

A point annotation marks a single geographic location, ideal for identifying landmarks, points of interest, or specific objects. The example below places a point labeled "landmark."

```python
import dtlpy as dl

point = dl.Gis(
    annotation_type=dl.GisType.POINT,
    geo=[-118.33540, 33.82642],
    label='landmark')
```


## Create GIS Polygon Annotation

A polygon annotation is used to define an area by connecting multiple points. The first and last points must be the same to form a closed shape. The example below creates a polygon labeled "building."

```python
import dtlpy as dl

polygon = dl.Gis(
    annotation_type=dl.GisType.POLYGON,
    geo=[
        [
            [-118.33543, 33.82641],
            [-118.33541, 33.82641],
            [-118.33541, 33.82639],
            [-118.33543, 33.82639]
        ]
    ], label='building')
```


## Attach Annotations to Item

Once annotations are created, they must be attached to an item before being uploaded. The following example adds all previously created annotations to an item and uploads them.

```python
import dtlpy as dl

builder = item.annotations.builder()
builder.add(annotation_definition=box)
builder.add(annotation_definition=polyline)
builder.add(annotation_definition=point)
builder.add(annotation_definition=polygon)
item.annotations.upload(annotations=builder)
```

## Export GIS Annotations

You can export GIS annotations via the SDK:

```python
# Export annotations to JSON
annotations = item.annotations.export()
with open("annotations.json", "w") as f:
    f.write(annotations)
```

## **Changing Annotation Labels**

Modify annotation labels programmatically:
```python
annotation.label = "new_label"
annotation.update()
```

## **Set Attributes for an Annotation**

You can set attributes for an annotation:
```python
annotation.attributes = {"color": "red", "height": "5m"}
annotation.update()
```

## **Delete Annotations**

Remove annotations from an item:
```python
annotation.delete()
```

## 💡 Pro Tips for GIS Annotations
- **Use AOI Efficiently**: Always define an **Area of Interest (AOI)** to keep annotations within valid boundaries.
- **Leverage Multi-Layers**: Enable multiple layers to compare different geospatial data sources for better accuracy.
- **Shortcut Navigation**: Use **keyboard shortcuts** for faster annotation (e.g., `Ctrl + Z` for undo, `Shift + Drag` for zooming).
- **Optimize Performance**: Large datasets? Use **COG format** for efficient access and streaming.

## 🔧 Troubleshooting Common Issues
- **Annotations Not Visible?** Ensure the correct **layer** is selected and visible.
- **Coordinate Mismatch?** Verify that annotations use the correct **EPSG projection** (default: **4326**).
- **Performance Issues?** Reduce layer opacity or limit the number of active layers.
- **Upload Failure?** Double-check **JSON format** and required metadata fields.

