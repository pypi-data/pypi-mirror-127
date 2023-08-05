from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cancel:
	"""Cancel commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cancel", core, parent)

	def set(self) -> None:
		"""SCPI: CALibration:CANCel \n
		Snippet: driver.calibration.cancel.set() \n
		Cancels the channel adjustment. \n
		"""
		self._core.io.write(f'CALibration:CANCel')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALibration:CANCel \n
		Snippet: driver.calibration.cancel.set_with_opc() \n
		Cancels the channel adjustment. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALibration:CANCel', opc_timeout_ms)
