import csv
from django.core.management.base import BaseCommand

from courses.models import Course

class Command(BaseCommand):
    help = 'Export courses to a specified path as a CSV file'
    
    def add_arguments(self, parser):
        parser.add_argument('output_file', type=str, help='The path for exporting courses')
    
    def handle(self, *args, **kwargs):
        output_file = kwargs.get('output_file')
        if not output_file:
            self.stdout.write(self.style.ERROR('Please provide a valid output path for the CSV file'))
            return
        
        courses = Course.objects.all()
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'description'])
            for course in courses:
                writer.writerow([course.title , f'{course.description}'])
            
        self.stdout.write(self.style.SUCCESS(f'Successfully exported {courses.count()} courses to {output_file}!')) # note that some description lines will be in quotes and some will not.