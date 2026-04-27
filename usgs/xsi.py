

def _get_xsd_boolean(element):
    pass


def _get_xsd_int(element):
    pass


def _get_xsd_double(element):
    pass

    
def _get_xsd_long(element):
    pass


def _get_xsd_string(element):
    pass


def _get_xsd_array(element):
    pass


def _get_none(element):
    pass


_dtypes = {
    "xsd:string": _get_xsd_string,
    "xsd:boolean": _get_xsd_boolean,
    "xsd:int": _get_xsd_int,
    "xsd:double": _get_xsd_double,
    "xsd:long": _get_xsd_long,
    
    "ns1:ArrayOfService_Inventory_DisplayListValue": _get_xsd_array,
    "ns1:Service_Inventory_Bounds": _get_xsd_array,
    "ns1:Service_Class_Coordinate": _get_xsd_array,
    
    None: _get_none
}


def get(element):
    key = element.attrib.get("{http://www.w3.org/2001/XMLSchema-instance}type")
    return _dtypes[key](element)

