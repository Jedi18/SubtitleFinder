# THIS FILE IS RESPONSIBLE FOR TRAVERSING THE WEB,
# FINDING THE SUBTITLE AND DOWNLOADING IT SO THAT IT CAN BE USED BY THE MAIN GUI
import json
import re

shows = {'Brooklyn Nine Nine': 'Brooklyn Nine-Nine'}

class tvShow:
    def __init__(self, name):
        self.name = name

    seasons = {}
    episodes = {}

    def get_name(self):
        return self.name


brooklyn99 = tvShow("Brooklyn Nine-Nine")

with open('C:\\Users\\targe\\PycharmProjects\\SubtitleFinder\\brooklynEp.json') as f:
    brooklyn99.seasons = json.load(f)


def return_episode_name(show,sea,epNum):
    se = str(sea)
    return show.seasons[se][epNum-1]


def show_to_link(show, sea, epNum):
    show_f = show.get_name().replace(" ", "_")
    name_f = return_episode_name(show,sea,epNum).replace(" ", "_")
    link = 'http://www2.addic7ed.com/serie/{}/{}/{}/{}'.format(show_f, sea, epNum, name_f)
    print(link)

def get_download_list(fileName):
    episodeInfo = get_show(fileName)
    print(episodeInfo)

def get_show(fileName):
    pattern = re.compile(r'S[0-9][0-9]E[0-9][0-9]')
    matches = pattern.search(fileName)

    ep_info = matches.group(0)
    ep_info_index = fileName.find(ep_info)

    name = fileName[:ep_info_index]
    name = name.replace('.', ' ').strip()

    return {'show': shows[name], 'sea': ep_info[:3], 'epNum': ep_info[3:]}
