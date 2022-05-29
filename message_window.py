import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk



SCREEN_SIZE_TO_MESSAGE_WIDTH = {
    1100: 900,
    950: 700,
    750: 550
}
username=""

class MessageWindow(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs, highlightthickness=0)

        self.messages_frame = ttk.Frame(container, style="Messages.TFrame")
        self.messages_frame.columnconfigure(0, weight=1)

        self.scrollable_window = self.create_window((0, 0), window=self.messages_frame, anchor="nw",
                                                    width=self.winfo_width())

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.messages_frame.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta / 120), "units")

    def update_message_widgets(self, messages, message_labels):
        existing_labels = [
            (message["text"], time["text"]) for message, time in message_labels
        ]

        for message in messages:
            message_time = datetime.datetime.fromtimestamp(message["date"]).strftime(
                "%d-%m-%Y %H:%M:%S"
            )
            if "/*/" in message["message"]:
                if (message["message"].split("/*/")[0], message_time) not in existing_labels:
                    if "/*/" in message["message"]:
                        global username
                        username = message["message"].split("/*/")[1]
                        self._create_message_container(message["message"].split("/*/")[0], message_time, message_labels,username)

    def _create_message_container(self, message_content, message_time, message_labels,un):
        container = ttk.Frame(self.messages_frame, style="Messages.TFrame")
        container.columnconfigure(1, weight=1)
        container.grid(sticky="EW", padx=(10, 50), pady=10)

        def reconfigure_message_labels(event):
            closest_break_point = min(SCREEN_SIZE_TO_MESSAGE_WIDTH.keys(),
                                      key=lambda b: abs(b - container.winfo_width()))
            for label, _ in message_labels:
                if label.winfo_width() < closest_break_point:
                    label.configure(wraplength=SCREEN_SIZE_TO_MESSAGE_WIDTH[closest_break_point])
            self.messages_frame.update()

        container.bind("<Configure>", reconfigure_message_labels)
        if un=="WaleedShanaa":
            un="WaleedShanaa-Project Manger"

        elif un=="EsenTekkanat":
            un="EsenTekkanat-documentarian"

        elif un=="GamzeKrc":
            un="GamzeKırıcı-Designer"

        elif un=="AliNazm":
            un="AliNazım-Debugger"

        elif un=="EmreTanker":
            un="EmreTanker-Problem Solver"
        else:
            un = "PhoebeShanaa-Troublemaker"


        self._create_message_bubble(container, message_content, message_time, message_labels,un)

    def _create_message_bubble(self, container, message_content, message_time, message_labels,unson):
        if username=="PhoebeShanaa":
            avatar_image = Image.open("PhoebeShanaa.jpg")
        elif username=="WaleedShanaa":
            avatar_image = Image.open("WaleedShanaa.jpg")
        elif username=="AliNazm":
            avatar_image = Image.open("AliNazım.jpeg")
        elif username=="EsenTekkanat":
            avatar_image = Image.open("EsenTekkanat.jpeg")
        elif username=="GamzeKrc":
            avatar_image = Image.open("GamzeKırıcı.jpeg")
        elif username=="EmreTanker":
            avatar_image = Image.open("EmreTanker.jpeg")
        else:
            avatar_image = Image.open("PhoebeShanaa.jpg")

        avatar_photo = ImageTk.PhotoImage(avatar_image)

        avatar_label = ttk.Label(
            container,
            image=avatar_photo,
            style="Avatar.TLabel"
        )

        avatar_label.image = avatar_photo
        avatar_label.grid(
            row=0,
            column=0,
            rowspan=2,
            sticky="NEW",
            padx=(0, 10),
            pady=(5, 0)
        )

        User_label=ttk.Label(
            container,
            text=unson,

        )


        time_label = ttk.Label(
            container,
            text=message_time,
            style="Time.TLabel"
        )

        time_label.grid(row=0, column=2, sticky="NEW")
        User_label.grid(row=0, column=1, sticky="NEW")

        message_label = ttk.Label(
            container,
            text=message_content,
            wraplength=800,
            justify="left",
            anchor="w",
            style="Message.TLabel"
        )

        message_label.grid(row=1, column=1, sticky="NEW")

        message_labels.append((message_label, time_label))