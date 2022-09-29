from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error(
                "title", f'"{title}" is already taken. Please pick another one.'
            )
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data  # <--- dict
    #     title = cleaned_data.get("title")
    #     if title.lower().strip() == "friends":
    #         raise forms.ValidationError("This title is taken!")
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data  # <--- dict
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower().strip() == "friends":
            self.add_error("title", "This title is taken!")
            # raise forms.ValidationError("This title is taken!")
        if "friends" in content or "friends" in title.lower():
            self.add_error("content", "Firends cannot be in content")
            raise forms.ValidationError("Firends is not allowed")
        return cleaned_data
