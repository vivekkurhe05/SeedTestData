from __future__ import print_function
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gfgp_db.settings")
django.setup()
from faker import Faker

fake = Faker('en_US')
fake.seed(0000)

print('Address type of data')
print('City->', fake.city())
print('Zip_code_plus->', fake.zipcode_plus4())
# print('Random letters->', fake.random_letters(length=16))
# print('Postal code->', fake.postalcode_plus4())
# print('Street name->', fake.street_name())
# print('Random int range->', fake.random_int(min=0, max=9999))
# print('Secondary address->', fake.secondary_address())
# print('Simple zip code->', fake.zipcode())
# print('Postal code->', fake.postalcode())
# print('State abbreviation->', fake.state_abbr(include_territories=True))
# print('Country->', fake.country())
# print('Country code->', fake.country_code(representation="alpha-2"))
# print('Address->', fake.address())
# print('State->', fake.state())
# print('Street address->', fake.street_address())

# print('\n==============================')
# print('Barcode type of data')
# print('Barcode->', fake.ean(length=13))

# print('\n==============================')
# print('Credit card type of data')
# print('Credit card CVV->', fake.credit_card_security_code(card_type=None))
# print('Credit card full details->', fake.credit_card_full(card_type=None))
# print('Credit card expiry->', fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"))
# print('Credit card number->', fake.credit_card_number(card_type=None))
# print('Credit card provider->', fake.credit_card_provider(card_type=None))

# print('\n==============================')
# print('File type of data')
# print('Unix data->', fake.unix_device(prefix=None))
# print('File path->', fake.file_path(depth=1, category=None, extension=None))
# print('File extension->', fake.file_extension(category='image'))
# print('File name->', fake.file_name(category=None, extension=None))

print('\n================================')
print('Geo_location type of data')
print('Fake lat_long->', fake.latlng())
print('Fake longitude->', fake.longitude())
print('latitude->', fake.latitude())
print('location on land->', fake.location_on_land(coords_only=True)[1])
print('coordinates->', fake.coordinate(center=None, radius=0.001))
print('local lat_long->', fake.local_latlng(country_code="US", coords_only=False))

# print('\n================================')
# print('Internet type of data')
# print('URI->', fake.uri_extension())
# print('Safe mail->', fake.safe_email())
# print('URL->', fake.url(schemes=None))
# print(fake.image_url(width=None, height=None))
# print('URI->', fake.uri())
# print('Email->', fake.email())
# print('URI page->', fake.uri_page())
# print('Free email->', fake.free_email())
# print('Username->', fake.user_name())
# print('Free email domain->', fake.free_email_domain())

# print('\n================================')
# print('Lorem ipsum type of data')
# print('Sentence->', fake.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None))
# print('Text->', fake.text(max_nb_chars=200, ext_word_list=None))
# print('Words->', fake.words(nb=3, ext_word_list=None, unique=False))
# print('Paragraph->', fake.paragraph(nb_sentences=1, variable_nb_sentences=True, ext_word_list=None))
# print('Fake word->', fake.word(ext_word_list=None))
# print('Paragraph->', fake.paragraphs(nb=3, ext_word_list=None))
# print('Sentences->', fake.sentences(nb=3, ext_word_list=None))

# print('\n================================')
# print('Miscelleneous type of data')
# print('Boolean value->', fake.boolean(chance_of_getting_true=50))
# print('Password->', fake.password(length=5, special_chars=False, digits=True, upper_case=False, lower_case=True))

# print('\n================================')
# print('Phone number type of data')
# print('Phone number->', fake.phone_number())

# print('\n================================')
# print('Profile type of data')
# d = {'sex'}
# print(fake.profile(fields=d, sex=None))

# print('\n================================')
# print('Currency type of data')
# print('Currency name->', fake.currency_name())
# print('Currency code->', fake.currency_code())

# print('\n================================')
# print(fake.random_int(min=0, max=1))
# print(fake.locale())
# print(fake.first_name_female())
# print(fake.paragraph())
