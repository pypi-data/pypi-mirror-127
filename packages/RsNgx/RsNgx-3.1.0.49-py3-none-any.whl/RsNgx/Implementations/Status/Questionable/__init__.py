from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Questionable:
	"""Questionable commands group definition. 10 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("questionable", core, parent)

	@property
	def instrument(self):
		"""instrument commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_instrument'):
			from .Instrument import Instrument
			self._instrument = Instrument(self._core, self._cmd_group)
		return self._instrument
