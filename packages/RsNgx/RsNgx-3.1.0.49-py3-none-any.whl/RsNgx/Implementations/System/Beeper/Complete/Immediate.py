from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:BEEPer[:COMPlete][:IMMediate] \n
		Snippet: driver.system.beeper.complete.immediate.set() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:BEEPer:COMPlete:IMMediate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:BEEPer[:COMPlete][:IMMediate] \n
		Snippet: driver.system.beeper.complete.immediate.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:BEEPer:COMPlete:IMMediate', opc_timeout_ms)
