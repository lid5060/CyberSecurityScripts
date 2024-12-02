# Kyle Pendleton
# 02/12/2024
# this will retrieve exif data from a provided image

from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os

def get_exif_metadata(path_of_image):
    exif_image_data = {}
    picture = Image.open(path_of_image)
    if hasattr(picture, '_getexif'):
        exif_data = picture._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                decoded = TAGS.get(tag, tag)
                exif_image_data[decoded] = value
    decode_gps_info(exif_image_data)
    return exif_image_data

def convert_to_degress(value):
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def decode_gps_info(exif):
    gps_information = {}
    if 'GPSInfo' in exif:
        for key in exif['GPSInfo'].keys():
            decode = GPSTAGS.get(key, key)
            gps_information[decode] = exif['GPSInfo'][key]
        exif['GPSInfo'] = gps_information

        latitude = exif['GPSInfo']['GPSLatitude']
        latitude_ref = exif['GPSInfo']['GPSLatitudeRef']
        longitude = exif['GPSInfo']['GPSLongitude']
        longitude_ref = exif['GPSInfo']['GPSLongitudeRef']
        if latitude:
            latitude_value = convert_to_degress(latitude)
            if latitude_ref != 'N':
                latitude_value = -latitude_value
        else:
            return {}
        if longitude:
            longitude_value = convert_to_degress(longitude)
            if longitude_ref != 'E':
                longitude_value = -longitude_value
        exif['GPSInfo'] = {"Latitude": latitude_value, "Longitude": longitude_value}

def printMetadata():
    for dirpath, dirnames, files in os.walk("Images"):
        for name in files:
            print("[+] Metadata for file: %s " % (dirpath + os.path.sep + name))
            try:
                exif_image_data = {}
                exif = get_exif_metadata(dirpath + os.path.sep + name)
                for metadata in exif:
                    print("Metadata: %s - Value: %s " % (metadata, exif[metadata]))
                print("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    printMetadata()