'''
Jinja is fast, extensible, expressive templeting engine.
We can add string in files.
We can put condition, loop by using Jinja.
Also, we can inherit one file into another file.

To install this library: pip install Jinja2
https://ttl255.com/jinja2-tutorial-part-1-introduction-and-variable-substitution/
'''

'''
Points from trainner:
    
'''

from jinja2 import Environment, FileSystemLoader
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

# trim_blocks will remove \n, extra space, etc. from whole block
env.trim_blocks = True

# Starting Jinja2 blocks from the beginning of the line and applying
# indentation inside-of them is roughly equivalent to enabling lstrip_block.
env.lstrip_blocks = True


# todo: pass simple variable into file
templates = env.get_template('hello_world.txt')
output = templates.render(name="hrudratt", color="black", color_list=['Black','White','Red','Green'], input_number=2)
print(output)

# # todo: pass dict into file
# templates = env.get_template('second.txt')
# person = {'name':'Hrudratt', 'color':'Black'}
# output = templates.render(data=person)

# # todo: condition
# # {% endif %} in txt file means end of if statement
# templates = env.get_template('truth.txt')
# output = templates.render(truth=True)
# print(output)

# # todo: For Loop
# # {% endfor %} in txt file means end of for loop
# templates = env.get_template('rainbow.txt')
# output = templates.render(colors=['Black','White','Red','Green'])
# print(output)

# # todo: inheritance
# template = env.get_template('child.html')
# output = template.render(Title='My First Project', body='Stuff')
# print(output)

# todo: Filters
'''
Let's jump straight in. Jinja2 filter is something we use to transform data
held in variables. We apply filters by placing pipe symbol | after the 
variable followed by name of the filter.

Ex:
1. <title>{{Title | capitalize }}</title> 
# capitalize is used for capitalize(1st letter capital) your string

2. ip name-server {{ name_servers | join(" ") }}  
Data:
name_servers:
['1.1.1.1','8.8.8.8','9.9.9.9','8.8.4.4']
Result:
ip name-server 1.1.1.1 8.8.8.8 9.9.9.9 8.8.4.4

3. {{ scraped_acl | first | trim }}
first named filter will take first only value of the list.
trim will remove extra spaces from string.

4. {% for i in  sflow_boxes|batch(2) %}
Sflow group{{ loop.index }}: {{ i | join(', ') }}
{% endfor %}
Batch filter splitting items into groups of fixed size.

Data:
sflow_boxes:['10.180.0.1','10.180.0.2','10.180.0.3','10.180.0.4','10.180.0.5']
Result:
Sflow group1: 10.180.0.1, 10.180.0.2
Sflow group2: 10.180.0.3, 10.180.0.4
Sflow group3: 10.180.0.5


You can refer more filters from: 
https://ttl255.com/jinja2-tutorial-part-4-template-filters/
'''

# # todo: pass function into file
# def name():
#     return "Hrudratt"
#
# def color():
#     return "black"
#
# templates = env.get_template('second.txt')
# person = {'name':name(), 'color':color()}
# output = templates.render(data=person)
# print(output)

# todo: Rest of things are pending...