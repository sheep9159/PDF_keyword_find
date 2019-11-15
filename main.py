import os
import shutil
from io import StringIO
import time


from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

years = 'HCII2019'


def readPdf(pdf_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr=rsrcmgr, outfp=retstr, laparams=laparams)

    process_pdf(rsrcmgr=rsrcmgr, device=device, fp=pdf_file)
    device.close()

    content = retstr.getvalue()
    retstr.close()

    return content


def file_name(file_dir):
    file_names = []
    for root, dirs, files in os.walk(file_dir, topdown=False):
        for file in files:
            if 'pdf' in file and 'back' not in file and 'front' not in file:
                file_names.append(os.path.join(root, file))

    return file_names


if __name__ == '__main__':

    dir = 'experiment/' + years
    num_airbus = 0
    num_boeing = 0

    for dir_and_name in file_name(dir):
        with open(dir_and_name, 'rb') as pdf_file:
            print(dir_and_name)
            file_origin = dir_and_name
            try:
                content = readPdf(pdf_file)

                if 'Airbus' in content or 'airbus' in content:
                    file_target = 'result' + '/' + years + '/' +'airbus' + '/' + str(time.strftime( '%c' )) + '.' + 'pdf'
                    shutil.copyfile(file_origin, file_target)
                    num_airbus += 1

                if 'Boeing' in content or 'boeing' in content:
                    file_target = 'result' + '/' + years + '/' + 'boeing' + '/' + str(time.strftime( '%c' )) + '.' + 'pdf'
                    shutil.copyfile(file_origin, file_target)
                    num_boeing += 1

            except:
                file_target = 'result' + '/' + years + '/' + 'wrong_pdf' + '/' + str(time.strftime('%c')) + '.' + 'pdf'
                shutil.copyfile(file_origin, file_target)

    print('there are {} pdfs about airbus in {} HCII'.format(num_airbus, years))
    print('there are {} pdfs about boeing in {} HCII'.format(num_boeing, years))
