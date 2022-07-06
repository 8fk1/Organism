from django import forms
from . import models


class OrganismEditForm(forms.ModelForm):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     # 全てのフィールドを必須とする
    #     for k in self.fields:
    #         if k == 'name_ja':
    #             self.fields[k].required = True

    class Meta:
        model = models.Organism
        fields = (
            'name_ja',
            'name_en',
            'domain',
            'kingdom',
            'division',
            'classis',
            'order',
            'family',
            'status',
            'outline',
            'picture',
        )
