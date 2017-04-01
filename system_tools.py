"""Contains useful tools to work with decision system"""
import decision_system
import universal_tools
import math


def get_system_attributes(system_file):
    """Return attributes and their values from system type file"""
    system_file.seek(0)  # return to beginning of file
    first_line = system_file.readline()[:-2]
    first_line = first_line.rstrip().split(' ')  # remove from end all white chars and split row by ' '
    attributes = []
    if first_line != '':  # true if line isn't empty
        for index, value in enumerate(first_line):
            attributes.append(decision_system.Attribute("a{}".format(index)))  # return list of Attributes
    return attributes


def get_system_objects(system_file, attributes):
    """get info about system, return list of Decision Objects and unique decisions"""
    system_file.seek(0)  # return to beginning of file
    objects = []
    for line in system_file:
        if line.strip() != '':  # true if line isn't empty
            objects.append(__get_object__(line, attributes))  # append Decision Object to list of objects
    return objects


def __get_object__(line, attributes):
    """Private method. Return Decision Object with list of descriptors and decision"""
    descriptors = []
    line = line.rstrip().split(' ')  # remove from end all white chars and split row by ' '
    for index, attribute in enumerate(attributes):
        descriptor = decision_system.Descriptor(attribute, line[index])
        descriptors.append(descriptor)
    decision = line[-1]  # last value from current line is decision for current object
    decision_object = decision_system.DecisionObject(descriptors, decision)
    return decision_object


def is_object_meets_rule(rule, decision_object):
    """Return true if meets; return false if not"""
    for descriptor in rule.descriptors:
        if descriptor not in decision_object.descriptors:
            return False
    else:
        return True


def is_rule_consistency(rule, objects):
    """Return true if """
    for decision_object in objects:
        if is_object_meets_rule(rule, decision_object) and rule.decision != decision_object.decision:
            return False
    else:
        return True


def make_rule(decision_object, combination):
    """Return rule"""
    return decision_system.Rule(combination, decision_object.decision)