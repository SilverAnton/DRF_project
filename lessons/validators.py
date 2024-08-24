from rest_framework.exceptions import ValidationError


def validate_video_link(value):
    if "youtube.com" not in value:
        raise ValidationError("Video link must be a YouTube link.")
