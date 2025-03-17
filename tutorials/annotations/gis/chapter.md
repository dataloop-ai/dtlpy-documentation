# GIS Annotations

## Overview
The **GIS Annotation SDK** enables users to efficiently annotate geospatial data within Dataloop's platform. With this SDK, you can create, manage, and share geospatial annotations such as bounding boxes, polygons, polylines, and points directly on maps. The SDK supports various GIS file formats and provides full control over annotation workflows.

## Upload GIS Items
GIS items can be uploaded programmatically via the SDK using the GIS-Item JSON format. The uploaded items retain all associated metadata, including the Area of Interest (AOI), if specified.

### **Example: Upload GIS Item**
```python
import dtlpy as dl

# Upload GIS item from a local file
gis_item = dl.ItemGis.from_local_file(filepath="item_path")
```

## Upload GIS Annotations
The SDK supports GIS-specific annotations using **latitude and longitude** coordinates instead of pixel-based (x, y) values.

### **Supported GIS Annotation Types**

#### **GIS Classification**
Classification annotations follow the standard classification structure.
```python
class GisClassification(label, attributes=None, description=None)
```

#### **GIS Bounding Box**
A bounding box is defined using latitude and longitude coordinates.
```python
class GisBox(geo, label=None, attributes=None, description=None, angle=None)
```
- `geo`: List of lat-long coordinates defining the bounding box.
- `angle`: Optional, used for rotated boxes.
- **Box is created using two points (top-left and bottom-right).**

#### **GIS Polygon**
A polygon is defined using a list of latitude and longitude coordinates. The first and last coordinates must be identical to close the shape.
```python
class GisPolygon(geo, label, attributes=None, description=None)
```

#### **GIS Polyline**
A polyline consists of a list of latitude and longitude points.
```python
class GisPolyline(geo, label, attributes=None, description=None)
```

#### **GIS Point**
A point annotation is defined by a single latitude and longitude coordinate.
```python
class GisPoint(lat, long, label, attributes=None, description=None)
```

## Example: Uploading GIS Annotations
Below is an example of adding various GIS annotation types using the SDK.

```python
import dtlpy as dl

# Create GIS Box Annotation
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

# Create GIS Polyline Annotation
polyline = dl.Gis(
    annotation_type=dl.GisType.POLYLINE,
    geo=[
        [-118.33542, 33.82643],
        [-118.33540, 33.82643],
        [-118.33540, 33.82642]
    ], label='road')

# Create GIS Point Annotation
point = dl.Gis(
    annotation_type=dl.GisType.POINT,
    geo=[-118.33540, 33.82642],
    label='landmark')

# Create GIS Polygon Annotation
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

# Attach Annotations to Item
builder = item.annotations.builder()
builder.add(annotation_definition=box)
builder.add(annotation_definition=polyline)
builder.add(annotation_definition=point)
builder.add(annotation_definition=polygon)
item.annotations.upload(annotations=builder)
```

## Supported File Formats
The GIS SDK supports various file formats for geospatial data:
- **COG (Cloud-Optimized GeoTIFF)** – Optimized for cloud storage and efficient access.
- **GeoTIFF** – Standard raster data format with geospatial metadata.
- **OSM (OpenStreetMap)** – Vector-based format used for open-source map data.
- **XYZ (Tile Map Services)** – Used for map tiles in web mapping applications.

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

## 📚 Learn More
For more details on GIS annotations and formats, refer to the following documentation:
- [GIS Studio](https://docs.dataloop.ai/docs/gis-studio)
- [GIS JSON Format](https://docs.dataloop.ai/docs/gis-json-format)
- [GIS Item JSON Format](https://docs.dataloop.ai/docs/gis-item-json-format)

