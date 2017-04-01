"""Object oriented Decision System"""
import system_tools
import universal_tools


class DecisionSystem:
    """Contains list of DecisionObjects and list of Attributes"""
    def __init__(self, system_data):
        """Create system from data and type files"""
        self.attributes = system_tools.get_system_attributes(system_data)  # list of Attributes
        self.objects = system_tools.get_system_objects(system_data, self.attributes)  # list of Decision Objects


class DecisionObject:
    """Contains list of Descriptors"""
    def __init__(self, descriptors, decision):
        self.descriptors = descriptors
        self.decision = decision


class Descriptor:
    """Information about descriptor. Contains Attribute and his value"""
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value


class Attribute:
    """Information about attribute. Contains id, type, basic calculated values."""
    def __init__(self, identity):
        self.identity = identity


class Rule:
    """Information about rule. Contains descriptors, decision and support."""
    def __init__(self, descriptors, decision):
        self.descriptors = descriptors
        self.decision = decision
        self.support = 0

