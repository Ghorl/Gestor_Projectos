from django import forms

class create_new_projects(forms.Form):
      name=forms.CharField(label='Name of the project',max_length=200,
                           widget=forms.TextInput(attrs={'class':'input'}))
      
class create_new_instrument(forms.Form):
      n_instrument=forms.CharField(label='Name of the instrument',max_length=200,
                                   widget=forms.TextInput(attrs={'class':'input'}))