import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class BMICalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("📊 BMI / ИМТ Эксперт")
        self.geometry("540x640")
        self.resizable(False, False)

        self.current_lang = "ru"

        self.localization = {
            "ru": {
                "title": "Индекс Массы Тела (ИМТ)",
                "subtitle": "Скрининг рисков по критериям ВОЗ",
                "weight_lbl": "Вес (кг):",
                "height_lbl": "Рост (см или м):",
                "btn_calc": "Рассчитать",
                "disclaimer": "⚠️ Внимание! ИМТ не является диагнозом. Для оценки состояния здоровья обратитесь к врачу.",
                "your_bmi": "Ваш ИМТ:",
                "underweight": "Недостаточная масса тела\n\nВозможные риски:\n- Анемия\n- Остеопороз\n- Дефицит витаминов и минералов\n- Ослабление иммунной системы\n- Бесплодие и нарушения менструального цикла\n- Замедленное заживление ран",
                "normal": "Нормальная масса тела\n\nМинимальный риск заболеваний, связанных с весом.",
                "overweight": "Избыточная масса тела\n\nПовышенный риск:\n- Артериальная гипертензия\n- Сахарный диабет 2 типа\n- Ишемическая болезнь сердца\n- Инсульт\n- Повышенный холестерин\n- Желчнокаменная болезнь\n- Остеоартрит\n- Синдром обструктивного апноэ сна",
                "obesity_1": "Ожирение I степени\n\nВысокий риск:\n- Гипертония\n- Сахарный диабет 2 типа\n- Атеросклероз\n- Инфаркт миокарда\n- Инсульт\n- Неалкогольная жировая болезнь печени\n- Апноэ сна\n- Остеоартрит",
                "obesity_2": "Ожирение II степени\n\nОчень высокий риск:\n- Инфаркт миокарда\n- Инсульт\n- Сердечная недостаточность\n- Хроническая болезнь почек\n- Тяжелое апноэ сна\n- Жировая болезнь печени\n- Тромбозы\n- Депрессия и тревожные расстройства",
                "obesity_3": "Ожирение III степени\n\nКрайне высокий риск:\n- Инфаркт миокарда\n- Инсульт\n- Сердечная недостаточность\n- Хроническая болезнь почек\n- Сахарный диабет 2 типа\n- Тяжелое апноэ сна\n- Остеоартрит\n- Желчнокаменная болезнь\n- Некоторые виды рака (молочной железы, эндометрия, толстой кишки, почки, печени, желчного пузыря)"
            },
            "en": {
                "title": "Body Mass Index (BMI)",
                "subtitle": "Risk screening based on WHO criteria",
                "weight_lbl": "Weight (kg):",
                "height_lbl": "Height (cm or m):",
                "btn_calc": "Calculate",
                "disclaimer": "⚠️ Attention! BMI is not a medical diagnosis. Consult a healthcare professional for a proper health assessment.",
                "your_bmi": "Your BMI:",
                "underweight": "Underweight\n\nPossible risks:\n- Anemia\n- Osteoporosis\n- Vitamin and mineral deficiencies\n- Weakened immune system\n- Infertility and menstrual disorders\n- Slow wound healing",
                "normal": "Healthy Weight\n\nMinimal risk of weight-related diseases.",
                "overweight": "Overweight\n\nIncreased risk:\n- Hypertension\n- Type 2 Diabetes\n- Coronary Heart Disease\n- Stroke\n- High Cholesterol\n- Gallstones\n- Osteoarthritis\n- Obstructive Sleep Apnea",
                "obesity_1": "Obesity Class I\n\nHigh risk:\n- Hypertension\n- Type 2 Diabetes\n- Atherosclerosis\n- Heart Attack\n- Stroke\n- Nonalcoholic Fatty Liver Disease\n- Sleep Apnea\n- Osteoarthritis",
                "obesity_2": "Obesity Class II\n\nVery high risk:\n- Heart Attack\n- Stroke\n- Heart Failure\n- Chronic Kidney Disease\n- Severe Sleep Apnea\n- Fatty Liver Disease\n- Thrombosis\n- Depression and Anxiety Disorders",
                "obesity_3": "Obesity Class III\n\nExtremely high risk:\n- Heart Attack\n- Stroke\n- Heart Failure\n- Chronic Kidney Disease\n- Type 2 Diabetes\n- Severe Sleep Apnea\n- Osteoarthritis\n- Gallstones\n- Certain types of cancer (Breast, Endometrial, Colon, Kidney, Liver, Gallbladder)"
            }
        }

        self.lang_switch = ctk.CTkSegmentedButton(self, values=["RU", "EN"], command=self.change_language)
        self.lang_switch.pack(anchor="e", padx=20, pady=(15, 0))
        self.lang_switch.set("RU")

        self.lbl_title = ctk.CTkLabel(self, text="", font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"))
        self.lbl_title.pack(anchor="w", padx=25, pady=(10, 2))

        self.lbl_subtitle = ctk.CTkLabel(self, text="", font=ctk.CTkFont(family="Segoe UI", size=13), text_color="#71717a")
        self.lbl_subtitle.pack(anchor="w", padx=25, pady=(0, 20))

        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(fill="x", padx=25, pady=5)

        self.lbl_weight = ctk.CTkLabel(self.input_frame, text="", font=ctk.CTkFont(weight="bold", size=13))
        self.lbl_weight.grid(row=0, column=0, sticky="w", pady=(0, 4))
        self.ent_weight = ctk.CTkEntry(self.input_frame, placeholder_text="70", width=220, height=38, corner_radius=8)
        self.ent_weight.grid(row=1, column=0, padx=(0, 20))

        self.lbl_height = ctk.CTkLabel(self.input_frame, text="", font=ctk.CTkFont(weight="bold", size=13))
        self.lbl_height.grid(row=0, column=1, sticky="w", pady=(0, 4))
        self.ent_height = ctk.CTkEntry(self.input_frame, placeholder_text="175", width=220, height=38, corner_radius=8)
        self.ent_height.grid(row=1, column=1)

        self.btn_calc = ctk.CTkButton(self, text="", font=ctk.CTkFont(weight="bold", size=14), height=42, corner_radius=8, command=self.calculate_bmi)
        self.btn_calc.pack(fill="x", padx=25, pady=20)

        self.result_frame = ctk.CTkScrollableFrame(self, height=260, corner_radius=12, border_width=1, border_color=("#e4e4e7", "#27272a"))
        self.result_frame.pack(fill="both", expand=True, padx=25, pady=(0, 15))

        self.lbl_result_text = ctk.CTkLabel(self.result_frame, text="", font=ctk.CTkFont(family="Segoe UI", size=14), justify="left", anchor="nw", wraplength=440)
        self.lbl_result_text.pack(fill="both", expand=True, padx=10, pady=10)

        self.lbl_disclaimer = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=11), text_color="#a1a1aa", justify="center", wraplength=480)
        self.lbl_disclaimer.pack(padx=25, pady=(0, 15))

        self.update_ui_texts()

    def change_language(self, value):
        self.current_lang = value.lower()
        self.update_ui_texts()
        self.lbl_result_text.configure(text="")

    def update_ui_texts(self):
        lang = self.current_lang
        texts = self.localization[lang]

        self.lbl_title.configure(text=texts["title"])
        self.lbl_subtitle.configure(text=texts["subtitle"])
        self.lbl_weight.configure(text=texts["weight_lbl"])
        self.lbl_height.configure(text=texts["height_lbl"])
        self.btn_calc.configure(text=texts["btn_calc"])
        self.lbl_disclaimer.configure(text=texts["disclaimer"])

    def calculate_bmi(self):
        lang = self.current_lang
        texts = self.localization[lang]

        try:
            weight_str = self.ent_weight.get().strip()
            height_str = self.ent_height.get().strip()

            w = float(weight_str.replace(",", "."))
            h = float(height_str.replace(",", "."))

            if w <= 0 or h <= 0:
                raise ValueError

            if h > 3:
                h /= 100

            bmi = w / (h ** 2)

            result_output = f"{texts['your_bmi']} {bmi:.2f}\n"
            result_output += "─" * 40 + "\n\n"

            if bmi < 18.5:
                result_output += texts["underweight"]
            elif bmi < 25:
                result_output += texts["normal"]
            elif bmi < 30:
                result_output += texts["overweight"]
            elif bmi < 35:
                result_output += texts["obesity_1"]
            elif bmi < 40:
                result_output += texts["obesity_2"]
            else:
                result_output += texts["obesity_3"]

            self.lbl_result_text.configure(text=result_output)

        except ValueError:
            error_msg = "Ошибка: Введите корректные числа!" if lang == "ru" else "Error: Please enter valid numbers!"
            self.lbl_result_text.configure(text=error_msg)

if __name__ == "__main__":
    app = BMICalculatorApp()
    app.mainloop()
