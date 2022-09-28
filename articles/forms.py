from distutils.command.clean import clean
from django import forms


class ArticleForm(forms.Form):
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
