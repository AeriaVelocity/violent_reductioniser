"""
Violent Reductioniser GUI

Author: Arsalan 'Aeri' Kazmi <https://aeriavelocity.github.io>
Licence: GPL-3.0-or-later

This file is part of Violent Reductioniser.
"""

import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import subprocess
import os
from .strings import STRINGS

class ViolentReductioniser:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(STRINGS["title"])

        frame = ttk.Frame(self.root)
        frame.pack()

        try:
            subprocess.check_output(["ffmpeg", "-version"])
        except FileNotFoundError:
            messagebox.showerror(STRINGS["error_title"], STRINGS["missing_ffmpeg"])
            exit(1)

        cwd = os.getcwd()
        if cwd[:-1] != os.sep:
            cwd = cwd + os.sep

        homedir = os.path.expanduser("~")
        if cwd == homedir:
            cwd = "~"
        elif cwd.startswith(homedir):
            cwd = "~" + cwd[len(homedir):]

        self.cwd_label = ttk.Label(frame, text=STRINGS["cwd_label"] + cwd)
        self.cwd_label.pack()

        self.input_label = ttk.Label(frame, text=STRINGS["input_label"])
        self.input_label.pack()
        self.input_entry = ttk.Entry(frame, width=50)
        self.input_entry.pack()
        self.browse_input_button = ttk.Button(frame,
                                             text=STRINGS["browse_button"],
                                             command=self.browse_input)
        self.browse_input_button.pack()

        self.output_label = ttk.Label(frame, text=STRINGS["output_label"])
        self.output_label.pack()
        self.output_entry = ttk.Entry(frame, width=50)
        self.output_entry.pack()
        self.browse_output_button = ttk.Button(frame,
                                              text=STRINGS["browse_button"],
                                              command=self.browse_output)
        self.browse_output_button.pack()

        self.button = ttk.Button(frame,
                                text=STRINGS["reductionise_button"],
                                command=self.run_ffmpeg)
        self.button.pack()

    def browse_input(self):
        self.browse_for_file("input")

    def browse_output(self):
        self.browse_for_file("output")

    def browse_for_file(self, mode):
        if mode not in ["input", "output"]:
            raise ValueError("`mode` must be either 'input' or 'output'")

        valid_file_types = [
            ("MPEG-4 Video Files", ".mp4"),
            ("WebM Video Files", ".webm"),
            ("MKV Video Files", ".mkv"),
            ("All files (not recommended)", "*.*"),
        ]

        if mode == "input":
            dialog = filedialog.askopenfilename(
                title=STRINGS["browse_input_title"],
                filetypes=valid_file_types,
            )
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, dialog)
        elif mode == "output":
            dialog = filedialog.asksaveasfilename(
                title=STRINGS["browse_output_title"],
                confirmoverwrite=True,
                filetypes=valid_file_types,
            )
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, dialog)

    def run_ffmpeg(self):
        input_file = self.input_entry.get()
        output_file = self.output_entry.get()

        if not input_file or not output_file:
            messagebox.showerror(STRINGS["error_title"], STRINGS["missing_fields"])
            return

        if os.path.abspath(input_file) == os.path.abspath(output_file):
            messagebox.showerror(STRINGS["error_title"], STRINGS["input_is_output"])
            return

        if messagebox.askyesno(STRINGS["warning_title"], STRINGS["warning_message"]):
            if not os.path.isfile(input_file):
                messagebox.showerror(STRINGS["error_title"], STRINGS["file_not_found"].format(input_file))
                return

            ffmpeg_command = [
                "ffmpeg",
                "-i", input_file,
                "-vcodec", "libx264",
                "-crf", "50",
                "-preset", "veryslow",
                "-vf", "scale=60:-2",
                "-r", "6",
                "-acodec", "aac",
                "-b:a", "8k",
                "-ar", "8000",
                "-ac", "1",
                "-y",
                output_file
            ]

            try:
                subprocess.run(ffmpeg_command, check=True)
                messagebox.showinfo(STRINGS["success_title"], STRINGS["success_message"])
            except subprocess.CalledProcessError as e:
                messagebox.showerror(STRINGS["error_title"], STRINGS["ffmpeg_error"] + ":" + str(e))

def main():
    app = ViolentReductioniser()
    app.root.mainloop()

if __name__ == "__main__":
    main()
