# Pakarlib

Unified data for Pikud Ha'Oref. All data is versioned, but you can run the build to update all files:

```bash
$ pipenv run build
```

Currently supports:

- Fetching cities metadata in 4 languages (he, ar, en, ru)
- Fetching segments metadata
- Fetching all polygons for all segments, published and unpublished
- Generation of unified geojson data for later consumption
