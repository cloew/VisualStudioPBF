from pbf.helpers.configuration_helper import GetRelativePathFromConfigurationsDirectory
from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf.helpers.Project.project_xml_helper import SaveProjectXML


from xml.etree.ElementTree import SubElement

class AddVSSettings:
    """ Represents command to add Visual Studio Settings to the current Project """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('sln', action='store', help='Visual Studio Solution File')
    
    def run(self, arguments):
        """ Run the command """
        solution = arguments.sln
            
        pbfProject = GetParentProjectFromDirectory()
        if pbfProject is None:
            print "No PBF project for current directory"
        else:
            self.addVSSettings(pbfProject, solution)
            
    def addVSSettings(self, pbfProject, solution):
        """ Add Visual Studio Settings to the project XML """
        vsElement = SubElement(pbfProject.projectXML, "visual-studio")
        solutionElement = SubElement(vsElement, "solution")
        solutionElement.text = GetRelativePathFromConfigurationsDirectory(solution)
            
        SaveProjectXML()
