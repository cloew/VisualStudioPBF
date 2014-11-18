from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf_vs.helpers.visual_studio_project import VisualStudioProject

def GetCurrentVSProject():
    """ Get Toggl Project for the current directory """
    project = GetParentProjectFromDirectory()
    return VisualStudioProject(project)