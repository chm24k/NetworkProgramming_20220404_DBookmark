from django import forms

from bookmark.models import Bookmark


class BookmarkCreationForm(forms.ModelForm):
    url = forms.CharField(label='링크', widget=forms.TextInput)

    class Meta:
        model = Bookmark
        fields = ['name', 'url']

    def clean_url(self):
        url = self.cleaned_data.get('url') #url 가져오자
        if not (url.startswith('http://') or url.startwidth('https://')):   #만약 http:// 나 https://가 없으면,
            url = 'http://' + url      #https:// 추가하자
        return url


    def save(self, commit=True):
        new_bookmark = Bookmark.objects.create(
            name=self.cleaned_data.get('name'),     #사용자가 입력한 내용을 한번 clean_name()하고 깨끗해진거 가져옴
            url=self.cleaned_data.get('url'),     #사용자가 입력한 내용을 한번 clean_url()하고 깨끗해진거 가져옴
        )
        return new_bookmark