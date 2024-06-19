# -*- coding: utf-8 -*-
import random

import fitz
import pywintypes
import win32api
import win32con
import win32gui
import win32print
from PIL import Image, ImageWin


class Printer:
    def __init__(self):
        self.config = None  # pywintypes.DEVMODEType()
        self.is_color = False
        self.pages = []
        # 设置双面打印
        self.is_double_page = False
        self.long_line_turn = False
        # 设置打印机纸盒
        self.set_cartridge = None
        # 打印机名字
        self.printer_name = "XabVPrinter"
        # 打印纸张大小
        self.page_size = "A4"
        # 打印份数
        self.print_num = 2
        # 横向打印
        self.is_transverse = False
        self.printer_config = None
        self.task_name = f"task {random.randint(0, 10000)}"

    def print_img(self, _file_list):
        self.set_printer_config()
        self.get_printer_info()
        win32print.StartDoc(self.hDC, (self.task_name, None, None, 0))
        for file in _file_list:
            win32print.StartPage(self.hDC)
            bmp, scale = self._open_img(file)
            dib = ImageWin.Dib(bmp)
            scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
            x1 = int((self.printer_size[0] - scaled_width) / 2)
            y1 = int((self.printer_size[1] - scaled_height) / 2)
            x2 = x1 + scaled_width
            y2 = y1 + scaled_height
            dib.draw(self.hDC, (x1, y1, x2, y2))
            win32print.EndPage(self.hDC)
        win32print.EndDoc(self.hDC)
        win32gui.DeleteDC(self.hDC)

    # _file_list = [{"fileName": "", "pages": [1, 3]}, ...]
    def print_pdf(self, _file_list):
        self.set_printer_config()
        self.get_printer_info()
        for pdf in _file_list:
            pages = self.load_pdf(pdf['fileName'], pdf['pages'])
            self.get_printer_info()
            win32print.StartDoc(self.hDC, (self.task_name, None, None, 0))
            for page in pages:
                win32print.StartPage(self.hDC)
                dib = ImageWin.Dib(page)
                dib.draw(self.hDC, (0, 0, self.printer_size[0], self.printer_size[1]))
                win32print.EndPage(self.hDC)
            win32print.EndDoc(self.hDC)
        win32gui.DeleteDC(self.hDC)

    def print_docx_wps(self, _file_name):
        self.set_printer_config()
        self.get_printer_info()
        win32api.ShellExecute(0, "print", _file_name, None, ".", 0)

    def load_doc(self):
        pass

    def load_pdf(self, file_name, pages: tuple) -> list:
        doc = fitz.open(file_name)
        page_nums = doc.page_count
        res_pages = []
        for index in range(pages[0] - 1, min(page_nums, pages[1])):
            cur_page = doc[index]
            pix = cur_page.get_pixmap()
            mode = "RGBA" if pix.alpha else "RGB"
            img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
            res_pages.append(img)
        return res_pages

    def set_printer_config(self):
        printaccess = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
        cur_handle = win32print.OpenPrinter(self.printer_name, printaccess)
        properties = win32print.GetPrinter(cur_handle, 2)
        self.config = properties['pDevMode']
        self._set_config()
        try:
            win32print.SetPrinter(cur_handle, 2, properties, 0)
        except Exception as e:
            print(e)
        win32print.SetDefaultPrinter(self.printer_name)

    def get_printer_info(self):
        self.hDC = win32gui.CreateDC(self.printer_name, self.printer_name, None)
        self.printable_area = win32print.GetDeviceCaps(self.hDC, win32con.HORZRES), win32print.GetDeviceCaps(self.hDC,
                                                                                                             win32con.VERTRES)  # 获取打印机纸质宽 高
        self.printer_size = win32print.GetDeviceCaps(self.hDC, win32con.PHYSICALWIDTH), win32print.GetDeviceCaps(
            self.hDC, win32con.PHYSICALHEIGHT)  # 打印页面物理宽 高
        self.printer_margins = win32print.GetDeviceCaps(self.hDC, win32con.PHYSICALOFFSETX), win32print.GetDeviceCaps(
            self.hDC, win32con.PHYSICALOFFSETY)  # 打印机的可打印的水平

    # @param file_name: 文件的绝对路径
    def _open_img(self, file_name):
        bmp = Image.open(file_name)
        if not self.is_color:
            bmp = bmp.convert('1')
        if bmp.size[0] > bmp.size[1]:
            bmp = bmp.rotate(90)
        ratios = [1.0 * self.printable_area[0] / bmp.size[0], 1.0 * self.printable_area[1] / bmp.size[1]]
        scale = min(ratios)
        return bmp, scale

    def _set_config(self):
        if self.is_color:
            self.config.Color = win32con.DMCOLOR_COLOR
        else:
            self.config.Color = win32con.DMCOLOR_MONOCHROME
        # 设置单双面打印
        if self.is_double_page:
            self.config.Duplex = win32con.DMDUP_HORIZONTAL
        else:
            self.config.Duplex = win32con.DMDUP_SIMPLEX
        # 打印朝向
        if self.is_transverse:
            self.config.Orientation = win32con.DMORIENT_LANDSCAPE
        else:
            self.config.Orientation = win32con.DMORIENT_PORTRAIT

        if self.page_size is 'A4':
            self.config.PaperSize = win32con.DMPAPER_A4


if __name__ == '__main__':
    file_list = [
        r'D:\Desktop\test1.jpeg'
        # r'D:\Desktop\test2.jpeg'
    ]
    pdf_list = [{"fileName": r'D:\Desktop\安装控件说明\test.pdf', "pages": [1, 3]}]
    doc_filename = r'D:\Desktop\安装控件说明\test1.docx'
    p = Printer()
    p.print_doc(doc_filename)
