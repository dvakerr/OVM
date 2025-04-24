from pynput.keyboard import Key, Controller
import speech_recognition as sr
import time
import os
import tkinter as tk
from tkinter import simpledialog, messagebox



def __init__(self, root):
    icon_path = os.path.join(os.path.dirname(__file__), 'OVM.ico')
    self.root.iconbitmap(icon_path)
    self.root.title("OVM!")
    self.root = root
def get_microphone():
    # Получаем список доступных микрофонов
    mic_list = sr.Microphone.list_microphone_names()
    return mic_list[:6]

def choose_microphone():
    mic_list = get_microphone()

    if not mic_list:
        messagebox.showerror("Ошибка", "Не найдено доступных микрофонов.")
        return None

    # Создаем окно для выбора микрофона
    root = tk.Tk()
    root.withdraw()  # Скрываем главное окно

    # Запрос выбора микрофона
    mic_choice = simpledialog.askstring("Выбор микрофона",
                                         "Введите номер микрофона:\n" +
                                         "\n".join(f"{i}: {mic}" for i, mic in enumerate(mic_list)))

    # Проверяем, что введен корректный номер
    try:
        mic_index = int(mic_choice)
        if 0 <= mic_index < len(mic_list):
            return mic_index  # Возвращаем индекс микрофона
        else:
            messagebox.showerror("Ошибка", "Неверный номер микрофона.")
            return None
    except (ValueError, TypeError):
        messagebox.showerror("Ошибка", "Ошибка ввода. Попробуйте снова.")
        return None


def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        print("Скажите команду...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Распознаю...")
        return recognizer.recognize_google(audio, language="ru-RU")
    except sr.UnknownValueError:
        print("Не удалось распознать речь.")
        return None
    except sr.RequestError:
        print("Ошибка сервиса распознавания речи.")
        return None


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    mic_index = choose_microphone()
    if mic_index is None:
        return  # Завершаем программу, если выбор микрофона не удался

    print(f"Выбранный индекс микрофона: {mic_index}")  # Отладочный вывод

    try:
        microphone = sr.Microphone(device_index=mic_index)  # Используем device_index
    except AssertionError as e:
        messagebox.showerror("Ошибка", f"Ошибка при создании микрофона: {str(e)}")
        return

    try:
        microphone = sr.Microphone(device_index=mic_index)  # Используем device_index
    except AssertionError as e:
        messagebox.showerror("Ошибка", f"Ошибка при создании микрофона: {str(e)}")
        return
    keyboard = Controller()

    print("Голосовое меню для osu! Чтобы начать играть скажите: 'играть'.")

    while True:
        command = recognize_speech_from_mic(recognizer, microphone)

        if command:
            command = command.lower()
            print(f"Вы сказали: {command}")

            # Запуск и выход из игры
            if "играть" in command:
                print("Запуск игры osu!...")

                os.startfile(r'C:\Users\Ivan\AppData\Local\osu!\osu!.exe')

            elif "выход" in command:
                print("Выход из игры. До свидания!")
                os.system('taskkill /f /im osu!.exe')
                break

            # Взаимодействие с геймплеем в игре

            elif "пауза" in command:
                print("Игра поставлена на паузу.")
                keyboard.press(Key.esc)
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release(Key.esc)

            elif "продолжить" in command:
                print("Игра поставлена на паузу.")
                keyboard.press(Key.esc)
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release(Key.esc)

            elif "ретрай" in command:
                print("Ретраим мапу.")
                keyboard.press('~')
                time.sleep(2.0)  # Задержка в 100 мс
                keyboard.release('~')

            # Взаимодействие с мапами в игре

            elif "random" in command:
                print("Крутим карты.")
                keyboard.press(Key.f2)
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release(Key.f2)

            elif "обратно" in command:
                print("Возвращаем предыдущую карту обратно.")
                keyboard.press(Key.shift)
                keyboard.press(Key.f2)
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release(Key.shift)
                keyboard.release(Key.f2)

            elif "старт" in command:
                print("Начинаем играть мапу.")
                keyboard.press(Key.enter)
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release(Key.enter)

            # Взаимодействие с модами

            elif "моды" in command:
                print("Открываем моды.")
                keyboard.press(Key.f1)
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release(Key.f1)

            # Первая строка модов

            elif "easyaaww" in command:
                print("Включаем мод Easy.")
                keyboard.press('q')
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release('q')

            elif "no fail" in command:
                print("Включаем мод No Fail.")
                keyboard.press('w')
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release('w')

            elif "half time" in command:
                print("Включаем мод Half Time.")
                keyboard.press('e')
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release('e')

            # Вторая строка модов

            elif "hr" in command:
                print("Включаем мод Hard Rock.")
                keyboard.press('a')
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release('a')

            elif "sd" in command:
                print("Включаем мод Sudden Death / Perfect.")
                keyboard.press('s')
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release('s')


            elif "дт" in command:
                print("Включаем мод Double Time / Nightcore.")
                keyboard.press('d')
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release('d')

            elif "hd" in command:
                print("Включаем мод Hidden.")
                keyboard.press('f')
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release('f')

            elif "fl" in command:
                print("Включаем мод Flashlight.")
                keyboard.press('g')
                time.sleep(0.1)  # Задержка в 100 мс
                keyboard.release('g')

            # 3я строка модов

            elif "синема" in command:
                print("Включаем мод Auto / Cinema.")
                keyboard.press('v')
                time.sleep(0.2)  # Задержка в 100 мс
                ('v')

            elif "релакс" in command:
                print("Включаем мод Relax.")
                keyboard.press('z')
                time.sleep(0.2)  # Задержка в 100 мс
                keyboard.release('z')

            elif "ап" in command:
                print("Включаем мод Autopilot.")
                keyboard.press('x')
                time.sleep(0.2) # Задержка в 100 мс
                keyboard.release('x')

            elif "v2" in command:
                print("Включаем мод ScoreV2.")
                keyboard.press('b')
                time.sleep(0.2)  # Задержка в 100 мс
                keyboard.release('b')

            elif "со" in command:
                print("Включаем мод Spun Out.")
                keyboard.press('c')
                time.sleep(0.2)  # Задержка в 100 мс
                keyboard.release('c')

            # интерфейс
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
    main()