from django import forms
from .models import User


class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ['FIO', 'gender', 'number', 'number2', 'birthday_date', 'adres', 'code',
                  'family_field', 'FIO_family', 'number_family', 'email', 'status', 'blacklist',
                  'source', 'class_format', 'personal_disc', 'Vk_id', 'Fb_id', 'Ig_id', 'contraindications', 'sms',
                  'email_choise', 'notes_unvi', 'notes_visible', 'passport', 'passport_date', 'passport_org', 'org_code',
                  ]

        widgets = {
            'FIO': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'number2': forms.NumberInput(attrs={'class': 'form-control'}),
            'birthday_date': forms.TextInput(attrs={'class': 'form-control'}),
            'adres': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'family_field': forms.TextInput(attrs={'class': 'form-control'}),
            'FIO_family': forms.TextInput(attrs={'class': 'form-control'}),
            'number_family': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'blacklist': forms.Select(attrs={'class': 'form-control'}),
            'source': forms.Select(attrs={'class': 'form-control'}),
            'class_format': forms.TextInput(attrs={'class': 'form-control'}),
            'personal_disc': forms.NumberInput(attrs={'class': 'form-control'}),
            'Vk_id': forms.TextInput(attrs={'class': 'form-control'}),
            'Fb_id': forms.TextInput(attrs={'class': 'form-control'}),
            'Ig_id': forms.TextInput(attrs={'class': 'form-control'}),
            'contraindications': forms.TextInput(attrs={'class': 'form-control'}),
            'sms': forms.Select(attrs={'class': 'form-control'}),
            'email_choise': forms.Select(attrs={'class': 'form-control'}),
            'notes_unvi': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'notes_visible': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'passport': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_date': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_org': forms.TextInput(attrs={'class': 'form-control'}),
            'org_code': forms.NumberInput(attrs={'class': 'form-control'}),
        }