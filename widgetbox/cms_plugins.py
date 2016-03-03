from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import (
    Button, Quote,
    Gallery, GalleryImage,
    FaqTopic, Faq,
    Divider,
    HTML,
    Row, Column, Container,
    List, ListItem
)


class ButtonPlugin(CMSPluginBase):
    model = Button
    module = "Widget Box"
    name = "Button"
    render_template = "widgetbox/button.html"


class QuotePlugin(CMSPluginBase):
    model = Quote
    module = "Widget Box"
    name = "Quote"
    render_template = "widgetbox/quote.html"


class GalleryPlugin(CMSPluginBase):
    model = Gallery
    module = "Widget Box"
    name = "Gallery"
    allow_children = True
    child_classes = ["GalleryImagePlugin"]
    render_template = "widgetbox/gallery.html"


class GalleryImagePlugin(CMSPluginBase):
    model = GalleryImage
    module = "Widget Box"
    name = "Gallery Image"
    parent_classes = ["GalleryPlugin"]
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


class DividerPlugin(CMSPluginBase):
    model = Divider
    module = "Widget Box"
    name = "Horizontal divider"
    render_template = "widgetbox/divider.html"


class HTMLPlugin(CMSPluginBase):
    model = HTML
    module = "Widget Box"
    name = "HTML (unsafe)"
    render_template = "widgetbox/html.html"


class RowPlugin(CMSPluginBase):
    model = Row
    module = "Widget Box"
    name = "Row"
    allow_children = True
    render_template = "widgetbox/row.html"


class ColumnPlugin(CMSPluginBase):
    model = Column
    module = "Widget Box"
    name = "Column"
    allow_children = True
    render_template = "widgetbox/column.html"


class ContainerPlugin(CMSPluginBase):
    model = Container
    module = "Widget Box"
    name = "Container"
    allow_children = True
    render_template = "widgetbox/container.html"


class ListPlugin(CMSPluginBase):
    model = List
    module = "Widget Box"
    name = "List"
    allow_children = True
    child_classes = ["ListItemPlugin"]
    render_template = "widgetbox/list.html"


class ListItemPlugin(CMSPluginBase):
    model = ListItem
    module = "Widget Box"
    name = "List Item"
    allow_children = True
    parent_classes = ["ListPlugin"]
    render_template = "widgetbox/list-item.html"


plugin_pool.register_plugin(ButtonPlugin)
plugin_pool.register_plugin(QuotePlugin)
plugin_pool.register_plugin(GalleryPlugin)
plugin_pool.register_plugin(GalleryImagePlugin)
plugin_pool.register_plugin(FaqTopicPlugin)
plugin_pool.register_plugin(FaqPlugin)
plugin_pool.register_plugin(DividerPlugin)
plugin_pool.register_plugin(HTMLPlugin)
plugin_pool.register_plugin(RowPlugin)
plugin_pool.register_plugin(ColumnPlugin)
plugin_pool.register_plugin(ContainerPlugin)
plugin_pool.register_plugin(ListPlugin)
plugin_pool.register_plugin(ListItemPlugin)
