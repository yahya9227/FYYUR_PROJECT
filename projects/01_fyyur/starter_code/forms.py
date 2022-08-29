from datetime import datetime
from email import message
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL
import enum

class Genre(enum.Enum):
            Alternative = 'Alternative'
            Blues ='Blues'
            Classical = 'Classical'
            Country = 'Country'
            Electronic ='Electronic'
            Folk = 'Folk'
            Funk = 'Funk'
            Hip_Hop = 'Hip-Hop'
            Heavy_Metal = 'Heavy Metal'
            Instrumental = 'Instrumental'
            Jazz = 'Jazz'
            Musical_Theatre = 'Musical Theatre'
            Pop = 'Pop'
            Punk = 'Punk'
            R_B = 'R&B'
            Reggae  = 'Reggae'
            Rock_n_Rolls = 'Rock n Roll'
            Soul = 'Soul'
            Other = 'Other'
            @classmethod
            def choices(cls):
                return [(choice.name,choice.value) for choice in cls]
        

class State(enum.Enum):
            AL  = 'AL'
            AK = 'AK'
            AZ = 'AZ'
            AR = 'AR'
            CA = 'CA'
            CO = 'CO'
            CT = 'CT'
            DE = 'DE'
            DC = 'DC'
            FL = 'FL'
            GA = 'GA'
            HI = 'HI'
            ID = 'ID'
            IL = 'IL'
            IN = 'IN'
            IA = 'IA'
            KS = 'KS'
            KY = 'KY'
            LA = 'LA'
            ME = 'ME'
            MT = 'MT'
            NE = 'NE'
            NV = 'NV'
            NH = 'NH'
            NJ = 'NJ'
            NM = 'NM'
            NY = 'NY'
            NC = 'NC'
            ND = 'ND'
            OH = 'OH'
            OK = 'OK'
            OR = 'OR'
            MD = 'MD'
            MA = 'MA'
            MI = 'MI'
            MN = 'MN'
            MS = 'MS'
            MO = 'MO'
            PA = 'PA'
            RI = 'RI'
            SC = 'SC'
            SD = 'SD'
            TN = 'TN'
            TX = 'TX'
            UT = 'UT'
            VT = 'VT'
            VA = 'VA'
            WA = 'WA'
            WV = 'WV'
            WI = 'WI'
            WY = 'WY'
            @classmethod
            def choices(cls):
                return [(choice.name,choice.value) for choice in cls]
        

class ShowForm(Form):
    artist_id = StringField(label=('artist_id'),
    validators=[DataRequired()]

    )
    venue_id = StringField(label=('venue_id'),
    validators=[DataRequired()]
    )
    start_time = DateTimeField(label=('start_time'),
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(label=('name'), 
    validators=[DataRequired()]
    )
    city = StringField(label=('city'), 
    validators=[DataRequired()]
    )
    state = SelectField(label=('state'), 
    validators=[DataRequired()],
        choices= State.choices()
    )
    address = StringField(label=('address'), 
    validators=[DataRequired()]
    )
    
    image_link = StringField(label=('image_link'),
    validators=[URL()]
    )
    genres = SelectMultipleField(label=('genres'),
        # TODO implement enum restriction
        validators=[DataRequired()],
        choices = Genre.choices()
    )
    facebook_link = StringField(label=('facebook_link'), 
    validators=[URL()]
    )
    website_link = StringField(label=('website_link'),
    validators=[URL()]
    )

    seeking_talent = BooleanField(label=('seeking_talent'),
    validators=[DataRequired()]
    )

    seeking_description = StringField(
        'seeking_description'
    )
    phone = IntegerField(label=('phone'),
    validators=[DataRequired()]
    )


class ArtistForm(Form):
    name = StringField(label=('name'), 
    validators=[DataRequired()]
    )
    city = StringField(label=('city'), 
    validators=[DataRequired()]
    )
    state = SelectField(label=('state'), 
    validators=[DataRequired()],
        choices= State.choices()
    )
    phone = IntegerField(label=('phone'),
        # TODO implement validation logic for phone 
        validators=[DataRequired()]
    )
    
    image_link = StringField(label=('image_link'),
    validators=[URL()]
    )
    genres = SelectMultipleField(label=('genres'), 
    validators=[DataRequired()],
        choices= Genre.choices()
     )
    facebook_link = StringField(label=('facebook_link'),
        # TODO implement enum restriction'', 
    validators=[URL()]
     )

    website_link = StringField(label=('website_link'),
    validators=[URL()]
     )

    seeking_venue = BooleanField(label=('seeking_venue'),
    validators=[DataRequired()]
    )

    seeking_description = StringField(label=('seeking_description')
     )


