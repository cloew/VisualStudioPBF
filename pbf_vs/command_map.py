from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig("add folder", "pbf_vs.Commands.add_folder.AddFolder", description="Add Folder to a Visual Studio Solution"),
            CommandConfig("add vs-settings", "pbf_vs.Commands.add_vs_settings.AddVsSettings", description="Add Visual Studio settings to the current project")]

RegisterCommands(commands)