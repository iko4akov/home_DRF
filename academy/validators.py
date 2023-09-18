import re
from rest_framework.validators import ValidationError


class VideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        succesful_urls = ['https://youtube.com', 'https://www.youtube.co']
        video_field = dict(value).get(self.field)
        if video_field not in succesful_urls:
            raise ValidationError('Ссылка на видео должна начинаться с https://youtube.com')
