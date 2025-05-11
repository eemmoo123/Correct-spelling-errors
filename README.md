# Correct-spelling-errors
# Simple Spelling Correction with ipywidgets  
# أداة بسيطة لتصحيح الأخطاء الإملائية باستخدام ipywidgets

## 📌 Description | الوصف

This is a simple interactive tool for correcting English spelling mistakes using the `pyspellchecker` library. It works inside a Google Colab notebook and uses `ipywidgets` for an easy-to-use interface.  
هذه أداة تفاعلية بسيطة لتصحيح الأخطاء الإملائية في اللغة الإنجليزية باستخدام مكتبة `pyspellchecker`. تعمل داخل بيئة Google Colab وتستخدم مكتبة `ipywidgets` لتوفير واجهة سهلة الاستخدام.

---

## ✅ Features | المميزات

- 🔤 Corrects English spelling mistakes.
- 🧑‍💻 Simple and interactive interface using `ipywidgets`.
- ⚙️ Works inside Google Colab without any setup.

- 🔤 تصحيح الأخطاء الإملائية في اللغة الإنجليزية.
- 🧑‍💻 واجهة تفاعلية باستخدام مكتبة `ipywidgets`.
- ⚙️ تعمل داخل Google Colab مباشرة بدون إعدادات معقدة.

---

## 📦 Requirements | المتطلبات

- Python 3.6+
- Google Colab
- Libraries:
  - `pyspellchecker`
  - `ipywidgets`

---

## 🚀 How to Use | طريقة الاستخدام

1. Open a new Google Colab notebook.  
   افتح دفتر جديد في Google Colab.
2. Copy and paste the full code into a cell.  
   انسخ الكود بالكامل وألصقه في خلية.
3. Run the cell. The user interface will appear.  
   شغل الخلية، وستظهر لك الواجهة التفاعلية.
4. Type your text in the input box and click **"Correct Spelling"**.  
   اكتب النص في مربع الإدخال واضغط على زر **"Correct Spelling"**.
5. The corrected text will appear below.  
   سيظهر النص المصحح في المربع السفلي.

---

## 🧠 How It Works | طريقة العمل

- The tool splits the input text into words.
- Each word is checked for the most likely correct spelling using `SpellChecker`.
- If a correction is found, it's used; otherwise, the original word is kept.

- الأداة تقوم بتقسيم النص إلى كلمات.
- يتم تصحيح كل كلمة باستخدام مكتبة `SpellChecker`.
- في حال تم العثور على تصحيح، يتم استبداله؛ وإذا لم يوجد، تُستخدم الكلمة الأصلية.

---

## ⚠️ Limitations | القيود

- Only supports English language.
- Does not understand sentence context.
- May not always give the correct correction.

- تدعم اللغة الإنجليزية فقط.
- لا تفهم سياق الجملة.
- قد لا تكون التصحيحات دقيقة دائماً.

---

## 🛠️ Future Improvements | تحسينات مستقبلية

- Context-aware correction.
- Support for multiple languages.
- Custom word dictionaries.

- تصحيح يعتمد على سياق الجملة.
- دعم لغات متعددة.
- إمكانية تخصيص القاموس الإملائي.

---

## 📄 License

[MIT License] – Feel free to use, modify, and share!

---

## ✍️ Author

Developed by [Your Name Here].  
تم تطويرها بواسطة [اسمك هنا].
