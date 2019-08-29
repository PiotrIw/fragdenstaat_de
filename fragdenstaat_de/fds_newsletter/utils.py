from newsletter.models import Subscription

REFERENCE_PREFIX = 'newsletter-'


def handle_bounce(sender, bounce, should_deactivate=False, **kwargs):
    if not should_deactivate:
        return
    if bounce.user:
        Subscription.objects.filter(
            user=bounce.user
        ).update(subscribed=False)
    else:
        Subscription.objects.filter(
            email_field=bounce.email
        ).update(subscribed=False)
