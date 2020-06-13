import pymongo
import dns
from models.blog import Blog
from database import Database
from menu import Menu


# client = pymongo.MongoClient("mongodb+srv://iv20023:Pppp363&@cluster0-4iffi.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test


# defining client that will connect to "udemy" db
#client = pymongo.MongoClient(uri)
# database=client['udemy']
# collection=database['students']

Database.initialize()

# post = Post(blog_id="123",
#             title="Another day in paradise",
#             content="bla-bla-bla",
#             author="Jorg"
#             )

#posts=Post.from_blog('123')
#print(posts)

# blog1 = Blog("Igor Velimirovic", "Remek djela velikih slikara", "Opis lijepih slika velikih autora")
# blog1.new_post()
# blog1.save_to_mongo()

menu=Menu()
menu.run_menu()
