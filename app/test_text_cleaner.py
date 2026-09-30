from text_processor.text_cleaner import preprocess_resume


text = """   
Aaryan       Thopate


Computer       Science       Data       Science


SKILLS:


Python       Java       SQL


Machine       Learning


PROJECTS:

AI       Resume       Analyzer
"""


cleaned_text = preprocess_resume(text)

print("----- ORIGINAL TEXT -----")
print(text)

print("\n----- CLEANED TEXT -----")
print(cleaned_text)