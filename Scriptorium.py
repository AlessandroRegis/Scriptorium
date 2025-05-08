import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Classe per la barra dei menu
class MenuBar:
    def __init__(self, parent):
        font_specs = ("ubuntu", 12)

        # Creazione della barra dei menu
        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        # Creazione del menu a tendina "File"
        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="Nuovo file",
                                  accelerator="Ctrl+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Apri file",
                                  accelerator="Ctrl+O",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Salva file",
                                  accelerator="Ctrl+S",
                                  command=parent.save)
        file_dropdown.add_command(label="Salva file come",
                                  accelerator="Ctrl+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Esci",
                                  command=parent.master.destroy)

        # Creazione del menu a tendina "A riguardo"
        about_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        about_dropdown.add_command(label="Note di rilascio",
                                   command=self.show_release_notes)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="A riguardo",
                                   command=self.show_about_info)

        # Aggiunta dei menu a tendina alla barra dei menu
        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="A riguardo", menu=about_dropdown)

    # Metodo per mostrare le informazioni "A riguardo"
    def show_about_info(self):
        box_title = "Riguardo su Scriptorium"
        box_message = "Scriptorium è un editor di testo sviluppato in Python con Tkinter"
        messagebox.showinfo(box_title, box_message)

    # Metodo per mostrare le note di rilascio
    def show_release_notes(self):
        box_title = "Note di rilascio"
        box_message = "Versione 0.1 - Gutenberg"
        messagebox.showinfo(box_title, box_message)

# Classe per la barra di stato
class StatusBar:
    def __init__(self, parent):
        font_specs = ("ubuntu", 12)
        self.status = tk.StringVar()
        self.status.set("Scriptorium - 0.1 Gutenberg")
        label = tk.Label(parent.textarea, textvariable=self.status, fg="black",
                         bg="lightgrey", anchor="sw", font=font_specs)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    # Metodo per aggiornare lo stato della barra di stato
    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Il file è stato salvato")
        else:
            self.status.set("Scriptorium - 0.1 Gutenberg")

# Classe principale dell'applicazione
class Pytext:
    def __init__(self, master):
        master.title("Scriptorium")
        master.geometry("1200x700")

        font_specs = ("ubuntu", 12)

        self.master = master
        self.filename = None

        # Creazione dell'area di testo e della scrollbar
        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Creazione della barra dei menu e della barra di stato
        self.menubar = MenuBar(self)
        self.statusbar = StatusBar(self)

        # Associazione delle scorciatoie da tastiera
        self.bind_shortcuts()

    # Metodo per impostare il titolo della finestra
    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - Scriptorium")
        else:
            self.master.title("Senza titolo - Scriptorium")

    # Metodo per creare un nuovo file
    def new_file(self, *args):
        self.textarea.delete("1.0", tk.END)
        self.filename = None
        self.set_window_title()

    # Metodo per aprire un file esistente
    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Tutti i file", "*.*"),
                       ("File di testo", "*.txt"),
                       ("File Python", "*.py"),
                       ("File JavaScript", "*.js"),
                       ("File HTML", "*.html"),
                       ("File CSS", "*.css"),
                       ("File JSON", "*.json"),
                       ("File XML", "*.xml"),
                       ("File YAML", "*.yaml"),
                       ("File Markdown", "*.md"),
                       ("File CSV", "*.csv"),
                       ("File SQL", "*.sql"),
                       ("File Java", "*.java"),
                       ("File C", "*.c"),
                       ("File C++", "*.cpp"),
                       ("File C#", "*.cs"),
                       ("File PHP", "*.php"),
                       ("File Ruby", "*.rb")
            ])
        if self.filename:
            self.textarea.delete("1.0", tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(tk.END, f.read())
            self.set_window_title(self.filename)

    # Metodo per salvare il file corrente
    def save(self):
        if self.filename:
            try:
                textarea_content = self.textarea.get("1.0", tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    # Metodo per salvare il file corrente con un nuovo nome
    def save_as(self):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Senza titolo.txt",
                defaultextension=".txt",
                filetypes=[("Tutti i file", "*.*"),
                           ("File di testo", "*.txt"),
                           ("File Python", "*.py"),
                           ("File JavaScript", "*.js"),
                           ("File HTML", "*.html"),
                           ("File CSS", "*.css"),
                           ("File JSON", "*.json"),
                           ("File XML", "*.xml"),
                           ("File YAML", "*.yaml"),
                           ("File Markdown", "*.md"),
                           ("File CSV", "*.csv"),
                           ("File SQL", "*.sql"),
                           ("File Java", "*.java"),
                           ("File C", "*.c"),
                           ("File C++", "*.cpp"),
                           ("File C#", "*.cs"),
                           ("File PHP", "*.php"),
                           ("File Ruby", "*.rb")
                ])
            if not new_file.endswith(".txt"):
                new_file += ".txt"
            with open(new_file, "w") as f:
                textarea_content = self.textarea.get("1.0", tk.END)
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)

        except Exception as e:
            print(e)

    # Metodo per uscire dall'applicazione
    def exit(self):
        pass

    # Metodo per mostrare le informazioni "A riguardo"
    def about(self):
        pass

    # Metodo per associare le scorciatoie da tastiera
    def bind_shortcuts(self):
        self.textarea.bind("<Control-n>", self.new_file)
        self.textarea.bind("<Control-o>", self.open_file)
        self.textarea.bind("<Control-s>", self.save)
        self.textarea.bind("<Control-S>", self.save_as)
        self.textarea.bind("<Key>", self.statusbar.update_status)

    # Metodo per gestire l'evento di focus
    def focus_in(self, event):
        pass

# Punto di ingresso
if __name__ == "__main__":
    master = tk.Tk()
    pt = Pytext(master)
    master.mainloop()