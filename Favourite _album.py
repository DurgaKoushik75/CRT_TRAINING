class Favourite_album:
    def __init__(self):
       self.album = []
    def add_to_album(self , song):
        self.album.append(song)
    def play_next_song(self):
        if self.is_album_empty() == False:
            print("playing " , self.album[-1])
    def play_album(self):
        while True:
            if self.is_album_empty() == False:
                print("playing",self.album[-1])
                self.album.pop()
            else:
                print("album is empty")
            
    def is_album_empty(self):
        if len(self.album) == 0:
            return True
        else:
            return False
obj = Favourite_album()
obj.add_to_album("og")
obj.add_to_album("pushpa")
obj.add_to_album("kalki")
obj.add_to_album("salaar")
obj.add_to_album("hanuman")
obj.add_to_album("khaleja")
obj.add_to_album("orange")
obj.add_to_album("jailer")
obj.play_next_song()
obj.play_album()
        