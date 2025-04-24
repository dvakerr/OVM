from pynput.keyboard import Key, Controller
from tkinter import ttk
import speech_recognition as sr
import time
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import threading

keyboard = Controller()

class VoiceControlApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x200")
        self.root.title("OVM!")
        self.recognizer = sr.Recognizer()
        self.microphone = None

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.voice_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.voice_tab, text='Voice Control')

        self.mic_button = tk.Button(self.voice_tab, text="Выбрать микрофон", command=self.choose_microphone)
        self.mic_button.pack(pady=10)

        self.start_button = tk.Button(self.voice_tab, text="Начать распознавание", command=self.start_recognition_thread)
        self.start_button.pack(pady=10)

        self.status_label = tk.Label(self.voice_tab, text="", wraplength=300)
        self.status_label.pack(pady=20)

        self.help_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.help_tab, text='About')

        self.help_label = tk.Label(self.help_tab,
                                   text="Программа написана Иваном Двакером в 2025 году \n на чистом энтузиазме.")
        self.help_label.pack(pady=20)

    def get_microphone(self):
        mic_list = sr.Microphone.list_microphone_names()
        return mic_list[:6]

    def choose_microphone(self):
        mic_list = self.get_microphone()
        if not mic_list:
            messagebox.showerror("Ошибка", "Не найдено доступных микрофонов.")
            return None

        mic_choice = simpledialog.askstring("Выбор микрофона",
                                             "Введите номер микрофона:\n" +
                                             "\n".join(f"{i}: {mic}" for i, mic in enumerate(mic_list)))
        try:
            mic_index = int(mic_choice)
            if 0 <= mic_index < len(mic_list):
                self.microphone = sr.Microphone(device_index=mic_index)
                messagebox.showinfo("Успех", f"Выбран микрофон: {mic_list[mic_index]}")
            else:
                messagebox.showerror("Ошибка", "Неверный номер микрофона.")
        except (ValueError, TypeError):
            messagebox.showerror("Ошибка", "Ошибка ввода. Попробуйте снова.")

    def recognize_speech_from_mic(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            return self.recognizer.recognize_google(audio, language="ru-RU")
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None

    def start_recognition_thread(self):
        if self.microphone is None:
            messagebox.showwarning("Предупреждение", "Сначала выберите микрофон.")
            return

        recognition_thread = threading.Thread(target=self.start_recognition)
        recognition_thread.daemon = True
        recognition_thread.start()

    def find_osu_exe():
        for root, dirs, files in os.walk('C:\\', 'D:\\'):
            if 'osu!.exe' in files:
                return os.path.join(root, 'osu!.exe')
        return None

    osu_path = find_osu_exe()

    def start_recognition(self):
        while True:
            self.status_label.config(text="Скажите команду...")
            command = self.recognize_speech_from_mic()
            if command:
                command = command.lower()
                self.status_label.config(text=f"Вы сказали: {command}")
                time.sleep(1)
            else:
                self.status_label.config(text="Не удалось распознать речь.")
                time.sleep(1)
                continue

            if "играть" in command:
                print("Запуск osu!...")
                os.startfile(self.osu_path)

            elif "выход" in command:
                print("Выход из игры. До свидания!")
                os.system('taskkill /f /im osu!.exe')
                break

            # Взаимодействие с геймплеем в игре

            elif "пауза" in command:
                print("Игра поставлена на паузу.")
                keyboard.press(Key.esc)
                time.sleep(0.1)
                keyboard.release(Key.esc)

            elif "продолжить" in command:
                print("Игра поставлена на паузу.")
                keyboard.press(Key.esc)
                time.sleep(0.1)
                keyboard.release(Key.esc)

            elif "ретрай" in command:
                print("Ретраим мапу.")
                keyboard.press('`')
                time.sleep(1)
                keyboard.release('`')

            # Взаимодействие с мапами в игре

            elif "random" in command:
                print("Крутим карты.")
                keyboard.press(Key.f2)
                time.sleep(0.1)
                keyboard.release(Key.f2)

            elif "обратно" in command:
                print("Возвращаем предыдущую карту обратно.")
                keyboard.press(Key.shift)
                keyboard.press(Key.f2)
                time.sleep(0.1)
                keyboard.release(Key.shift)
                keyboard.release(Key.f2)

            elif "старт" in command:
                print("Начинаем играть мапу.")
                keyboard.press(Key.enter)
                time.sleep(0.1)
                keyboard.release(Key.enter)

            # Взаимодействие с модами

            elif "моды" in command:
                print("Открываем моды.")
                keyboard.press(Key.f1)
                time.sleep(0.1)
                keyboard.release(Key.f1)

            # Первая строка модов

            elif "easy" in command:
                print("Включаем мод Easy.")
                keyboard.press('q')
                time.sleep(0.1)
                keyboard.release('q')

            elif "no fail" in command:
                print("Включаем мод No Fail.")
                keyboard.press('w')
                time.sleep(0.1)
                keyboard.release('w')

            elif "half time" in command:
                print("Включаем мод Half Time.")
                keyboard.press('e')
                time.sleep(0.1)
                keyboard.release('e')

            # Вторая строка модов

            elif "hr" in command:
                print("Включаем мод Hard Rock.")
                keyboard.press('a')
                time.sleep(0.1)
                keyboard.release('a')

            elif "sd" in command:
                print("Включаем мод Sudden Death / Perfect.")
                keyboard.press('s')
                time.sleep(0.1)
                keyboard.release('s')


            elif "дт" in command:
                print("Включаем мод Double Time / Nightcore.")
                keyboard.press('d')
                time.sleep(0.1)
                keyboard.release('d')

            elif "hd" in command:
                print("Включаем мод Hidden.")
                keyboard.press('f')
                time.sleep(0.1)
                keyboard.release('f')

            elif "fl" in command:
                print("Включаем мод Flashlight.")
                keyboard.press('g')
                time.sleep(0.1)
                keyboard.release('g')

            # 3я строка модов

            elif "синема" in command:
                print("Включаем мод Auto / Cinema.")
                keyboard.press('v')
                time.sleep(0.1)
                keyboard.release('v')

            elif "релакс" in command:
                print("Включаем мод Relax.")
                keyboard.press('z')
                time.sleep(0.1)
                keyboard.release('z')

            elif "ап" in command:
                print("Включаем мод Autopilot.")
                keyboard.press('x')
                time.sleep(0.1)
                keyboard.release('x')

            elif "v2" in command:
                print("Включаем мод ScoreV2.")
                keyboard.press('b')
                time.sleep(0.1)
                keyboard.release('b')

            elif "со" in command:
                print("Включаем мод Spun Out.")
                keyboard.press('c')
                time.sleep(0.2)
                keyboard.release('c')

            #Опять интерфейс

            elif "fps" in command:
                print("Меняем FPS.")
                keyboard.press(Key.f7)
                time.sleep(0.2)
                keyboard.release(Key.f7)

            elif "чат" in command:
                print("Открываем чат.")
                keyboard.press(Key.f8)
                time.sleep(0.2)
                keyboard.release(Key.f8)

            elif "люди" in command:
                print("Открываем список людей.")
                keyboard.press(Key.f9)
                time.sleep(0.2)
                keyboard.release(Key.f9)

            elif "мышь" in command:
                print("Отключение / Включение кнопок мыши.")
                keyboard.press(Key.f10)
                time.sleep(0.2)
                keyboard.release(Key.f10)

            elif "скриншот" in command:
                print("Делаем скриншот.")
                keyboard.press(Key.f12)
                time.sleep(0.2)
                keyboard.release(Key.f12)

            elif "replay" in command:
                print("Делаем скриншот.")
                keyboard.press(Key.f2)
                time.sleep(0.2)
                keyboard.release(Key.f2)

            elif "посмотреть реплей" in command:
                print("Открываем реплей.")
                keyboard.press(Key.f1)
                time.sleep(0.2)
                keyboard.release(Key.f1)

            elif "настройки" in command:
                print("Открываем настройки.")
                keyboard.press(Key.ctrl)
                keyboard.press('o')
                time.sleep(0.2)
                keyboard.release(Key.ctrl)
                keyboard.release('o')

            elif "мульти" in command:
                print("Заходим в мультиплеер.")
                keyboard.press("p")
                time.sleep(0.5)
                keyboard.press("p")
                time.sleep(0.5)
                keyboard.press("m")
                time.sleep(0.5)
                keyboard.release("p")
                keyboard.release("p")
                keyboard.release("m")

            elif "редактор" in command:
                print("Открываем редактор карт.")
                keyboard.press("e")
                time.sleep(0.3)
                keyboard.press("e")
                time.sleep(0.3)
                keyboard.release("e")
                time.sleep(0.3)
                keyboard.release("e")
                time.sleep(0.3)

            elif "стандарт" in command:
                print("Переходим в режим стд.")
                keyboard.press(Key.ctrl)
                time.sleep(0.2)
                keyboard.press("1")
                time.sleep(0.2)
                keyboard.release(Key.ctrl)
                time.sleep(0.2)
                keyboard.release("1")

            elif "тайко" in command:
                print("Переходим в режим тайко.")
                keyboard.press(Key.ctrl)
                time.sleep(0.2)
                keyboard.press("2")
                time.sleep(0.2)
                keyboard.release(Key.ctrl)
                time.sleep(0.2)
                keyboard.release("2")

            elif "catch" in command:
                print("Переходим в режим Catch The Beat.")
                keyboard.press(Key.ctrl)
                time.sleep(0.2)
                keyboard.press("3")
                time.sleep(0.2)
                keyboard.release(Key.ctrl)
                time.sleep(0.2)
                keyboard.release("3")

            elif "мания" in command:
                print("Переходим в режим Mania.")
                keyboard.press(Key.ctrl)
                time.sleep(0.2)
                keyboard.press("4")
                time.sleep(0.2)
                keyboard.release(Key.ctrl)
                time.sleep(0.2)
                keyboard.release("4")

            else:
                print("Неизвестная команда. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = VoiceControlApp(root)
    root.mainloop()