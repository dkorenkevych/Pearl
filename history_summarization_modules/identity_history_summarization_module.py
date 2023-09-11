from pearl.api.observation import Observation
from pearl.core.common.replay_buffer.replay_buffer import ReplayBuffer
from pearl.core.common.replay_buffer.transition import TransitionBatch
from pearl.history_summarization_modules.history_summarization_module import (
    HistorySummarizationModule,
    SubjectiveState,
)


class IdentityHistorySummarizationModule(HistorySummarizationModule):
    """
    A history summarization module that simply uses the original observations.
    """

    def __init__(self, **options) -> None:
        pass

    def summarize_history(
        self, subjective_state: SubjectiveState, observation: Observation
    ) -> SubjectiveState:
        return observation

    def learn(self, replay_buffer: ReplayBuffer) -> None:
        pass

    def learn_batch(self, batch: TransitionBatch) -> None:
        pass