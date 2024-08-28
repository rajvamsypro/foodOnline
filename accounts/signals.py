from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User,UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_reciever(sender,instance,created,**kwargs):
    #post_save.connect(post_save_create_profile_reciever,sender=User)
    print(created)
    if created:
        print('HELL YEAH')
        UserProfile.objects.create(user=instance)
        print('create the user profile')
    
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
           
        except Exception:
            # create the user profile if not exist
            UserProfile.objects.create(user=instance)
            print('Profile was not existed, but we created one')
                
        print('user is updated')