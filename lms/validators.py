from rest_framework.serializers import ValidationError

allowed_prefixes = ['youtube.com', 'https://youtube.com', 'http://youtube.com']

def validate_youtube_url(value):
    if not any(value.startswith(prefix) for prefix in allowed_prefixes):
        raise ValidationError('Ссылка должна начинаться с youtube.com')