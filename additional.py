#Flattern nested json 
JSOn = 
{
  "destination_addresses": [
    "Philadelphia, PA, USA"
  ], 
  "origin_addresses": [
    "New York, NY, USA"
  ], 
  "rows": [{
    "elements": [{
      "distance": {
        "text": "94.6 mi",
        "value": 152193
      },  
      "duration": {
        "text": "1 hour 44 mins",
        "value": 6227
      }, 
      "status": "OK" 
    }] 
  }], 
  "status": "OK" 
}

def extract_value(obj, val):
    ans =[]

    def extraction(obj, ans, val):
        if isinstance(obj, dict):
            for key, value in obj.itmes():


