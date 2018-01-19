import media
import fresh_tomatoes

'''
media contains the Movie class, It accepts the title, summary of the movies, the url of the picture and the url of the trailer in that order.
fresh_tomatoes contains the code for creating the html file.
'''

toy_story_2 = media.Movie('Toy Story',
						'''Woody is stolen by a toy dealer and when Buzz lightyear and some other toys try to rescue him, he decides to stay because he discovered that he was part of past television show.''',
						'https://vignette.wikia.nocookie.net/disney/images/9/92/Toy_Story_2_-_Poster.jpg/revision/latest?cb=20150108180811',
						'https://www.youtube.com/watch?v=Lu0sotERXhI')

avatar_movie = media.Movie('Avatar',
							''''Jake Sully paralyzed ex-machine links with an human/alien hybrid called Avatar to allow him move freely on an alien planet and falls in love with an alien woman and is drawn into a war to save hrer world''',
							'''https://i.pinimg.com/originals/f7/bc/7b/f7bc7b19e7f8555ba0f36aa3f2bc5dcd.jpg''',
							'''https://www.youtube.com/watch?v=uZNHIU3uHT4''')

justice_league = media.Movie('Justice League',
							''''Bruce Wayne and Wonder Woman now face an even greater threat of a newly awoken evil, they must now form an alliance of collection of heroes to face this''',
							'''https://i1.wp.com/batman-news.com/wp-content/uploads/2017/10/Justice-League-Poster-UK.jpg''',
							'''https://www.youtube.com/watch?v=3cxixDgHUYw''')

thor            = media.Movie('Thor',
							''''Thor is stripped of his power and sent to earth as punishment for starting a dormant war, while Loki has other plans after finding out that he is actually adopted''',
							'''https://static.comicvine.com/uploads/original/11111/111114602/5392367-1851099656-91P1w.jpg''',
							'''https://www.youtube.com/watch?v=lKoN-dTaepA''')

thor_ragnarok = media.Movie('Thor: Ragnarok',
							''''Imprisoned, the mighty Thor finds himself in a lethal gladiatorial contest against the Hulk, his former ally. Thor must fight for survival and race against time to prevent the all-powerful Hela from destroying his home and the Asgardian civilization.''',
							'''https://i.pinimg.com/originals/6e/3e/21/6e3e21906de36251ba03d265d58810a6.jpg''',
							'''https://www.youtube.com/watch?v=ue80QwXMRHg''')

creed         = media.Movie('Creed',
							''''The former World Heavyweight Champion Rocky Balboa serves as a trainer and mentor to Adonis Johnson, the son of his late friend and former rival Apollo Creed.''',
							'''https://images-na.ssl-images-amazon.com/images/M/MV5BODg5NDM1MDI4NF5BMl5BanBnXkFtZTgwMzg0MzQxNzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg''',
							'''https://www.youtube.com/watch?v=Uv554B7YHk4''')

black_panther = media.Movie('Black Panther',
							''''T'Challa, after the death of his father, the King of Wakanda, returns home to the isolated, technologically advanced African nation to succeed to the throne and take his rightful place as king.''',
							'''https://i.pinimg.com/originals/88/35/e1/8835e1a57282fafd2ffd831558030e4e.jpg''',
							'''https://www.youtube.com/watch?v=xjDjIWPwcPU''')

assasins_creed = media.Movie('Assasins Creed',
							''''Callum Lynch explores the memories of his ancestor Aguilar de Nerha and gains the skills of a Master Assassin, before taking on the secret Templar society.''',
							'''https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2ODczODg4Nl5BMl5BanBnXkFtZTgwMTQ5ODM3MDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg''',
							'''https://www.youtube.com/watch?v=gfJVoF5ko1Y''')

transformers_last_knight = media.Movie('Transformers: The Last Knight',
							''''Autobots and Decepticons are at war, with humans on the sidelines. Optimus Prime is gone. The key to saving our future lies buried in the secrets of the past, in the hidden history of Transformers on Earth.''',
							'''https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3OTI3MDk4N15BMl5BanBnXkFtZTgwNDg2ODIyMjI@._V1_UY1200_CR93,0,630,1200_AL_.jpg''',
							'''https://www.youtube.com/watch?v=gfJVoF5ko1Y''')


'''We then create a list of the movies and pass it into the open movies function in fresh tomatoes'''

movies = [toy_story_2, avatar_movie, justice_league, thor, thor_ragnarok, creed, black_panther, assasins_creed, transformers_last_knight]

fresh_tomatoes.open_movies_page(movies)
