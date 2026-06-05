#love - calcualtor

'''
def male(name):
        #print(len(name))
        countx = 0
        for x in name:
         for y in "true":
            if x == y:
             countx+= 1
        #print(countx)
        #print(type(countx))
        
        county = 0
        for a in name:
            for b in "love":
                if a == b:
                    county+=1
        #print(county)
        return countx+county   
def female(name):
        #print(len(name))
        countx = 0
        for x in name:
         for y in "true":
            if x == y:
             countx+= 1
        #print(countx)
        #print(type(countx))
        
        county = 0
        for a in name:
            for b in "love":
                if a == b:
                    county+=1
        #print(county)
        return countx+county



def love_calculator(malename,femalename):
    result = str(male(malename)) + str(female(femalename))
    print(result)

  

 #Example 
love_calculator("Kanye West", "Kim Kardashian")



'''

#A Different approach 


def truecal(male,female):
    countx = 0
    for x in male:
     for y in "true":
        if x == y:
           countx+=1
    county = 0
    for a in female:
       for b in "true":
          if a == b:
             county+=1
    return countx + county
    

def lovecal(male, female):
   counta = 0
   for p in male:
      for q in "love":
         if p == q:
            counta+=1
   counts = 0
   for s in female:
      for t in "love":
         if s == t:
            counts+=1  
   return counts + counta   

#truecal("Angela Yu", "Jack Bauer") 
#lovecal("Angela Yu", "Jack Bauer") 

def couplename():
   oneside = truecal("Angela Yu", "Jack Bauer") 
   otherside = lovecal("Angela Yu", "Jack Bauer") 
   combined = str(oneside) + str(otherside)
   return combined


score = couplename()
print("Love score:", score)
           
    
   
             
   
  
    


  
            