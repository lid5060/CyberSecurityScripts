from torrequest import TorRequest

with TorRequest() as tr:
  URL = input("Enter URL:")
  response = tr.get(URL)
  print(response.text)