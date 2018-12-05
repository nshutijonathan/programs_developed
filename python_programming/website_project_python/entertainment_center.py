import fresh_tomatoes
import os
import sys
import media
toy_story=media.Movie("toy story",
                      "a story of boy anh his toys",r"C:\Users\Technician\Desktop\website_project_python\photos\toystory.jpg"
                      ,"https://www.youtube.com/watch?v=xItITCJfM3E")
#print(toy_story,storyline)
avatar=media.Movie("Avatar",r"a marine on the alien",
                   r"C:\Users\Technician\Desktop\website_project_python\photos\avatar.jpg"
                   ,r"C:\Users\Technician\Desktop\malaika.mp4")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock=media.Movie("school of rock","using rock music",r"C:\Users\Technician\Desktop\website_project_python\photos\school_of_rock.jpg",
                           "https://www.youtube.com/watch?v=FiCYoL7sIx0")
ratatouille=media.Movie("Ratatoiulle"," a rat is a chief in paris",
                        r"C:\Users\Technician\Desktop\website_project_python\photos\ratatouille.jpg"
                        ,"https://www.youtube.com/watch?v=nTTxc1Vf2pQ")
midnight_in_paris=media.Movie("midnight",
                              "going back",
                              r"C:\Users\Technician\Desktop\website_project_python\photos\midnight_in_paris.jpg"
                              ,"https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games=media.Movie("Hunger games","a realy show",r"C:\Users\Technician\Desktop\website_project_python\photos\hunger_games.jpg"
                         ,"https://www.youtube.com/watch?v=dF8Yteu29Tk")


movies=[toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)
