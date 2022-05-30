regions =  ['delhi', 'chennai', 'mumbai', 'kolkata']
colors = ['red', 'green' , 'blue' , 'yellow']

neighbour = {}
neighbour['delhi'] = ['mumbai','chennai']
neighbour['chennai'] = ['mumbai','kolkata','delhi']
neighbour['mumbai'] = ['delhi','chennai', 'kolkata']
neighbour['kolkata'] = ['mumbai','chennai']

region_color = {}

def validation(region,color):
  for i in neighbour.get(region):
    nb_color = region_color.get(i)
    #print(nb_color)
    
    if(nb_color == color):
      #print(color)
      return False
  return True

def colorselection(region):
  for color in colors:
    if(validation(region,color)):
      return color

def final_call():
  for region in regions:
    region_color[region] = colorselection(region)


final_call()

print(region_color)

  

if(region_color.values() == True):
  print("Insufficient color please more color") 
