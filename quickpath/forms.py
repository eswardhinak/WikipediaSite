from django import forms

class ArticleForm(forms.Form):
	start_article = forms.CharField(label = 'Start Article', max_length=250)
	end_article = forms.CharField(label = 'End Article', max_length=250)
	