from collections import namedtuple
import os
import sys

import requests
import requests_cache

requests_cache.install_cache()

plus_encoded = '%2C+'
Video = namedtuple('Video', 'title views likes')

base_url = 'https://www.googleapis.com/youtube/v3'
channel_id = 'UCrJhliKNQ8g0qoE_zvL8eVg'  # pycon
api_key = os.environ.get('YT_API_KEY') or sys.exit('set YT api key in env')
maxres = 50
next_page = 'none'

fmt = '{}/search?part=id,snippet&channelId={}'
fmt += '&type=video&key={}&maxResults={}&pageToken={}'
search_url = fmt.format(base_url, channel_id, api_key, maxres, next_page)


def get_videos(url):
    '''Get all video ids for a YT channel id using its API'''
    global next_page
    videos = {}
    while 1:
        resp = requests.get(url).json()
        for item in resp['items']:
            id_ = item['id']['videoId']
            videos[id_] = item['snippet']['title']
        prev_page = next_page
        next_page = resp.get('nextPageToken')
        if next_page:
            url = url.replace(prev_page, next_page)
        else:
            break
    return videos


def get_stats(videos):
    '''Get stats for a list of video ids'''
    video_ids = list(videos.keys())
    for i in range(0, len(video_ids), maxres):
        start, end = i, i + maxres
        vids = plus_encoded.join(video_ids[start:end])
        fmt = '{}/videos?part=statistics&id={}&key={}'
        stats_url = fmt.format(base_url, vids, api_key)
        resp = requests.get(stats_url).json()
        for item in resp['items']:
            yield Video(
                title=videos.get(item['id']),
                views=item['statistics'].get('viewCount', 0),
                likes=item['statistics'].get('likeCount', 0)
            )


if __name__ == '__main__':
    videos = get_videos(search_url)
    assert len(videos) == 143

    stats = list(get_stats(videos))
    assert len(stats) == 143

    row = '{:<10} {}'
    top = 10

    print()
    print('** Top {} views'.format(top))
    for vid in sorted(stats, key=lambda v: int(v.views),
                      reverse=True)[:top]:
        print(row.format(vid.views, vid.title))

    print()
    print('** Top {} likes'.format(top))
    for vid in sorted(stats, key=lambda v: int(v.likes),
                      reverse=True)[:top]:
        print(row.format(vid.likes, vid.title))
