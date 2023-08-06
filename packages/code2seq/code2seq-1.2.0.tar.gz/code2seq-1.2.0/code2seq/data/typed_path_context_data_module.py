from os.path import exists, join
from typing import List, Optional

from commode_utils.vocabulary import build_from_scratch
from omegaconf import DictConfig

from code2seq.data.path_context import LabeledTypedPathContext, BatchedLabeledTypedPathContext
from code2seq.data.path_context_data_module import PathContextDataModule
from code2seq.data.typed_path_context_dataset import TypedPathContextDataset
from code2seq.data.vocabulary import TypedVocabulary


class TypedPathContextDataModule(PathContextDataModule):
    _vocabulary: TypedVocabulary

    def __init__(self, data_dir: str, config: DictConfig):
        super().__init__(data_dir, config)

    @staticmethod
    def collate_wrapper(  # type: ignore[override]
        batch: List[Optional[LabeledTypedPathContext]],
    ) -> BatchedLabeledTypedPathContext:
        return BatchedLabeledTypedPathContext(batch)

    def _create_dataset(self, holdout_file: str, random_context: bool) -> TypedPathContextDataset:
        if self._vocabulary is None:
            raise RuntimeError(f"Setup vocabulary before creating data loaders")
        return TypedPathContextDataset(holdout_file, self._config, self._vocabulary, random_context)

    def setup_vocabulary(self) -> TypedVocabulary:
        if not exists(join(self._data_dir, TypedVocabulary.vocab_filename)):
            print("Can't find vocabulary, collect it from train holdout")
            build_from_scratch(join(self._data_dir, f"{self._train}.c2s"), TypedVocabulary)
        vocabulary_path = join(self._data_dir, TypedVocabulary.vocab_filename)
        return TypedVocabulary(
            vocabulary_path, self._config.labels_count, self._config.tokens_count, self._config.types_count
        )

    @property
    def vocabulary(self) -> TypedVocabulary:
        if self._vocabulary is None:
            raise RuntimeError(f"Setup data module for initializing vocabulary")
        return self._vocabulary
