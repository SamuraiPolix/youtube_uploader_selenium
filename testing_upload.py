from youtube_uploader_selenium import YouTubeUploader
import helper

title = 'title'
desc = 'desc'
tags = ['tag1', 'tag2']
video_path = 'C:/Bots/youtube_uploader_selenium/sources/1.mp4'
metadata_path = 'C:/Bots/youtube_uploader_selenium'   # '/metadata.json'
thumbnail_path = 'C:/Bots/youtube_uploader_selenium/sources/thumbnail.jpg'

helper.create_metadata(title, desc, tags, metadata_path)
metadata_path = f"{metadata_path}/metadata.json"

uploader = YouTubeUploader(video_path, metadata_path, thumbnail_path, profile_path="C:/Users/samla/AppData/Roaming/Mozilla/Firefox/Profiles/t9oijvlw.default-release")
was_video_uploaded, video_id = uploader.upload()
assert was_video_uploaded
