from random import randint

from django import template

from constants import DEPARTMENTS, SEMESTERS

register = template.Library()


@register.inclusion_tag('easy_admin/easy_table.html')
def easy_table(table_data):
    return table_data


@register.inclusion_tag('easy_admin/link_buttons_group.html')
def link_buttons_group(buttons):
    return {'buttons': buttons}


@register.inclusion_tag('easy_admin/enable_field_button.html')
def enable_f_button(field_id):
    return {'field_id': str(field_id)}


@register.filter
def join_s(a, b):
    return str(a) + str(b)


@register.filter
def dept_name(dept):
    for code, name in DEPARTMENTS:
        if code == dept:
            return name
    return "Unknown"


@register.filter
def semester_name(semester):
    for code, name in SEMESTERS:
        if code == semester:
            return name
    return "Unknown"


@register.filter(name='add_classes')
def add_classes(value, arg="form-control"):
    """
    Add provided classes to form field
    :param value: form field
    :param arg: string of classes seperated by ' '
    :return: edited field
    """
    css_classes = value.field.widget.attrs.get('class', '')
    # check if class is set or empty and split its content to list (or init list)
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []
    # prepare new classes to list
    args = arg.split(' ')
    for a in args:
        if a not in css_classes:
            css_classes.append(a)
    # join back to single string
    return value.as_widget(attrs={'class': ' '.join(css_classes)})


@register.filter
def hide_field(value):
    return value.as_widget(attrs={'hidden': True})


@register.filter
def disable_field(value, field_id=randint(1, 1000000), args=''):
    classes = value.field.widget.attrs.get('class', '')
    if classes:
        classes = classes.split(' ')
    else:
        classes = []
    args = args.split(' ')
    classes = [*classes, *args]
    return value.as_widget(attrs={
        'disabled': True,
        'class': ' '.join(classes),
        'id': field_id,
    })


@register.filter
def readonly_field(value, field_id=randint(1, 1000000), args=''):
    classes = value.field.widget.attrs.get('class', '')
    if classes:
        classes = classes.split(' ')
    else:
        classes = []
    args = args.split(' ')
    classes = [*classes, *args]
    return value.as_widget(attrs={
        'readonly': True,
        'class': ' '.join(classes),
        'id': field_id,
    })


@register.filter
def readonly_field(value, field_id=randint(1, 1000000), args=''):
    classes = value.field.widget.attrs.get('class', '')
    if classes:
        classes = classes.split(' ')
    else:
        classes = []
    args = args.split(' ')
    classes = [*classes, *args]
    return value.as_widget(attrs={
        'readonly': True,
        'class': ' '.join(classes),
        'id': field_id,
    })


@register.inclusion_tag('easy_admin/disable_with_button.html')
def disable_with_button(field, classes='form-control'):
    field_id = randint(1, 1000000)
    return {'field': readonly_field(field, field_id, classes), 'id': field_id, 'label': field.label}


@register.inclusion_tag('easy_admin/two_rwb.html')
def double_rwb(field1, field2, classes='form-control'):
    id1 = randint(1, 1000000)
    id2 = randint(1, 1000000)
    return {
        'field1': readonly_field(field1, id1, classes), 'id1': id1, 'label1': field1.label,
        'field2': readonly_field(field2, id2, classes), 'id2': id2, 'label2': field2.label,
    }


@register.inclusion_tag('easy_admin/two_fields.html')
def double_field(field1, field2, classes='form-control'):
    id1 = randint(1, 1000000)
    id2 = randint(1, 1000000)
    return {
        'field1': add_classes(field1, classes), 'id1': id1, 'label1': field1.label,
        'field2': add_classes(field2, classes), 'id2': id2, 'label2': field2.label,
    }


@register.inclusion_tag('easy_admin/two_fields.html')
def double_field_readonly(field1, field2, classes='form-control'):
    id1 = randint(1, 1000000)
    id2 = randint(1, 1000000)
    return {
        'field1': readonly_field(field1, id1, classes), 'id1': id1, 'label1': field1.label,
        'field2': readonly_field(field2, id2, classes), 'id2': id2, 'label2': field2.label,
    }


@register.inclusion_tag('easy_admin/single_field.html')
def single_field(field1, classes='form-control'):
    id1 = randint(1, 1000000)
    return {
        'field1': add_classes(field1, classes), 'id1': id1, 'label1': field1.label
    }


@register.inclusion_tag('easy_admin/single_field.html')
def single_field_readonly(field1, classes='form-control'):
    id1 = randint(1, 1000000)
    return {
        'field1': readonly_field(field1, id1, classes), 'id1': id1, 'label1': field1.label
    }
