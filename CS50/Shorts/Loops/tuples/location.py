import sys

def main():

    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]

    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")
#    latitude, longitude = coordinates
#    print(f"Latitude: {latitude}")
#    print(f"Latitude: {longitude}")

#    print(f"Latitude: {coordinates[0]}")
#    print(f"Longitude: {coordinates[1]}")

 #   latitude = 42.376
 #   longitude = -71.115

main()