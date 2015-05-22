from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import (
    ButtonPlugin, QuotePlugin,
    GalleryPlugin, GalleryImagePlugin,
    FaqTopic, Faq
)


class CMSButtonPlugin(CMSPluginBase):
    model = ButtonPlugin
    module = "Widget Box"
    name = "Button"
    render_template = "widgetbox/button.html"


class CMSQuotePlugin(CMSPluginBase):
    model = QuotePlugin
    module = "Widget Box"
    name = "Quote"
    render_template = "widgetbox/quote.html"


class CMSGalleryPlugin(CMSPluginBase):
    model = GalleryPlugin
    module = "Widget Box"
    name = "Gallery"
    allow_children = True
    child_classes = ["CMSGalleryImagePlugin"]
    render_template = "widgetbox/gallery.html"


class CMSGalleryImagePlugin(CMSPluginBase):
    model = GalleryImagePlugin
    module = "Widget Box"
    name = "Gallery Image"
    parent_classes = ["CMSGalleryPlugin"]
    render_template = "widgetbox/gallery-image.html"


class FaqTopicPlugin(CMSPluginBase):
    model = FaqTopic
    module = "Widget Box"
    name = "FAQ Topic"
    allow_children = True
    child_classes = ["FaqPlugin"]

    def get_render_template(self, context, instance, placeholder):
        return instance.style


class FaqPlugin(CMSPluginBase):
    model = Faq
    module = "Widget Box"
    name = "FAQ"
    parent_classes = ["FaqTopicPlugin"]

    def get_render_template(self, context, instance, placeholder):
        return "widgetbox/faq.html"
        # a = dir(instance)
        # b = dir(context)
        c = dir(placeholder)
        parent = dir(instance.get_parent())
        assert False
        return instance.style


plugin_pool.register_plugin(CMSButtonPlugin)
plugin_pool.register_plugin(CMSQuotePlugin)
plugin_pool.register_plugin(CMSGalleryPlugin)
plugin_pool.register_plugin(CMSGalleryImagePlugin)
plugin_pool.register_plugin(FaqTopicPlugin)
plugin_pool.register_plugin(FaqPlugin)
