import os
import shutil
import PyPDF2


def file_name(file_dir):
    file_names = []
    for root, dirs, files in os.walk(file_dir, topdown=False):
        for file in files:
            if 'pdf' in file and 'back' not in file and 'front' not in file:
                file_names.append(os.path.join(root, file))

    return file_names


if __name__ == '__main__':
    dir = 'test2'
    num = 0

    for dir_and_name in file_name(dir):
        with open(dir_and_name, 'rb') as pdf_file:
            pdfReader = PyPDF2.PdfFileReader(pdf_file)
            for i in range(pdfReader.numPages):
                print(i)
                # page = pdfReader.getPage(i)
                # if 'Airbus' in page.extractText():
                #     file_origin = dir_and_name
                #     file_target = 'result' + '/' + str(num) + '.' + 'pdf'
                #     shutil.copyfile(file_origin, file_target)
                #     i += 1
                #     break


    print('there are {} pdfs in 2018 HCII'.format(num))