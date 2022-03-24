from guizero import App, Text, TitleBox, TextBox, ListBox

def enter_pressed(event_data):
  if event_data.key == "\r":

    listbox.append(todo.value)
    todo.value = ""


def delete_item(value):
  listbox.remove(value)

app = App(title = "To Do List",
         width = 400,
         bg = 'lightblue')

title = Text(app, "To Do List",
            color = 'darkblue',
            size = 24)

titlebox = TitleBox(app,
                    "Add an Item",
                    border = 2)

todo = TextBox(titlebox,
               text = '',
               width = 30)

todo.when_key_pressed = enter_pressed

space = Text(app, "")

listbox = ListBox(app,
                  command =
                  delete_item,
                  items = [],
                 )

app.display()
