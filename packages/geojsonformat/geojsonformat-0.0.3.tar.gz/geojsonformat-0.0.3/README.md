# GeoJSON format

Formatting geojson with each feature on its own line

## Requirements
* **Python**: >=3.5

## Installation
```sh
python -m pip install geojsonformat
```

## Usage example
Input:
```json
{"type":"FeatureCollection","name":"ne_50m_admin_0_countries_lakes","crs":{"type":"name","properties":{"name":"urn:ogc:def:crs:OGC:1.3:CRS84"}},"features":[{"type":"Feature","properties":{"featurecla":"Admin-0 country","scalerank":1},"geometry":{"type":"Polygon","coordinates":[[[26.1474609375, 56.78884524518923],[25.521240234375, 56.24334992410525],[26.54296875,55.979945357882315],[27.158203125,56.52919914018469],[27.290039062499996,56.90900226702048],[26.1474609375, 56.78884524518923]]]}},{"type":"Feature","properties":{"featurecla":"Admin-0 country"},"geometry":{"type":"Polygon","coordinates":[[[26.1474609375, 56.78884524518923],[25.521240234375, 56.24334992410525],[26.54296875,55.979945357882315],[27.158203125,56.52919914018469],[27.290039062499996,56.90900226702048],[26.1474609375, 56.78884524518923]]]}}]}
```

Formatting:
```sh
geojsonformat input.geojson out.geojson
```

Output:
```json
{"type": "FeatureCollection", "name": "ne_50m_admin_0_countries_lakes", "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},"features":[
{"type": "Feature", "properties": {"featurecla": "Admin-0 country", "scalerank": 1}, "geometry": {"type": "Polygon", "coordinates": [[[26.1474609375, 56.78884524518923], [25.521240234375, 56.24334992410525], [26.54296875, 55.979945357882315], [27.158203125, 56.52919914018469], [27.290039062499996, 56.90900226702048], [26.1474609375, 56.78884524518923]]]}},
{"type": "Feature", "properties": {"featurecla": "Admin-0 country"}, "geometry": {"type": "Polygon", "coordinates": [[[26.1474609375, 56.78884524518923], [25.521240234375, 56.24334992410525], [26.54296875, 55.979945357882315], [27.158203125, 56.52919914018469], [27.290039062499996, 56.90900226702048], [26.1474609375, 56.78884524518923]]]}}
]}
```
