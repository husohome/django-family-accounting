from django.forms import ModelForm, RadioSelect
from .models import Entry

def generate_choices():
    items = list(set([(e.item, e.item) for e in Entry.objects.order_by('-pub_date')]))
    return items

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['pub_date', 'item', 'entry_type', 'amount', 'note', 'receipt']
        widgets = {
            #'item': Select(choices = generate_choices()),
            #'entry_type': RadioSelect()
        }
        localized_fields = ('pub_date',)

#class ItemForm(ModelForm):
#    class Meta:
#        model = Item
#        fields = ['item_text']
