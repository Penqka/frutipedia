from django import forms


from frutipedia.app.models import Profile, Fruit


class ProfileBaseFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password',)
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',

        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                }
            ),
        }


class ProfileEditForm(ProfileBaseFrom):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image', 'age')
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'image': 'Image URL:',
            'age': 'Age:',
        }


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        labels = {
            'name': '',
            'image': '',
            'description': '',
            'nutrition': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Fruit Name'
            }),
            'image': forms.URLInput(attrs={
                'placeholder': 'Fruit Image URL'
            }),
            'description': forms.Textarea(attrs={
                'rows': '10',
                'cols': '50',
                'placeholder': 'Fruit Description',
            }),
            'nutrition': forms.Textarea(attrs={

                'placeholder': 'Nutrition Info',
                'rows': '10',
                'cols': '50',
            }),
        }


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': 'Name:',
            'image': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }


class FruitDeleteForm(FruitEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('nutrition')
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
