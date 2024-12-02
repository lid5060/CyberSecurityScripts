# Kyle Pendleton
# 02/12/2024
# This will retrieve the geolocation of a specified IP address

import requests

class Geolocation_of_IP(object):

    def __init__(self, remote_ip_address):
        self.latitude = ''
        self.longitude = ''
        self.country = ''
        self.city = ''
        self.time_zone = ''
        self.remote_ip_address = remote_ip_address
        self.location()

    def location(self):

        json_user_request = requests.get('http://ip-api.com/json/%s' % self.remote_ip_address).json()
        print(json_user_request)

        if 'country' in json_user_request.keys():
            self.country = json_user_request['country']
        if 'countryCode' in json_user_request.keys():
            self.country_code = json_user_request['countryCode']
        if 'timezone' in json_user_request.keys():
            self.time_zone = json_user_request['timezone']
        if 'city' in json_user_request.keys():
            self.city = json_user_request['city']
        if 'lat' in json_user_request.keys():
            self.latitude = json_user_request['lat']
        if 'lon' in json_user_request.keys():
            self.longitude = json_user_request['lon']

if __name__ == '__main__':
    geo_location = Geolocation_of_IP('213.24.76.23')
    print(geo_location.__dict__)