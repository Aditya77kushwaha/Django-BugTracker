# from django import forms
# from .models import Bug

# class AddBugForm(forms.ModelForm):
#     class Meta:
#         model = Bug
#         fields = ('name','desc','priority','state')
#         widgets = {
#             'name': forms.TextInput(attrs = {
#                 'class': 'form-control'
#             }),
#             'desc': forms.Textarea(attrs = {
#                 'class': 'form-control'
#             }),
#             'priority': forms.Select(attrs = {
#                 'class': 'form-control'
#             }),
#             'state': forms.Select(attrs = {
#                 'class': 'form-control'
#             })
#         }
from django import forms
from .models import Bug

class AddBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = '__all__'
        # widgets = {
        #     'name': forms.TextInput(attrs = {
        #         'class': 'form-control'
        #     }),
        #     'desc': forms.Textarea(attrs = {
        #         'class': 'form-control'
        #     }),
        #     'priority': forms.Select(attrs = {
        #         'class': 'form-control'
        #     }),
        #     'state': forms.Select(attrs = {
        #         'class': 'form-control'
        #     }),
        #     'developer': forms.TextInput(attrs = {
        #         'class': 'form-control'
        #     }),
        #     'created_date': forms.TextInput(attrs = {
        #         'class': 'form-control'
        #     }),
        #     'developer_email': forms.TextInput(attrs = {
        #         'class': 'form-control'
        #     })
        # }