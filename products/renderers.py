from rest_framework_xml.renderers import XMLRenderer


class NaverPayXMLRenderer(XMLRenderer):
    root_tag_name = "products"
    item_tag_name = "product"
