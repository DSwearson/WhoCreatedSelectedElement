"""
Copyright (c) 2018 Daniel J. Swearson
"""

__author__= 'Daniel J. Swearson'
__doc__ = 'Reports author of created element within a worksharing enviornment'

from Autodesk.Revit.DB import WorksharingUtils

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

import clr

show_view = doc.ActiveView
show_id = show_view.Id.ToString()
show_name = show_view.Name
show_author = WorksharingUtils.GetWorksharingTooltipInfo(doc, show_view.Id).Creator

print("Current view: " + show_name)
print("ID number: " + show_id)
print("Author: " + show_author)
