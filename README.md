# Pakarlib

Unified data for Pikud Ha'Oref. All data is versioned, but you can run the build to update all files:

```bash
$ pipenv run build
```

Or fetch all files:

```bash
$ pipenv run fetch
```

Currently supports:

- Fetching cities and districts metadata in 4 languages (he, ar, en, ru) from Pikud Ha'Oref unofficial ajax APIs
- Fetching segments metadata all polygons for all segments from unofficial Android app APIs
- Compilation of all unified data for later consumption (e.g. GeoJSON files)
