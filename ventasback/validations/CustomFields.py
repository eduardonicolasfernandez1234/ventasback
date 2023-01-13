from django.db import models

class TitleField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(TitleField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).title()
    