class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_birthday = Song(["happy birthday to you", "i dont want to get sued", "So I'll stop right there"])

happy_birthday.sing_me_a_song()