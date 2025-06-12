movies_db = {
    2021: {
                 "shershah":["siddharth mlhotra","kiara advani"],
                 "shiddat":["sunny kaushal","radhika madan"]
             },
    2022: {
                 "bhool bhoolaiya2":["kartik aryan","kiara advani","tabu"],
                 "jugjug jiyo":["anil kapoor","nitu kapoor","varun dhavan","kiara advani"]
             },
    2023: {
                "pathan":["shah rukh khan","deepika padukone","john abrahim"],
                 "animal":["ranbir kapoor","rashmika mandana",]
             },

    2024 :{
               "fighter":["hritik roshan","deepika padukone"],
                 "kalki":["prabhas","deepika padukone"]   
             },
    2025: {
               "deva":["shahid kapoor","puja hegde"],
               "chhaava":["vicky kaushal","rashmika mandana"]

             }                        
             
           }
print(movies_db)

print("all movies of year 2023 are:", movies_db[2023])

print("print the cast of movie:",movies_db[2025]["deva"])

#print movies name and count from actors name
def find_actor(actor_name):
    found_movies = []
    for year,movies in movies_db.items():
        for movie,cast in movies.items():
            if actor_name in cast:
                found_movies.append(movie)

                if found_movies:
    
                    print("movie:",movie)
                    print("total movies:",len(found_movies))

actor_input=input("enter actor name:")
find_actor(actor_input)                        