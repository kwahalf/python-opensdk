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
from src.testproject.classes import ProxyDescriptor


class ActionProxy:
    """Base class that needs to be extended by custom Actions

    Attributes:
        _proxydescriptor (ProxyDescriptor): Contains the description of the custom action
    """

    def __init__(self):
        self._proxydescriptor = None

    @property
    def proxydescriptor(self):
        """Getter for the proxydescriptor"""
        return self._proxydescriptor

    @proxydescriptor.setter
    def proxydescriptor(self, value):
        """Setter for the proxydescriptor"""
        self._proxydescriptor = value
