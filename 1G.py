
import json
filename = "s1G.json"
with open(filename) as file_obj:
  HH = json.load(file_obj)
filename1 = "s2G.json"
with open(filename1) as file_obj:
  HH1 = json.load(file_obj)
filename2 = "s3G.json"
with open(filename2) as file_obj:
  HH2 = json.load(file_obj)
filename3 = "s4G.json"
with open(filename3) as file_obj:
  HH3 = json.load(file_obj)
filename4 = "sk1G.json"
with open(filename4) as file_obj:
  Hk1 = json.load(file_obj)
filename5 = "sl1G.json"
with open(filename3) as file_obj:
  Hl1 = json.load(file_obj)
filename6 = "st3G.json"
with open(filename6) as file_obj:
  Ht3 = json.load(file_obj)
filename7 = "st4G.json"
with open(filename7) as file_obj:
  Ht4 = json.load(file_obj)
def get_piority(crime_t,threat, know, need):
    piority=0
    if (crime_t=="Robbery" or crime_t=="Theft") and need=="Lost can be recoverd":
      piority =1
    elif need !="Lost can be recoverd" and (crime_t=="Robbery" or crime_t=="Theft") :
      piority =2
    elif(crime_t=="Sexual assualt" and know=="No"):
      piority=3
    elif(crime_t=="Sexual assualt" and know=="Yes"):
      piority=4
    elif(crime_t=="domestic" and know=="Yes"):
      piority=5
    else:
      piority=6
    if (threat=="Yes"):
      piority+=6
    return piority


def get_piorityl(crime_t,lan):
  piority =0
  if(lan=="No"):
    piority +=1
  if(crime_t=="Robbery" or crime_t=="Theft"):
    piority+=1
  elif (crime_t=="Assault and battery"):
    piority+=2
  return piority
def get_piorityt(crime_t,threat):
    piortiy=0
    if(crime_t=="Robbery" and threat=="Yes"):
        piority=1
    elif (crime_t == "domestic" and threat == "Yes"):
        piority=2
    elif(threat=="Yes"):
        piority =3
    return piority

def compute_solution(piority1,piority2,piority3):
    if(piority1%6==1 or piority1%6==2):
        result = HH
    elif(piority1%6==3):
        result = HH1
    elif(piority1%6==4 or piority1%6==5):
        result =HH2
    elif(piority1%6==6):
        result =HH3
    if(piority1>6):
        result += Ht3
    if(piority2>=2):
        result +=Ht4
    if(piority3>2):
        result+=Hl1
    return result
