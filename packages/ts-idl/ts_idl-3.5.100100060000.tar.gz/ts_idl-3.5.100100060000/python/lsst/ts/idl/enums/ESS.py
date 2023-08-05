# This file is part of ts_idl.
#
# Developed for the Vera C. Rubin Observatory Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__all__ = ["ErrorCode"]

from enum import IntEnum


class ErrorCode(IntEnum):
    """Error codes that can be used by the ESS CSC."""

    NotConnected = 1
    AlreadyConnected = 2
    NotConfigured = 3
    BadConfiguration = 4
    ReadLoopFailed = 5
    TelemetryError = 6
    HardwareError = 7
