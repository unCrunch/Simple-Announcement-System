from django import forms

class BulkAssignmentUploadForm(forms.Form):
    csv_file = forms.FileField(label="Please Select a CSV File... ")
    
    def clean_csv_file(self):
        file = self.cleaned_data.get('csv_file')
        
        if not file.name.endswith('.csv'):
            raise forms.ValidationError("Please Upload a Valid CSV File.")
        
        if file.content_type != 'text/csv':
            raise forms.ValidationError("File Type is Not CSV.")
        
        return file