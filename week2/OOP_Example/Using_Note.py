from note import Note
from note import Notebook

my_notebook = Notebook("lecture_note")
print(my_notebook.title)

new_note = Note("Basic AI coursre")
print(new_note)
new_note_2 = Note("Python Lecture")
print(new_note_2)


my_notebook.add_note(new_note_2, 100)

my_notebook.notes[1] = new_note
my_notebook.notes[2] = Note("hello")

print(my_notebook.notes)
print(my_notebook.get_number_of_pages())