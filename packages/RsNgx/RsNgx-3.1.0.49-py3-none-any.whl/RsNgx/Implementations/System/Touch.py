from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Touch:
	"""Touch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("touch", core, parent)

	def get_state(self) -> bool:
		"""SCPI: SYSTem:TOUCh[:STATe] \n
		Snippet: value: bool = driver.system.touch.get_state() \n
		Enables or disables touch interface beep. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('SYSTem:TOUCh:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, arg_0: bool) -> None:
		"""SCPI: SYSTem:TOUCh[:STATe] \n
		Snippet: driver.system.touch.set_state(arg_0 = False) \n
		Enables or disables touch interface beep. \n
			:param arg_0:
				- 1: Touch interface beep is activated.
				- 0: Touch interface beep is deactivated."""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'SYSTem:TOUCh:STATe {param}')
