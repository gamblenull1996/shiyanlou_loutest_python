# -*- coding:utf-8 -*-

import copy

class Course(object):
    OBJECT_TYPE = 'COURSE'
    def __init__(self, name, public, lab_count):
        self.name = name
        self.public = public
        self.lab_count = lab_count

    # @property
    def count(self):
        return self.lab_count

    @staticmethod
    def typename(cls):
        return cls.OBJECT_TYPE

    def info(self):
        print Course.typename(), self.name

    def is_public(self):
        return self.public

class BootcampCourse(Course):
    def __init__(self, name, lab_count, price):
        self.lab_count = lab_count
        self.public = True
        self.price = price

    def update(self, lab_count, price):
        self.lab_count = lab_count
        self.price = price

    def info(self):
        print 'Lab count:', self.lab_count # 有问题
        print 'Public:', self.public
        print 'Price:', self.price

if __name__ == "__main__":
    linux_course = BootcampCourse('Linux', 10, 99)
    python_course = BootcampCourse('Python', 7, 79)

    # build course dict
    course_dict = {'Linux': linux_course, 'Python': python_course}

    # copy and backup course dict
    backup_course_dict = copy.deepcopy(course_dict)

    # update lab count and price
    linux_course.update(20, 199)
    python_course.update(10, 99)

    # compare with backup
    for name in ('Linux', 'Python'):
        print name, '- New Data'
        print course_dict[name].info()
        print name, '- Old Data'
        print backup_course_dict[name].info()
        print '---------------------------'



