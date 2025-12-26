from django import forms

class create_new_projects(forms.Form):
      name=forms.CharField(label='Name of the project',max_length=200,
                           widget=forms.TextInput(attrs={'class':'input'}))
      
class create_new_instrument(forms.Form):
      n_instrument=forms.CharField(label='Name of the instrument',max_length=200,
                                   widget=forms.TextInput(attrs={'class':'input'}))

class create_new_study(forms.Form):
      n_study=forms.CharField(label='Name of the study',max_length=50,
                             widget=forms.TextInput(attrs={'class':'input'}))
      t_study=forms.CharField(label='Type of study',max_length=100,
                             widget=forms.TextInput(attrs={'class':'input'}))
      year = forms.ChoiceField(
                   choices=[(y, y) for y in range(2026, 2101)]
                  )

      season=forms.ChoiceField(label='Season',choices=[
            ('humeda','húmeda'),
            ('seca','seca'),
            ('fria','fría'),
            ('calida','cálida'),
            ('transicion','transición')
      ])
      n_specialist=forms.CharField(label='Name of specialist',max_length=100,
                                   widget=forms.TextInput(attrs={'class':'input'})) 
      
      country=forms.ChoiceField(
                              choices=[
                                    ('Peru','Perú')
                              ])
      taxon=forms.ChoiceField(
                            choices=[
                                  ('plantas','Plantas'),
                                  ('mamiferos','Mamíferos'),
                                  ('aves','Aves'),
                                  ('anfibios','Anfibios'),
                                  ('reptiles','Reptiles')
                            ])
      field=forms.FileField(label='File')