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

    def covering(self):
        """Calculate rules with Sequential Covering algorithm"""
        rules = []
        for scale in range(self.objects.__len__()):
            scale += 1
            for decision_object in self.objects:
                if hasattr(decision_object, "eliminated"):
                    continue
                combination_of_descriptors = list(itertools.combinations(decision_object.descriptors, scale))
                for descriptor_combination in combination_of_descriptors:
                    rule = Rule(descriptor_combination, decision_object.decision, scale)
                    if system_tools.is_rule_inconsistent(rule, self.objects):
                        system_tools.calculate_support(rule, self.objects)
                        rules.append(rule)
                        break
            if system_tools.is_this_the_end(self.objects):
                break

    def exhaustive(self):
        rules = []
        matrix = {}

        objects_combinations = tuple(itertools.combinations([x for x in range(self.objects.__len__())], 2))
        for object_combination in objects_combinations:
            first_object = self.objects[object_combination[0]]  # object based on first index from tuple
            second_object = self.objects[object_combination[1]]  # object based on second index from tuple
            if not first_object.equal_decision(second_object):
                descriptors = system_tools.get_same_descriptors(first_object, second_object)
                matrix[object_combination] = descriptors
            else:
                matrix[object_combination] = []

        for scale in range(self.objects.__len__()):
            scale += 1
            for index, decision_object in enumerate(self.objects):
                if hasattr(decision_object, "eliminated"):
                    continue
                eliminated_descriptors = system_tools.get_descriptors_from_object_column(matrix, index)
                combination_of_descriptors = list(itertools.combinations(decision_object.descriptors, scale))
                r = system_tools.get_not_used_descriptors(eliminated_descriptors,combination_of_descriptors,
                                                          decision_object, scale)
                if r is not None:
                    for a in r:
                        rules.append(a)


class DecisionObject:
    """Contains list of Descriptors"""
    def __init__(self, descriptors, decision):
        self.descriptors = descriptors
        self.decision = decision

    def equal_decision(self, other):
        return True if self.decision == other.decision else False


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
