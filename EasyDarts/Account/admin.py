from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

import datetime
from Account.models import *
from persiantools.jdatetime import JalaliDateTime


class AccountAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name' , 'nick_name' , 'email', 'phone_number', 'password1', 'password2', 'role',
                       'national_code', 'isReferee' , 'isCoach' ,'ageType' , 'gender', 'birthday', 'image', 'bio',)}),)
    list_display = ('user_id', 'first_name' ,'last_name', 'ageType' , 'isReferee' , 'isCoach' , 'nick_name' , 'email', 'get_date_joined', 'role', 'is_admin')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('role',)
    exclude = ('password',)
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('email',)

    filter_horizontal = ()
    fieldsets = ()

    def get_date_joined(self, obj):
        timestamp = datetime.datetime.timestamp(obj.date_joined)
        jalali_datetime = JalaliDateTime.fromtimestamp(timestamp)
        return jalali_datetime.strftime("%Y/%m/%d - %H:%M")

admin.site.register(Account, AccountAdmin)

class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['id','email','vc_code' , 'time_generated']
    search_fields = ['email']

    class Meta:
        model = VerificationCode

    def get_time_generated(self,obj):
        timestamp = datetime.datetime.timestamp(obj.time_generated)
        jalali_datatime = JalaliDateTime.fromtimestamp(timestamp)
        return jalali_datatime.strftime("%Y/%m/%d - %H:%M")

admin.site.register(VerificationCode, VerificationCodeAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['document_id' , 'get_user']
    list_filter = ['user']

    def get_user(self,obj):
        myId = obj.user_id
        result = Account.objects.get(user_id=myId)
        return result.__str__()

    class Meta:
        model = Document

admin.site.register(Document , DocumentAdmin)
