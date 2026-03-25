from django.core.management.base import BaseCommand
from django.core.mail import send_mail

from courses.models import Submission

class Command(BaseCommand):
    help = 'Notify instructors that there have been new submissions for an assignment'
    
    def handle(self, *args, **kwargs):
        new_submissions = Submission.objects.filter(instructor_notified = False)
        
        count = new_submissions.count()
        if count == 0:
            self.stdout.write(self.style.SUCCESS('No new submissions'))
            return
        
        for submission in new_submissions:
            instructor = submission.assignment.owner
            send_mail(
                subject = 'New Submission Received',
                message = f'{submission.assignment.title} has a new submission for {submission.student_name}',
                from_email = 'notification@test.com',
                recipient_list = [instructor.email],
            )
        
            submission.instructor_notified = True
            submission.save()
            
        self.stdout.write(self.style.SUCCESS(f'Successfully notified instructor(s) about {count} new submissions.'))