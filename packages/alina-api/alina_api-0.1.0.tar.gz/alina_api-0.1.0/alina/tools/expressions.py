from re import compile

'''
Month cases:
    >>> date_pattern.match('2021-9-1')            # month is '9' string
    True
    >>> date_pattern.match('2021-09-1')           # month is '09 string 
    True

Day cases:
    >>> date_pattern.match('2021-11-1')           # day is '1' string
    True
    >>> date_pattern.match('2021-11-01')          # day is '01' string
    True 
'''

date_pattern = compile('(?P<date>(19|20\d\d)[-\.](0[1-9]|[1-9]|1[012])[- \.](0[1-9]|[12][0-9]|3[01]|[1-9]))')

hour_pattern = compile('(\d+:\d+)')

text_pattern = compile('\w+')

""" 
allocation_information_container_pattern matches container from an allocation container tag that is not made for 
'comparision'. 
"""
allocation_information_container_pattern = compile('^allocation-info ((?!comparison).)*$')

allocation_start_timeline, allocation_end_timeline = 'begin', 'end'
allocation_timeline_pattern = compile(f'^({allocation_start_timeline}|{allocation_end_timeline})')

allocation_id_pattern = compile('(id=)(?P<id>\d+)')

allocation_component_pattern = compile('^(duty-components).*')