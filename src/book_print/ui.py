import tkinter
import tkinter.ttk

from book_print.pages import calculate_packs, print_sick2

FILENAME = 'SEQUENCE.txt'


def mk_scrollable_area(obj, obj_frame, sbars):
    obj.grid(row=0, column=0, sticky='NSWE')

    if 'y' in sbars:
        yscrollbar = tkinter.ttk.Scrollbar(obj_frame)
        yscrollbar.grid(row=0, column=1, sticky='NS')
        yscrollbar['command'] = obj.yview
        obj['yscrollcommand'] = yscrollbar.set
    if 'x' in sbars:
        xscrollbar = tkinter.ttk.Scrollbar(obj_frame, orient='horizontal')
        xscrollbar.grid(row=1, column=0, sticky='WE')
        xscrollbar['command'] = obj.xview
        obj['xscrollcommand'] = xscrollbar.set

    obj_frame.columnconfigure(1, 'minsize')
    obj_frame.columnconfigure(0, weight=1)
    obj_frame.rowconfigure(1, 'minsize')
    obj_frame.rowconfigure(0, weight=1)


class View(object):
    root = None

    buttons = {}
    edits = {}
    text = {}
    labels = {}

    edit_pages = None

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Book Printing Tools')

        x, y, w, h = 0, 0, 400, 500
        self.root.geometry('%sx%s+%s+%s' % (w, h, x, y))

        self.edits['pages'] = tkinter.IntVar()

        self.labels['sel_pages'] = tkinter.IntVar()
        self.labels['sel_pack_size'] = tkinter.IntVar()

        self.labels['written'] = tkinter.StringVar()

        main_frame = tkinter.ttk.Frame(self.root)
        main_frame['padding'] = (5, 5)
        main_frame.pack(side='top', fill='both', expand=True)

        label1 = tkinter.ttk.Label(main_frame, text='Enter pages:')
        label1.pack(side='top', fill='x')

        input_frame = tkinter.ttk.Frame(main_frame)
        input_frame.pack(side='top', fill='x')

        self.edit_pages = tkinter.ttk.Entry(input_frame,
                                            textvariable=self.edits['pages'])
        self.edit_pages.pack(side='left', fill='x')

        self.buttons['calculate'] = tkinter.ttk.Button(input_frame,
                                                       text='Calculate')
        self.buttons['calculate'].pack(side='left', fill='x')

        table_frame = tkinter.ttk.Frame(main_frame)
        table_frame.pack(side='top', fill='x')

        self.table = tkinter.ttk.Treeview(table_frame, height=7)
        self.table.pack(side='left', fill='x', expand=True)
        self.table['columns'] = ('a4_pack',
                                 'pages_pack',
                                 'pack_count',
                                 'good_choice')

        self.table.column('a4_pack', width=50)
        self.table.column('pages_pack', width=50)
        self.table.column('pack_count', width=50)
        self.table.column('good_choice', width=50)

        self.table.heading('a4_pack',     text='A4 / Pack')
        self.table.heading('pages_pack',  text='Pages / Pack')
        self.table.heading('pack_count',  text='Pack Count')
        self.table.heading('good_choice', text='Good Choice')

        self.table['show'] = 'headings'

        mk_scrollable_area(self.table, table_frame, 'y')

        generate_frame = tkinter.ttk.Frame(main_frame)
        generate_frame.pack(side='top', fill='x')

        selected_frame = tkinter.Frame(generate_frame)
        selected_frame.pack(side='left', fill='x')

        label2 = tkinter.Label(selected_frame,
                               text='Selected choice:',
                               anchor='w',
                               justify='left'
                               )
        label2.pack(side='top', fill='x')

        selected_frame2 = tkinter.Frame(selected_frame, relief='sunken', bd=3)
        selected_frame2.pack(side='top', fill='x')

        label3 = tkinter.Label(selected_frame2, text='Pages: ')
        label3.pack(side='left', fill='x')

        label4 = tkinter.Label(selected_frame2,
                               textvariable=self.labels['sel_pages'])
        label4.pack(side='left', fill='x')

        label3 = tkinter.Label(selected_frame2, text='Pack size: ')
        label3.pack(side='left', fill='x')

        label4 = tkinter.Label(selected_frame2,
                               textvariable=self.labels['sel_pack_size'])
        label4.pack(side='left', fill='x')

        self.buttons['generate'] = tkinter.ttk.Button(generate_frame,
                                                      text='Generate')
        self.buttons['generate'].pack(side='right', fill='x')

        label3 = tkinter.ttk.Label(main_frame, text='Side A:')
        label3.pack(side='top', fill='x')

        side_a_frame = tkinter.ttk.Frame(main_frame)
        side_a_frame.pack(side='top', fill='x')

        self.text['side_a'] = tkinter.Text(side_a_frame, height=5)

        mk_scrollable_area(self.text['side_a'], side_a_frame, 'y')

        label4 = tkinter.ttk.Label(main_frame, text='Side B:')
        label4.pack(side='top', fill='x')

        side_b_frame = tkinter.Frame(main_frame)
        side_b_frame.pack(side='top', fill='x')

        self.text['side_b'] = tkinter.Text(side_b_frame, height=5)

        mk_scrollable_area(self.text['side_b'], side_b_frame, 'y')

        label5 = tkinter.ttk.Label(main_frame,
                                   textvariable=self.labels['written'])
        label5.pack(side='top', fill='x')

    def close(self):
        self.root.destroy()
        self.root.quit()

    def display_list(self, lst):
        self.table.delete(*self.table.get_children())

        for a4, pack_size, pack_count, is_good in lst:
            if is_good:
                txt = 'OK'
            else:
                txt = ''
            self.table.insert('', 'end', values=(str(a4),
                                                 str(pack_size),
                                                 str(pack_count),
                                                 txt))

    def get_pages(self):
        return self.edits['pages'].get()

    def display_side_ab(self, line_a, line_b):
        self.text['side_a'].delete(1.0, 'end')
        self.text['side_b'].delete(1.0, 'end')

        self.text['side_a'].insert('end', line_a)
        self.text['side_b'].insert('end', line_b)

        self.labels['written'].set('Lines written in %s' % FILENAME)

    def display_selected(self, pages, pack_size):
        self.labels['sel_pages'].set(pages)
        self.labels['sel_pack_size'].set(pack_size)


