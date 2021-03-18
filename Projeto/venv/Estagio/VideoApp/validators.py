from django.core.exceptions import ValidationError

def file_size(value):
   filesize=value.size
   if filesize>10737418240:
       raise ValidationError("maximum size is 10GB")