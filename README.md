# Pakarlib

Unified data for Pikud Ha'Oref. All data is versioned, but you can run the build and fetch scripts to update all files:

```bash
$ uv sync
$ uv run build
$ uv run fetch
```

Currently supports:

- Fetching cities and districts metadata in 4 languages (he, ar, en, ru) from Pikud Ha'Oref unofficial ajax APIs
- Fetching segments metadata all polygons for all segments from unofficial Android app APIs
- Compilation of all unified data for later consumption (e.g. GeoJSON files)
