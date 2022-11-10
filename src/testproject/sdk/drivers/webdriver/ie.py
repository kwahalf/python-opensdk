# Copyright 2020 TestProject (https://testproject.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from selenium.webdriver.ie.options import Options

from src.testproject.enums.report_type import ReportType
from src.testproject.sdk.drivers.webdriver.base import BaseDriver
from src.testproject.sdk.internal.agent import AgentClient


class Ie(BaseDriver):
    """Used to create a new Internet Explorer browser instance

    Args:
        ie_options (Options): IE automation session desired capabilities and options
        desired_capabilities (dict): Dictionary object containing desired capabilities for IE automation session
        token (str): The developer token used to communicate with the agent
        project_name (str): Project name to report
        job_name (str): Job name to report
        disable_reports (bool): set to True to disable all reporting (no report will be created on TestProject)
        report_type (ReportType): Type of report to produce - cloud, local or both.
        socket_session_timeout (int): The connection timeout to the agent in milliseconds.
    """

    def __init__(
        self,
        ie_options=None,
        desired_capabilities=None,
        token=None,
        project_name=None,
        job_name=None,
        disable_reports=False,
        report_type=ReportType.CLOUD_AND_LOCAL,
        agent_url=None,
        report_name=None,
        report_path=None,
        socket_session_timeout=AgentClient.NEW_SESSION_SOCKET_TIMEOUT_MS,
    ):
        # If no options or capabilities are specified at all, use default Options
        if ie_options is None and desired_capabilities is None:
            caps = Options().to_capabilities()
        else:
            # Specified IE Options take precedence over desired capabilities but either can be used
            caps = ie_options.to_capabilities() if ie_options is not None else desired_capabilities

        super().__init__(
            capabilities=caps,
            token=token,
            project_name=project_name,
            job_name=job_name,
            disable_reports=disable_reports,
            report_type=report_type,
            agent_url=agent_url,
            report_name=report_name,
            report_path=report_path,
            socket_session_timeout=socket_session_timeout,
        )
