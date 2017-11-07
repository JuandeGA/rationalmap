#rationalmap/models.py

from django.db import models 

class User(models.Model): 
    
    user_id = models.AutoField(primary_key=True)
    
    #user_name includes first and last names
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    
    #email recovered from credentials' extraction external method
    email = models.EmailField()
    
    EMAIL_TYPE_CHOICES = (
        ('gmail', 'Gmail'),
        ('hotmail', 'Hotmail'),
        ('other', 'Other')
    )

    email_type = models.CharField(max_length=7,choices=EMAIL_TYPE_CHOICES)
    
    EMAIL_USE_CHOICES = (
        (1, 'Personal'),
        (2, 'Freelance'),
        (3, 'Enterprise'),
    )
    
    email_use = models.IntegerField(choices=EMAIL_USE_CHOICES)

    LANGUAGE_CHOICES = (
        ('es', 'Spanish'),
        ('en', 'English'),
    )
    
    pref_language = models.CharField(max_length=2,choices=LANGUAGE_CHOICES,default='en')
    
    TIMEZONE_CHOICES = (
        ('-12', 'GMT -12:00 Eniwetok, Kwajalein'),
        ('-11.0', 'GMT -11:00 Midway Island, Samoa'),
        ('-10.0', 'GMT -10:00 Hawaii'),
        ('-9.0', 'GMT -9:00 Alaska'),
        ('-8.0', 'GMT -8:00 Pacific Time (US & Canada)'),
        ('-7.0', 'GMT -7:00 Mountain Time (US & Canada)'),
        ('-6.0', 'GMT -6:00 Central Time (US & Canada, Mexico City'),
        ('-5.0', 'GMT -5:00 Eastern Time (US & Canada), Bogota, Lima'),
        ('-4.0', 'GMT -4:00 Atlantic Time (Canada), Caracas, La Paz'),
        ('-3.5', 'GMT -3:30 Newfoundland'),
        ('-3.0', 'GMT -3:00 Brazil, Buenos Aires, Georgetown'),
        ('-2.0', 'GMT -2:00 Mid-Atlantic'),
        ('-1.0', 'GMT -1:00 hour Azores, Cape Verde Islands'),
        ('0.0', 'GMT Western Europe Time, London, Lisbon, Casablanca'),
        ('1.0', 'GMT +1:00 Brussels, Copenhagen, Madrid, Paris'),
        ('2.0', 'GMT +2:00 Kaliningrad, South Africa'),
        ('3.0', 'GMT +3:00 Baghdad, Riyadh, Moscow, St. Petersburg'),
        ('3.5', 'GMT +3:30 Tehran'),
        ('4.0', 'GMT +4:00 Abu Dhabi, Muscat, Baku, Tbilisi'),
        ('4.5', 'GMT +4:30 Kabul'),
        ('5.0', 'GMT +5:00 Ekaterinburg, Islamabad, Karachi, Tashkent'),
        ('5.5', 'GMT +5:30 Bombay, Calcutta, Madras, New Delhi'),
        ('5.75', 'GMT +5:45 Kathmandu'),
        ('6.0', 'GMT +6:00 Almaty, Dhaka, Colombo'),
        ('7.0', 'GMT +7:00 Bangkok, Hanoi, Jakarta'),
        ('8.0', 'GMT +8:00 Beijing, Perth, Singapore, Hong Kong'),
        ('9.0', 'GMT +9:00 Tokyo, Seoul, Osaka, Sapporo, Yakutsk'),
        ('9.5', 'GMT +9:30 Adelaide, Darwin'),
        ('10.0', 'GMT +10:00 Eastern Australia, Guam, Vladivostok'),
        ('11.0', 'GMT +11:00 Magadan, Solomon Islands, New Caledonia'),
        ('12.0', 'GMT +12:00 Auckland, Wellington, Fiji, Kamchatka'),
    )
    
    timezone = models.CharField(max_length=5,choices=TIMEZONE_CHOICES,default='GMT')
    
    #class User methods:
    
    def __str__(self):
        return "Usuario " + self.first_name + " " + self.last_name + " dado de alta"

    def get_absolute_url(self):
    #Returns the url to access a particular instance of the model
        return reverse('model-detail-view', args=[str(self.id)])
    
    def get_name(self):
        return self.firt_name + ' ' + self.last_name
    
    
class Company(models.Model):
    
    company_id=models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    
    #class Company methods:
    
    def __str__(self):
        return "Empresa " + self.company_name + " dada de alta"
    
    def get_absolute_url(self):
    #Returns the url to access a particular instance of the model
        return reverse('model-detail-view', args=[str(self.id)])
    
    
class Employee(models.Model):
    
    company_id = models.ForeignKey('Company')
    user_id = models.ForeignKey('User')
    
    department = models.CharField(max_length=40)
    
    PROFILE_CHOICES = (
        (1, 'CEO'),
        (2, 'Senior Manager'),
        (3, 'Sales'),
        (4, 'Administrations, Financial, Operations'),
        (5, 'Marketing & PR'),
        (6, 'Consulting, Projet Management'),
        (7, 'Customer Care'),
        (8, 'Engineering, Systems, R&D'),
        (9, 'Training'),
    )
    
    profile = models.IntegerField(choices=PROFILE_CHOICES)
        
    WORKINGTIME_CHOICES = (
        (1, 'Fulltime'),
        (2, 'Partime'),
    )
    
    working_time = models.IntegerField(choices=WORKINGTIME_CHOICES,default=1)
    
    #class Employee methods:
    
    def __str__(self):
        return str(self.user_id) + " " + str(self.company_id)

    def get_absolute_url(self):
    #Returns the url to access a particular instance of the model
        return reverse('model-detail-view', args=[str(self.id)])
    
    #def dept_manager(company_id, department):
        