from django.db import models
from hostel_app.models import CustomUser
from multiselectfield import MultiSelectField


class Hostel(models.Model):
    HOSTEL_TYPES = [
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
        
    ]

    ROOM_TYPES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        
    ]
    

    hostel_name = models.CharField(max_length=255)
    hostel_type = models.CharField(max_length=10, choices=HOSTEL_TYPES)
    location = models.CharField(max_length=255)
    number_of_floors = models.PositiveIntegerField()
    number_of_rooms = models.PositiveIntegerField()
    type_of_room = models.CharField(max_length=10, choices=ROOM_TYPES)
    warden_assigned = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='hostels')

    def __str__(self):
        return self.hostel_name
    




    

    

class Room(models.Model):
    ROOM_ASSETS_CHOICES = [
        ('Air Conditioner', 'Air Conditioner'),
        ('Water Heater', 'Water Heater'),
        ('Bed', 'Bed'),
        ('Fridge', 'Fridge'),
        ('Stove', 'Stove'),
    ]

    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    room_strength = models.IntegerField()
    room_assets = MultiSelectField(choices=ROOM_ASSETS_CHOICES, max_choices=3, max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return {self.room_number}
    



class Warden(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    register_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='warden')
    hostel_assigned = models.CharField(max_length=100, default="Hostel_Name")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='wardens')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    register_number = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    parents_number = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5)
    department = models.CharField(max_length=50)
    check_in_date = models.DateField()
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='hostelstudent')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    email = models.EmailField()
    child = models.OneToOneField(Student, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='parents')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class HostelFees(models.Model):
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.DecimalField(max_digits=10, decimal_places=2)
    transport = models.DecimalField(max_digits=10, decimal_places=2)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fees')

    def __str__(self):
        return {self.hostel}


