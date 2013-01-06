class Enum(object):
    def __init__(self, module_globals, member_list):
        forward_dict = {}
        reverse_dict = {}
        next_value = 0
        for member in member_list:
            if isinstance(member, basestring):
                name = member
                value = None
            else:
                name, value = member
            if value is None:
                value = next_value
            if name in forward_dict:
                raise ValueError('Multiple definitions for name %r' % (name, ))
            forward_dict[name] = value
            next_value = value + 1
            if value in reverse_dict:
                raise ValueError('Multiple names for value %r: %r, %r' %
                    (value, reverse_dict[value], name))
            reverse_dict[value] = name
            module_globals[name] = value
        self.forward_dict = forward_dict
        self.reverse_dict = reverse_dict

    def __call__(self, value):
        return self.reverse_dict[value]

    def get(self, value, default=None):
        return self.reverse_dict.get(value, default)

