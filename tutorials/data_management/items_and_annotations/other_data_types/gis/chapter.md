## Overview

The **GIS Data** enables users to efficiently annotate geospatial data within Dataloop's platform. With this SDK, you can create, manage, and upload GIS Data items into the Dataloop platform for the annoattion process. The SDK supports various GIS file formats and provides full control over annotation workflows. Read the [GIS user documentation](https://docs.dataloop.ai/docs/gis-studio) for information.

## Supported File Formats

The GIS SDK supports various file formats for geospatial data:
- **COG (Cloud-Optimized GeoTIFF)** – Optimized for cloud storage and efficient access.
- **GeoTIFF** – is a raster image format that includes embedded geographic metadata to align the image with geospatial coordinates. is an image file, like a map or satellite photo, that also has location data so it knows where on Earth it belongs.
- **OSM (OpenStreetMap)** – is a free, editable map of the world made by people, showing roads, places, and more, that anyone can use and improve. this is just an optional layer we provide users.
- **XYZ (Tile Map Services)** – is a way to show maps by cutting them into small square images (tiles) that load one by one as you zoom or move around.

In the GIS Annotation Studio, annotations are created using geospatial data, utilizing latitude and longitude coordinates instead of pixel-based positioning. Below are the key components that define how GIS layers, boundaries, and settings are structured in the SDK.

### 1️⃣ Main Layer and Optional Layers

**Main Layer**

- The top GIS layer used for annotations.
- It contains geospatial data in various formats (e.g., GeoTIFF, XYZ tiles, OpenStreetMap (OSM)).
- The Main Layer is defined in the layer field of the GIS Item JSON structure.

**Optional Layers**

- Additional layers that can be overlaid at the bottom of the Main Layer.
- These can include satellite imagery, road networks, elevation maps, or any other supporting geospatial data.
- Defined in the optionalLayers field in GIS Item JSON.
- Can be toggled on/off in the Layers Controller.

Example JSON structure


```json
{
  "layer": {
    "name": "Base Map",
    "type": "geoTiff",
    "ref": "<item_id>"
  },
  "optionalLayers": [
    {
      "name": "OpenStreetMap",
      "type": "osm",
      "url": ""
    }
  ]
}
```

### 2️⃣ AOI (Area of Interest)

- The Area of Interest (AOI) is the defined workspace for creating annotations in the GIS Annotation Studio.
- Specified in the GIS-Item JSON as a polygon, usually a 2D rectangle.
- All annotations must be placed within the AOI; any point outside is automatically adjusted to the nearest border.
- Visual indicators:
	- Black, dashed border with no background color.
	- Tooltip displays “Area of Interest” when hovered.
- Behavior:
	- Non-interactive — cannot be selected, moved, or modified.
- Map settings:
	- Sets the boundaries and default zoom level in the studio.
	- Zoom level and map bounds extend 10% beyond the AOI to provide surrounding context.


Example AOI Definition:

```json
{
  "aoi": [
    [5.096927, 51.8843133],
    [5.076927, 51.8843133],
    [5.076927, 51.8643163],
    [5.096927, 51.8643163],
    [5.096927, 51.8843133]
  ]
}
```

- The first and last coordinate must be the same to close the polygon.
- Projection
- Sysytem



### 3️⃣ Bounds

- Defines the visible map area in the GIS Annotation Studio.
- Used to set the extent of the map a user can pan and zoom into.
- It is defined as a bounding box (top-left & bottom-right coordinates).
- Annotations cannot be created outside the bounds, ensuring the dataset remains within the relevant geospatial area.


Example Bounds Definition:

```json
{
  "bounds": [
    [5.046927, 51.9243133],  // Top-left corner
    [5.126927, 51.8243163]   // Bottom-right corner
  ]
}
```

### 4️⃣ Coordinate System


- Defines how locations on Earth are represented using numerical values (latitude & longitude).
- The Geographic Coordinate System (GCS) represents locations on a 3D spherical model of the Earth.
- Example: WGS 84 (EPSG:4326), which is widely used for GPS and global mapping applications.


**Example:**

```json
{
  "epsg": "4326" // WGS 84
}
```

### 5️⃣ Zoom, Min Zoom, Max Zoom

- Controls how much users can zoom in or out on the map.
- Defines the minimum and maximum zoom levels for the dataset.

**Zoom Levels**

- zoom: Default zoom level when the GIS item is loaded.
- minZoom: The lowest level a user can zoom out (e.g., 0 for world view).
- maxZoom: The highest level a user can zoom in (e.g., 28 for detailed view).

**Example Zoom Configuration:**

```json
{
  "zoom": 10,     // Default zoom level
  "minZoom": 5,   // Prevents zooming out too far
  "maxZoom": 20   // Allows zooming in for detailed annotations
}
```





## Create a GIS Item

Users can create GIS items using the SDK with support types such as `XYZ` or `GeoTiff`. Refer to the following JSON formats to create a GIS item:


**XYZ Format**

