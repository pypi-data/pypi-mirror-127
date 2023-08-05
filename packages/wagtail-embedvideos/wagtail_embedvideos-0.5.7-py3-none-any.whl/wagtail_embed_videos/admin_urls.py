from django.urls import path

from wagtail_embed_videos.views import chooser, embed_videos

app_name = "wagtail_embed_videos"

urlpatterns = [
    path("", embed_videos.index, name="index"),
    path("<int:embed_video_id>/", embed_videos.edit, name="edit"),
    path("<int:embed_video_id>/delete/", embed_videos.delete, name="delete"),
    path("add/", embed_videos.add, name="add"),
    path("usage/<int:embed_video_id>/", embed_videos.usage, name="embed_video_usage"),
    path("chooser/", chooser.chooser, name="chooser"),
    path("chooser/<int:embed_video_id>/", chooser.embed_video_chosen, name="embed_video_chosen"),
    path("chooser/upload/", chooser.chooser_upload, name="chooser_upload"),
]
