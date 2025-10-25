# Kode-Wilayah-CSV-to-JSON
A converter to transform **kode wilayah** CSV into hierarchical JSON format based on the [@kodewilayah/permendagri-72-2019](https://github.com/kodewilayah/permendagri-72-2019)  `dist/base.csv` dataset. 

## Features
- Converts raw region data **provinsi** (province), **kota** (city/district), **kecamatan** (sub-district), **desa** (village) from a CSV file into structured JSON.
- Saves the resulting JSON file with a clear, nested structure.

## Output JSON Structure Hierarcy
```json title="wilayah_id.json"
[
    {
	"kode_wilayah": ["11"],
        "provinsi": "ACEH",
        "kota": [
            {
                "kode_wilayah":  ["11", "01"],
                "kota": "KAB. ACEH SELATAN",
                "type": "kabupaten",
                "kecamatan": [
                    {
                        "kode_wilayah":   ["11", "01", "01"],
                        "kecamatan": "Bakongan",
                        "desa": [
                            {
                                "kode_wilayah":  ["11", "01", "01", "2001"],
                                "desa": "Keude Bakongan"
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
```

## JSON Breakdown
1. Provinsi (Province): The top-level administrative region.
   - `"kode_wilayah"`: Province code as an array (e.g., `["11"]` for ACEH).
   - `"provinsi"`: Name of the province.
   - `"kota"`: List of cities or districts (kota/kabupaten) under the `"provinsi"` (province).

3. Kota/Kabupaten (City/District): Contains data on cities or districts.
   - `"kode_wilayah"`: Array containing the province and city/district codes (e.g., `["11", "01"]` for KAB. ACEH SELATAN).
   - `"kota"`: Name of the city or district.
   - `"type"`: Determines whether the area is a `"kota"` (city) or `"kabupaten"` (district).
   - `"kecamatan"`: List of kecamatan (sub-districts) under this `"kota"` (city/district).

4. Kecamatan (Sub-district): Contains sub-district-level data.
   - `"kode_wilayah"`: Array containing province, city/district, and sub-district codes.
   - `"kecamatan"`: Name of the sub-district.
   - `"desa"`: List of desa (villages) under this `"kecamatan"` (sub-district).

5. Desa (Village): The bottom administrative unit.
   - `"kode_wilayah"`: Full region code including province, city/district, sub-district, and village.
   - `"desa"`: Name of the village.

## Usage
1. Prepare the CSV File
   - Download the base.csv from the [@kodewilayah/permendagri-72-2019](https://github.com/kodewilayah/permendagri-72-2019) repository.
2. Run The Script
```bash
python kode_wilayah_convert_id.py
```
3. Output
   - The output will be saved as a file named `wilayah_id.json`

## Requirements
This script requires Python 3.x and the following Python libraries:

- `csv` (Standard Python Library)
- `json` (Standard Python Library)
- No additional third-party dependencies are needed.

## License
	
