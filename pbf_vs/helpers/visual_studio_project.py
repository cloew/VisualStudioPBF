from pbf.helpers.configuration_helper import GetConfigurationPathRelativeToCurrentDirectory

class VisualStudioProject:
    """ Represents a Toggl Project """
    
    def __init__(self, project):
        """ Initialize the Toggl Project """
        self.project = project
        self.vsXML = self.project.projectXML.find('visual-studio')
        
    @property
    def solution(self):
        """ Return the Visual Studio Solution File """
        return GetConfigurationPathRelativeToCurrentDirectory(self.vsXML.findtext('solution'))