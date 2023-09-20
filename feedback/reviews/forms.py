from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ['owner_comment']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Review",
            "ratings": "Your Rating"
        }
        error_messages = {
            "user_name": {
              "required":"Brooo Don't be lazy, enter something",
              "max_length": "Acchhoo you have a huge name sweetie, Try to make it shorter"
            },
            "review_text":{
              "required":"Brooo Don't be lazy, enter something",
              "max_length": "Antha ekkuva vaddu le,kosey konchem"
            },
            "ratings":{
                "required":"Ignore why, ichesi povach ga",
                "max_value":"Antha prema vaddu le,5 lopala ivvu"
            }
        }