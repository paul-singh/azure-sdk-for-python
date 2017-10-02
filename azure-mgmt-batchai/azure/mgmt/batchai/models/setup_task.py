# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SetupTask(Model):
    """Specifies a setup task which can be used to customize the compute nodes of
    the cluster.

    :param command_line: Command Line to start Setup process.
    :type command_line: str
    :param environment_variables: Collection of environment settings.
    :type environment_variables: list of :class:`EnvironmentSetting
     <azure.mgmt.batchai.models.EnvironmentSetting>`
    :param run_elevated: Specifies whether to run the setup task in elevated
     mode. The default value is false.  Default value: False .
    :type run_elevated: bool
    :param std_out_err_path_prefix: The path where the Batch AI service will
     upload stdout and stderror of setup task.
    :type std_out_err_path_prefix: str
    """

    _validation = {
        'command_line': {'required': True},
        'std_out_err_path_prefix': {'required': True},
    }

    _attribute_map = {
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'environment_variables': {'key': 'environmentVariables', 'type': '[EnvironmentSetting]'},
        'run_elevated': {'key': 'runElevated', 'type': 'bool'},
        'std_out_err_path_prefix': {'key': 'stdOutErrPathPrefix', 'type': 'str'},
    }

    def __init__(self, command_line, std_out_err_path_prefix, environment_variables=None, run_elevated=False):
        self.command_line = command_line
        self.environment_variables = environment_variables
        self.run_elevated = run_elevated
        self.std_out_err_path_prefix = std_out_err_path_prefix
