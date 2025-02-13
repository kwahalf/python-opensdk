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


class AgentStatusResponse:
    """Represent a response message object returned by the Agent when requesting its status

    Args:
        tag (str): The Agent version

    Attributes:
        _tag (str): The Agent version
    """

    def __init__(self, tag):
        self._tag = tag

    @property
    def tag(self):
        """Getter for the Agent version field ('tag' in the JSON response)"""
        return self._tag