```json
{
    "shebang": "dataloop",                      //For the type of Web Map Item, it should be dataloop only and mandatory
    "metadata": {
        "dltype": "gis"                         //For the type of Web Map Item, it should be gis only and mandatory
    },
    "layer": {                                  // Representing the Tile Layer - it's a mandatory layer object
        "name": "OpenStreetMap",
        "type": "xyz",                          // Currently supporting "xyz", "osm" and "cog" types only. XYZ can be an OpenStreetMap.
        "url": ""				//URL source for the layer (empty means default XYZ tiles will be used).
    },
    "optionalLayers":                           // Representing the Optional Layers array, which can have multiple layers("xyz", "osm" and "cog")
    [ 
        {
            "name": "OpenStreetMap",
            "type": "osm",
            "url": ""
        }
    ],
    "zoom":20,                                  // It's an optional zoom level, which can be between 0 to 28
    "minZoom":0,                                // It's an optional min zoom level, which can be between 0 to 28
    "maxZoom":30,                               // It's an optional max zoom level, which can be between 1 to 28
    "epsg":"4326",                              // Representing the file's Coordinate System (EPSG). Currently we only support epsg 4326 (WGS84)
    "bounds": [                                 // The coordinates that represents the (square) area within the map that the user can view, and should add/edit the annotations. I.e. the bounds where the projection is valid. Optional field.
        [-118.33559370040894, 33.82662439264756],  //top left
        [-118.33497619628906, 33.82610016009953]   //bottom right
    ],
    "aoi": [                                    // Coordinates representing the Area of Interest -- The areas within the bounds of the tile layer, where I allow to create annotations. I.e. the “boarders of the canvas”. Optional field. 
        [-118.33545684814453, 33.826504880358854],
        [-118.33545684814453, 33.82621967238824],
        [-118.33511352539062, 33.82621967238824],
        [-118.33511352539062, 33.826504880358854],
        [-118.33545684814453, 33.826504880358854]
    ]
}

```

**GeoTiff (Ref or URL) Example**


```json
{
    "shebang": "dataloop",                      //For the type of Web Map Item, it should be dataloop only and mandatory
	"metadata": {
        "dltype": "gis"                         //For the type of Web Map Item, it should be gis only and mandatory
    },
    "layer": {  
        "name": "GeoTIFF Image",  // User-defined name for the main GIS layer.
        "type": "geoTiff",  // Specifies the layer type. Options: "geoTiff" (raster-based GIS format), "xyz", "osm".
        "ref": "67d14487f561d469323d8996"  // Reference ID for the GIS item stored in Dataloop. ** It can be either `ref` or `url`.
    },
    "optionalLayers": [  
        {
            "name": "OpenStreetMap",  // Name of the optional overlay layer.
            "type": "osm",  // Type of the optional layer. Can be "osm", "xyz", or "cog".
            "url": ""  // URL source for the optional layer (empty means default OSM tiles will be used).
        }
    ],
    "epsg": "4326",  // Representing the file's Coordinate System (EPSG). Currently we only support epsg 4326 (WGS84).
    "bounds": [  
        [5.046927, 51.9243133],  // Top-left coordinate of the bounding box (longitude, latitude).
        [5.126927, 51.8243163]   // Bottom-right coordinate of the bounding box (longitude, latitude). Defines the visible area where annotations can be created.
    ],
    "aoi": [  
        [5.096927, 51.8843133],  // First coordinate of the Area of Interest (AOI).
        [5.076927, 51.8843133],  // Second coordinate of the AOI polygon.
        [5.076927, 51.8643163],  // Third coordinate of the AOI polygon.
        [5.096927, 51.8643163],  // Fourth coordinate of the AOI polygon.
        [5.096927, 51.8843133]   // Closing coordinate (same as the first), forming a closed polygon. Defines the area where annotations are allowed.
    ]
}

```

Key Takeaways:

- "shebang" and "dltype" are mandatory fields that define the system format.
- "layer" specifies the main GIS dataset, which is required.
- `layer` -> `url` URL to fetch the GeoTIFF raster layer. This serves as the primary layer. The URL allows streaming the GIS item directly from the Dataloop API. 
- `epsg`: Representing the file's Coordinate System (EPSG).
	- EPSG:4326 - WGS 84 (commonly used for GPS & mapping). 
    - EPSG:3857 - Web Mercator (used in most online maps).
    - EPSG:3035 - Albers Equal-Area (preserves area accuracy).

- "optionalLayers" allows adding additional overlays (e.g., OpenStreetMap).
- "proj" determines the coordinate reference system used.
- "bounds" limits the visible area for annotation.
- "aoi" specifies the exact annotation area, ensuring that annotations are placed in the correct region.


#### 📚 Learn More

For more details on GIS user documentation and GIS output formats, refer to the following documentation:
- [GIS User Documentation ](https://docs.dataloop.ai/docs/gis-studio)
- [GIS Annotations JSON Format](https://docs.dataloop.ai/docs/gis-json-format)
- [GIS Item JSON Format](https://docs.dataloop.ai/docs/gis-item-json-format)



## Upload GIS Items

GIS items can be uploaded programmatically via the SDK using the GIS-Item JSON format. The uploaded items retain all associated metadata, including the Area of Interest (AOI), if specified.

```python
import dtlpy as dl

# Replace "project_name" with the actual name of your Dataloop project
project = dl.projects.get(project_name="project_name") 


# Replace "dataset_name" with the name of the dataset you want to upload to
dataset = project.datasets.get(dataset_name="dataset_name")

# Replace "item_path" with the path to your local GIS file (e.g., a GeoJSON or Shapefile)
gis_item = dl.ItemGis.from_local_file(filepath="item_path")

# This uploads the GIS item into the dataset
item = dataset.items.upload(local_path=gis_item)
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

