from django.db import models

class TitleField(models.CharField):
    """Override a custom validation field.
    
    This field is used to transform the text value where each word is titlecased.
    
    """

    def __init__(self, *args, **kwargs):
        super(TitleField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).title()
    