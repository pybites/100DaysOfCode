#!python3
# subclass_template.py is a usable, blank template
# for creating a Python Class with subclass.


class Class1(object):
    def __init__(self, attribute1, attribute2, attribute3):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3

    # Class Function Examples:

    def ClassFunction_1(self):
        pass

    def ClassFunction_2(self):
        return self.attribute2

    def ClassFunction_3(self):
        variable = int(self.attribute1 + self.attribute3)
        return variable


# Define an "empty" subclass off the primary class above
class SubClass1(Class1):
    def __init__(self,
                 attribute1,
                 attribute2,
                 attribute3,
                 sub_attr_1,
                 sub_attr_2):
        super().__init__(attribute1, attribute2, attribute3)
        self.sub_attr_1 = sub_attr_1
        self.sub_attr_2 = sub_attr_2

    def SubClassFunction_1(self):
        return self.sub_attr_1
