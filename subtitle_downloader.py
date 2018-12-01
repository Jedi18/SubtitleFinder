# THIS FILE IS RESPONSIBLE FOR TRAVERSING THE WEB,
# FINDING THE SUBTITLE AND DOWNLOADING IT SO THAT IT CAN BE USED BY THE MAIN GUI
import json
import re
import parse_subtitle_link

show_info = {'Brooklyn Nine Nine': ['Brooklyn Nine-Nine','C:\\Users\\targe\\PycharmProjects\\SubtitleFinder\\brooklynEp.json']}

seasons = {}

final_link = ''

def get_download_list(fileName):
    episodeInfo = get_show(fileName)
    load_show(episodeInfo)
    parse_subtitle_link.parseLink(final_link)

def get_show(fileName):
    pattern = re.compile(r'S[0-9][0-9]E[0-9][0-9]')
    matches = pattern.search(fileName)

    ep_info = matches.group(0)
    ep_info_index = fileName.find(ep_info)

    name = fileName[:ep_info_index]
    name = name.replace('.', ' ').strip()

    return {'show': name, 'sea': ep_info[:3], 'epNum': ep_info[3:]}

def load_show(episodeInfo):
    global seasons
    linka = show_info[episodeInfo['show']][1]
    with open(linka) as f:
        seasons = json.load(f)

    episode_number = int(episodeInfo['epNum'][1:])
    if episodeInfo['sea'][1] == '0':
        season_number = episodeInfo['sea'][2:]
    else:
        season_number = episodeInfo['sea'][1:]

    show_to_link(show_info[episodeInfo['show']][0], season_number, episode_number)

def return_episode_name(sea, epNum):
    return seasons[sea][epNum-1]

def show_to_link(show_name,sea, epNum):
    global final_link
    show_f = show_name.replace(" ", "_")
    name_f = return_episode_name(sea, epNum).replace(" ", "_")
    link = 'http://www2.addic7ed.com/serie/{}/{}/{}/{}'.format(show_f, sea, epNum, name_f)
    final_link = link
