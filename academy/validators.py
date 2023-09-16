import re
from rest_framework.validators import ValidationError

class VideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r"https://youtube.com")
        video_field = dict(value).get(self.field)
        print(video_field)
        if not bool(reg.search(video_field)):
            raise ValidationError('Ссылка на видео  должна начинаться с https://youtube.com')