class Model(object):
    ui = None

    pack_list = None

    def __init__(self, view):
        self.ui = view
        self.pack_list = []

    def calculate(self):
        print('calculate')
        pages = self.ui.get_pages()
        self.pack_list = calculate_packs(pages)
        self.ui.display_list(self.pack_list)

    def table_select(self):
        cur_item = self.ui.table.focus()
        pack_size = self.ui.table.item(cur_item)['values'][1]
        pages = self.ui.get_pages()
        self.ui.display_selected(pages, pack_size)

    def generate(self):
        print('generate')
        pages = self.ui.get_pages()
        cur_item = self.ui.table.focus()
        pack_size = self.ui.table.item(cur_item)['values'][1]

        [side_a, side_b] = print_sick2(pages, pack_size)

        side_a = list(map(lambda item: str(item), side_a))
        side_b = list(map(lambda item: str(item), side_b))
        line_a = ','.join(side_a)
        line_b = ','.join(side_b)

        self.ui.display_side_ab(line_a, line_b)

        with open(FILENAME, 'w') as sf:
            sf.write('%s\n' % line_a)
            sf.write('\n')
            sf.write('%s\n' % line_b)


class Ctrl(object):
    view = None
    model = None

    def __init__(self):
        self.view = View()
        self.model = Model(self.view)

        self.bind()

        self.view.root.protocol('WM_DELETE_WINDOW', self.close_handler)
        self.view.root.mainloop()

    def bind(self):
        self.view.buttons['calculate'].bind("<Button-1>", self.calculate_handler)
        self.view.buttons['generate'].bind("<Button-1>", self.generate_handler)

        self.view.table.bind("<ButtonRelease-1>", self.table_select_handler)
        self.view.table.bind("<Double-1>", self.generate_handler)
        self.view.edit_pages.bind('<Return>', self.calculate_handler)

    def calculate_handler(self, event):
        self.model.calculate()

    def generate_handler(self, event):
        self.model.generate()

    def table_select_handler(self, event):
        self.model.table_select()

    def close_handler(self):
        self.view.close()


class App(object):
    ctrl = None

    def __init__(self):
        self.ctrl = Ctrl()
