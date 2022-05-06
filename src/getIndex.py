import requests
import json

if __name__ == '__main__':

   URL = "http://api.openweathermap.org/data/2.5/forecast?q=Brno,CZE&cnt=16&appid=3861e019ae65e62dfa70cf06d6299e09"
   response = requests.get(URL)
   indexy = list()
   if response.status_code == 200:
      data = response.json()
      for day in data["list"]:
         denni = 0
         pocasi = day["weather"][0]["main"].lower()
         if "rain" in pocasi:
            denni += 5
         elif "cloud" in pocasi:
            denni += 3
         indexy.append(denni)

      tmp_indexy = 16 * [0]

      for ind in range(13):
         tmp_indexy[ind] = 0
         for inc in range(3):
            tmp_indexy[ind] += indexy[ind + inc]

      den = tmp_indexy.index(min(tmp_indexy[0:13]))
      print("Umyt auto je nejlepsi za {} dni".format(den))
      print("Tento den bude pocasi" + data["list"][den]["weather"][0]["main"].lower())

   else:
      print("Error in the HTTP request")
