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
import logging
import os
from time import sleep

from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.remote_connection import RemoteConnection

from src.testproject.enums import SleepTimingType, TakeScreenshotConditionType


class StepHelper:
    def __init__(self, executor, w3c, session_id):
        self.executor = executor
        self.w3c = w3c
        self.session_id = session_id

    def handle_timeout(self, timeout):
        if timeout > 0:
            logging.debug("Setting driver implicit wait to {} milliseconds.".format(timeout))
            if self.w3c:
                self.executor.execute(Command.SET_TIMEOUTS, {"sessionId": self.session_id, "implicit": int(timeout)})
            else:
                self.executor.execute(Command.IMPLICIT_WAIT, {"sessionId": self.session_id, "ms": float(timeout)})

    @staticmethod
    def handle_sleep(sleep_timing_type, sleep_time, command=None, step_executed=False):
        """Handles step sleep before/after step execution."""
        # Sleep Before if not Quit command
        if command is not Command.QUIT:
            if sleep_timing_type:
                sleep_timing_type_condition = SleepTimingType.After if step_executed else SleepTimingType.Before
                if sleep_timing_type is sleep_timing_type_condition:
                    logging.debug(
                        "Step is designed to sleep for {} milliseconds {} execution.".format(
                            sleep_time, sleep_timing_type.name
                        )
                    )
                    sleep(sleep_time / 1000.0)

    @staticmethod
    def take_screenshot(take_screenshot_condition, passed):
        """Returns true if the step report should include screenshot."""
        if take_screenshot_condition is TakeScreenshotConditionType.Always:
            return True
        if take_screenshot_condition is TakeScreenshotConditionType.Never:
            return False
        if passed and (take_screenshot_condition is TakeScreenshotConditionType.Success):
            return True
        if not passed and (take_screenshot_condition is TakeScreenshotConditionType.Failure):
            return False
        return False

    @staticmethod
    def handle_step_result(step_result, base_msg=None, invert_result=False, always_pass=False):
        """Handles the step result.

        Returns a tuple of the changed result and a formatted step message for reporting.
        """
        result_str, result_opposite_str = ("Passed", "Failed") if step_result else ("Failed", "Passed")
        invert_msg = (
            "Step result {} inverted to {}.{}".format(result_str, result_opposite_str, os.linesep)
            if invert_result
            else ""
        )
        failure_behavior_msg = (
            "Failure behaviour 'Always Pass' is configured, step result is forcibly set as Passed.{}".format(os.linesep)
            if always_pass
            else ""
        )
        # Create a base message if none was provided.
        base_msg = base_msg if base_msg else "Step {}.".format(result_str)
        # Add a line break to the base message.
        base_msg = base_msg if base_msg.endswith(os.linesep) else base_msg + os.linesep

        # Handle invert result
        step_result = not step_result if invert_result else step_result

        # Handle always pass
        step_result = True if always_pass else step_result

        return step_result, "{}{}{}".format(base_msg, invert_msg, failure_behavior_msg)
