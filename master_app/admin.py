from django.contrib import admin


from .models import Student,Hostel,HostelFees,Room,Parent,Warden


admin.site.register(Student)
admin.site.register(Hostel)
admin.site.register(HostelFees)
admin.site.register(Room)
admin.site.register(Warden)
admin.site.register(Parent)
