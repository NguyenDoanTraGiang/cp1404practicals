from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(visual_basic)

class_objects = [ProgrammingLanguage.object_list(ruby), ProgrammingLanguage.object_list(python),
                 ProgrammingLanguage.object_list(visual_basic)]
print("\nThe dynamically typed languages are:")
for class_object in class_objects:
    if class_object[2] is True:
        print(class_object[0])
