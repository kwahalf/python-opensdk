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

from selenium.webdriver.common.by import By

from src.testproject.enums import ExecutionResultType
from src.testproject.sdk.drivers.actions import DriverActions
from src.testproject.sdk.drivers.actions.action_guids import web_actions
from src.testproject.sdk.internal.agent import AgentClient


class WebActions(DriverActions):
    """Offers methods to execute web actions

    Args:
        agent_client (AgentClient): client to communicate with the Agent
        timeout (int): timeout for action execution
    """

    def __init__(self, agent_client, timeout):
        super().__init__(agent_client, timeout)

    def move_mouse_to_element(self, by, by_value):
        """Moves the mouse to the middle of an element and scrolls it into view

        Args:
            by (By): Selenium locator strategy (By.ID, By.NAME, ...)
            by_value (str): The associated value for the locator strategy

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        response = self.action_execute(web_actions["MOVE_MOUSE_TO_ELEMENT_ID"], {}, by, by_value)
        return response.executionresulttype == ExecutionResultType.Passed

    def navigate_forward(self):
        """Navigate forward

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        response = self.action_execute(web_actions["NAVIGATE_FORWARD_ID"], {}, None, "")
        return response.executionresulttype == ExecutionResultType.Passed

    def navigate_back(self):
        """Navigate back

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        response = self.action_execute(web_actions["NAVIGATE_BACK_ID"], {}, None, "")
        return response.executionresulttype == ExecutionResultType.Passed

    def refresh(self):
        """Refresh the current browser tab

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        response = self.action_execute(web_actions["REFRESH_ID"], {}, None, "")
        return response.executionresulttype == ExecutionResultType.Passed

    def navigate_to_url(self, url):
        """Navigates to the specified URL in the active browser tab

        Args:
            url (str): The URL to navigate to

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        body = {"url": url}
        response = self.action_execute(web_actions["NAVIGATE_TO_URL_ID"], body, None, "")
        return response.executionresulttype == ExecutionResultType.Passed

    def get_current_url(self):
        """Retrieves the current URL from the active browser tab

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        response = self.action_execute(web_actions["GET_CURRENT_URL_ID"], {}, None, "")
        if response.executionresulttype != ExecutionResultType.Passed:
            return None
        return response.outputs["url"]

    def scroll_window(self, pixels_x_axis, pixels_y_axis):
        """Navigates to the specified URL in the active browser tab

        Args:
            pixels_x_axis (int): Amount of pixels to scroll on X axis. A negative value means opposite direction
            pixels_y_axis (int): Amount of pixels to scroll on Y axis. A negative value means opposite direction

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        body = {"x": pixels_x_axis, "y": pixels_y_axis}
        response = self.action_execute(web_actions["SCROLL_WINDOW_ID"], body, None, "")
        return response.executionresulttype == ExecutionResultType.Passed

    def select_all_options_by_value(self, by, by_value, option_value):
        """Select all options that have a value matching the argument

        Args:
            by (By): Selenium locator strategy (By.ID, By.NAME, ...)
            by_value (str): The associated value for the locator strategy
            option_value (str): The value of the option to select

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        body = {"value": option_value}
        response = self.action_execute(web_actions["SELECT_ALL_OPTIONS_BY_VALUE_ID"], body, by, by_value)
        return response.executionresulttype == ExecutionResultType.Passed

    def switch_to_window(self, index):
        """Select a window using its index

        Args:
            index (int): The index of the window to select

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        body = {"index": index}
        response = self.action_execute(web_actions["SWITCH_TO_WINDOW_ID"], body, None, "")
        return response.executionresulttype == ExecutionResultType.Passed

    def close_window(self, index):
        """Closes the window with the given index

        Args:
            index (int): The index of the window to close

        Returns:
            bool: True if action was performed successfully, False otherwise
        """
        body = {"index": index}
        response = self.action_execute(web_actions["CLOSE_WINDOW_ID"], body, None, "")
        return response.executionresulttype == ExecutionResultType.Passed
