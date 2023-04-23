
python3 manage.py shell

from main.models import Item, ToDoList'

>>> from main.models import Item, ToDoList
>>> t = ToDoList(name='Ivanchika todo list')
>>> t.save()
>>> ToDoList.objects.all()
<QuerySet [<ToDoList: Ivan's List>]
>>> ToDoList.objects.get(id=4)

>>> t
<ToDoList: Ivanchika todo list>
>>> t.item_set.all()
<QuerySet []>
>>> t.item_set.create(text='go to school',complete=False)
<Item: go to school>
>>> t.item_set.get(id=3)
<Item: go to school>

>>> objects = ToDoList.objects.all()
>>> id_name_pair = [(object.id, object.name) for object in objects]
>>> id_name_pair
[(0, ''), (15, 'Ivanchika todo list')]