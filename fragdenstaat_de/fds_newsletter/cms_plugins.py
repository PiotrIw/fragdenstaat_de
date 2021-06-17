from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


@plugin_pool.register_plugin
class NewsletterPlugin(CMSPluginBase):
    module = _("Newsletter")
    name = _('Newsletter Formular')
    cache = True
    text_enabled = True
    render_template = "fds_newsletter/plugins/newsletter_form.html"


@plugin_pool.register_plugin
class SmartNewsletterPlugin(CMSPluginBase):
    module = _("Newsletter")
    name = _('Smart Newsletter Formular')
    cache = False
    text_enabled = True
    render_template = "fds_newsletter/plugins/smart_newsletter.html"
