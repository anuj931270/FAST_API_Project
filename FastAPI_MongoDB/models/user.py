from mongoengine import Document , StringField  , EmailField
# from dependencies.auth import get_current_user
# from dependencies.auth import get_current_user
class User(Document):
    full_name=StringField(
        required=True,
        max_length=100
    )
    
    email = EmailField(
        required=True,
        unique=True
    )
    
    phone = StringField(
        required=True,
        unique=True,
        max_length=10
    )
    
    password=StringField(
        required=True
    )
    
    meta={
        "collection":"users"
    }