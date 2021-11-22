from django.contrib import admin

from varzeshkaran.models import *


class RaceAdmin(admin.ModelAdmin):
    add_fields = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name', 'holdingDate', 'location', 'conditions', 'EntranceFee',
                'Awards', 'registrationDate', 'capacity',)
        }
         )
    )
    list_display = ('name', 'holdingDate', 'conditions')
    search_fields = ('name',)

    class Meta:
        model = Race


admin.site.register(Race, RaceAdmin)


class AthleteAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'email', 'phone_number', 'ageType', 'gender', 'image',)}),)

    list_display = (
        'user_id', 'first_name', 'last_name', 'ageType', 'isReferee', 'isCoach', 'nick_name', 'email', 'role',
        'is_admin')


admin.site.register(Athlete, AthleteAdmin)


class CoachAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'email', 'phone_number', 'ageType', 'gender', 'image',)}),)

    list_display = (
        'user_id', 'first_name', 'last_name', 'ageType', 'isReferee', 'isCoach', 'nick_name', 'email', 'role',
        'is_admin')


admin.site.register(Coach, CoachAdmin)


class RefreeAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'email', 'phone_number', 'ageType', 'gender', 'image',)}),)

    list_display = (
        'user_id', 'first_name', 'last_name', 'ageType', 'isReferee', 'isCoach', 'nick_name', 'email', 'role',
        'is_admin')


admin.site.register(Refree, RefreeAdmin)


class ClubAdmin(admin.ModelAdmin):
    add_fields = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'city', 'Images', 'discription', 'AllAwards')
        })
    )

    list_display = ('name', 'city', 'Images',)


admin.site.register(Club, ClubAdmin)


class ClubAdministratorAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'email', 'phone_number', 'ageType', 'gender', 'image',)}),)

    list_display = (
        'user_id', 'first_name', 'last_name', 'ageType', 'nick_name', 'email', 'role', 'is_admin')


admin.site.register(AdminOfClub , ClubAdministratorAdmin)
