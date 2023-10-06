# Python program to read 
# file word by word
# opening the text file
import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

a = getText('test.docx')
print(a)