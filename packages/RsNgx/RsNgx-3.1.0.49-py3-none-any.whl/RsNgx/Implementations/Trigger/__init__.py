from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 14 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	@property
	def enable(self):
		"""enable commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import Enable
			self._enable = Enable(self._core, self._cmd_group)
		return self._enable

	@property
	def direction(self):
		"""direction commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_direction'):
			from .Direction import Direction
			self._direction = Direction(self._core, self._cmd_group)
		return self._direction

	@property
	def logic(self):
		"""logic commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_logic'):
			from .Logic import Logic
			self._logic = Logic(self._core, self._cmd_group)
		return self._logic

	@property
	def channel(self):
		"""channel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def condition(self):
		"""condition commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_condition'):
			from .Condition import Condition
			self._condition = Condition(self._core, self._cmd_group)
		return self._condition

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def sequence(self):
		"""sequence commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequence'):
			from .Sequence import Sequence
			self._sequence = Sequence(self._core, self._cmd_group)
		return self._sequence
