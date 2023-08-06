from typing import Optional, Any, Protocol, Union, Type, Dict

from aiogram import Bot, Router
from aiogram.dispatcher.fsm.state import State, StatesGroup

from ..context.context import Context
from ..context.events import StartMode, ChatEvent, Data, DialogUpdate
from ..context.stack import Stack


class ManagedDialogProto(Protocol):
    def register(self, registry: "DialogRegistryProto", router: Router, *args, **kwargs) -> None:
        pass

    def states_group_name(self) -> str:
        pass

    def states_group(self) -> Type[StatesGroup]:
        pass

    async def process_close(self, result: Any, manager: "DialogManager"):
        pass

    async def process_start(self, manager: "DialogManager", start_data: Any,
                            state: Optional[State] = None) -> None:
        pass

    async def show(self, manager: "DialogManager"):
        pass

    async def process_result(self, start_data: Data, result: Any, manager: "DialogManager"):
        pass

    async def next(self, manager: "DialogManager"):
        pass

    async def back(self, manager: "DialogManager"):
        pass

    async def switch_to(self, state: State, manager: "DialogManager"):
        pass

    def find(self, widget_id) -> Optional[Any]:
        pass


class DialogRegistryProto(Protocol):
    def find_dialog(self, state: Union[State, str]) -> ManagedDialogProto:
        pass

    async def notify(self, bot: Bot, update: DialogUpdate) -> None:
        pass


class BaseDialogManager(Protocol):
    event: ChatEvent

    async def done(self, result: Any = None) -> None:
        pass

    async def mark_closed(self) -> None:
        pass

    async def start(
            self,
            state: State,
            data: Data = None,
            mode: StartMode = StartMode.NORMAL,
    ) -> None:
        pass

    async def switch_to(self, state: State) -> None:
        pass

    async def update(self, data: Dict) -> None:
        pass

    def bg(
            self,
            user_id: Optional[int] = None,
            chat_id: Optional[int] = None,
            stack_id: Optional[str] = None,
    ) -> "BaseDialogManager":
        pass


class DialogManager(BaseDialogManager):
    event: ChatEvent  # current processing event
    data: Dict  # data from middleware

    def current_context(self) -> Optional[Context]:
        pass

    def current_stack(self) -> Optional[Stack]:
        pass

    def dialog(self) -> ManagedDialogProto:
        pass

    async def close_manager(self) -> None:
        pass
