import csv
import json

# Rename input CSV if you want
file = open("base.csv")
reader = csv.reader(file)

splitRegions = []
for row in reader:
    regionCode = row[0].split('.')
    splitRegions.append({
        'kode_wilayah': regionCode,
        'nama_wilayah': row[1]
    })
def add_provinsi():
    found_region = next((r for r in regions if r['provinsi'] == region['nama_wilayah']), None)
    if not found_region:
        regions.append({
            'kode_wilayah': region['kode_wilayah'],
            'provinsi': region['nama_wilayah'],
            'kota': []
        })

def add_kota_from_provinsi():
    for provinsi in regions:
        if region['kode_wilayah'][0] == provinsi['kode_wilayah'][0]:
            kab_or_kota = 'kota' if int(region['kode_wilayah'][1]) >= 71 else 'kabupaten'
            provinsi['kota'].append({
                'kode_wilayah': region['kode_wilayah'],
                'kota': region['nama_wilayah'],
                'type': kab_or_kota,
                'kecamatan': []
            })

def add_kecamatan_from_kota():
    for provinsi in regions:
        if region['kode_wilayah'][0] == provinsi['kode_wilayah'][0]:
            for kota in provinsi['kota']:
                if region['kode_wilayah'][1] == kota['kode_wilayah'][1]:
                    kota['kecamatan'].append({
                        'kode_wilayah': region['kode_wilayah'],
                        'kecamatan': region['nama_wilayah'],
                        'desa': []
                    })


def add_desa_from_kecamatan():
    for provinsi in regions:
        if region['kode_wilayah'][0] == provinsi['kode_wilayah'][0]:
            for kota in provinsi['kota']:
                if region['kode_wilayah'][1] == kota['kode_wilayah'][1]:
                    for kecamatan in kota['kecamatan']:
                        if region['kode_wilayah'][2] == kecamatan['kode_wilayah'][2]:
                            kecamatan['desa'].append({
                                'kode_wilayah': region['kode_wilayah'],
                                'desa': region['nama_wilayah']
                            })

regions = []
for region in splitRegions:
    if len(region['kode_wilayah']) == 1:
       add_provinsi()

    if len(region['kode_wilayah']) == 2:
        add_kota_from_provinsi()

    if len(region['kode_wilayah']) == 3:
        add_kecamatan_from_kota()

    if len(region['kode_wilayah']) == 4:
        add_desa_from_kecamatan()

jsonDump = json.dumps(regions, indent=4)
print(jsonDump)

# Rename this json output file to whatever you want
f = open('wilayah_id.json', 'w')

f.write(jsonDump)
f.close()
