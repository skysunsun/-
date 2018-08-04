class song(object):

    def __init__(self, lyrics):#__init__是两个下划线
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = song(["There rally around the family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()


bulls_on_parade.sing_me_a_song()
