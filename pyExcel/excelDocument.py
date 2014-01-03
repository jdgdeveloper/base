"""
Class ExcelDocument
Beth Finn

adapted from http://snippets.dzone.com/posts/show/2036
"""

from win32com.client import constants, Dispatch
import pythoncom
import os

borderTop = 3 
borderBottom = 4
borderLeft = 1
borderRight = 2
borderSolid = 1
borderDashed = 2
borderDotted = 3
colorBlack = 1
directionUp = -4162
directionDown = -4121
directionLeft = -4131
directionRight = -4152

class ExcelDocument(object):
  """
  Some convenience methods for Excel documents accessed
  through COM.
  """
  
  def __init__(self, visible=False):
    print("in __init__")
    self.app = Dispatch("Excel.Application")
    self.app.Visible = visible
    self.sheet = 1
  
  def new(self, filename=None):
    """
    Create a new Excel workbook. If 'filename' specified,
    use the file as a template.
    """
    self.app.Workbooks.Add(filename)
  
  def open(self, filename):
    """
    Open an existing Excel workbook for editing.
    """
    self.app.Workbooks.Open(filename)
  
  def set_sheet(self, sheet):
    """
    Set the active worksheet.
    """
    self.sheet = sheet
  
  def get_range(self, range):
    """
    Get a range object for the specified range or single cell.
    """
    return self.app.ActiveWorkbook.Sheets(self.sheet).Range(range)
  
  def set_value(self, cell, value=''):
    """
    Set the value of 'cell' to 'value'.
    """
    self.get_range(cell).Value = value
  
  def get_value(self, cell):
    """
    Get the value of 'cell'.
    """
    value = self.get_range(cell).Value
    if isinstance(value, tuple):
      value = [v[0] for v in value]
    return value
  
  def set_border(self, range, side, line_style=borderSolid, color=colorBlack):
    """
    Set a border on the specified range of cells or single cell.
    'range' = range of cells or single cell
    'side' = one of borderTop, borderBottom, borderLeft, borderRight
    'line_style' = one of borderSolid, borderDashed, borderDotted, others?
    'color' = one of colorBlack, others?
    """
    range = self.get_range(range).Borders(side)
    range.LineStyle = line_style
    range.Color = color
  
  def sort(self, range, key_cell):
    """
    Sort the specified 'range' of the activeworksheet by the
    specified 'key_cell'.
    """
    range.Sort(Key1=self.get_range(key_cell), Order1=1, Header=0, OrderCustom=1, MatchCase=False, Orientation=1)
  
  def hide_row(self, row, hide=True):
    """
    Hide the specified 'row'.
    Specify hide=False to show the row.
    """
    self.get_range('a%s' % row).EntireRow.Hidden = hide
  
  def hide_column(self, column, hide=True):
    """
    Hide the specified 'column'.
    Specify hide=False to show the column.
    """
    self.get_range('%s1' % column).EntireColumn.Hidden = hide
  
  def delete_row(self, row, shift=directionUp):
    """
    Delete the entire 'row'.
    """
    self.get_range('a%s' % row).EntireRow.Delete(Shift=shift)
  
  def delete_column(self, column, shift=directionLeft):
    """
    Delete the entire 'column'.
    """
    self.get_range('%s1' % column).EntireColumn.Delete(Shift=shift)
    
  def fit_column(self, column):
    """
    Resize the specified 'column' to fit all its contents.
    """
    self.get_range('%s1' % column).EntireColumn.AutoFit()
  
  def save(self):
    """
    Save the active workbook.
    """
    self.app.ActiveWorkbook.Save()
  
  def save_as(self, filename, delete_existing=False):
    """
    Save the active workbook as a different filename.
    If 'delete_existing' is specified and the file already
    exists, it will be deleted before saving.
    """
    if delete_existing and os.path.exists(filename):
      os.remove(filename)
    self.app.ActiveWorkbook.SaveAs(filename)
  
  def print_out(self):
    """
    Print the active workbook.
    """
    self.app.Application.PrintOut()
  
  def close(self):
    """
    Close the active workbook.
    """
    self.app.ActiveWorkbook.Close()
  
  def quit(self):
    """
    Quit Excel.
    """
    return self.app.Quit()
 


def run(filename = "default_summary"):
    # create a new spreadsheet
    print("creating doc % ...", filename)
    # for now create it without a template document
    # summary = excelDocument(filename)    
    summary = ExcelDocument()


if __name__ == '__main__':
    # test
    print("in main")
    Tk().withdraw()
    #test()
    run("new_summary")
      
