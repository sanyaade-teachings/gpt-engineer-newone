"""
Base Agent Module

This module provides an abstract base class for an agent that interacts with code. It defines the interface
for agents capable of initializing and improving code based on a given prompt. Implementations of this class
are expected to provide concrete methods for these actions.

Classes:
    BaseAgent: Abstract base class for an agent that interacts with code.
"""
from abc import ABC, abstractmethod

from gpt_engineer.core.files_dict import FilesDict


class BaseAgent(ABC):
    """
    Abstract base class for an agent that interacts with code.

    Defines the interface for agents capable of initializing and improving code based on a given prompt.
    Implementations of this class are expected to provide concrete methods for these actions.

    Methods
    -------
    init(self, prompt: str) -> FilesDict
        Initialize a new piece of code based on the given prompt and return a FilesDict object.
    improve(self, files_dict: FilesDict, prompt: str) -> FilesDict
        Improve an existing piece of code based on the given prompt and return the updated FilesDict object.
    """

    @abstractmethod
    def init(self, prompt: str) -> FilesDict:
        pass

    @abstractmethod
    def improve(self, files_dict: FilesDict, prompt: str) -> FilesDict:
        pass
