from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        required=True, 
        widget=forms.Textarea()
    )
    class Meta:
        fields = [
            'name', 'subject', 'from_email', 'message'
        ]