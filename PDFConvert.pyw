########################################################################################################
# Projet : PDFConvert                                                                                  #
# Auteur : Soradev                                                                                     #
# Version : 1.0.0                                                                                      #
########################################################################################################
# Description :                                                                                        #
#   Concert EML to PDF                                                                                 #
########################################################################################################
# For any questions or contributions, please contact the author at sora.dev.pro@gmail.com              #
########################################################################################################


import os
import re
import shutil
from subprocess import Popen, PIPE

# Mettre à jour le chemin pour le binaire wkhtmltopdf dans resource/bin/wkhtmltox
WKHTMLTOPDF_EXECUTABLE = os.path.join(os.path.dirname(__file__), 'bin', 'wkhtmltox', 'bin', 'wkhtmltopdf.exe')

WKHTMLTOPDF_ERRORS_IGNORE = frozenset([
    r'QFont::setPixelSize: Pixel size <= 0 \(0\)',
    r'Invalid SOS parameters for sequential JPEG',
    r'libpng warning: Out of place sRGB chunk',
    r'Exit with code 1 due to network error: ContentNotFoundError',
    r'Exit with code 1 due to network error: UnknownContentError'
])

class HtmltoPdf:
    def __init__(self):
        if not os.path.isfile(WKHTMLTOPDF_EXECUTABLE):
            raise Exception("wkhtmltopdf executable not found in the application directory.")

    def save_pdf(self, html, output_pdf_file):
        output_path = self.__get_unique_version(output_pdf_file)
        wkh2p_process = Popen([WKHTMLTOPDF_EXECUTABLE, '-q',
                               '--load-error-handling', 'ignore',
                               '--load-media-error-handling', 'ignore',
                               '--encoding', 'utf-8', '-', output_path],
                              stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, error = wkh2p_process.communicate(input=html.encode('utf-8'))
        ret_code = wkh2p_process.returncode
        assert output == b''
        self.__process_errors(ret_code, error)
        return output_path

    def __get_unique_version(self, filename):
        counter = 1
        file_name_parts = os.path.splitext(filename)
        while os.path.isfile(filename):
            filename = f"{file_name_parts[0]}_{counter}{file_name_parts[1]}"
            counter += 1
        return filename

    def __process_errors(self, ret_code, error):
        stripped_error = str(error, 'utf-8')
        for error_pattern in WKHTMLTOPDF_ERRORS_IGNORE:
            stripped_error = re.sub(error_pattern, '', stripped_error)
        if ret_code > 0 and stripped_error.strip():
            raise Exception(f"wkhtmltopdf failed with exit code {ret_code}, error: {stripped_error}")

def convert_html_to_pdf(html_content, output_pdf_file):
    converter = HtmltoPdf()
    converter.save_pdf(html_content, output_pdf_file)
