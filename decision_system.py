"""Object oriented Decision System"""
import system_tools
import itertools
import universal_tools


class DecisionSystem:
    """Contains list of DecisionObjects and list of Attributes"""
    def __init__(self, system_data):
        """Create system from data and type files"""
        self.attributes = system_tools.get_system_attributes(system_data)  # list of Attributes
        self.objects = system_tools.get_system_objects(system_data, self.attributes)  # list of Decision Objects

    def do_staff(self):
        rules = []
        for scale in range(self.objects.__len__()):
            scale += 1
            for decision_object in self.objects:
                if hasattr(decision_object, "eliminated"):
                    continue
                descriptor_combinations = list(itertools.combinations(decision_object.descriptors, scale))
                for descriptor_combination in descriptor_combinations:
                    rule = Rule(descriptor_combination, decision_object.decision, scale)
                    if system_tools.is_rule_inconsistent(rule, self.objects):
                        system_tools.calculate_support(rule, self.objects)
                        rules.append(rule)
                        break
            if system_tools.is_this_end(self.objects):
                break
        a = 0


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

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Attribute:
    """Information about attribute. Contains id, type, basic calculated values."""
    def __init__(self, identity):
        self.identity = identity


class Rule:
    """Information about rule. Contains descriptors, decision and support."""
    def __init__(self, descriptors, decision, scale):
        self.descriptors = descriptors
        self.decision = decision
        self.scale = scale
        self.support = 0


